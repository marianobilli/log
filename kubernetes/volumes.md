```
containers:
  - name: blah
    image: bleh
    volumeMounts:
      - name: aws
        mountPath: /.aws
      - name: tmp
        mountPath: /tmp
      - name: backup-script
        mountPath: /opt/vault
        readOnly: true
volumes:
  - name: aws
    emptyDir: {}
  - name: tmp
    emptyDir: {}
  - name: backup-script
    configMap:
      name: backup-script
      defaultMode: 0777
      items:
      - key: "backup.sh"
        path: "backup.sh"
```
