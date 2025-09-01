<div class="flex-container">
        <img src="https://github.com/ProfessionalLinuxUsersGroup/img/blob/main/Assets/Logos/ProLUG_Round_Transparent_LOGO.png?raw=true" width="64" height="64"></img>
    <p>
        <h1>Unit 8 Lab - Configuration Drift and Remediation</h1>
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

- <a href="./assets/downloads/u8/u8_lab.txt" target="_blank" download>📥 u8_lab(`.txt`)</a>
- <a href="./assets/downloads/u8/u8_lab.pdf" target="_blank" download>📥 u8_lab(`.pdf`)</a>

## Lab 🧪

These labs focus on configuration drift tracking and remediation.

### Operational Activities

![Image 1](./assets/images/u8/image1.jpeg)

1. Check your stig viewer and go to RHEL 9 stigs.

2. Set a filter for “change management”.

   - How many STIGs do you see?

3. Review the wording, what is meant by a robust change management process?
   - Do you think this can be applied in just one STIG? Why or why not?
   - What type of control is being implemented with change management in these STIGS?
     - Is it different across the STIGs or all the same?

### Monitoring configuration drift with Aide

1. Go into the sandbox lab: <https://killercoda.com/playgrounds/scenario/ubuntu>

2. Install aide and watch the installation happen.

   ```bash
   apt -y install aide
   ```

   - What is being put in the path `/etc/aide/aide.conf.d/`?
     - How many files are in there?

3. Check your version of aide

   ```bash
   aide -v
   ```

4. Read the man page (first page).

   ```bash
   man aide
   ```

   - What does aide try to do, and how does it do it?

5. What is the configuration of cron found in `/etc/cron.daily/dailyaidecheck`?

   - What does this attempt to do?
   - What checks are there before execution?
   - Read the man for `capsh`, what is it used for?

6. Set up aide according to the default configuration
   ```bash
   time aide -i -c /etc/aide/aide.conf
   ```
   - How long did that take?
     - How much time was wall clock v. system/user time?
     - Why might you want to know this on your systems?
     - What do you notice about the output?
       1. What do you need to go read about?

![Image 2](./assets/images/u8/image2.jpeg)

(Mine took 5 minutes 8 seconds to run on the lab system)

7. Set the database up properly

   ```bash
   cp /var/lib/aide/aide.db.new /var/lib/aide/aide.db
   ```

8. Test aide by making files in a tracked directory

   ```bash
   mkdir /root/prolug
   touch /root/prolug/test1
   touch /root/prolug/test2
   time aide -c /etc/aide/aide.conf --check
   ```

   - Did you see your new files created?
   - How long did this take to run?
     1. What type of usage do you see against user/system space?

![Image 3](./assets/images/u8/image3.png)

### Using Ansible to fix drift

1. Complete the lab here: <https://killercoda.com/het-tanis/course/Ansible-Labs/16-Ansible-Web-Server-Env-Deploy>

2. When you finish ensure that you see broken output for 8081, as required.

   ```bash
   curl node01:8081
   ```

3. One of the dev teams figured out they could modify the `test` and `qa`
   environments because a previous engineer left them in the sudoers file. You can
   address that separately with the security team, but for now you need to get those
   environments back to working. Run your original deployment command to see if it sets
   mhe environment back properly.

   ```bash
   ansible-playbook -i /root/hosts /root/web_environment.yaml
   ```

![Image 4](./assets/images/u8/image4.png)

- Did this force the system back into a working configuration?
  - If it worked, would it always work, or would they (the systems) need to be
    manually intervened?
  - What is your test? (hint: `curl` the ports `8080`, `8081`, and `8082` from previous commands)
- Could this cause potential problems in the environment?
  - If so, is that problem based on technology or operational practices? Why?

### Digging Deeper challenge (not required for finishing lab)

1. Complete this lab: <https://killercoda.com/het-tanis/course/Ansible-Labs/19-Ansible-csv-report>
   - Can you think about how you’d use this to verify that a system was stamped
     according to your build process?
     - You may have to tie it in with something like this lab and add some variables
       to your custom facts files, maybe the date of deployment:
       <https://killercoda.com/het-tanis/course/Ansible-Labs/12-Ansible-System-Facts-Grouping>

> Be sure to `reboot` the lab machine from the command line when you are done.
