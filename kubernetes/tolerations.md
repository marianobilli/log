# Tolerations and node selector

```
      .
      .
      .
      nodeSelector:
        dedicated: gpu
      tolerations:
        - key: "dedicated"
          operator: "Equal"
          value: "gpu"
          effect: "NoSchedule"
      containers:
      .
      .
      .
      
```
