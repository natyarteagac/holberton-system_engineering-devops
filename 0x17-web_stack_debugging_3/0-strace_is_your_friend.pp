# Restarting Apache2


exec { 'Restart Apache':
    exec     => '/etc/init.d/apache2 restart',
    provider => shell,
}
