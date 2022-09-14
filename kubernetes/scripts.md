# Update ingress controller annotations
```
#!/bin/bash
echo "Reading namespaces..."
for namespace in $(kubectl get ns | tail -n +2 | awk '{print $1}')
do
    echo "Reading ingresses of namespace $namespace"
    for ingress in $(kubectl get ingress -n $namespace | tail -n +2 | awk '{print $1}')
    do
        auth=$(kubectl get ingress -n $namespace $ingress -o json | jq 'del(.status)' | jq '.metadata.annotations."nginx.ingress.kubernetes.io/auth-url"' -r)
        if [ $auth = "https://another-ldap.ingress-controllers.svc.cluster.local/auth" ]
        then
            echo "Changing $ingress..."
            kubectl get ingress -n $namespace $ingress -o json | jq 'del(.status)' | sed -r "s/(.*local\/auth)/\1?callback=\$host\&use_case=${namespace}/g" > updated_ingress.json
            kubectl apply -f updated_ingress.json
        fi
    done
done
```
