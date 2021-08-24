# Creating a HTTP header X-Served-By

exec { 'executing in nginx':
  command  => 'sudo apt-get -y update',
  command  => 'sudo apt-get -y upgrade',
  command  => 'sudo apt-get -y install nginx',
  command  => 'sudo service nginx start',
  command  => '/etc/nginx/nginx.conf/sudo sed -i 11i \\\t add_header X-Served-By $servername always;\n',
  command  => 'sudo service nginx restart',
  provider => shell,
}
