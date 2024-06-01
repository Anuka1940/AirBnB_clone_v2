# Configuring web server using puppet

# Ngninx
$config = "server {
        root        /etc/nginx/html;
        add_header X-Served-By ${hostname};
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
}"
package { 'nginx':
    ensure   => 'present',
    provider => 'apt'
}

-> file { ['/data/', '/data/web_static/', '/data/web_static/releases/',
        '/data/web_static/releases/test/', '/data/web_static/shared']:
    ensure => 'directory'
}

-> file {'/data/web_static/releases/test/index.html':
    ensure  => 'present',
    content => "Holberton School\n",
}

-> file { '/data/web_static/current':
    ensure => 'link',
    target => '/data/web_static/releases/test/'
}

-> exec { 'chown -R ubuntu:ubuntu /data/':
    path => '/usr/bin/:/usr/local/bin/:/bin/'
}
file { ['/var/','/var/www/','/var/www/html']:
    ensure => 'directory'
}
-> file { '/var/www/html/index.html':
    ensure  => 'present',
    content => "Holberton School\n"
}
-> file { '/var/www/html/404.html':
    ensure  => 'present',
    content => "Ceci n'est pas une page\n"
}
-> file { '/etc/nginx/sites-available/default':
    ensure  => 'present',
    content => $config,
}

-> exec { 'nginx restart':
    path => '/etc/init.d'
}
