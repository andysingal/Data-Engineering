Minikube

```
# Install Minikube (latest 1.33.x series)
curl -LO https://storage.googleapis.com/minikube/releases/latest/minikube-linux-amd64
sudo install minikube-linux-amd64 /usr/local/bin/minikube

# Verify the podman driver is available
minikube driver list
# You should see “podman” under the “Available” column.
```

| Section | What you’ll do |
|---------|----------------|
| **0️⃣ Pre‑flight** | Verify `podman`, `minikube`, `helm`. |
| **1️⃣ Clean any existing Minikube/K3s** | Stop & delete old Minikube, optionally stop the manual K3s. |
| **2️⃣ Start Minikube with the Podman driver** | Spin up a fresh K3s node inside a Podman container. |
| **3️⃣ Verify storage class** | Confirm `local‑path` is present (the default). |
| **4️⃣ Pull the Ollama image with Podman & load it into Minikube** | Avoid long pulls on every redeploy. |
| **5️⃣ Add the official Ollama Helm repo** | One‑liner to get the chart. |
| **6️⃣ Create a custom Helm `values.yaml` (CPU‑only)** | Disable GPU, point PVC to `local‑path`, set resources. |
| **7️⃣ Install (or upgrade) the chart** | Helm creates Namespace, PVC, Deployment, Service. |
| **8️⃣ Wait for the pod, test the API** | Verify the server is up and can generate text. |
| **9️⃣ Troubleshooting cheat‑sheet** | Common “stuck in Pending / ContainerCreating” reasons. |
| **🔚 Clean‑up** | How to tear everything down. |

1.  Initialize Minikube with Podman

First, you need to spin up your local cluster by explicitly targeting Podman as the virtualization driver

```
# Start Minikube using Podman and CRI-O container runtime
minikube start --driver=podman --container-runtime=cri-o

# Optional: Set Podman as your permanent default driver
minikube config set driver podman
```

2. Configure Your Target Namespace

Isolate your AI components by spinning up a specific namespace inside the cluster

```
sudo vi /etc/containers/containers.conf

[engine]
runtime = "runc"

```

Clear Out Existing Residual States

```
sudo podman volume rm minikube --force
minikube delete --all --purge
rm -rf ~/ollama-models
sudo rm -rf /opt/models
```

### Download and Prepare the Data Layout on Host

```
# 1. Create the system storage directories
sudo mkdir -p /opt/models
mkdir -p ~/ollama-models/gemma4-26b-local

# 2. Pull the model binary directly from Hugging Face
cd ~/ollama-models/gemma4-26b-local
wget https://huggingface.co/google/gemma-4-26B-A4B-it-qat-q4_0-gguf/resolve/main/gemma-4-26B-it-mmproj.gguf

# 3. Relocate the large binary payload to your system folder
sudo mv gemma-4-26B-it-mmproj.gguf /opt/models/

# 4. Enforce strict ownership permissions for your active 'ubuntu' user account
sudo chown -R ubuntu:ubuntu /opt/models
sudo chown -R ubuntu:ubuntu ~/ollama-models
```

#### Create the Modelfile on Host
Write the model parsing parameters file inside your active ~/ollama-models/gemma4-26b-local directory:

```
cat << 'EOF' > Modelfile
FROM /opt/models/gemma-4-26B-it-mmproj.gguf

PARAMETER temperature 0.7
PARAMETER top_p 0.9
PARAMETER num_ctx 8192

TEMPLATE """{{ .Prompt }}"""
EOF
```

#### Start Minikube forcing Directory Mounts
```
Isolate your proxy environment variables and boot the cluster layout with host mounts active:
# Bypass corporate proxy limits for internal cluster addressing
export NO_PROXY="$NO_PROXY,192.168.49.2,10.42.0.0/16,10.43.0.0/16"

# Spin up Minikube pointing straight to your host storage blocks
minikube start --driver=podman --container-runtime=cri-o --cpus=4 --memory=8192 \
  --mount \
  --mount-string="/opt/models:/opt/models" \
  --mount-string="/home/ubuntu/ollama-models:/root/ollama-models"
```

### Create the Kubernetes Manifest
```
cat << 'EOF' > ollama-local.yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: ollama
  namespace: ollama
  labels:
    app: ollama
spec:
  replicas: 1
  selector:
    matchLabels:
      app: ollama
  template:
    metadata:
      labels:
        app: ollama
    spec:
      containers:
        - name: ollama
          image: ollama/ollama:latest
          imagePullPolicy: IfNotPresent
          env:
            - name: OLLAMA_MODELS
              value: /root/ollama-models/.ollama/models
          ports:
            - containerPort: 11434
              name: api
          volumeMounts:
            - name: host-models
              mountPath: /opt/models
            - name: host-workspace
              mountPath: /root/ollama-models
      volumes:
        - name: host-models
          hostPath:
            path: /opt/models
        - name: host-workspace
          hostPath:
            path: /root/ollama-models
---
apiVersion: v1
kind: Service
metadata:
  name: ollama
  namespace: ollama
spec:
  type: ClusterIP
  ports:
    - port: 11434
      targetPort: 11434
      protocol: TCP
      name: api
  selector:
    app: ollama
EOF
```
Apply the deployment manifest directly yo Kubernetes

```
kubectl create namespace ollama
kubectl apply -f ollama-local.yaml
```
#### Exec into the Container and Run Offline
```
# 1. Fetch your active container pod name and enter its shell
POD_NAME=$(kubectl get pods -n ollama -l app=ollama -o jsonpath="{.items[0].metadata.name}")
kubectl exec -it $POD_NAME -n ollama -- /bin/bash
```
```
# 2. Instruct the shell window profile to look at your persistent folder storage path
export OLLAMA_MODELS=/root/ollama-models/.ollama/models

# 3. Enter your mounted configuration workspace
cd /root/ollama-models/gemma4-26b-local

# 4. Compile the local GGUF model binary (Takes a while to process)
ollama create gemma4-26b-local -f Modelfile

# 5. Launch your completely offline command line chat interface!
ollama run gemma4-26b-local
```



