# Find outdated versions of helm charts
## Source
https://nova.docs.fairwinds.com/

## installation
```
brew tap fairwindsops/tap
brew install fairwindsops/tap/nova
```

## Usage
```
nova find --wide
```

### output
```
Release Name      Chart Name        Namespace         HelmVersion    Installed    Latest     Old     Deprecated
============      ==========        =========         ===========    =========    ======     ===     ==========
goldilocks        goldilocks        goldilocks        3              3.3.1        4.0.1      true    false
metrics-server    metrics-server    metrics-server    3              5.6.0        5.10.10    true    false
redis             redis             redis             3              15.4.1       15.5.5     true    false
```
