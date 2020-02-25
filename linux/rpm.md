Queries
All rpm inquiries include the -q option, which can be combined with numerous sub-options.

Which version of a package is installed?
```
$ rpm -q bash
```

Which package did this file come from?
```
$ rpm -qf /bin/bash
```

What files were installed by this package?
```
$ rpm -ql bash
```

Show information about this package.
```
$ rpm -qi bash
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
```

To verify all packages on the system
```
rpm -Va
```

Verify specific package
```
rpm -V bash