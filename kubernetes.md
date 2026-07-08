Kubernetes: A container orchestration technology that manages and deploys thousands of containers in a cluster

<img width="977" height="502" alt="Screenshot 2026-07-07 at 8 11 45 PM" src="https://github.com/user-attachments/assets/936620b4-73c2-431a-b987-fc7949992339" />

The master watches over the nodes in the cluster and is responsible for the actual orchestration of containers on the worker nodes

Components:

<img width="417" height="335" alt="Screenshot 2026-07-07 at 8 13 41 PM" src="https://github.com/user-attachments/assets/3b6c36d7-7f59-4ae5-9429-277ad2e4bef4" />

etcd: Think of it this way when you have multiple nodes and multiple masters in your cluster, etcd stores. Etcd is responsible for implementing locks within the cluster 
to ensure that there are no conflicts 

Controller: brain behind orchestration. They are responsible for noticing and responding when nodes , containers, or endpoints goes down . Containers make decisions for bringing up new containers


<img width="847" height="476" alt="Screenshot 2026-07-07 at 8 20 12 PM" src="https://github.com/user-attachments/assets/afb3eb5a-722b-4545-8a9f-ed3688a1980b" />





[Docker Containers vs. Kubernetes Pods - Taking a Deeper Look](https://labs.iximiuz.com/tutorials/containers-vs-pods)

### Kubectl

```py
kubectl run hello-minikube
```

```
kubectl cluster-info
```
```
kubectl get nodes
```

```
kubectl run nginx-pod --image=nginx
```

### Pods

<img width="688" height="465" alt="Screenshot 2026-07-06 at 10 23 08 PM" src="https://github.com/user-attachments/assets/a1549bfa-4cb0-4d96-a9c0-f3e12bd57ecb" />

<img width="494" height="385" alt="Screenshot 2026-07-06 at 10 24 32 PM" src="https://github.com/user-attachments/assets/bf02e0b5-1b93-42bf-b736-5655d0daec14" />

```
kubectl get pods --no-headers | wc -l
```
### State
```
kubectl get pod webapp
```
```
kubectl describe pod webapp
```

### YAML
<img width="959" height="570" alt="Screenshot 2026-07-06 at 10 36 27 PM" src="https://github.com/user-attachments/assets/a3fa9fd8-c87b-4533-863d-461307bc616b" />

<img width="425" height="428" alt="Screenshot 2026-07-06 at 10 47 03 PM" src="https://github.com/user-attachments/assets/507b19fc-345e-40c8-be41-79d5b7686b3d" />


## Pods with YAML

<img width="931" height="478" alt="Screenshot 2026-07-06 at 11 11 34 PM" src="https://github.com/user-attachments/assets/987380ca-774d-4eaf-9a4c-b5a9986fc877" />

```
apiVersion: v1
kind: Pod
metadata:
  name: web-pod
  labels:
    app: web
    env: prod
spec:
  containers:
    - name: nginx-container
      image: nginx
```

```
kubectl exec node-api -- printenv APP_COLOR
green
```

Container:

<img width="851" height="530" alt="Screenshot 2026-07-07 at 8 26 07 PM" src="https://github.com/user-attachments/assets/a341f69d-e590-4dfe-a935-6649958c9246" />

<img width="923" height="488" alt="Screenshot 2026-07-07 at 8 31 27 PM" src="https://github.com/user-attachments/assets/9a819172-30ff-4cd6-ac02-b1c6437bb042" />




History: 
<img width="860" height="553" alt="Screenshot 2026-07-07 at 8 25 06 PM" src="https://github.com/user-attachments/assets/4382b8aa-4502-4fd5-ad7a-38002075ee9a" />

