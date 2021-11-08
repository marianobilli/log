# Run conatiner and command ad-hoc

## Just run one command
```
kubectl run <pod-name> --image=<your_image>--namespace=<your-ns> --overrides='{"spec":{"serviceAccount":"your-service-account"}}' --command -- <your-command>
```

## Example
```
kubectl run aws-cl --image=amazon/aws-cli --namespace=default --overrides='{"spec":{"serviceAccount":"default"}}' --command -- sleep infinity
kubectl exec -ti aws-cli -- aws sts get-caller-identity
```

# Useful images
```
amazon/aws-cli                # AWS command line client
travelping/nettools:latest    # Network tools such as nslookup, curl, telnet, ping, etc
```
