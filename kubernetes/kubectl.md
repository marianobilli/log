## Deployment oneliner
```
k create deployment awscli --image=amazon/aws-cli --replicas=1 -- sleep infinity
```

## Pod oneliner (with custom serivice account)
```
kubectl run <pod-name> --image=<your_image> --namespace=<your-ns> --overrides='{"spec":{"serviceAccount":"your-service-account"}}' --command -- <your-command>
```

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

## Custom output 
```
k get pod -o custom-columns=NAME:.metadata.name,NodeSelector:.spec.nodeSelector
```
