## Context and namespace switch
More info -> https://github.com/ahmetb/kubectx

### Installation
```
$ brew install kubectx

# Remember to cofigure autocompletion
```

### Usage
```
$ kubectx arn:aws:eks:eu-west-1:356003666994:cluster/sbx        # This will switch context to sbx clustervim .b
$ kubens kube-system                                            # This will switch namespace to kube-system
```

## Tail multiple pods
More info -> https://github.com/johanhaleby/kubetail

### Installation
```
brew tap johanhaleby/kubetail && brew install kubetail
```
### Usage
```
> kubectx
```
## Kubernetes prompt
More info -> https://github.com/jonmosco/kube-ps1

### Installation
```
$ brew install kube-ps1
```

### .bash_profile setup
```
source /usr/local/opt/kube-ps1/share/kube-ps1.sh
PS1='[\u@\h \W $(kube_ps1)]\$ '
kubeoff
```
### Usage
```
# To activate the kube prompt simply run
$ kubeon

# To deactivate
$ kubeoff
```
