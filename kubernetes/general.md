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

Workload bucket Summary: This is the Workload Bucket.. the core of how applications run in Kubernetes

- Pods- Smallest deployable unit in Kubernetes. One or more containers
- Deployment: Manages stateless apps. Handles replicas, updates, rollbacks
- HPA/VPA: Horizontal & Vertical Pod Autoscalers. Scale based on metrics or resource usage
- ClusterAutoscaler: Automatically adds or removes nodes in the cluster
- KEDA: Event driven autoscaling. Scale based on external triggers (queues, metrics, custom events)
- StatefulSet: For stateful applications. Provides stable identifies and persistent storage
- DaemonSet: Runs one pod on every node. USed for node-level agents
- Job: Run a pod to completion. Does the work and exits
- CronJob: Runs Jobs on a schedule(like cron, but Kubernetes native). Great for batch tasks


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

   ### KEDA: Extends HPA to scale on anything, queue depth, request rate, Prometheus metrics, GPU utilization, cloud queue length 

   KEDA = HPA on steroids.. Scale on signal that matters 

  ### Key Components


#### Event Sources:

- Message queue (e.g., RabbitMQ)
- Prometheus metrics
- Cloud queue (e.g., SQS)
- GPU utilization
- HTTP request rate

#### KEDA Operator:

Manages ScaledObject CRD (Custom Resource Definition).
Example configuration:

```yml
ScaledObject CRD
trigger: rabbitmq
queueLength: 5
minReplicas: 1
```

HPA (Extended by KEDA):

- Works with Deployments or ReplicaSets.
- Scales pods based on signals from KEDA.

Deployment/ReplicaSet:

- Target for scaling (e.g., Pod1, Pod2, Pod3, Pod4).
- Pods can be in states like inference or new.


StatefulSet

- db-0/ pvc-db-0
- db-1 (Replica)
- db-2 (Repica)/ pvc-db-2

AI relevance --> Vector databases, model registeries, Kafka, Postgres - all run as StatefulSets


DaemonSet

3 Nodes = 3 Pods
- node-1.. fluentbit.. log collector
- node-3 .. fluentbit log collector
- node-4 .. GPU. H100. 80GB.. fluentbit.. log collector

Running beneath every cluster
- CoreDNS: Service discovery, so pods find each other by name
- Cilium: Networking & Security policy enforcement
- FluentBit: Collects logs from every container on the node
- NodeExporter: Exposes CPU, memory, disk metrics to Prometheus

AI world
GPU drivers: NVIDIA drivers installed on every GPU node(A100, H100)
Device Plugin: Exposes GPUs to Kubernetes scheduler
DCGM exporter: GPU utilization, temp, power metrics


## Job & Cron Job
created --> Running --> Completed --> Done



## Scheduling.. Resource Requests and Lists

Pod Manifest:
```yaml
###manifest.yaml
containers:
  resources:
   requests:
    cpu: 2
    memory: 256Mi
  limits:
    cpu: 4
    memory: 512Mi
```

### Node Selector
- Pod section

Pod: llm-inference
Needs a GPU node to run the model
nodeSelector: gpu=true ✅

- node-1

8 CPU · 32 Gi · no GPU
tier=frontend
region=us-east

- node-2

16 CPU · 64 Gi · no GPU
tier=backend
region=us-east

### Node Affinity

```
affinity:
  nodeAffinity:
    requiredDuringSchedulingIgnoredDuringExecution:
      nodeSelectorTerms:
        - matchExpressions:
            - key: accelerator
              operator: In
              values: ["nvidia-a100", "nvidia-h100"]
    preferredDuringSchedulingIgnoredDuringExecution:
      - weight: 50
        preference:
          matchExpressions:
            - key: topology.kubernetes.io/zone
              operator: In
              values: ["us-east-1a"]
```

- Pod Affinity: It attracts pods together --> to keep training pods on the same rack 
- Anti-Affinity: Pushes (pods) apart > to spread model replica across diferent zones


