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

# Patch ingress controllers 
```
#!/bin/bash
echo "Reading namespaces..."
for namespace in $(kubectl get ns | tail -n +2 | awk '{print $1}')
# for namespace in "orvoc"
do
    echo "Reading ingresses of namespace $namespace"
    for ingress in $(kubectl get ingress -n $namespace | tail -n +2 | awk '{print $1}')
    # for ingress in "ffanitab-vockol"
    do
        project=$(kubectl get ingress -n $namespace $ingress -o json | jq '.metadata.annotations["nginx.ingress.kubernetes.io/auth-snippet"]' | grep -oE "Lab (\w+) default" | awk '{print $2}')
        user=$(kubectl get ingress -n $namespace $ingress -o json | jq '.metadata.annotations["nginx.ingress.kubernetes.io/auth-snippet"]' | grep -oE 'Ldap-Allowed-Users \\\"(\w+)' | tr -d "\\" | tr -d '"' | awk '{print $2}')
        echo "ingress $ingress, project $project, user $user"
        if [[ -n $user && -n $project && $ingress == *-$project ]]; then
            json_patch=$(sed "s/{PROJECT}/$project/g" patch.json | sed "s/{USER}/$user/g")
            echo $json_patch >> patch_$user-$project.json
            echo $json_patch
            echo "Changing $ingress... with project $project and user $user"
            kubectl patch ingress -n $namespace $ingress --type=json --patch-file patch_$user-$project.json
        fi
    done
done
```
