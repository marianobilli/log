# Empty volumes
```
containers:
  - name: blah
    image: bleh
    volumeMounts:
      - name: aws
        mountPath: /.aws
      - name: tmp
        mountPath: /tmp
volumes:
  - name: aws
    emptyDir: {}
  - name: tmp
    emptyDir: {}
```

# Mount multiple files in configmap to directory
```
containers:
  - name: blah
    image: bleh
    volumeMounts:
      - name: backup-script
        mountPath: /opt/vault
        readOnly: true
volumes:
  - name: backup-script
    configMap:
      name: backup-script
      defaultMode: 0777
      items:
      - key: "backup.sh"
        path: "backup.sh"
      - key: "other.conf"
        path: "other.conf"
```

# python - conda and pip repo config 
```
        containers:
        - name: blah
          image: blah
          volumeMounts:
            - name: python-repos
              mountPath: /etc/pip.conf
              subPath: pip.conf
            - name: python-repos
              mountPath: /root/.condarc
              subPath: .condarc
        volumes:
          - name: python-repos
            configMap:
              name: python-repos
```

## example of pip conf annd .condarc
```
---
apiVersion: v1
kind: ConfigMap
metadata:
  name: python-repos
  namespace: trylab
data:
  pip.conf: |
    [global]
    timeout = 60
    index-url = https://artifactory.your.domain/artifactory/api/pypi/python/simple
    
  .condarc: |
    channel_alias: https://artifactory.your.domain/artifactory/api/conda/conda
    channels:
      - https://artifactory.your.domain/artifactory/api/conda/conda
    default_channels:
      - https://artifactory.your.domain/artifactory/api/conda/conda
```

## PVC directly on Deployments
```
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
            - mountPath: /ebs
              name: ebs
      volumes:
        - name: tmp
          emptyDir: {}
        - name: aws
          emptyDir: {}
      restartPolicy: Always
  volumeClaimTemplates:
  - metadata:
      name: ebs
    spec:
      accessModes:
        - ReadWriteOnce
      resources:
        requests:
          storage: 8Gi
      storageClassName: gp3
```
