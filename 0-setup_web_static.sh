#!/usr/bin/env bash
# Sets up web servers for deployment of web_static.

sudo apt-get update
sudo apt-get install -y nginx
mkdir -p /data/web_static/releases
mkdir -p /data/web_static/shared
mkdir -p /data/web_static/releases/test
echo "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua." > /data/web_static/releases/test/index.html
sudo rm -f /data/web_static/current
sudo ln -sf /data/web_static/releases/test /data/web_static/current
sudo sed -i "0,/_;/s//_;\n\n\tlocation \/hbnb_static {\n\t\talias \/data\/web_static\/current\/;\n\t}/" /etc/nginx/sites-enabled/default 
sudo chown -R ubuntu:ubuntu /data/
