# Dr. ViKi DevOps Pipeline - Complete CI/CD Solution

##  Assignment Overview
This project demonstrates a complete DevOps pipeline with automated CI/CD, monitoring, and security scanning for a Flask web application deployed on Azure VM.

##  Architecture
- **Application**: Python Flask web app displaying "Hello from Dr. ViKi DevOps Pipeline!"
- **Containerization**: Docker with multi-stage builds
- **CI/CD**: GitHub Actions with automated testing and deployment
- **Infrastructure**: Azure Virtual Machine
- **Monitoring**: Prometheus + Grafana stack
- **Security**: Trivy vulnerability scanning

##  Live Application URLs
- **Web Application**: http://57.159.29.158:8080
- **Grafana Dashboard**: http://57.159.29.158:3000 (admin/password)
- **Prometheus Metrics**: http://57.159.29.158:9090

##  Assignment Deliverables

### Screenshot Locations:
- **Screenshot 1**: GitHub Actions workflow → [Repository Actions Tab](https://github.com/dilliramshah4/sample-app/actions)
  <img width="1903" height="950" alt="Screenshot 2025-10-21 154418" src="https://github.com/user-attachments/assets/3026493f-b965-4109-a3f5-6593b8f772b5" />

- **Screenshot 2**: Live web app → http://57.159.29.158:8080
 <img width="1917" height="865" alt="Screenshot 2025-10-21 154502" src="https://github.com/user-attachments/assets/09c2365a-0ed7-4460-9dc7-3b02dd1f786b" />

- **Screenshot 3**: Grafana monitoring dashboard → http://57.159.29.158:3000
  <img width="1916" height="1007" alt="Screenshot 2025-10-21 161105" src="https://github.com/user-attachments/assets/191be2d7-5bae-4874-9795-86a737596da0" />

- **Screenshot 4**: Docker containers running → SSH to VM: `docker ps`
 <img width="1912" height="856" alt="Screenshot 2025-10-21 161143" src="https://github.com/user-attachments/assets/9529853d-ace7-40a2-af4a-8b09549fa801" />

- **Screenshot 5**: Security scan results → GitHub Actions logs (security-scan job)
 <img width="1908" height="962" alt="Screenshot 2025-10-21 161358" src="https://github.com/user-attachments/assets/879460b0-2f00-4108-8e45-0d0eafa29484" />


##  Technical Implementation

### Step 1: Sample Application
Flask application with timestamp display and health endpoints

### Step 2: Containerization
Docker containerization with Python slim base image for optimal performance

### Step 3: CI/CD Pipeline
- **Build**: Docker image creation
- **Test**: Endpoint testing with curl
- **Security**: Trivy vulnerability scanning
- **Deploy**: Automated deployment to Azure VM

### Step 4: Monitoring Stack
- **Prometheus**: Metrics collection from `/metrics` endpoint
- **Grafana**: Visualization dashboard with custom panels
- **Docker Compose**: Orchestrated monitoring services

### Step 5: Security & Cost Optimization

##  Security Measures Implemented
- Trivy vulnerability scanning in CI/CD pipeline
- SSH key-based authentication for deployment
- GitHub secrets for sensitive data management
- Network security groups with minimal port exposure
- Container security with non-root user execution

##  Cost Optimization Strategies
- **Resource Efficiency**: Using lightweight Python slim base image
- **Auto-scaling**: Can implement Azure VM Scale Sets for traffic-based scaling
- **Resource Scheduling**: Stop/start VMs during off-hours using Azure Automation
- **Container Optimization**: Multi-stage Docker builds to reduce image size
- **Monitoring**: Prometheus metrics help identify resource waste

##  Quick Start Guide

### Prerequisites
- Azure VM with Docker and Docker Compose installed
- GitHub repository with required secrets configured

### Local Testing
Build and run the application locally using Docker commands

### GitHub Secrets Required
- AZURE_VM_HOST: Your Azure VM IP address
- AZURE_VM_USER: VM username
- AZURE_VM_PRIVATE_KEY: SSH private key
- GRAFANA_PASSWORD: Secure password for Grafana

## 📊 Monitoring Queries Available
- Application health monitoring
- Request rate tracking
- Response time metrics
- System performance metrics

##  Tools & Technologies Used
- **CI/CD**: GitHub Actions
- **Containerization**: Docker, Docker Compose
- **Cloud Platform**: Microsoft Azure (Virtual Machine)
- **Monitoring**: Prometheus, Grafana
- **Security**: Trivy vulnerability scanner
- **Web Framework**: Python Flask with Gunicorn
- **Infrastructure**: Ubuntu Linux, SSH, Firewall rules

##  Key Achievements
 Automated CI/CD pipeline with 3-stage workflow  
 Live application deployment with zero-downtime updates  
 Comprehensive monitoring with custom metrics  
 Security scanning integrated into pipeline  
 Cost-optimized infrastructure setup  
 Complete documentation and reproducible setup  

##  Assignment Completion Status
- [x] Flask app with timestamp display
- [x] Docker containerization
- [x] GitHub Actions CI/CD pipeline
- [x] Azure VM deployment
- [x] Prometheus + Grafana monitoring
- [x] Trivy security scanning
- [x] Live URLs accessible
- [x] All screenshots available
- [x] Security and cost optimization documented

## Submission Details
- **GitHub Repository**: https://github.com/dilliramshah4/sample-app
- **Live Application**: http://57.159.29.158:8080
- **Deployment Duration**: Automated deployment in ~3 minutes
- **Monitoring**: Real-time metrics and alerting capability
- **Security**: Vulnerability scanning with every code change

---
*This project demonstrates enterprise-level DevOps practices with automated testing, deployment, monitoring, and security scanning suitable for production environments.*
