# secure pods

```
.
.
.
  containers:
    - name: blah
      image: bleh
      securityContext:
        runAsNonRoot: true
        allowPrivilegeEscalation: false
        readOnlyRootFilesystem: true
        runAsUser: 10001
        runAsGroup: 10001
    
```
