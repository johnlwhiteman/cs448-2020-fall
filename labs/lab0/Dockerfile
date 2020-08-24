FROM alpine:latest
RUN apk update
RUN apk add bash
WORKDIR /home
COPY forever forever
ENTRYPOINT ["/bin/bash", "/home/forever"]
