
# Krew Plugin manager Installatiion
```
# for ZSH or Bash
(
  set -x; cd "$(mktemp -d)" &&
  OS="$(uname | tr '[:upper:]' '[:lower:]')" &&
  ARCH="$(uname -m | sed -e 's/x86_64/amd64/' -e 's/\(arm\)\(64\)\?.*/\1\2/' -e 's/aarch64$/arm64/')" &&
  curl -fsSLO "https://github.com/kubernetes-sigs/krew/releases/latest/download/krew.tar.gz" &&
  tar zxvf krew.tar.gz &&
  KREW=./krew-"${OS}_${ARCH}" &&
  "$KREW" install krew
)


# add this to .`zshrc
export PATH="${KREW_ROOT:-$HOME/.krew}/bin:$PATH"
```

# Tools
## Context and namespace switch
More info -> https://github.com/ahmetb/kubectx

### Installation
```
$ brew install kubectx

# Remember to cofigure autocompletion
```

### Use
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
### Use
```
> kubectx
```

## to really list all object types
### Installation
```
kubectl krew install get-all
```
### Use
```
kubectl get-all -n <namespace>
```

## whoami
### Installation
```
kubectl krew install whoami
```
### Use
```
kubectl whoami
```
