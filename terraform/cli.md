# grep and destroy oneliner
```
tf destroy $(tf state list | grep eks | awk  '{print "-target "$0}' | tr "\n" " ")  
```
