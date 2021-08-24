# Creating a HTTP header X-Served-By

exec { 'executing in nginx':
  command  => 'sudo apt-get -y update;
               sudo apt-get -y upgrade;
               sudo apt-get -y install nginx;
               sudo service nginx start;
               sudo chmod 777 /var/www/html/index.nginx-debian.html;
               echo "Holberton School" | sudo tee /var/www/html/index.nginx-debian.html;
               /etc/nginx/sites-enabled/default/sudo sed -i /server_name _;/ a \\trewrite\
             ^/redirect_me https://www.youtube.com/watch?v=QH2-TGUlwu4 permanent;
               echo "C'est pas a page" | sudo tee /usr/share/nginx/html/custom_404.html;
               /etc/nginx/sites-enabled/default/sudo sed -i 20i \\\terror_page 404 /custom_404.html;\n\tlocation =\
             /custom_404.html {\n\t root /usr/share/nginx/html;\n\tinternal;\n\t};
               sudo sed -i "11i \\\t add_header X-Served-By $HOSTNAME always;\n" /etc/nginx/nginx.conf;
               sudo service nginx restart',
  provider => shell,
}
