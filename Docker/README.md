1. ```docker run -p 3000:80 -d --rm (image-id)``` ... ```docker stop image_id```
2. ```docker image inspect (image-id)```
3. ```docker build -t goals:latest .```
4. ```docker run -p 3000:80 -d --rm --name goalsapp goals:latest```
5. ```docker tag node-demo:latest academind/node-hello-world:latest``` --Rename docker image

6. ```docker login ``` ... followed by ```docker push academind/node-hello-world:latest```

## VOLUME [v1](https://headsigned.com/posts/mounting-docker-volumes-with-docker-toolbox-for-windows/)
- docker run -d -p 3000:80 --rm --name feedback-app -v feedback:/app/feedback feedback-node:volumes
