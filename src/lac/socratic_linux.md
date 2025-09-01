## Socratic Linux

<details>
<summary>Can you list the number of CPUs?</summary>

- `lscpu`
- `nproc`
- `cat /proc/cpuinfo | grep -i proc`
- `python3 -c "import multiprocessing as mp; print(mp.cpu_count())"`
</details>

<details>
<summary>Can you tell me the speed in MHz?</summary>

- `dmesg | grep -i mhz`
- `lscpu`
- `cat /proc/cpuinfo`
</details>

<details>
<summary>Can you tell me the manufacturer of the chip?</summary>

- `lscpu`
- `cat /proc/cpuinfo`
- `lshw | grep -i intel`
</details>

<details>
<summary>Can you tell the architecture of this chip?</summary>

- `lscpu`
- `uname -m `
</details>

<details>
<summary>Can you tell me if this system is physical or virtual?</summary>

- `lshw -C system`
- `dmidecode -s system-manufacturer`
- `virt-what`
- `lspci #look for something like QEMU`
- `systemd-detect-virt`
</details>

<details>
<summary>Can you spin up the CPU to high load for 3 minutes?</summary>

- `stress -c 4 --timeout 180`
- `for i in $(seq 100); do dd if=/dev/urandom bs=1024k count=5000 | bzip2 -9 > /dev/null & done`
- `openssl speed -multi $(nproc)`
</details>

## Memory Topics

<details>
<summary>Can you tell me how much RAM we have?</summary>

- `free -m`
- `cat /proc/meminfo`
- `htop`
- `neofetch`
</details>

<details>
<summary>Can you tell me how much RAM we have used?</summary>

- `free -m`
- `htop`
</details>

<details>
<summary>Can you tell me how much swap we have?</summary>

- `free -m`
</details>

<details>
<summary>Can you free all of the cached memory?</summary>

- `echo 3 > /proc/sys/vm/drop_caches`
</details>

<details>
<summary>Can you generate high memory load for 3 minutes?</summary>

- `stress --vm 4 --timeout 180s`
</details>

## Filesystem Topics

<details>
<summary>Can you show all of the used space of the / (root) partition?</summary>

- `df -h /`
- `lsblk -f `
</details>

<details>
<summary>Can you show all of the inodes of the / (root) partition?</summary>

- `df -i /`
</details>

<details>
<summary>Can you show the used space of the directory you're in?</summary>

- `du -sh .`
</details>

<details>
<summary>Can you show all processes in the directory you're in?</summary>

- `lsof .`
</details>

<details>
<summary>Check long listing of files, do you know the permissions?</summary>

- `ls -ld #Directory or file`
</details>

<details>
<summary>Can you create 3 hard links to a file?</summary>

- `Yes -  ln /tmp/testfile /tmp/otherfile1`
</details>

<details>
<summary>Can you hard link to a file across filesystem boudary?</summary>

- `No`
</details>

<details>
<summary>Cat out the file that defines mount points in the system?</summary>

- `cat /etc/fstab`
- `cat /etc/mtab`
</details>

<details>
<summary>Speed tests of writes and reads</summary>

- `for i in $(seq 5); do echo "I am writing $i file"; time dd if=/dev/zero of=bigfile$i bs=4096k count=250; done`
- `for i in $(seq 5); do echo "I am reading $i file"; time dd if=bigfile$i of=/dev/null; done`
</details>

<details>
<summary>Can you show all the interfaces?</summary>

- `ip a`
- `ip addr `
- `ifconfig`
- `ip -br a`
</details>

<details>
<summary>Can you show that the interface is connected physically?</summary>

- `ethtool enp1s0`
</details>

<details>
<summary>Can you determine default route?</summary>

- `ip r`
- `route`
</details>

<details>
<summary>Can you ping the default gateway 3 times?</summary>

- `ping -c3 172.30.1.1`
</details>

<details>
<summary>Can you determine the MTU of the network with ping?</summary>

