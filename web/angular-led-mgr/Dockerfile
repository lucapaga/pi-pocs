FROM nginx
MAINTAINER Luca Paganelli <luca.paga@gmail.com>

#ENV PROXY_PASS_URI=https://pi-web-pubsub-py-be-dot-luca-paganelli-formazione.appspot.com
#ENV PROXY_PASS_URI=http://192.168.1.132:5000

#COPY ./conf/default.conf /etc/nginx/conf.d/default.conf
COPY ./conf/nginx.conf /etc/nginx/nginx.conf

COPY ./dist /usr/share/nginx/html
RUN chmod -R a+r /usr/share/nginx/html

RUN mkdir -p /var/log/app_engine && \
    mkdir -p /usr/share/nginx/html/_ah && \
    echo "healthy" > /usr/share/nginx/html/_ah/health
