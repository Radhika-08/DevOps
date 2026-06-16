# DevOps Day 05

## Objective

The objective of this task is to learn Docker Containerization, CI/CD Pipelines, Cloud Deployment Basics, Monitoring and Logging, and Infrastructure Automation. This task focuses on creating a complete deployment workflow starting from application containerization to deployment, monitoring, backup management, and workflow automation using GitHub Actions.

---

# Topics Covered

## 1. Docker and Containerization

Docker is a containerization platform that enables applications to run consistently across different environments. Containers package application code, dependencies, and configurations together, ensuring portability and reliability.

### Activities Performed

* Created a Flask backend application
* Created a Dockerfile for application packaging
* Built Docker images
* Executed application containers
* Verified container functionality

### Commands Practiced

```bash
docker build -t day05-app .
docker run -d -p 5000:5000 day05-app
docker ps
```

### Benefits

* Consistent application execution
* Simplified deployment process
* Improved portability
* Faster application delivery

---

## 2. CI/CD Pipelines

CI/CD (Continuous Integration and Continuous Delivery/Deployment) automates software development workflows and deployment processes.

### Activities Performed

* Created GitHub Actions workflow
* Configured automated repository validation
* Triggered workflow execution on code push
* Verified successful pipeline execution

### Workflow Created

```text
.github/workflows/deploy.yml
```

### CI/CD Pipeline Flow

```text
Code Commit
      ↓
GitHub Repository
      ↓
GitHub Actions Workflow
      ↓
Validation
      ↓
Deployment Ready
```

### Benefits

* Reduced manual effort
* Faster development cycle
* Improved code quality
* Automated workflow execution

---

## 3. Cloud Deployment Basics

Deployment is the process of making an application available for users. Docker Compose simplifies service deployment and management.

### Activities Performed

* Configured deployment using Docker Compose
* Managed application services
* Verified deployment workflow
* Restarted and monitored deployed services

### Commands Used

```bash
docker compose up -d
docker compose ps
docker compose down
```

### Benefits

* Easy service management
* Reliable deployments
* Simplified scaling
* Faster deployment process

---

## 4. Monitoring and Logging

Monitoring helps track application performance, resource utilization, and operational health. Logging helps identify and troubleshoot issues.

### Activities Performed

* Monitored running containers
* Collected container logs
* Analyzed resource usage
* Verified service health

### Commands Practiced

```bash
docker ps
docker logs day05-web
docker stats
```

### Purpose

* Application health monitoring
* Resource utilization tracking
* Log analysis
* Troubleshooting support

### Benefits

* Improved reliability
* Faster issue detection
* Better operational visibility
* Performance monitoring

---

## 5. Infrastructure Automation

Infrastructure automation reduces manual work and improves consistency by automating operational tasks.

### Activities Performed

* Created backup automation script
* Generated container configuration backups
* Automated infrastructure information collection
* Improved deployment management

### Backup Script

```bash
#!/bin/bash

mkdir -p backups

docker inspect day05-web > backups/container_backup.json

echo "Backup Created Successfully"
```

### Benefits

* Automated backup management
* Reduced operational effort
* Improved disaster recovery readiness
* Consistent infrastructure handling

---

# Practical Tasks Completed

## Task 1: Containerize Backend Application

### Completed

* Developed Flask backend application
* Created Dockerfile
* Built Docker image
* Executed containerized application
* Verified application functionality

---

## Task 2: Create Deployment Workflow

### Completed

* Configured Docker Compose deployment
* Managed service lifecycle
* Verified deployment execution

---

## Task 3: Configure Environment Variables

### Completed

* Created .env file
* Defined application configuration variables
* Verified environment variable usage

### Variables Configured

```env
APP_NAME=DevOps-Day05
ENVIRONMENT=Production
```

---

## Task 4: Set Up GitHub Actions Pipeline

### Completed

* Created GitHub Actions workflow
* Configured automatic workflow execution
* Validated repository structure
* Verified successful workflow completion

---

## Task 5: Deploy Sample Application

### Completed

* Built Docker image
* Started deployment services
* Verified application accessibility
* Confirmed deployment status

---

## Task 6: Configure Monitoring Tools

### Completed

* Monitored active containers
* Viewed application logs
* Analyzed container resource usage
* Verified service health

---

## Task 7: Create Backup Strategy

### Completed

* Developed backup automation script
* Generated container metadata backup
* Verified backup creation process

---

## Task 8: Manage Project Repository

### Completed

* Tracked project changes using Git
* Created commits
* Pushed updates to GitHub repository
* Maintained project version control

---

## Task 9: Document Deployment Processes

### Completed

* Documented deployment workflow
* Documented monitoring procedures
* Documented backup process
* Documented CI/CD implementation

---

## Task 10: Demonstrate Complete Deployment Workflow

### Workflow Demonstrated

```text
Application Development
          ↓
Containerization
          ↓
Docker Image Build
          ↓
Docker Compose Deployment
          ↓
Environment Configuration
          ↓
Monitoring & Logging
          ↓
Backup Creation
          ↓
GitHub Actions Validation
```

### Completed

* Application containerization
* Deployment automation
* Monitoring implementation
* Backup management
* CI/CD workflow execution

---

# Project Structure

```text
Day05/
│
├── README.md
├── Dockerfile
├── app.py
├── requirements.txt
├── .env
├── docker-compose.yml
│
├── .github/
│   └── workflows/
│       └── deploy.yml
│
├── monitoring/
│   └── backup.sh
│
└── Screenshots.pdf
```

---

# Screenshots Included

Screenshots have been captured for:

* Flask Application Creation
* Dockerfile Configuration
* Environment Variables Setup
* Docker Image Build Process
* Container Execution
* Docker Compose Deployment
* Browser Output Verification
* Monitoring Commands
* Container Logs
* Docker Statistics
* Backup Script Execution
* GitHub Actions Workflow
* Successful CI/CD Execution

---

# Learning Outcomes

Through this task, I learned:

* Docker containerization fundamentals
* Backend application deployment
* Environment variable management
* Docker Compose deployment workflow
* GitHub Actions automation
* CI/CD pipeline implementation
* Monitoring and logging practices
* Infrastructure automation concepts
* Backup strategy implementation
* Deployment lifecycle management
* Repository management using Git and GitHub

---

# Conclusion

This task provided hands-on experience in implementing a complete DevOps deployment workflow. Starting from application containerization and deployment to monitoring, backup automation, and CI/CD implementation, the task demonstrated essential DevOps practices used in modern software development environments.

---

# Repository Status

✅ Day 05 DevOps Task Completed Successfully.
