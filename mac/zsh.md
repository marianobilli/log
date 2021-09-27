# Oh my zsh
```
sh -c "$(curl -fsSL https://raw.github.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"
```

# My plugins
edit `~/.zshrc`
```
plugins=(git docker docker-compose terraform ansible aws brew helm kops kubectl kubectx kube-ps1 nmap pip python vim-interaction zsh-navigation-tools )

source /path/to/kube-ps1.sh
PROMPT='$(kube_ps1)'$PROMPT
kubeoff
```
