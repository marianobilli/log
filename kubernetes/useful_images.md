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
<!--       serviceAccountName: <if_needed> -->
      containers:
        - image: travelping/nettools:latest
          imagePullPolicy: Always
          command:
            - sleep
          args:
            - infinity
          name: nettools
          securityContext:
            runAsNonRoot: true
            allowPrivilegeEscalation: false
            readOnlyRootFilesystem: true
            runAsUser: 10001
            runAsGroup: 10001
          resources:
            requests:
              cpu: "100m"
              memory: "32Mi"
            limits:
              cpu: "1"
              memory: "1Gi"
              memory: "1Gi"
```
