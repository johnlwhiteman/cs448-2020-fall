# Docker


## Bash Script

```bash
sudo apt --fix-broken install -y
sudo rm -f /usr/bin/docker-compose
curl -fsSL https://download.docker.com/linux/debian/gpg | sudo apt-key add 
sudo bash -c  "echo 'deb [arch=amd64] https://download.docker.com/linux/debian buster stable' > /etc/apt/sources.list.d/docker.list"
sudo apt-key fingerprint 0EBFCD88
sudo apt-get update
sudo apt-get remove docker docker-engine docker.io containerd runc -y
sudo apt-get update
sudo apt-get install apt-transport-https ca-certificates gnupg-agent software-properties-common -y  
sudo apt-get install docker-ce docker-ce-cli containerd.io -y
sudo docker run hello-world
sudo docker run hello-world
sudo systemctl stop docker
sudo systemctl enable docker
sudo systemctl start docker
sudo curl -L "https://github.com/docker/compose/releases/download/1.25.0/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/


sudo curl -L "https://github.com/docker/compose/releases/latest/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/

docker-compose
sudo chmod +x /usr/local/bin/docker-compose
sudo ln -s /usr/local/bin/docker-compose /usr/bin/docker-compose
docker --version
docker-compose --version
```

# References

https://docs.docker.com/engine/install/ubuntu/


https://github.com/docker/compose/releases/latest