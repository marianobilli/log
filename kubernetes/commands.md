# really Get all objects in namespace
```
k get -n {namespace} $(k get-all -n {namespace} | grep -v 'NAME' | awk '{print $1}' | tr '/' ' ' | awk '{print $1}' | tr '\n' ',' | sed 's/.\{1\}$//')
```
