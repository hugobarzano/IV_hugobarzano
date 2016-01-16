#!/bin/bash
sudo apt-key adv --keyserver hkp://p80.pool.sks-keyservers.net:80 --recv-keys 58118E89F3A912897C070ADBF76221572C52609D
echo /etc/apt/sources.list.d/docker.list deb https://apt.dockerproject.org/repo ubuntu-trusty main
sudo apt-get update
sudo apt-get install linux-image-extra-$(uname -r)
sudo apt-get -y install docker-engine
sudo apt-get -y install python-pip
sudo pip install docker-compose
