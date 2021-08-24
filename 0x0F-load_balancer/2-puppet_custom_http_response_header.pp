# Creating a HTTP header X-Served-By

exec {
  command  => 'sudo apt-get -y update',
  command  => 'sudo apt-get -y upgrade',
  command  => 'sudo apt-get -y install nginx',
  command  => 'sudo service nginx start',
  command  => '/etc/nginx/nginx.conf/sudo sed -i 11i \\\t add_header X-Served-By 'hostname' always;\n',
  command  => 'sudo service nginx restart',
  provider => shell,
}
