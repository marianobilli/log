some useful options
```
    options {
        disableConcurrentBuilds()
        buildDiscarder(logRotator(numToKeepStr: '100'))
    }
```