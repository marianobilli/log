A collection of commands to help troubleshooting package installation on RHEL/Centos

Which version of a package is installed?
```
$ rpm -q bash
```

To verify all packages on the system
```
rpm -Va
```

Verify specific package
```
rpm -V bash
```

Which package did this file come from?
```
[root@linux-foundation ~]# rpm -qf /etc/logrotate.conf
logrotate-3.8.6-17.el7.x86_64
-----
[root@linux-foundation ~]# yum whatprovides /etc/logrotate.conf
Loaded plugins: fastestmirror
Loading mirror speeds from cached hostfile
 * base: mirror-pl.kielcetechnologypark.net
 * elrepo: elrepo.reloumirrors.net
 * epel: ftp.upjs.sk
 * extras: mirror-pl.kielcetechnologypark.net
 * updates: mirror-pl.kielcetechnologypark.net
logrotate-3.8.6-17.el7.x86_64 : Rotates, compresses, removes and mails system log files
Repo        : base
Matched from:
Filename    : /etc/logrotate.conf
```

What files were installed by this package?
```
$ rpm -ql bash
```

Show information about this package.
```
$ rpm -qi bash
$ yum info bash
```

Show information about this package from the package file, not the package database.
```
$ rpm -qip foo-1.0.0-1.noarch.rpm
```

List all installed packages on this system.
```
$ rpm -qa
```

A couple of other useful options are --requires and --whatprovides.

The --requires option will return a list of prerequisites for a package:
```
$ rpm -qp --requires foo-1.0.0-1.noarch.rpm
```

The --whatprovides option will show what installed package provides a particular requisite package:
```
$ rpm -q --whatprovides libc.so.6
$ yum whatprovides libc.so.6
```

