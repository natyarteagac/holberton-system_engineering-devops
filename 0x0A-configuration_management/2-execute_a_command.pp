# Manifiest that kill a process named "killmenow"

exec { 'killmenow':
  command  => 'pkill -f killmenow',
  provider => shell,
}
