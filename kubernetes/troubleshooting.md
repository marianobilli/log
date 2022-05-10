# Useful images
```
amazon/aws-cli                # AWS command line client
travelping/nettools:latest    # Network tools, this nsloolup did not worked with etc/resolv.conf
jonlabelle/network-tools      # Network tools, this nsloolup worked with etc/resolv.conf but not dig
```

# Run conatiner and command ad-hoc
## Just run one command
```
kubectl run <pod-name> --image=<your_image> --namespace=<your-ns> --overrides='{"spec":{"serviceAccount":"your-service-account"}}' --command -- <your-command>
```

## Example
```
kubectl run aws-cl --image=amazon/aws-cli --namespace=default --overrides='{"spec":{"serviceAccount":"default"}}' --command -- sleep infinity
kubectl run nettools --image=jonlabelle/network-tools --namespace=default --overrides='{"spec":{"serviceAccount":"default"}}' --command -- sleep infinity
kubectl run nettools --image=travelping/nettools --namespace=default --overrides='{"spec":{"serviceAccount":"default"}}' --command -- sleep infinity

kubectl exec -ti aws-cli -- aws sts get-caller-identity
```

# Call api from within pod
```
token=$(cat /var/run/secrets/kubernetes.io/serviceaccount/token)
curl -v --insecure -H "Authorization: Bearer $token" https://$KUBERNETES_SERVICE_HOST:$KUBERNETES_PORT_443_TCP_PORT/api/v1/nodes
```


# Run as deployments
```
---
apiVersion: apps/v1
kind: Deployment
metadata:
  name: aws-cli
  namespace: trylab
  labels:
    app: aws-cli
spec:
  replicas: 1
  selector:
    matchLabels:
      app: aws-cli
  template:
    metadata:
      labels:
        app: aws-cli
    spec:
      serviceAccountName: trylab-iam
      containers:
        - image: amazon/aws-cli:latest
          imagePullPolicy: Always
          name: aws-cli
          command:
            - sleep
          args:
            - infinity
          resources:
            requests:
              cpu: "100m"
              memory: "256Mi"
            limits:
              cpu: "300m"
              memory: "512Mi"
          securityContext:
            runAsNonRoot: true
            allowPrivilegeEscalation: false
            readOnlyRootFilesystem: false
            runAsUser: 10001
            runAsGroup: 10001
          volumeMounts:
            - name: tmp
              mountPath: /tmp
            - name: aws
              mountPath: /.aws
      volumes:
        - name: tmp
          emptyDir: {}
        - name: aws
          emptyDir: {}
```

# Force delete a namespace
```
(
NAMESPACE=your-rogue-namespace
kubectl proxy &
kubectl get namespace $NAMESPACE -o json |jq '.spec = {"finalizers":[]}' >temp.json
curl -k -H "Content-Type: application/json" -X PUT --data-binary @temp.json 127.0.0.1:8001/api/v1/namespaces/$NAMESPACE/finalize
)
```
