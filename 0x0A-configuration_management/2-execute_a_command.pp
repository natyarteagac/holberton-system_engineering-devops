# Manifiest that kill a process named "killmenow"

exec { 'killmenow':
  command  => 'pkill -i',
  provider => shell,
  onlyif   => 'killmenow',
}
