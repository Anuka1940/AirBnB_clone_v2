#!/usr/bin/env bash
<<<<<<< HEAD
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
=======
#Install Nginx if not already installed
if ! command -v nginx &> /dev/null; then
        apt-get update
        apt-get -y install nginx
fi

# Create necessary dicectories
sudo mkdir -p /data/web_static/{releases/test,shared}
sudo chown -R ubuntu:ubuntu /data/

# Create a fake HTML file
echo "<html>
  <head>
  </head>
  <body>
   <h1>Holberton School</h1>
   </body>
  </html>" | sudo tee /data/web_static/releases/test/index.html  > /dev/null

# Create or recreate the symbolic link
[ -d /data/web_static/current ] && sudo rm -rf /data/web_static/current
sudo ln -sf /data/web_static/releases/test /data/web_static/curren

# Give ownership of the /data/ folder
config_file="/etc/nginx/sites-available/default"
nginx_config="
server {
    listen 80 default_server;
    listen [::]:80 default_server;

    server_name _;
    index index.html;
    add_header X-Served-By /$hostname;

    location / {
            root /var/www/html/;
            try_files \$uri\$uri/ =404
    }
    location /hbnb_static/ {
        alias /data/web_static/current/;
        try_files \$uri \$uri/ =404;
}
"
echo "$nginx_config" | sudo tee "$config_file" > /dev/null
sudo service nginx restart
exit 0
>>>>>>> 2a1a463b62a130dd5a46dafc2e4097c8e2397546
