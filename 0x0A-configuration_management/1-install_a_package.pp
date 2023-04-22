# install flask from pip3
package {'python3-pip':
  ensure => 'installed',
}

package {'flask':
  ensure   => 'latest',
  provider => 'pip3',
}
