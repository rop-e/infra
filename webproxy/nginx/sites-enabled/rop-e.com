upstream webapp01 {
    # server APP_SERVER_1_IP;
    # server APP_SERVER_2_IP;
    server webapp:8000;
}

server {
    listen 80 default_server;
    return 444;
}

server {
    listen 80;
    listen [::]:80;
    server_name rop-e.com;
    return 301 https://$server_name$request_uri;
}

server {
    listen 443 ssl;
    listen [::]:443 ssl;
    server_name rop-e.com;

    access_log /var/log/nginx/rop-e_com-access.log;
    error_log /var/log/nginx/error.log info;

    # SSL
    ssl_certificate /etc/letsencrypt/live/rop-e.com/fullchain.pem;
    ssl_certificate_key /etc/letsencrypt/live/rop-e.com/privkey.pem;

    #ssl_session_cache shared:le_nginx_SSL:10m;
    #ssl_session_timeout 1440m;
    #ssl_session_tickets off;

    #ssl_protocols TLSv1.2 TLSv1.3;
    #ssl_prefer_server_ciphers off;

    #ssl_ciphers "ECDHE-ECDSA-AES128-GCM-SHA256:ECDHE-RSA-AES128-GCM-SHA256:ECDHE-ECDSA-AES256-GCM-SHA384:ECDHE-RSA-AES256-GCM-SHA384:ECDHE-ECDSA-CHACHA20-POLY1305:ECDHE-RSA-CHACHA20-POLY1305:DHE-RSA-AES128-GCM-SHA256:DHE-RSA-AES256-GCM-SHA384";

    client_max_body_size 4G;
    keepalive_timeout 5;

        location / {
          proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
          proxy_set_header X-Forwarded-Proto $scheme;
          proxy_set_header Host $http_host;
          proxy_redirect off;
    	  add_header P3P 'CP="ALL DSP COR PSAa PSDa OUR NOR ONL UNI COM NAV"';
          proxy_pass http://webapp01;
        }

    location ^~ /.well-known/acme-challenge {
        root /www;
    }

    location /static {
        alias /www/static;
    }

    location /media {
        alias /www/media;
    }

}
