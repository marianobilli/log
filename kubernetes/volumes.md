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
