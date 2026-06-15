# DevOps Day 02

## Objective

To learn and practice Advanced Linux Commands, Git Branching and Merging, Shell Scripting, CI/CD Fundamentals, and Docker basics. The objective of this task is to gain hands-on experience with version control, automation through scripts, containerization, and modern DevOps workflows.

----

## Topics Covered

### 1. Advanced Linux Commands

Advanced Linux commands are used for system monitoring, resource management, networking, and troubleshooting.

Commands Practiced:

* ps
* top
* df -h
* du -sh
* uname -a
* free -h
* ping
* curl
* wget
* tar

Purpose:

* Monitor running processes
* Check disk usage
* Analyze memory consumption
* Verify network connectivity
* Download files from the internet
* Create and extract archives

----

### 2. Git Branching and Merging

Git branching allows developers to work on different features independently without affecting the main project.

Commands Practiced:

```bash
git branch
git checkout -b feature-branch
git checkout main
git merge feature-branch
git branch -d feature-branch
```

Activities Performed:

* Created a new feature branch
* Switched between branches
* Added changes inside the feature branch
* Merged feature branch into the main branch
* Deleted the merged branch

Benefits:

* Parallel development
* Easier collaboration
* Safe feature implementation
* Better project management

----

### 3. Shell Scripting Basics

Shell scripting helps automate repetitive tasks by executing multiple Linux commands from a single file.

Scripts Created:

#### hello.sh

Displays a welcome message, current user information, and system date.

#### system_info.sh

Displays:

* Hostname
* Username
* Current Date
* System Uptime

Commands Used:

```bash
chmod +x hello.sh
./hello.sh

chmod +x system_info.sh
./system_info.sh
```

Benefits of Shell Scripting:

* Automation of tasks
* Faster execution
* Reduced manual effort
* Useful for system administration
* Essential for DevOps automation

----

### 4. CI/CD Fundamentals

CI/CD stands for Continuous Integration and Continuous Delivery/Deployment.

#### Continuous Integration (CI)

Continuous Integration is the practice of frequently integrating code changes into a shared repository.

Advantages:

* Early bug detection
* Automated testing
* Improved code quality

#### Continuous Delivery (CD)

Continuous Delivery ensures code is always ready for deployment.

Advantages:

* Faster releases
* Reduced deployment risks
* Improved reliability

#### CI/CD Pipeline

```text
Code
 ↓
Build
 ↓
Test
 ↓
Deploy
 ↓
Monitor
```

Common CI/CD Tools:

* Jenkins
* GitHub Actions
* GitLab CI/CD
* Azure DevOps

----

### 5. Introduction to Docker

Docker is a containerization platform used to package applications along with their dependencies.

Docker Concepts Learned:

#### Image

A read-only template used to create containers.

#### Container

A running instance of a Docker image.

#### Dockerfile

A file containing instructions for building Docker images.

Commands Practiced:

```bash
docker --version
docker build -t my-python-app .
docker run my-python-app
docker images
docker ps
```

Files Created:

#### app.py

```python
print("Hello from Docker Container")
```

#### Dockerfile

```dockerfile
FROM python:3.11-slim

WORKDIR /app

COPY app.py .

CMD ["python", "app.py"]
```

Benefits of Docker:

* Consistent environments
* Faster deployments
* Application portability
* Resource efficiency
* Simplified dependency management

----

## Practical Tasks Completed

### Task 1: Create and Manage Git Branches

Completed the following:

* Created a feature branch
* Switched branches
* Committed changes
* Merged branch into main branch
* Deleted feature branch

----

### Task 2: Write Simple Shell Scripts

Created:

* hello.sh
* system_info.sh

Executed both scripts successfully.

----

### Task 3: Containerize a Sample Application Using Docker

Completed the following:

* Created Python application
* Created Dockerfile
* Built Docker image
* Executed Docker container
* Verified application output

----

### Task 4: Push the Project to GitHub

Completed the following:

* Added files to Git
* Committed changes
* Pushed Day02 project to GitHub repository

----

### Task 5: Demonstrate Git Workflow

Demonstrated:

* Branch creation
* Feature development
* Commit process
* Merge process
* Push to remote repository

----

## Project Structure

```text
Day02/
│
├── README.md
├── Advanced-Linux-Commands.md
├── Git-Branching-and-Merging.md
├── Shell-Scripting.md
├── hello.sh
├── system_info.sh
├── app.py
├── Dockerfile
└── Screenshots.pdf
```

----

## Screenshots

Screenshots have been captured for:

* Advanced Linux Commands
* Git Branch Creation
* Git Merge Process
* Shell Script Execution
* Docker Image Build
* Docker Container Execution
* GitHub Repository Push
* Git Workflow Demonstration

----

## Learning Outcomes

Through this task, I learned:

* Advanced Linux system management commands
* Git branching and merging workflow
* Shell scripting fundamentals
* CI/CD concepts and pipeline stages
* Docker image creation and container execution
* Version control best practices
* Basic DevOps workflow implementation

----

## Repository Status

✅ Day 02 DevOps task completed successfully.
