
How to run adhoc shell commands

```
ansible [group] -i [inventory] -u [user] [--become] [--vault-password-file {file}] [--private-key {file}] -m shell -a '{here goes the command}'
ansible [group] -i [inventory] -u [user] [--become] [--vault-password-file {file}] [--private-key {file}] -m file -a 'path=/blah state=directory mode=0444'
```
