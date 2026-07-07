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


