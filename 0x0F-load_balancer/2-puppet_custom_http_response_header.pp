# Creating a HTTP header X-Served-By

exec { 'executing in nginx':
  command  => 'sudo apt-get -y update && sudo apt-get -y upgrade && sudo apt-get -y install nginx && sudo service nginx start && /etc/nginx/nginx.conf/sudo sed -i 11i \\\t add_header X-Served-By $servername always;\n && sudo service nginx restart',
  provider => shell,
}
