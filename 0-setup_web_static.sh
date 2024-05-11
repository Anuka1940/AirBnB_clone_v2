#!/usr/bin/env bash
# Setting up web serverto deploy web static

apt-get update
apt-get install -y nginx
# Creatind Test and shared dirs
mkdir -p /data/web_static/releases/test/
mkdir -p /data/web_static/shared/
echo "Holberton School" > /data/web_static/releases/test/index.html
ln -sf /data/web_static/releases/test/ /data/web_static/current

#Making change of Owner and group
chown -R ubuntu /data/
chgrp -R ubuntu /data/

# Allow http rule
sudo ufw allow 'Nginx HTTP'

printf %s "server {
        root        /etc/nginx/html;
        add_header X-Served-By $HOSTNAME;
        index       index.html index.htm;
        listen      80 default_server;
        listen      [::]:80 default_server;
        location /redirect_me {
            return 301 https://www.youtube.com/watch?v=QH2-TGUlwu4;
        }
        location /hbnb_static {
            alias /data/web_static/current;
            index index.html index.htm;
        }
        error_page 404 /404.html;
        location /404 {
            root /etc/nginx/html;
            internal;
        }
}
" >/etc/nginx/sites-available/default
service nginx restart
