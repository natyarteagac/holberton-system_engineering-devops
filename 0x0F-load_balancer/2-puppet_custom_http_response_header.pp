# Creating a HTTP header X-Served-By

exec {
  cwd      => /etc/nginx/nginx.conf,
  command  => 'sudo sed -i 11i \\\t add_header X-Served-By '$HOSTNAME' always;\n',
  provider => shell,
}
