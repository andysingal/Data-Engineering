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

```
kubectl run nginx --image=nginx

kubectl get pods

kubectl create deployment nginx --image=nginx

```

### YAML
A YAML file is used to represent data, in this case configuration data.

<img width="959" height="570" alt="Screenshot 2026-07-06 at 10 36 27 PM" src="https://github.com/user-attachments/assets/a3fa9fd8-c87b-4533-863d-461307bc616b" />

<img width="889" height="483" alt="Screenshot 2026-07-09 at 7 42 56 PM" src="https://github.com/user-attachments/assets/deacf608-b88b-450e-94f8-bb010e4ae829" />


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

```
kubectl create deployment hello-minikube --image=kicbase/echo-server:1.0
kubectl expose deployment hello-minikube --type=NodePort --port=8080
```


[minikube](https://minikube.sigs.k8s.io/docs/start/?arch=%2Fmacos%2Farm64%2Fstable%2Fbinary+download#Service)

to scale up, you create new pods, and to scale down you delete existing pods
You do not add additional containers to an existing pod to scale your application 

A single pod can have multiple containers(helper container), except for the fact that they they're usually not multiple containers 

<img width="621" height="398" alt="Screenshot 2026-07-09 at 7 17 26 PM" src="https://github.com/user-attachments/assets/bc9e6f6c-21d3-4b74-a113-bf2fc6f6e94d" />

<img width="985" height="519" alt="Screenshot 2026-07-09 at 7 22 23 PM" src="https://github.com/user-attachments/assets/3e36afef-0084-4a59-987d-402922d93b0a" />

<img width="1000" height="530" alt="Screenshot 2026-07-09 at 7 27 46 PM" src="https://github.com/user-attachments/assets/25f5832e-8d0f-4ed0-a7fe-d46a969668e9" />




Container:

<img width="851" height="530" alt="Screenshot 2026-07-07 at 8 26 07 PM" src="https://github.com/user-attachments/assets/a341f69d-e590-4dfe-a935-6649958c9246" />

<img width="923" height="488" alt="Screenshot 2026-07-07 at 8 31 27 PM" src="https://github.com/user-attachments/assets/9a819172-30ff-4cd6-ac02-b1c6437bb042" />




History: 
<img width="860" height="553" alt="Screenshot 2026-07-07 at 8 25 06 PM" src="https://github.com/user-attachments/assets/4382b8aa-4502-4fd5-ad7a-38002075ee9a" />

