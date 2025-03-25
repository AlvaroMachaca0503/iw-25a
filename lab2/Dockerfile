FROM nginx:latest

COPY default.conf /etc/nginx/conf.d/default.conf

COPY lab01.html /usr/share/nginx/html/
COPY css /usr/share/nginx/html/css/
COPY js /usr/share/nginx/html/js/

EXPOSE 8088

CMD ["nginx", "-g", "daemon off;"]
