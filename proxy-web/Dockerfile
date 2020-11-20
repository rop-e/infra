FROM nginx:1.19.0

COPY ./nginx/nginx.conf /etc/nginx/nginx.conf
COPY ./nginx/sites-enabled/seusite.com /etc/nginx/sites-available/seusite.com

RUN mkdir -p /etc/nginx/sites-enabled/\
    && ln -s /etc/nginx/sites-available/seusite.com /etc/nginx/sites-enabled/

CMD ["nginx", "-g", "daemon off;"]