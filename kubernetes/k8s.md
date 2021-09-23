# Deployment from Cli
```
kubectl create deployment pingtest --image=amazon/aws-cli --replicas=1 -- sleep infinity
```


### Find all objects in a namespace
```
kubectl api-resources --verbs=list --namespaced -o name | xargs -n 1 kubectl get -n <namespace>
```

### Scale replicas
```
kubectl scale --replicas=5 deployments/<deployment>
```
