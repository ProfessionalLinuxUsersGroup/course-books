# Unit 3 Lab

## Making and Using Inventories

!!! note

    If you are unable to finish the lab in the ProLUG lab environment we ask you `reboot`
    the machine from the command line so that other students will have the intended environment.

### Resources / Important Links

- [Unit 3 Lab on Killercoda](https://killercoda.com/het-tanis/course/Automation-Labs/Unit3_Inventories)

### Required Materials

- Lab Server [Killercoda recommended](https://killercoda.com/het-tanis/course/Automation-Labs/Unit3_Inventories)
    - Rocky 9.6+ - ProLUG Lab
    - Or comparable Linux box
- `root` or `sudo` command access

#### Downloads

The lab has been provided for convenience below:

- <a href="https://professionallinuxusersgroup.github.io/course-books/assets/pcae/downloads/u3/u3_lab.txt" target="_blank">📥 u3_lab(`.txt`)</a>
- <a href="https://professionallinuxusersgroup.github.io/course-books/assets/pcae/downloads/u3/u3_lab.md.txt" target="_blank">📥 u3_lab(`.md`)</a>

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

### Personal Lab Setup
Alternatively, for your own lab environment, clone down the necessary files
from GitHub.
```bash linenums="1" title="lab-setup"
cd /root
git clone https://github.com/het-tanis/prolug-labs.git
cp prolug-labs/AutomationLabs/Unit3_Inventories/assets/* /root
```

## Lab 🧪

This lab is designed to have the engineer verify and execute their automation tools to interact with the OS in a controlled fashion.

If you do the killercoda Lab 3, just answer these questions. If you are doing the lab in the ProLUG
environment, find the scripts in /labs/automation/unit3.

If you are doing the lab in the ProLUG environment, find the scripts
in `/labs/automation/unit3`.

### Bash execution

1. Execute script u3_script.sh and see if you can read the data
    ```bash
        /root/u3_script.sh
    ```
    - What values are shown?

2. What does the script look like in bash?
    ```bash
    cat /root/u3_script.sh
    ```
    - Could you modify this script to hit a different API endpoint and place the file in a different location?

3. Read the provided users.csv file
    ```bash
    cat /root/users.csv
    ```

4. Parse out the data for just the first and the third fields
    ```bash
    cat /root/users.csv | awk -F , '{print $1,$3}'
    ```
    - Could you parse out only the first and second fields?
    - Can you remove the header?

5. Regenerate the data for /root/users.csv

    ```bash
    /root/u3_script_user_generator.sh
    ```

### Python execution

1. Run the u3_script.py and look at what it shows you.
    ```bash
    /root/u3_script.py
    ```
    - What are you shown?

2. Inspect the file and see if you can figure out what it was doing.
    ```bash
    cat /root/u3_script.py
    ```
    - Note: Modify with vi or vim. Can you make this show the lowest 10 items, ordered by
    magnitude?
    - Can you generate a python script that parses the /root/users.csv file? (What resources might
    you use to do this?)

### Ansible execution

1. Run the u3_script.yml and look at what it shows you.
    ```bash
    ansible-playbook /root/u3_script.yml
    ```
    - What are you shown?
    - Can you modify this output so show other interesting parts of the API calls?
    - If you had to pull a specific field, could you do it

    Again, you don't know how data might come to you in your organization, so this is an exercise in parsing things different ways.

2. Inspect your current inventory files.
    ```bash
    cat /root/hosts
    cat /root/hosts_example2
    cat /root/hosts_example3
    ```
    - What file type are these? (<https://docs.ansible.com/ansible/latest/inventory_guide/intro_inventory.html>)?
    - What other file types might you use for inventories?
    - Do you have a preference on how the data are formatted, or where the variables are located on these?
    - Do you think some of this looks better formatted or do you prefer it as yaml?

3. Check the yaml versions of these files.
    ```bash
    ansible-inventory -i /root/hosts --list -y
    ansible-inventory -i /root/hosts_example2 --list -y
    ansible-inventory -i /root/hosts_example3 --list -y
    ```
    This is a very high level review of the many ansible-inventory commands. It is recommended
    that you parse and play with these files more, as the concepts will continue to be built on in
    later labs.

!!! note

    If you are unable to finish the lab in the ProLUG lab environment we ask you `reboot`
    the machine from the command line so that other students will have the intended environment.
