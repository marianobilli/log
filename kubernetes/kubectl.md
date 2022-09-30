## Deployment oneliner
```
k create deployment awscli --image=amazon/aws-cli --replicas=1 -- sleep infinity
```

## Pod oneliner (with custom serivice account)
```
kubectl run <pod-name> --image=<your_image> --namespace=<your-ns> --overrides='{"spec":{"serviceAccount":"your-service-account"}}' --command -- <your-command>
```

## Pod oneliner (with node selector and taint toleration)
kubectl run <pod-name> --image=<your_image> --namespace=<your-ns> --overrides='{"spec":{"serviceAccount":"default","tolerations":[{"key":"dedicated", "operator":"Equal", "value":"taint-value"}], "nodeSelector":{"label-name":"label-value"}}}' --command -- sleep infinity

## Run a job once from a cronjob definitin 
```
kubectl create job --from=cronjob/<cronhob> <job>
```

## really Get all objects in namespace
```
k get -n {namespace} $(k get-all -n {namespace} | grep -v 'NAME' | awk '{print $1}' | tr '/' ' ' | awk '{print $1}' | tr '\n' ',' | sed 's/.\{1\}$//')
k api-resources --verbs=list --namespaced -o name | xargs -n 1 kubectl get -n <namespace>
k get-all -n <namespace> # Using Krew get-all plugin
```

## Expose service port locally
```
k port-forward service/redis 6379:6379 -n redis
```

## Scale replicas
```
k scale --replicas=5 deployments/<deployment>
```
  
### Scale a bunch of pods
If you cannot use pod selector use the custom output and the grep to filter
```
k get pod -o custom-columns="NAME:.metadata.name,image:.spec.containers[0].image,namespace:metadata.namespace,deployment:metadata.labels.app" -A | grep workspace | awk '{print $4,$3}' | xargs -L 1 bash -c 'kubectl scale deployment $0 --replicas 0 -n $1'
```

## Custom output 
```
k get pod -o custom-columns=NAME:.metadata.name,NodeSelector:.spec.nodeSelector
```
