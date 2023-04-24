# edit shh_config using puppet
exec { 'echo "PasswordAuthentication no\nIdentityFile ~/.ssh/school" >> /etc/ssh/ssh_config':
  path    => '/bin/'
}
