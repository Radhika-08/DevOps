# Advanced Linux Commands

Advanced Linux commands help users monitor system resources, manage processes, inspect network connectivity, and work efficiently in server environments.

----

## ps

Displays currently running processes.

Syntax:

```bash
ps
```

Example Output:

```bash
PID TTY          TIME CMD
1234 pts/0       00:00:00 bash
```

Use Case:

Used to check active processes running on the system.

----

## top

Displays real-time information about running processes and system resource usage.

Syntax:

```bash
top
```

Use Case:

Useful for monitoring CPU and memory consumption.

----

## df -h

Displays disk space usage in a human-readable format.

Syntax:

```bash
df -h
```

Use Case:

Helps identify available and used storage space.

----

## du -sh

Displays the size of a directory.

Syntax:

```bash
du -sh .
```

Use Case:

Useful for checking directory storage usage.

----

## uname -a

Displays detailed system information.

Syntax:

```bash
uname -a
```

Use Case:

Shows kernel version, architecture, and operating system details.

----

## free -h

Displays memory usage information.

Syntax:

```bash
free -h
```

Use Case:

Used to monitor RAM and swap memory.

----

## ping

Tests connectivity between systems.

Syntax:

```bash
ping google.com
```

Use Case:

Used for network troubleshooting.

----

## curl

Transfers data using URLs.

Syntax:

```bash
curl https://example.com
```

Use Case:

Useful for API testing and downloading content.

----

## wget

Downloads files from the internet.

Syntax:

```bash
wget https://example.com/file.zip
```

Use Case:

Used to download files directly from the terminal.

----

## tar

Creates and extracts archive files.

Create Archive:

```bash
tar -cvf backup.tar folder/
```

Extract Archive:

```bash
tar -xvf backup.tar
```

Use Case:

Used for backup and file packaging.

----

## Benefits of Advanced Linux Commands

* Efficient system monitoring
* Better resource management
* Improved troubleshooting
* Essential for server administration
* Widely used in DevOps environments
