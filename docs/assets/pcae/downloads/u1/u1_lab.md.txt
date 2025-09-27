# Unit 1 Lab

## Automation Tools - Installation and Execution

## Required Materials

- Putty or other terminal/connection tool
- Lab Server
- Root or sudo command access

## Lab

This lab is designed to have the engineer verify and execute their automation
tools in a controlled environment.

### Bash Execution

Execute some simple commands within your bash shell.

1. Verify your location and version of bash

   ```bash
   which bash
   /usr/bin/bash --version
   ```

2. Verify your shell PID

   ```bash
   echo $$
   ```

3. Verify your shell variable

   ```bash
   echo $SHELL
   ```

4. Loop over your target servers #Use your target servers
   ```bash
   for server in target1-1 target1-2; do timeout 10 ssh svc_ansible@$server 'uptime'; done
   ```
   Enter your password for svc_ansible from lab guide.

### Python Execution

Test and execute Python.

1. Verify your version of Python

   ```bash
   python3 --version
   ```

2. Test that you can import modules
   ```bash
   python3      # Will drop you into interactive shell
   import os    # Should work with no output
   import numpy # Should not work as you don’t have numpy on the system
   exit()       # Will exit the interactive python3 environment.
   ```

### Ansible Execution

Test and execute Ansible.

1. Verify your version of Ansible

   ```bash
   ansible –version
   ```

2. Check other ansible tools

   ```bash
   ansible- <tab><tab>
   ```

3. Check modules
   ```bash
   ansible-doc -l
   ansible-doc -l | wc -l
   ansible-doc -l | grep -i copy
   ```

