# Creating a HTTP header X-Served-By

exec { 'executing in nginx':
  command  => 'sudo apt-get -y update;
               sudo apt-get -y upgrade;
               sudo apt-get -y install nginx;
               sudo service nginx start;
               sudo chmod 777 /var/www/html/index.nginx-debian.html;
               echo 'Holberton School' | sudo tee /usr/share/nginx/html/custom_404.html;
               /etc/nginx/sites-enabled/default/sudo sed -i '20i \\\terror_page 404\
            /custom_404.html; \n\tlocation = /custom_404.html {\n\t root /usr/share/nginx/html;\n\tinternal;\n\t}';
               /etc/nginx/nginx.conf/sudo sed -i 11i \\\t add_header X-Served-By $servername always;\n;
               sudo service nginx restart',
  provider => shell,
}
