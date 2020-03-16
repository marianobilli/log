# Keytabs from Kerberos Master

A way of obtaining a keytab without knowing the password is to access the kerberos master, login as root and use the `kadmin.local` command to generate the keytab
```
kadmin.local -q 'ktadd -norandkey -k {{ keytab_filename }} {{ item }}'
```

The `{{ item }}` can be any of the principals you can get by running
```
kadmin.local -q 'listprincs'
```

This is especially usefull in hadoop environments with ambari to avoid asking ambari to regenerate keytabs, as it also changes some configurations

tags: `kerberos`, `hadoop`