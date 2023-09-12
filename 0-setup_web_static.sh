#!/usr/bin/env bash
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
