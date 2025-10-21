#!/bin/bash

# Run this script on your Azure VM to prepare it for deployment

echo "Installing Docker and Docker Compose..."

# Update package index
sudo apt-get update

# Install Docker
sudo apt-get install -y docker.io
sudo systemctl start docker
sudo systemctl enable docker

# Add user to docker group
sudo usermod -aG docker $USER

# Install Docker Compose
sudo curl -L "https://github.com/docker/compose/releases/download/v2.20.0/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
sudo chmod +x /usr/local/bin/docker-compose

# Open required ports in firewall
sudo ufw allow 8080  # Flask app
sudo ufw allow 3000  # Grafana
sudo ufw allow 9090  # Prometheus
sudo ufw allow 22    # SSH

echo "Setup complete! Please log out and log back in for docker group changes to take effect."
echo "Required GitHub Secrets to set:"
echo "- AZURE_VM_HOST: Your VM's public IP"
echo "- AZURE_VM_USER: Your VM username"
echo "- AZURE_VM_PRIVATE_KEY: Your SSH private key"
echo "- GRAFANA_PASSWORD: Password for Grafana admin user"
