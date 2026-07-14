nginx.yaml 

```
apiVersion: v1
kind: Pod
metadata:
    name: nginx-2
    labels:
       env: production
spec:
   containers:
       - name: nginx
         image: nginx

```    

postgres.yaml

```
apiVersion: v1
kind: Pod
metadata:
   name: postgres
   labels:
      tier: db-tier
spec:
    containers:
       - name: postgres
         image: postgres
```

v2
```
apiVersion: v1
kind: Pod
metadata:
  name: postgres
  labels:
    tier: db-tier
spec:
  containers:
    - name: postgres
      image: postgres
      env:
        - name: POSTGRES_PASSWORD
          value: mysecretpassword
```

```
kubectl run  redis --image=redis123 --dry-run=client -o yaml > redis.yaml

```
