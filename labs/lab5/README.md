# LAB 5

## Docker commands

### Build the Docker image
```
$ docker build --rm -t cs448/lottery .
```

### List Docker images
```
$ docker image ls
```

### Run the Docker image
```
$ docker run cs448/lottery <password>
```

### List all Docker containers
```
$ docker container ls -a
```

### Delete a specific Docker image by CONTAINER ID
```
$ docker container rm <CONTAINER ID>
```

### Delete a specific Docker image by IMAGE ID
```
$ docker rmi <IMAGE ID>
```

### Inspecting a container
```
docker inspect cs448/lottery | grep PWD
```

### Remove stuff that hasn't been running for awhile
```
$ docker container prune
$ docker image prune
```
