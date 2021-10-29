# Setup
```
data "aws_eks_cluster" "cluster" {
  name = module.eks_cluster.cluster_id
}

data "aws_eks_cluster_auth" "cluster" {
  name = module.eks_cluster.cluster_id
}
```

# Kubectl delete (eks)
```
resource "null_resource" "delete_default_crb" {
  provisioner "local-exec" {
      command = "kubectl delete clusterrolebinding  eks:podsecuritypolicy:authenticated --server=${data.aws_eks_cluster.cluster.endpoint} --token=${data.aws_eks_cluster_auth.cluster.token} --insecure-skip-tls-verify=true"
    }
    depends_on = [module.eks_cluster]
}
```


# Kubectl apply (eks)
```
resource "null_resource" "apply_kube_system_rb" {
   provisioner "local-exec" {
     command = "kubectl apply -f ./files/kube-system-rb.yaml --server=${data.aws_eks_cluster.cluster.endpoint} --token=${data.aws_eks_cluster_auth.cluster.token} --insecure-skip-tls-verify=true"
   }
   depends_on = [module.eks_cluster]
 }
```

# Appply manifests
## setup
```
terraform {
  required_version = "1.0.7"

  required_providers {
    aws         = ">= 3.57"
    kubernetes  = ">= 2.4.1"
    kubectl = {
      source  = "gavinbunney/kubectl"
      version = ">= 1.11.3"
    }
  }

  backend "s3" {
    bucket         = "tfstate"
    key            = "main.tfstate"
    region         = "eu-west-1"
    dynamodb_table = "terraform-lock"
  }
}

provider "kubernetes" {
  host                   = data.aws_eks_cluster.cluster.endpoint
  cluster_ca_certificate = base64decode(data.aws_eks_cluster.cluster.certificate_authority.0.data)
  token                  = data.aws_eks_cluster_auth.cluster.token
}
```

## Split and apply yaml files
```
data "kubectl_file_documents" "calico" {
  content = file("./files/calico-vxlan.yaml")
}

resource "kubectl_manifest" "calico" {
    for_each   = { for yaml in data.kubectl_file_documents.calico.documents : lower(join("/", compact([yamldecode(yaml).kind, yamldecode(yaml).metadata.name]))) => yaml }
    yaml_body  = each.value
}
```

## apply individual file
```
resource "kubectl_manifest" "ippool" {
    yaml_body = file("./files/ippool.yaml")
}
```