- `ip addr #To see MTU`
- `ping -c1 -s 1500 -M do www.yahoo.com`
</details>

<details>
<summary>Can you identify all your IPv4 and IPv6 networks? IPv4? IPv6? Both?</summary>

- `ip addr` - `IPv4 - enp1s0 docker0` - `IPv6 - Calico` - `Both - lo flannel.1`
</details>

<details>
<summary>Can you list your open ports?</summary>

- `netstat -ntulp`
- `ss -ntulp`
- `lsof -i :22`
</details>

<details>
<summary>Can you prove that your DNS is working?</summary>

- `ping anything by name outside of network.`
- `nslookup`
- `host`
- `dig `
</details>

<details>
<summary>What file do we edit to change service to port number mapping?</summary>

- `/etc/services`
</details>

<details>
<summary>Can we connect to another server and test for an open port?</summary>

- `telnet`
- `nc -vz node01 22`
- `timeout 3 nc node01 22`
</details>

<details>
<summary>Can you connect to another server with ssh and show debug 3 levels?</summary>

- `ssh -vvv node01 'uptime'`
</details>

<details>
<summary>Can we verify that nothing is blocking us to www.google.com?</summary>

- `curl www.google.com`
</details>

<details>
<summary>Can you copy a file from this server to another and back?</summary>

- `scp <local file> remotenode:/<filesystem>   #Send`
- `scp remotenode:/<filesystem> <local file>    #Pull`
</details>

<details>
<summary>Can we capture all the packets between interfaces and put them in file?</summary>

- `tcpdump ip host controlplane and node01 -c 10000 -i enp1s0 -w /tmp/wireshark1.pcap`
</details>

<details>
<summary>Can we test the speed between two systems?</summary>

- `iperf3` - `One node will function as the server - iperf3 -c` - `The other will test speed to it - iperf3 <nameofserver>`
</details>

<details>
<summary>Can we show all the hops between us and google?</summary>

- `traceroute www.google.com`
</details>

<details>
<summary>Can you show all the TCP/IP errors on an interface over one minute?</summary>

- `sar -n TCP,ETCP 60`
- `ifconfig `
</details>

<details>
<summary>Can you list the Doom port?</summary>

- `grep -i doom /etc/services`
</details>

<details>
<summary>Can you read from port 22 and see the banner information of the connection?</summary>

- `nc 127.0.0.1 22`
</details>

## Disk Topics

<details>
<summary>How do you check how many disks you have?</summary>

- `lsblk`
- `lsblk -f`
- `fdisk -l`
- `ls -l /dev/disk/by-*`
- `blkid`
</details>

<details>
<summary>How do you check how many disk partitions you have?</summary>

- `lsblk`
- `lsblk -f`
- `fdisl -l | grep -i vd`
</details>

<details>
<summary>How do you check which filesystems are on which partitions?</summary>

- `lsblk`
- `lsblk -f   #more information`
- `mount`
- `findmnt`
- `mount | grep -iE "ext4|xfs"`
</details>

<details>
<summary>Can you check for partitions that aren't even mounted for FS Types?</summary>

- `lsblk -f`
</details>

<details>
<summary>Can you check disk I/O over time?</summary>

- `bwm-ng -i disk`
- `iostat -d 1      #One second iterations forever`
- `iostat -d 1 10   #10 one second iterations`
- `iostat -xz       #Only things that have activity`
- `iotop            #By process I/O to disk`
</details>

<details>
<summary>Can you verify disk read and write speed?</summary>

- `for i in $(seq 5); do echo "I am writing $i file"; time dd if=/dev/zero of=bigfile$i bs=4096k count=250; done`
- `for i in $(seq 5); do echo "I am reading $i file"; time dd if=bigfile$i of=/dev/null; done`
</details>

## Security Topics

<details>
<summary>What users have logged into the system in the last 24 hours?</summary>

- `last | more`
- `last | tac`
- `lastlog | grep -v Never`
</details>

<details>
<summary>Can you tell what pid is listening on port 22?</summary>

