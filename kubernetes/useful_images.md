# Nettools

```
---
apiVersion: apps/v1
kind: Deployment
metadata:
  name: nettools
  namespace: vault
  labels:
    app: nettools
spec:
  replicas: 1
  selector:
    matchLabels:
      app: nettools
  template:
    metadata:
      labels:
        app: nettools
    spec:
      serviceAccountName: vault-backup
      containers:
        - image: travelping/nettools:latest
          imagePullPolicy: Always
          command:
            - sleep
          args:
            - infinity
          name: nettools
          securityContext:
            allowPrivilegeEscalation: false
            runAsNonRoot: true
            runAsUser: 10001
          resources:
            requests:
              cpu: "100m"
              memory: "32Mi"
            limits:
              cpu: "300m"
              memory: "15Gi"
```
