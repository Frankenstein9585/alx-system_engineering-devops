# edit shh_config using puppet
file_line {'add line to file':
  path    => '/etc/ssh/ssh_config',
  line => 'PasswordAuthentication no',
}

file_line{'add line to file':
  path => '/etc/ssh/ssh_config',
  line => 'IdentityFile ~/.ssh/school',
}
