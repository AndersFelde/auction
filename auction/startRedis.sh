#!/bin/bash
systemctl start docker.service
echo "starting docker service"
sudo docker run -p 127.0.0.1:6379:6379 -d redis:5
sudo docker ps