## Toleration and Taints
- gpu-training-job --- tolerates: gpu=true: NoSchedule , web-frontend.. no tolerance ....> scheduled gpu-node-1 
[image](https://www.youtube.com/watch?v=H_a5DTKSEjY&t=239s)

Topology spread constraint

1. Resource Requests and Limits: Scheduling resource requests or what your pod eeds
2. Node Selector and Node Affinity: For which nodes pod can run on
3. Pod Affinity and Antiaffinity
4. Toleration and Taints: To protect specific nodes
5. Topology spread constraints: For high availability


### Networkings 

Cluster
- node-1. cilium-agent
- node-2... cilium agent

```
helm install cilium cilium/cilium
## cilium-agent deployed to 3 nodes

$kubectl get ds -n kube-sysem

$kubectl get nodes -o wide
```

(Calico, Cilium, Flannel, Windows VPC CNI, Azure CNI)

***CNI gets installed asa daemon set right after cluster creation 

*** Without it, your nodes stay stuck and not ready and no pod even gets an IP


**** Why CNI matter for AI Workloads
- When you run distributed training,
- your pods are constantly exchanging gradients. That's basically gigabits of data flying between pods every second


**** For High-End Training Use cases
Ai clusters use specialized networking, such as Remote Direct memory Access, RoCEv2 or InfiniBand

These plug into Kubernetes through CNIs, which lets a single pod attach to multiple networks ,
one for regular traffic
another for the high speed fabric
between these accelerated compute

Cluster IP:
Service 10.96.0.12 port 80> Target Port 8080---> routes to the pods 

**** To access from your laptop you use Kubectl port-forward temporary tunnel 

-- Node Port: Open on all nodes
-- Load Balancer (selector:
```
selector:
   app: api
   port: 80    .... Which pods to route to
   targetPort: 8080  ... what the service exposes
   typr: LoadBalancer  ... port on the pod
```

Assists with Automatic Load Balancing


### Ingress and Gateway API

Service.. Layer 4.. IPs, Ports

Ingress: Layer-7.. Host based routing, Path based routing, TLS Termination


Ingress Controller (HAProxy, NGINX, Traefik) .. Rules 

Ingress(HTTP) --> Gateway API(HTTP, TCP,gRPC, TLS)


Gateway API.... Infrastructure teams manages the gateway
           ... Application teams manages the HTTP routes


FOR AI Workloads
- Path based Routing lets you serve multiple models rom one endpoint---- /v1/models/llama -> llama-svc:8080 ----> llama-svc, LLama 3. *B. vLLM
                                                                    ... /v1/models/mistral -> mistral-svc:8080 ----> mistral-svc Mistral 7B. TGI

- Canary Rollouts
- gRPC Support : Most Serving Framework such as K-Serve, vLLM... used for high throughput inference


### Storage
1. Persistent Volume the sorage object
2. Peristent Volume Claim.. how you request it
3. StorageClass automates provisioning
4. Container Storage Interface plugin layer connecting Kubernetes to actual storage

- Persistant Volume ... mounted at a path
- Pod created with PVC ... PVC (requests a StorageClass) --> StorageClass (provisioner calls cloud API)
- CSI(Container Storage Interface)... AWS EBS driver, GCP...(Daemon Set.. node plugin(lets kubelet mount volumes).. Deployment.. controller Plugin(talks to the storage backend to create and delete volumes)


## Config Map & Secrets- Holds env variables, config files, command line args

Container Image: ConfigMap (DB=localhost)
                ... ConfigMap DB=staging.internal
                ... ConfigMap DB=prod.internal

Secrets(sensitive data.. passwords, API Keys, TLS certs)... Pod(both injected at runtime)

AI Workloads.. Model Configs(Config Map), Secrets(Hub tokens or Registry creds)


Namespace: team-backend(pods | secrets | configmaps isolated from oter namespaes)
           team-frontend (pods | secrets | configmaps isolated from other namespaces)
           env-prod (same app. prod config own secrets & limits
           env-staging... same app. staging config own serets & limits

Resource Quota... CPU | Memory | Pods | GPUs


## Security and Access Control
- RBAC - Role Based Access Control
- Role Binding: ties Identity to permissions
- Role: read pods create deployments 


           
Blue-Green Deployment

- current
- testing

                
## Resources

[AI-DevOps-Kubernetes-Agent](https://github.com/iam-veeramalla/AI-DevOps-Kubernetes-Agent)


   
