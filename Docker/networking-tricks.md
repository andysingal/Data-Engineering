```mongodb://host.docker.internal:27017/swfavorites```

<img width="1043" alt="Screenshot 2024-09-14 at 6 13 27 PM" src="https://github.com/user-attachments/assets/23ee14c4-f671-46f1-9849-8c49c1b02f1e">


- docker run -d --name mongodb mongo
- docker container inspect mongodb

```mongodb:172.17.0.2:27017/swfavorites```

<img width="972" alt="Screenshot 2024-09-14 at 6 33 22 PM" src="https://github.com/user-attachments/assets/f859b41f-4fe8-4b86-8c54-096766d0764d">

## Docker network

- ```docker network create favorites-net```
- ```docker run -d --name mongodb --network favorites-net mongo```
- docker run --name favorites --network favorites-net -d --rm -p 3000:3000 favorites-node