- `ss -ntulp | grep 22`
- `ps -ef | grep -i sshd`
- `systemctl status sshd`
- `lsof -i :22`
</details>

<details>
<summary>Can you show how systemd started sshd?</summary>

- `systemctl status ssh`
- `systemctl cat ssh`
- `systemd-analyze critical-chain ssh.service`
</details>

<details>
<summary>Can you list the kernel modules?</summary>

- `lsmod`
</details>

<details>
<summary>Can you verify that a file has not changed in the last 3 days?</summary>

- `stat /etc/crontab`
- `Hashing function? #Tripwire`
</details>

<details>
<summary>Can you verify the hash of a file before and after you push it to another server?</summary>

- `md5sum /etc/crontab; scp /etc/crontab node01:/tmp/crontab; ssh node01 'md5sum /tmp/crontab'`
</details>

<details>
<summary>Can you encrypt a file with vi?</summary>

- `vi -x /tmp/somefile`
</details>

<details>
<summary>For any user can you determine their sudo permissions?</summary>

- `sudo -l -U scott`
</details>

<details>
<summary>For all users can you list a count of what default shells they have?</summary>

- `cat /etc/passwd | awk -F: '{print $7}' | sort | uniq -c`
- `cat /etc/passwd | awk -F: '{print $NF}' | sort | uniq -c`
</details>

<details>
<summary>Can you verify an individual user's limits of open files?</summary>

- `ulimit -a -u scott`
</details>

<details>
<summary>Where do you change user limits?</summary>

- ` vi /etc/security/limits.conf`
</details>

## General System

<details>
<summary>Can you show me how the system was booted by grub?</summary>

- `dmesg | head`
- `cat /proc/cmdline`
- `journalctl`
</details>

<details>
<summary>Can you tell me the running kernel version?</summary>

- `uname -r`
- `dmesg -k | head`
- `cat /proc/version`
- `cat /proc/cmdline`
</details>

<details>
<summary>Can you tell me how many older versions of the kernel are available?</summary>

- `ls -l /boot/vm*`
- `apt list --installed | grep linux-image`
</details>

<details>
<summary>Can you show that the ssh(d) server is running?</summary>

- `systemctl status ssh`
- `ps -aux | grep ssh`
- `ss -ntulp | grep -i ssh`
- `lsof -i : 22`
- `nc 127.0.0.1 22`
</details>

<details>
<summary>Can you show how the SSH(d) process was started? What's the parent process?</summary>

- `ps faux | grep -i ssh`
- `systemctl status ssh`
- `pstree -s -p <pid>`
- `ps -afg`
<details>
<summary>Can you edit the file that changes which kernel the system boots to?</summary>

- `view /etc/grub/grub.conf`
</details>

<details>
<summary>Can you tell me the version of Linux you're on?</summary>

- `cat /etc/*release`
- `lsb_release -a`
</details>

<details>
<summary>Can you describe the 7 fields of the /etc/passwd?</summary>

- `Yes`
  - `Colon Delimeted `
    Username : Password : UID : Primary Group GUID : Comment : Home : Default Shell

<details>
<summary>Can you show me all the unique shells in /etc/passwd</summary>

- `cat /etc/passwd | awk -F: '{print $7}' | sort | uniq -c`
</details>

<details>
<summary>Can we set one variable that is inherited by child processes and one that is not, and then prove it?</summary>

- `dino=rawr   #not inherited`
- `export dino2=rawr2    #is inherited`
</details>

<details>
<summary>Can you set a process to run every 5 minutes on a server?</summary>

- `*/5 * * * * 'echo "I love Linux" | wall'`
</details>

<details>
<summary>What is the user's home directory? What is Root's home directory?</summary>

- `Users: /home/<username>`
- `Root: /root`
</details>

<details>
<summary>Can you show all the aliases your user has available?</summary>

- `alias`
</details>

<details>
<summary>Can you create or remove an alias?</summary>

- `unalias`
- `alias`
</details>

<details>
<summary>Can you tell if the user has a password set?</summary>

