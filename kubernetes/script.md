curl-test

```
cat curl-test.sh 
for i in {1..35}; do
   kubectl exec --namespace=kube-public curl -- sh -c 'test=`wget -qO- -T 2  http://webapp-service.default.svc.cluster.local:8080/info 2>&1` && echo "$test OK" || echo "Failed"';
   echo ""
done
```

```
cat curl-pod.yaml 
apiVersion: v1 
kind: Pod
metadata:
  name: curl
  namespace: kube-public 
spec:
  containers:
  - image: byrnedo/alpine-curl:latest
    name: alpine-curl
    command: ["sleep", "5000"]
```

