#### Cloud Managed Kubernetes
- Managed control planes 
- EKS, GKE, AKS, OKE
- Node pools and workload deployment

### Control Plane Components

- API Server
   -- Front door of the cluster
   -- Authentication and validation

- ETCD
    - Distributed key value database 
    - Stores cluster state
    - Importance of backups and replication

- Scheduler 
  - Assigning pods to nodes
  - Resource requests and affinities

- Controller Manager
   - Desired state reconciliation
   - Deployment controller
   - ReplicaSet controller
   - Node controller 

Control loop is the core idea of Kubernetes.   
Deployment controller makes sure that a desired number of pods are always running . If you turn it off manually, deployment controller will bring it up automatically.

- Cloud Controller Manager
  - Bridge between Kubernested and cloud provide
  - Connects cluster with cloud services 
  - Provisions cloud load balancers 
  - Handles cloud infrastructur integration


##### DataPlane Objects  

- Kubelet
   - Node agent
   - Communicating with API server
   - Managing pods and reporting health

- Container Runtime
   - Dockershim removal
   - containerd and CRI-O
- CNI and Networking
   - Container Networking Interface
   - Kubernetes has no default networking plugin
   - Without CNI, pods cannot communicate

- DaemonSet
   - Pod that runs on every node in the cluster
   - Automatically deployed across all nodes 

- kube-proxy
    - Handles Kubernetes service networking
    - Routes service IPs to the correct pods
    - Uses IP tables for traffic routing 


#### Kubernetes Core Objects
- Pod, Services, Ingress, Volume, ConigMap, Secret

Workloads --> Scheduling --> Networking ---> Storage --> Config & Isolation --> Security and Access Control

Pod with Container
with shared network
shared volume

Init, log , pod run with app pod

```
apiVersion: v1
kind: Pod
spec:
  initContainers:
    - name: download-weights
      image: busybox
      command: ["wget", "-O", "/model/weights.bin", "https://storage/model.bin"]
      volumeMounts:
        - name: model-store
          mountPath: /model
  containers:
    - name: inference-server
      image: my-model:v1
      ports:
        - containerPort: 8080
      volumeMounts:
        - name: model-store
          mountPath: /model
    - name: metrics-exporter
      image: prom/node-exporter
  volumes:
    - name: model-store
      emptyDir: {}
    
 ```   

   Replica set and Deployment

   ```
   apiVersion: apps/v1
kind: Deployment
metadata:
  name: web-app
spec:
  replicas: 3
  selector:
    matchLabels:
      app: web  # must match template labels
  template:
    metadata:
      labels:
        app: web
    spec:
      containers:
        - name: web
          image: nginx:1.25
          ports:
            - containerPort: 80
          resources:
            requests:
              cpu: "500m"
              memory: "1Gi"
            limits:
              cpu: "1"
              memory: "2Gi"

   ```

   1. You update the image
   2. Deployment creates a new ReplicaSet
   3. Scales up the new Pods gradually
   4. Scale down the old Pods Gradually


##Manual Scaling
- developer (Kubectl apply)
- deployment YAML
- API Server.. Cluster 

  ###  HPA.. Autoscaling
  
   ```
   apiVersion: autoscaling/v2
kind: HorizontalPodAutoscaler
metadata:
  name: web-app-hpa
spec:
  scaleTargetRef:
    apiVersion: apps/v1
    kind: Deployment
    name: web-app
  minReplicas: 3
  maxReplicas: 20
  metrics:
    - type: Resource
      resource:
        name: cpu
        target:
          type: Utilization
          averageUtilization: 70
    ```

    ###VPA: Instead of adding more pods, VPA changes how much CPU & memory each pod gets by updatin requests and limits
    changes resources Requests & limit pods 
    Pod restarts to apply new values

    VPA controller(Monitorsactual usage over time. Recommends optimal requests and limits).. Mode: Auto
    ||
    |... Update pod spec
    |
    pod


   ## Cluster Autoscalar: Adds nodes when pods can't be scheduled , removes underutilized nodes. Part o the official K8s ecosystem

   It watches for unscheduled pods and idle nodes

   ### KEDA
