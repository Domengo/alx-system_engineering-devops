file { '/etc/ssh/ssh_config':
  ensure  => present,
  owner   => 'domengo',
  group   => 'domengo',
  mode    => '0644',
  content => "
Host 52.207.208.23
  HostName 52.207.208.23
  User ubuntu
  IdentityFile ~/.ssh/school
  PubkeyAuthentication yes
  PasswordAuthentication no
  ServerAliveInterval 60
  ServerAliveCountMax 3",
}
