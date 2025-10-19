# Unit 2 Lab 
## Interacting with the Operating System

This lab is designed to have the engineer verify and execute their automation tools to interact with the
OS in a controlled fashion.

If you do the Killercoda Lab 2, just answer these questions.  

If you are doing the lab in the ProLUG environment, find the scripts
in `/labs/automation/unit2`.

!!! note

    If you are unable to finish the lab in the ProLUG lab environment we ask you `reboot`
    the machine from the command line so that other students will have the intended environment.

### Resources / Important Links

- [Unit 2 Lab on Killercoda](https://killercoda.com/het-tanis/course/AutomationLabs/Unit2_Interacting_with_OS) 

### Required Materials

- Lab Server ([Killercoda recommended](https://killercoda.com/het-tanis/course/AutomationLabs/Unit2_Interacting_with_OS))
    - Rocky 9.4+ - ProLUG Lab
    - Or comparable Linux box
- `root` or `sudo` command access

#### Downloads

The lab has been provided for convenience below:
- <a href="../../assets/pcae/downloads/u2/u2_lab.txt" target="_blank" download>:material-download: u2_lab.txt</a>
- <a href="../../assets/pcae/downloads/u2/u2_lab.md.txt" target="_blank" download="u2_lab.md">:material-download: u2_lab.md</a>

<!-- - <a href="../../assets/pcae/downloads/u2/u2_lab.docx" target="_blank" download>:material-download: u2_lab.docx</a> -->
<!-- - <a href="../../assets/pcae/downloads/u2/u2_lab.pdf" target="_blank" download>:material-download: u2_lab.pdf</a> -->


## Pre-Lab (Lab Setup) 
If you're not doing the lab on Killercoda, make sure to follow the setup guide
below.  

### ProLUG Lab Setup
If you're using the ProLUG lab environment, run the following commands.  
```bash linenums="1" title="prolug-lab-setup"
cd /root
cp -r /labs/automation/unit2/* /root
chmod 755 /root/*.sh
chmod 755 /root/*.py
```

### Personal Lab Setup
Alternatively, for your own lab environment, clone down the necessary files
from GitHub.  
```bash linenums="1" title="lab-setup"
cd /root
git clone https://github.com/het-tanis/prolug-labs.git
cp prolug-labs/AutomationLabs/Unit2_Interacting_with_OS/assets/* /root
```

## Lab 🧪

In this lab, we will go through the process of executing our automation tools.  

### Bash Execution

1. Run the `u2_script1.sh` and look at what it shows you.
   ```bash
   /root/u2_script1.sh
   ```
    - What are you shown?

2. Inspect the file and see if you can modify it to show the first 15 lines.
   ```bash
   cat /root/u2_script1.sh
   ```
    - !!! note
         Modify with vi or vim. You may have to RTFM to continue.  


3. Run the u2_script2.sh and look at what it shows you.
   ```bash
   /root/u2_script2.sh
   ```
    - What happened in the script?
    - Did it work correctly?
      ```bash
      ls -l /root
      ```


4. Inspect the file and see if you can make it use a different date format. You may have to read the
   man pages for date command.
   ```bash
   cat /root/u2_script2.sh
   ```

As you're interacting with the OS, are there any observations you have about how the scripts are set up,
their structure and their output.   

- Is there anything you would add for your scripts?

- If you would add something, how does it improve the code?


---

### Python Execution

1. Run the u2_script1.py and look at what it shows you.
   ```bash
   /root/u2_script1.py
   ```
    - What are you shown?

2. Inspect the file and see if you can modify it to show the first and last 15 lines.
   ```bash
   cat /root/u2_script1.py
   ```
    - !!! note
          Modify with `vi` or `vim`. You may have to RTFM to continue.  

3. Run the u2_script2.py and look at what it shows you.
   ```bash
   /root/u2_script2.py
   ```
    - What are you shown?


4. Inspect the file and see if you can make it use a different user shell, maybe one you've seen from
   other output in this lab.
   ```bash
   cat /root/u2_script2.py
   ```
    - !!! note
          Modify with vi or vim. You may have to RTFM to continue.  


As you're interacting with the OS, are there any observations you have about how the scripts are set up,
their structure and their output.

- Is there anything you would add for your scripts?  

- If you would add something, how does it improve the code?

---

### Ansible Execution

1. Run the u2_script1.yml and look at what it shows you.
   ```bash
   ansible-playbook /root/u2_script1.yml
   ```
    - What are you shown?

2. Inspect the file and see if you can modify it to show the first and last 15 lines.
   ```bash
   cat /root/u2_script1.yml
   ```
    - !!! note
          Modify with vi or vim. You may have to RTFM to continue.  


3. Run the u2_script2.yml and look at what it shows you.
   ```bash
   ansible-playbook /root/u2_script2.yml
   ```
    - What are you shown?

4. Inspect the file and see if you can make it name the file differently or populate different content.
   ```bash
   cat /root/u2_script2.yml
   ```
    - !!! note
          Modify with vi or vim. You may have to RTFM to continue.    

5. Do one final `ls -l` against the `/root` directory. What is a difference 
   between the `.sh`, `.py`, and `.yml` files?
   ```bash
   ls -l
   ```

As you're interacting with the OS, are there any observations you have about how the scripts are set up,
their structure and their output.

- Is there anything you would add for your scripts?

- If you would add something, how does it improve the code?

---

!!! note

    If you are unable to finish the lab in the ProLUG lab environment we ask you `reboot`
    the machine from the command line so that other students will have the intended environment.

