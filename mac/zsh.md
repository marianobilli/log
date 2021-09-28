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

# Theme
https://github.com/romkatv/powerlevel10k#oh-my-zsh

## Install for oh-my-zsh
```
git clone --depth=1 https://github.com/romkatv/powerlevel10k.git ${ZSH_CUSTOM:-$HOME/.oh-my-zsh/custom}/themes/powerlevel10k
```

## Set .zshrc
```
ZSH_THEME="powerlevel10k/powerlevel10k"
```

## set kube-toggle in .zshrc
```
function kube-toggle() {
  if (( ${+POWERLEVEL9K_KUBECONTEXT_SHOW_ON_COMMAND} )); then
    unset POWERLEVEL9K_KUBECONTEXT_SHOW_ON_COMMAND
  else
    POWERLEVEL9K_KUBECONTEXT_SHOW_ON_COMMAND='kubectl|helm|kubens|kubectx|oc|istioctl|kogito|k9s|helmfile|flux|fluxctl|stern'
  fi
  p10k reload
  if zle; then
    zle push-input
    zle accept-line
  fi
}
```
