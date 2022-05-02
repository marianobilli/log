# How to debug a pyton program in a remote container

## In the container
```
import debugpy
from os import getenv

if getenv("REMOTE_DEBUG", None):
  debugpy.listen(5678)
```

## Remote container Dockerfile
Has to open the port
```
# In case we want to debug remotely
EXPOSE 5678/tcp
```

## In the deployment
```
spec:
  containers:
    - name: my_container
      image: some_image:latest
      ports:
        - containerPort: 5678
```

## In your computer
```
 kubectl port-forward pod/my-pod-579544f56-hzrng 5678:5678
```

## In vscode
just attach debugger to localhost:5678
