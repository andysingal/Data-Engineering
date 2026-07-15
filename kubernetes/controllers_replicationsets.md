Replication Controller - High Availability - Older technology that has been replaced by replica set

<img width="686" height="490" alt="Screenshot 2026-07-14 at 8 47 09 PM" src="https://github.com/user-attachments/assets/223d19e8-94db-4c5a-ab7c-6172f5c86a09" />

Load Balancing and Scaling

<img width="844" height="486" alt="Screenshot 2026-07-14 at 8 48 15 PM" src="https://github.com/user-attachments/assets/f155dd68-39ad-4474-8227-f5c1c759f9b0" />

rc-definitions.yaml

<img width="986" height="527" alt="Screenshot 2026-07-14 at 8 52 53 PM" src="https://github.com/user-attachments/assets/fb289787-8e50-42a7-b160-00d48953330c" />

```
kubectl create -f rc-definition.yml

### relicationcontroller "myapp-rc" created"

```

```
kubectl get replicationcontroller

```

Replicaset

<img width="458" height="508" alt="Screenshot 2026-07-14 at 8 58 10 PM" src="https://github.com/user-attachments/assets/e044c601-46a2-4ecc-90db-b04fdddac04c" />

```
kubectl create -f replicaset-definition.yml

### replicaset "myapp-replicaset" created

```

```
kubectl get replicaset
```

```
kubectl delete replicaset myapp-replicaset
```

### Labels and Selectors
- monitors the pods
- labeling the pods as a filter , which pods to monitor

### Scale

```

kubectl create -f replicaset-definition.yml

### replicaset "myapp-replicaset" created

or kubectl scale --replicas=6 -f replicaset-definition.yaml

kubectl describe replicaset myapp-replicaset

### to edit
kubectl edit replicaset myapp-replicaset

```

### Commands

<img width="676" height="404" alt="Screenshot 2026-07-14 at 9 06 29 PM" src="https://github.com/user-attachments/assets/97641825-1a00-4f61-933d-fbb286337da7" />



### Demo 




