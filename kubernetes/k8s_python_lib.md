# Basic client setup
I name this file `kubeapi.py`
```
'''Kubernetes api library wrapper'''
import logging
from os import getenv

from kubernetes import client, config

try:
    # read in token automounted from deployment
    f = open("/var/run/secrets/kubernetes.io/serviceaccount/token",
             "r", encoding="UTF-8")
    token = f.read()

    # generate k8s connection config
    configuration = client.Configuration()
    configuration.host = f'https://{getenv("KUBERNETES_SERVICE_HOST")}:{getenv("KUBERNETES_SERVICE_PORT")}'
    configuration.verify_ssl = True
    configuration.ssl_ca_cert = "/var/run/secrets/kubernetes.io/serviceaccount/ca.crt"
    if getenv("LOG_LEVEL", "INFO") == "DEBUG":
        configuration.debug = True
    else:
        configuration.debug = False
    configuration.api_key["authorization"] = "Bearer " + token
    client.Configuration.set_default(configuration)
    logging.debug("K8s config info:")
    logging.debug(configuration.__dict__)
except FileNotFoundError:
    # In case the module is ran locally for debugging
    config.load_kube_config()
    logging.debug("Config loaded from local...")
kubeApi = client.CoreV1Api()
```

# Usage on main.py
```
import kubeapi
```
