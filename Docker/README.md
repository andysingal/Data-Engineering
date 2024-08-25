1. ```docker run -p 3000:80 -d --rm (image-id)``` ... ```docker stop image_id```
2. ```docker image inspect (image-id)```
3. ```docker build -t goals:latest .```
4. ```docker run -p 3000:80 -d --rm --name goalsapp goals:latest```
5. ```docker tag node-demo:latest academind/node-hello-world:latest``` --Rename docker image

6. ```docker login ``` ... followed by ```docker push academind/node-hello-world:latest```