- `grep scott /etc/shadow`
- `chage -l scott`
</details>

<details>
<summary>Can you create an alias and make it permanent?</summary>

- `.bashrc or /etc/profile.d`
</details>

<details>
<summary>Do you know where the default user home directory files populate from?</summary>

- `/etc/skel`
</details>

<details>
<summary>Can you set a script that automatically runs on any user login?</summary>

- `/etc/profile.d/`
</details>

<details>
<summary>Can you check current users?</summary>

- `cat /etc/passwd`
</details>

<details>
<summary>Do you know your primary and secondary groups?</summary>

- `id <username>`
</details>

## Bash Scripting

<details>
<summary>Can you touch a file with today's date in the filename?</summary>

- `touch file.`date +%F``
- `touch file.$(date +%F%T)`
</details>

<details>
<summary>Can you create 100 files named file<number>?</summary>

- `for i in $(seq 100); do touch file$i; done`
- `touch file{1..100}`
- `count=1;while [ $count -lt 100 ]; do touch file$count; count=$((count+=1)); done`
</details>

<details>
<summary>Can you show the pid of the shell you're in?</summary>

- `echo $$`
</details>

<details>
<summary>Can you create files 1-199 skipping even numbers?</summary>

- `for i in `seq 1 2 199`; do echo "I am checking the number $i"; touch file$i; done`
</details>

<details>
<summary>Can you create a variable of one data point?</summary>

- `var1=100`
</details>

<details>
<summary>Can you loop forever watching uptime every 2 seconds</summary>

- `watch uptime`
- `while true; do uptime; sleep 2; done`
</details>

<details>
<summary>Can you make your system count to 100?</summary>

- `seq 100`
- `seq 1 100`
- `count=1;while [ $count -le 100 ]; do echo "$count"; count=$((count+=1)); done`
- `for ((i=1;i<=100;i++)); do echo "I am counting $i"; done`
- `awk '{for (i=1;i<=100;++i)print i}' <<< ""`
- `perl -e '$count=0; while($count <= 100){print "$count\n"; $count++;}'`
- `perl -E 'for ($i=1; $i<=100; $i++){print "$i \n";}'`
- `perl -E 'for ($i=1; $i<=100; $i++){say $i;}'`
</details>

<details>
<summary>Can you loop over lists/files?</summary>

- `for server in controlplane node01; do echo "I am working on server $server"; done`
- `for server in $(cat servers); do echo "I am working on server $server"; done`
- `while read -r server; do echo $server; done < servers`
</details>

<details>
<summary>Can you connect to two servers and show uptime in a file?</summary>

- `cat script.sh `
  ```bash
  #!/bin/bash
  ####################################################
  # Purpose:
  # Date:
  # Name:
  # Revisions:
  ####################################################
  startTime=`date`
  sleep 10
  endTime=`date`
  echo "The start was $startTime and the end was $endTime"
  ```

<details>
<summary>Can you test a variable against a know value?</summary>

- `if [ $shell == "/bin/bash" ]`
- `if [ $shell = "/bin/bash" ]`

</details>

## Software Packages

<details>
<summary>Can you show all the packaages that have SSL in their name?</summary>

- `dpkg -l | awk '{print $2}' | grep -i ssl`
- `dpkg -l | gawk '/ssl/{print $2}'`
</details>

<details>
<summary>Can you show when the system software was last modified?</summary>

- `cat /var/log/apt/history.log`
- `cat /var/log/dpkg.log | grep <tool>`
</details>

<details>
<summary>Can you verify that you have a software called cowsay? If not, install it?</summary>

- `dpkg -l | grep -i cowsay`
- `apt install cowsay`
</details>

<details>
<summary>Can we see if we have container software? Can we check for local images?</summary>

- `docker images`
- `podman images`
</details>

<details>
<summary>Can run a container? Can we verify it's running? Can we verify the image?</summary>

- `docker run -p 8080:80 -d nginx`
- `docker ps`
- `docker images` to see images
</details>
</div>
