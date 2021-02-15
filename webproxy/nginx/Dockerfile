FROM tutum/nginx
RUN rm /etc/nginx/sites-enabled/default
COPY sites-enabled /etc/nginx/sites-enabled

RUN apt-get update
RUN apt-get install coreutils

RUN mkdir -p /www/static
RUN mkdir -p /www/media

