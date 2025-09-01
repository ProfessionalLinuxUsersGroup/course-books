<div class="flex-container">
        <img src="https://github.com/ProfessionalLinuxUsersGroup/img/blob/main/Assets/Logos/ProLUG_Round_Transparent_LOGO.png?raw=true" width="64" height="64"></img>
    <p>
        <h1>Unit 1 Lab - Build Standards and Compliance</h1>
    </p>
</div>

> If you are unable to finish the lab in the ProLUG lab environment we ask you `reboot`
> the machine from the command line so that other students will have the intended environment.

### Required Materials

Putty or other connection tool Lab Server

Root or sudo command access

STIG Viewer 2.18 (download from <https://public.cyber.mil/stigs/downloads/> )

#### Downloads

The lab has been provided below. The document(s) can be transposed to
the desired format so long as the content is preserved. For example, the `.txt`
could be transposed to a `.md` file.

- <a href="./assets/downloads/u1/u1_lab.txt" target="_blank" download>📥 u1_lab(`.txt`)</a>
- <a href="./assets/downloads/u1/u1_lab.docx" target="_blank" download>📥 u1_lab(`.docx`)</a>

## Module 1: Exploring System Information

### Exercise 1.1: Familiarizing ourselves with the System

```bash
mount | grep -i noexec

mount | grep -i nodev

mount | grep -i nosuid

# Approximately how many of your mounted filesystems have each of these values?
```

### Exercise 1.2: Checking Mounted Systems

```bash
sysctl -a | grep -i ipv4

sysctl -a | grep -i ipv6

# How many of each are there?
```

```bash
sysctl -a | grep -i ipv4 | grep -i forward

# Does IPv4 forward on interfaces?
```

```bash
lsmod | grep -i tables

# What type of tables exist?
```

## Module 2: PreLAB

1. Download the STIG Viewer 2.18 from - <https://public.cyber.mil/stigs/downloads/>
   ![img](./assets/images/u1/mod2_prelab1.png)

2. Download the STIG for Mariadb and the import it into your STIG viewer.
   ![img](./assets/images/u1/mod2_prelab2.png)

## Module 3: Lab

This lab is designed to have the engineer practice securing a Linux server or service
against a set of configuration standards.
These standards are sometimes called benchmarks, checklists, or guidelines.  
The engineer will be using STIG Viewer 2.18 to complete this lab.

### MariaDB Service configuration:

1. Connect to a hammer server.
2. Install MariaDB.

```bash
dnf install mariadb-server

# Ensure that it is running

systemctl start mariadb

systemctl status mariadb

ss -ntulp | grep 3306
```

- Check and remediate v-253666 STIG.
  ![image](https://github.com/user-attachments/assets/e882e555-773f-43c2-b6df-a12fe34e64eb)

  - What is the problem?
  - What is the fix?
  - What type of control is being implemented?
  - Is it set properly on your system?

  Connect to MariaDB locally.

  ```bash
  mysql
  ```

  Run the SQL command in the STIG's Fix Text section:

  ```sql
  SELECT user, max_user_connections FROM mysql.user;
  ```

  ![image](https://github.com/user-attachments/assets/53984015-72ca-42c1-baa2-28e9a9470e3c)

  Can you remediate this finding?
  ![image](https://github.com/user-attachments/assets/a9410577-7250-421c-acdf-00cc7f54a3f0)

- Check and remediate `v-253677 STIG`
  - What is the problem?
  - What is the fix?
  - What type of control is being implemented?
  - Is it set properly on your system?
- Check and remediate `v-253678 STIG`
  - What is the problem?
  - What is the fix?
  - What type of control is being implemented?
  - Is it set properly on your system?
- Check and remediate `v-253734 STIG`
  - What is the problem?
  - What is the fix?
  - What type of control is being implemented?
  - Is it set properly on your system?

> Be sure to `reboot` the lab machine from the command line when you are done.
