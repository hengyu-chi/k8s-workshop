# k8s-workshop
for training

## Install workshop

step1.
```shell
kubectl apply -f deployment.yaml -n $your_namespace
```

step2.
```shell
kubectl apply -f service.yaml -n $your_namespace
```

step3.
```shell
kubectl apply -f ingress.yaml -n $your_namespace
```

Note: you will meet some problem, please try to fix them :)