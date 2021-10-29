# Setup
```
data "aws_eks_cluster" "cluster" {
  name = module.eks_cluster.cluster_id
}

data "aws_eks_cluster_auth" "cluster" {
  name = module.eks_cluster.cluster_id
}
```

# Kubectl delete
```
resource "null_resource" "delete_default_crb" {
  provisioner "local-exec" {
      command = "kubectl delete clusterrolebinding  eks:podsecuritypolicy:authenticated --server=${data.aws_eks_cluster.cluster.endpoint} --token=${data.aws_eks_cluster_auth.cluster.token} --insecure-skip-tls-verify=true"
    }
    depends_on = [module.eks_cluster]
}
```


# Kubectl apply
```
resource "null_resource" "apply_kube_system_rb" {
   provisioner "local-exec" {
     command = "kubectl apply -f ./files/kube-system-rb.yaml --server=${data.aws_eks_cluster.cluster.endpoint} --token=${data.aws_eks_cluster_auth.cluster.token} --insecure-skip-tls-verify=true"
   }
   depends_on = [module.eks_cluster]
 }
```
