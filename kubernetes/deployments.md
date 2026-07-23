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
