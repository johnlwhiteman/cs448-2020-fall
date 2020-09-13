FROM nginx:alpine
RUN apk update \
    && apk upgrade \
    && apk add bash curl --no-cache
#COPY default.conf /etc/nginx/conf.d/default.conf
EXPOSE 80 443