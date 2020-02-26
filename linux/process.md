A way to understand better which processes are running is showing the process tree

Option 1
```
$ ps auxf    # The f will show the tree
```

It can also be filtered by process name
```
$ ps auxf -C bash
```


Option 2
```
ptree -Upa

U for unicode format
p to show process IDs 
a to show command arguments
```
