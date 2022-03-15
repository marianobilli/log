## Kubectl
EKS requires a particular kubectl binary, for installation instructions go to [https://docs.aws.amazon.com/eks/latest/userguide/install-kubectl.html](https://docs.aws.amazon.com/eks/latest/userguide/install-kubectl.html)

## Set your kube config
```
aws eks --region <region-code> update-kubeconfig --name <cluster_name>
```
