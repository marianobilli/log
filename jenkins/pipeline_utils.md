# All available environmental variables in your server
https://your.server/env-vars.html/

# Parameters 
## Multiple choice
```
choice(name: 'env', choices:'int\nqa\nprod\nds', description: 'Environment INT, QA, PROD or DS.')
```

## string
```
string(name: 'server_url', defaultValue: "https://some_host:8000", description: 'The url of the server')

```
They later can used refering to them as `params.env` and `params.server_url`

# Options
some useful options
    options {
        disableConcurrentBuilds()
        buildDiscarder(logRotator(numToKeepStr: '100'))
    }
