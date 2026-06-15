# Shell Scripting Basics

Shell scripting is the process of writing a series of Linux commands in a file and executing them automatically.

----

## What is a Shell Script?

A shell script is a text file containing Linux commands executed sequentially by the shell.

Benefits:

* Automation
* Reduced manual work
* Faster execution
* Easy task scheduling

----

## Script 1: Hello World

```bash
#!/bin/bash

echo "Welcome to DevOps Day 02"
echo "Current User: $USER"
date
```

Explanation:

* #!/bin/bash specifies the shell interpreter.
* echo displays text.
* $USER displays the current user.
* date shows the current date and time.

----

## Executing the Script

```bash
chmod +x hello.sh
./hello.sh
```

----

## Script 2: System Information

```bash
#!/bin/bash

echo "System Information"

hostname
whoami
date
uptime
```

Explanation:

* hostname displays system hostname.
* whoami displays current user.
* date displays current date and time.
* uptime displays system running time.

----

## Running the Script

```bash
chmod +x system_info.sh
./system_info.sh
```

----

## Applications of Shell Scripting

* System administration
* Backup automation
* Monitoring systems
* Deployment automation
* CI/CD pipelines

Shell scripting is one of the most important skills for DevOps Engineers.