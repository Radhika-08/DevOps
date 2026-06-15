# DevOps Day 03

## Objective

To learn Docker fundamentals, Docker images and containers, environment variables, CI/CD concepts, and deployment basics. The objective of this task is to gain hands-on experience with containerization and modern DevOps practices.

----

## Topics Covered

### 1. Docker Fundamentals

Docker is a containerization platform that allows applications to run consistently across different environments.

Commands Practiced:

* docker --version
* docker info

Purpose:

* Verify Docker installation
* Check Docker configuration
* Understand Docker architecture

----

### 2. Docker Images and Containers

Docker images are read-only templates used to create containers. Containers provide isolated environments for running applications.

Commands Practiced:

```bash
docker build -t my-python-app .
docker run my-python-app
docker images
docker ps -a
```

Activities Performed:

* Created a sample Python application
* Created a Dockerfile
* Built a Docker image
* Executed a Docker container
* Verified container output

Benefits:

* Consistent execution environment
* Simplified application deployment
* Improved portability

----

### 3. Environment Variables

Environment variables help manage application configuration without modifying source code.

File Created:

```text
.env
```

Variables Used:

* APP_NAME
* ENVIRONMENT

Benefits:

* Better configuration management
* Easier environment customization
* Improved application flexibility

----

### 4. CI/CD Pipeline Overview

CI/CD stands for Continuous Integration and Continuous Delivery/Deployment. It is a modern DevOps practice that helps automate the software development lifecycle.

#### Continuous Integration (CI)

Continuous Integration is the process of regularly integrating code changes into a shared repository. It helps detect issues early and improves collaboration among team members.

Benefits:

* Early bug detection
* Improved code quality
* Better team collaboration

#### Continuous Delivery/Deployment (CD)

Continuous Delivery ensures applications are always ready for deployment, while Continuous Deployment automatically releases validated changes to production environments.

Benefits:

* Faster software delivery
* Reduced manual effort
* Consistent deployment process

#### CI/CD Pipeline Flow

```text
Code
 ↓
Build
 ↓
Test
 ↓
Deploy
```

In this task, Docker was used as the foundation for the Build and Deploy stages of the pipeline. Understanding CI/CD concepts is essential for implementing automated DevOps workflows in real-world projects.

----

### 5. Deployment Basics

Deployment is the process of making an application available for execution and use.

Activities Performed:

* Built Docker image
* Executed Docker container
* Verified application output

Benefits:

* Faster application delivery
* Reliable deployment process
* Consistent runtime environment

----

## Practical Tasks Completed

### Task 1: Install and Configure Docker

Completed:

* Verified Docker installation
* Checked Docker configuration
* Validated Docker environment

----

### Task 2: Containerize a Sample Application

Completed:

* Created Python application
* Created Dockerfile
* Built Docker image

----

### Task 3: Create a Dockerfile

Completed:

* Defined base image
* Configured working directory
* Added application file
* Defined container execution command

----

### Task 4: Run and Manage Containers

Completed:

* Executed Docker container
* Verified application output
* Listed available images
* Monitored container status

----

### Task 5: Push Code Changes to GitHub

Completed:

* Added project files to Git
* Created commit
* Pushed project to GitHub repository

----

## Project Structure

```text
Day03/
│
├── README.md
├── Dockerfile
├── app.py
├── .env
└── Screenshots.pdf
```

----

## Screenshots

Screenshots have been captured for:

* Docker Installation Verification
* Dockerfile Creation
* Docker Image Build
* Docker Container Execution
* Environment Variables Configuration
* CI/CD Pipeline Overview
* GitHub Repository Push

----

## Learning Outcomes

Through this task, I learned:

* Docker fundamentals
* Docker image creation
* Container execution and management
* Environment variable configuration
* CI/CD pipeline concepts
* Deployment basics
* GitHub version control workflow

----

## Repository Status

✅ Day 03 DevOps task completed successfully.
