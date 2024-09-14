1. ```docker run -p 3000:80 -d --rm (image-id)``` ... ```docker stop image_id```
2. ```docker image inspect (image-id)```
3. ```docker build -t goals:latest .```
4. ```docker run -p 3000:80 -d --rm --name goalsapp goals:latest```
5. ```docker tag node-demo:latest academind/node-hello-world:latest``` --Rename docker image

6. ```docker login ``` ... followed by ```docker push academind/node-hello-world:latest```

## VOLUME [v1](https://headsigned.com/posts/mounting-docker-volumes-with-docker-toolbox-for-windows/)
- docker run -d -p 3000:80 --rm --name feedback-app -v feedback:/app/feedback feedback-node:volumes
- docker run -d -p 3000:80 --rm --name feedback-app -v feedback:/app/feedback -v /app  feedback-node:volumes

``` docker volume --help ```
``` docker volume create --help```
```docker volume inspect {VOLUME_NAME}```

<img width="629" alt="Screenshot 2024-08-29 at 10 17 16 PM" src="https://github.com/user-attachments/assets/78e76aef-1288-47ab-8368-48f5b6f5d8b8">



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
