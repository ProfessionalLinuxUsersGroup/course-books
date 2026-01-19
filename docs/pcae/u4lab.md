# Unit 4 Lab

## Admin commands and one-offs

!!! note

    If you are unable to finish the lab in the ProLUG lab environment we ask you `reboot`
    the machine from the command line so that other students will have the intended environment.

### Resources / Important Links

- [Unit 4 on Killercoda Lab](https://killercoda.com/het-tanis/course/Automation-Labs/Unit4_Admin_Commands)

### Required Materials

- Lab Server [Killercoda recommended](https://killercoda.com/het-tanis/course/Automation-Labs/Unit4_Admin_Commands)
    - Rocky 9.6+ - ProLUG Lab
    - Or comparable Linux box
- `root` or `sudo` command access

#### Downloads

The lab has been provided for convenience below:

- <a href="https://professionallinuxusersgroup.github.io/course-books/assets/pcae/downloads/u4/u4_lab.txt" target="_blank">📥 u4_lab(`.txt`)</a>
- <a href="https://professionallinuxusersgroup.github.io/course-books/assets/pcae/downloads/u4/u4_lab.md.txt" target="_blank">📥 u4_lab(`.md`)</a>

## Pre-Lab (Lab Setup)

If you're not doing the lab on Killercoda, make sure to follow the setup guide
below.

### ProLUG Lab Setup

If you're using the ProLUG lab environment, run the following commands.  
```bash linenums="1" title="prolug-lab-setup"
cd /root
cp -r /labs/automation/unit3/* /root
chmod 755 /root/*.sh
chmod 755 /root/*.py
```

## Lab 🧪

This lab is designed to have the engineer verify and execute their automation tools to interact with the
OS in a controlled fashion.

If you do the killercoda Lab 4, just answer these questions. If you are doing the lab in the ProLUG
environment, find the scripts in `/labs/automation/unit4`.

In the ProLUG lab, you must edit `/root/hosts` to point at your correct environment based on which “auto{x}”
server you have connected to.

|Server|Hostgroup|TargetNodes|
|:-:|:-:|:-:|
|auto1|[webservers]|target1-1,target1-2|
|auto2|[webservers]|target2-1,target2-2|
|auto3|[webservers]|target3-1,target3-2|
|auto4|[webservers]|target4-1,target4-2|
|auto5|[webservers]|target5-1,target5-2|

!!! warning

    This lab is designed to be run in the killercoda environment and will take significant user tooling
    to change over to their own environment. This is not supported in this run of the course but the learner is welcome 
    to work with it and tool it over for that purpose as time permits.

!!! note

    If you are unable to finish the lab in the ProLUG lab environment we ask you `reboot`
    the machine from the command line so that other students will have the intended environment.
