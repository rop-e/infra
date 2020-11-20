server {

    listen 80;
    server_name rop-e.com www.rop-e.com;
    charset utf-8;
    client_max_body_size 75M;
    
    location /static {
        alias /www/static;
    }

    location /media {
        alias /www/media;
    }

    location / {
        proxy_pass http://webapp:8000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
    }

}