# DevOps Day 04

## Objective

To learn Docker Compose, Environment Configuration, GitHub Workflows, Deployment Concepts, and Monitoring Basics. The objective of this task is to understand multi-container applications, automate workflows using GitHub Actions, manage environment variables, deploy applications using Docker Compose, and monitor running containers.

----

## Topics Covered

### 1. Docker Compose

Docker Compose is used to define and manage multi-container Docker applications using a single YAML file.

Activities Performed:

* Created docker-compose.yml
* Configured multiple services
* Built containers
* Started containers using Docker Compose

Benefits:

* Simplified container management
* Multi-container orchestration
* Easy deployment

----

### 2. Environment Configuration

Environment variables help manage application settings without modifying source code.

File Created:

.env

Variables Configured:

* APP_NAME
* APP_PORT

Benefits:

* Secure configuration management
* Easy environment customization
* Improved portability

----

### 3. GitHub Workflows

GitHub Actions automates software workflows directly from GitHub repositories.

Workflow Created:

ci.yml

Activities Performed:

* Created GitHub workflow
* Automated repository validation
* Triggered workflow on push events

Benefits:

* Automated checks
* Faster development cycle
* CI/CD implementation

----

### 4. Deployment Concepts

Deployment is the process of making an application available for users.

Activities Performed:

* Built Docker images
* Started containers
* Redeployed services using Docker Compose

Commands Used:

```bash
docker compose up -d
docker compose down
```

Benefits:

* Faster releases
* Consistent deployments
* Easy scalability

----

### 5. Monitoring Basics

Monitoring helps track application health and container performance.

Commands Practiced:

```bash
docker ps
docker compose logs
docker stats
```

Purpose:

* Monitor running containers
* Check application logs
* Analyze resource usage

----

## Practical Tasks Completed

### Task 1: Create Multi-Container Setup

Completed:

* Created Docker Compose configuration
* Configured Flask and Nginx containers
* Verified container execution

----

### Task 2: Configure Environment Variables

Completed:

* Created .env file
* Configured application settings
* Verified environment configuration

----

### Task 3: Automate Code Management Using GitHub

Completed:

* Created GitHub Actions workflow
* Automated repository checks
* Verified successful workflow execution

---

### Task 4: Deploy Sample Application

Completed:

* Built Docker image
* Started application containers
* Verified application through browser

----

### Task 5: Document Deployment Steps

Documented:

* Build process
* Deployment process
* Monitoring commands
* GitHub workflow execution

----

## Project Structure

```text
Day04/
│
├── README.md
├── docker-compose.yml
├── .env
├── app/
│   ├── app.py
│   ├── requirements.txt
│   └── Dockerfile
│
├── .github/
│   └── workflows/
│       └── ci.yml
│
└── Screenshots.pdf
```

----

## Learning Outcomes

* Docker Compose fundamentals
* Multi-container deployment
* Environment variable management
* GitHub Actions automation
* Deployment concepts
* Container monitoring basics

----

## Repository Status

✅ Day 04 DevOps task completed successfully.
