FROM nginx:1.19.0

COPY ./nginx/nginx.conf /etc/nginx/nginx.conf
COPY ./nginx/sites-enabled/meunovosite.com /etc/nginx/sites-available/meunovosite.com

RUN mkdir -p /etc/nginx/sites-enabled/\
    && ln -s /etc/nginx/sites-available/meunovosite.com /etc/nginx/sites-enabled/

RUN mkdir -p /www/static
RUN mkdir -p /www/media



CMD ["nginx", "-g", "daemon off;"]
