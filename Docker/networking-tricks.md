```mongodb://host.docker.internal:27017/swfavorites```

<img width="1043" alt="Screenshot 2024-09-14 at 6 13 27 PM" src="https://github.com/user-attachments/assets/23ee14c4-f671-46f1-9849-8c49c1b02f1e">


- docker run -d --name mongodb mongo
- docker container inspect mongodb

```mongodb:172.17.0.2:27017/swfavorites```

<img width="972" alt="Screenshot 2024-09-14 at 6 33 22 PM" src="https://github.com/user-attachments/assets/f859b41f-4fe8-4b86-8c54-096766d0764d">

## Docker network

### Docker Network Drivers
Docker Networks actually support different kinds of "Drivers" which influence the behavior of the Network.

1. The default driver is the "bridge" driver - it provides the behavior shown in this module (i.e. Containers can find each other by name if they are in the same Network).

2. The driver can be set when a Network is created, simply by adding the --driver option.

```docker network create --driver bridge my-net```
3. Of course, if you want to use the "bridge" driver, you can simply omit the entire option since "bridge" is the default anyways.

4. Docker also supports these alternative drivers - though you will use the "bridge" driver in most cases:

i. host: For standalone containers, isolation between container and host system is removed (i.e. they share localhost as a network)

ii. overlay: Multiple Docker daemons (i.e. Docker running on different machines) are able to connect with each other. Only works in "Swarm" mode which is a dated / almost deprecated way of connecting multiple containers

iii. macvlan: You can set a custom MAC address to a container - this address can then be used for communication with that container

iv. none: All networking is disabled.

v. Third-party plugins: You can install third-party plugins which then may add all kinds of behaviors and functionalities



- ```docker network create favorites-net```
- ```docker run -d --name mongodb --network favorites-net mongo```
- ```docker run --name favorites --network favorites-net -d --rm -p 3000:3000 favorites-node```
