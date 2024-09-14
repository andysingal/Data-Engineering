1. ```docker run -p 3000:80 -d --rm (image-id)``` ... ```docker stop image_id```
2. ```docker image inspect (image-id)```
3. ```docker build -t goals:latest .```
4. ```docker run -p 3000:80 -d --rm --name goalsapp goals:latest```
5. ```docker tag node-demo:latest academind/node-hello-world:latest``` --Rename docker image

6. ```docker login ``` ... followed by ```docker push academind/node-hello-world:latest```

## VOLUME [v1](https://headsigned.com/posts/mounting-docker-volumes-with-docker-toolbox-for-windows/)

1. Containers can read + write data. Volumes can help with data storage. Bind Mounts can help with direct container interaction
2. Containers can read + write data, but written data is lost if the container is removed
3. Volumes are folders on the host machine, managed by docker, which are mounted into the COntainer
4. Named Volumes survive container removal and can therefore be used to store persistent data
5. Anonymous Volumes are attached to a container to save (temporary) data inside the container
6. Bind Mounts are folders on the host machine which are specified by the user and mounted into containers-like Named Volumes
7. Build Arguments and Runtime Environment variables can be used to make images and containers more dynamic/configurable

- ```docker run -d -p 3000:80 --rm --name feedback-app -v feedback:/app/feedback feedback-node:volumes```
- ```docker run -d -p 3000:80 --rm --name feedback-app -v feedback:/app/feedback -v /app  feedback-node:volumes```

- ``` docker volume --help ```
- ``` docker volume create --help```
- ```docker volume inspect {VOLUME_NAME}```

<img width="629" alt="Screenshot 2024-08-29 at 10 17 16 PM" src="https://github.com/user-attachments/assets/78e76aef-1288-47ab-8368-48f5b6f5d8b8">


*** WORKING WITH AGUMENTS & ENVIRONMENT VARIABLES  
```
ARG DEFAULT_PORT=80

ENV PORT $DEFAULT_PORT

EXPOSE $PORT
```
```-e PORT=8000``` *** if you create .env just mention --env-file ./.env [.env...PORT=8000] in the command line 

or
```
docker build -t feedback-node:dev --build-arg DEFAULT_PORT=8000 .
```

*** NETWORKING: Container Communication
<img width="794" alt="Screenshot 2024-09-14 at 5 04 26 PM" src="https://github.com/user-attachments/assets/1c55df51-928e-4169-9934-a9c1a7d7035b">


EXAMPLES to foloow:
```
export STORAGE_LOCATION=$HOME/anythingllm && \
 mkdir -p $STORAGE_LOCATION && \
 touch "$STORAGE_LOCATION/.env" && \
 docker run -d -p 3001:3001 \
 --cap-add SYS_ADMIN \
 -v ${STORAGE_LOCATION}:/app/server/storage \
 -v ${STORAGE_LOCATION}/.env:/app/server/.env \
 -e STORAGE_DIR="/app/server/storage" \
 mintplexlabs/anythingllm
```

reference:
- https://docs.anythingllm.com/installation/desktop/macos 
