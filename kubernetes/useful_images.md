# Useful images
```
amazon/aws-cli                # AWS command line client
travelping/nettools:latest    # Network tools such as nslookup, curl, telnet, ping, etc
```

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
