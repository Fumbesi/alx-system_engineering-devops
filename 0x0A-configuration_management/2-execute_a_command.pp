#This code will create a manifest that kills a process named killmenow.
exec { killmenow':
  command  => '/usr/bin/killmenow',
  provider  => 'shell',
  return  => [0, 1],
}
