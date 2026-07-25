<img width="885" height="575" alt="Screenshot 2026-07-23 at 2 54 23 PM" src="https://github.com/user-attachments/assets/e4116a67-e0ad-4583-9208-91c8f90ba3c6" />

<img width="1478" height="852" alt="Screenshot 2026-07-23 at 2 55 46 PM" src="https://github.com/user-attachments/assets/2737ea6f-b237-450a-8121-b1587512d594" />

```
kubectl create -f deployment-definition.yml

kubectl get deployments

kubectl get replicaset

kubectl get pods

kubectl get all

kubectl describe deployment <app>
```

```
apiVersion: apps/v1
kind: Deployment
metadata:
  name: frontend
  labels:
    app: mywebsite
    tier: frontend
spec:
  replicas: 4
  template:
    metadata:
      name: myapp-pod
      labels:
        app: myapp
    spec:
      containers:
        - name: nginx
          image: nginx
  selector: 
     matchLabels:
        app: myapp
```

### commands - Summary

```
kubectl create -f deployment-definition.yml   --- Create

kubectl get deployments  --- Get

-- Update
Kubectl apply -f deployment-definition.yml

kubectl set image deployment/myapp-deployment nginx=nginx:1.9.1

--- Status
kubectl rollout status deployment/myapp-deployment

kubectl rollout history deployment/myapp-deployment

-- Rollback
kubectl rollout undo deployment/myapp-deployment

```

```
kubectl create -f deployment-definition.yml

kubectl rollout status/history deployment/myapp-deployment

kubectl delete deployment myapp-deployment

```

<img width="969" height="231" alt="Screenshot 2026-07-25 at 3 07 40 PM" src="https://github.com/user-attachments/assets/36c305fa-8456-4df2-9fb7-9fa6b2c41fb0" />

<img width="966" height="415" alt="Screenshot 2026-07-25 at 3 13 02 PM" src="https://github.com/user-attachments/assets/967f046b-b58d-435e-a6a2-4a9b6078f643" />

### Recreate

```
kubectl get deployment frontend -o yaml | grep -A5 "strategy:"

kubectl patch deployment frontend --type='json' -p='[{"op":"remove","path":"/spec/strategy/rollingUpdate"},{"op":"replace","path":"/spec/strategy/type","value":"Recreate"}]'

kubectl get deployment frontend -o yaml | grep -A3 "strategy:"
    6  kubectl get deployment frontend -o yaml > frontend.yaml
    7  cat frontend.yaml 
    8  kubectl get deployment frontend -o jsonpath='{.spec.strategy.type}{"\n"}'
    9  kubectl get deployments

```
