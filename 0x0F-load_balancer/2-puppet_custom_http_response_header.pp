# Creating a HTTP header X-Served-By

class { 'http_hardening':
  nginx    => true,
  content  => ("X-Served-By", $HOSTNAME)
}