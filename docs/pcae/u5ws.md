# Unit 5 Worksheet

## Instructions

Fill out the worksheet as you progress through the lab and discussions.
Hold your worksheets until the end to turn them in as a final submission packet.

### Resources / Important Links

- Inventories: <https://docs.ansible.com/ansible/latest/inventory_guide/intro_inventory.html>
- Special Variables: <https://docs.ansible.com/ansible/latest/reference_appendices/special_variables.html>
- Variable Precedence: <https://docs.ansible.com/ansible/latest/playbook_guide/playbooks_variables.html#understanding-variable-precedence>
- Templates (Jinja2): <https://docs.ansible.com/ansible/latest/playbook_guide/playbooks_templating.html>

#### Downloads

The worksheet has been provided below. The document(s) can be transposed to
the desired format so long as the content is preserved. For example, the `.txt`
could be transposed to a `.md` file.

- <a href="https://professionallinuxusersgroup.github.io/course-books/assets/pcae/downloads/u5/u5_worksheet.md.txt" target="_blank">📥 u5_worksheet(`.md`)</a>
- <a href="https://professionallinuxusersgroup.github.io/course-books/assets/pcae/downloads/u5/u5_worksheet.txt" target="_blank">📥 u5_worksheet(`.txt`)</a>
- <a href="https://professionallinuxusersgroup.github.io/course-books/assets/pcae/downloads/u5/u5_worksheet.pdf" target="_blank">📥 u5_worksheet(`.pdf`)</a>

### Unit 5 Recording

<iframe
    style="width: 100%; height: 100%; border: none;
    aspect-ratio: 16/9; border-radius: 0.25rem; background:black"
    src="https://www.youtube.com/embed/LQ9aXRU3vts"
    title="Unit 5 Recording - ProLUG Linux Automation Engineering Course - Free in Discord"
    frameborder="0"
    allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share"
    referrerpolicy="strict-origin-when-cross-origin"
    allowfullscreen>
</iframe>

Link: <https://www.youtube.com/watch?v=LQ9aXRU3vts>

#### Discussion Post #1

You know about variable precedence and have decided to study it for your Ansible playbooks.
Read <https://docs.ansible.com/ansible/latest/playbook_guide/playbooks_variables.html> 
and answer the following questions:

1. What is variable precedence and why should it matter?

2. What does it mean to register a variable, and how is that variable used in the playbook?

3. How might variables be useful at the end of an automation, in relation to reporting out 
   what happened in the playbook?


#### Discussion Post #2

You've stumbled on a playbook and you're trying to figure out what the following line means:
<img src="../../assets/pcae/images/u5/u5_dp2_playbook.png"/>

You have reviewed Jinja2 filters
<https://docs.ansible.com/ansible/latest/playbook_guide/playbooks_filters.html#providingdefault-values>
and think you have a good handle on what is happening.

1. What is the variable name being called?

2. What is the default value if that variable does not exist or is not populated?

3. What is the reason this might be nice in your executions if you want them always to
   complete?

4. Is there a danger to always setting default values?
    1. Or another way to ask that, is there a tradeoff between always finishing and
       sometimes having incorrectly set values?
    2. Where will you use these in your automations?


!!! info

    Submit your input by following the link below. The discussion posts are done in Discord Forums.
    [Link to Discussion Posts](https://discord.com/channels/611027490848374811/1365776270800977962)


## Definitions

- Workflow - Execution
    1. Before
    2. During
    3. After

- Variables
    - Special Variables
    - Precedence

- Environment Files

- Jinja2

- Templates


## Digging Deeper

Work through the following labs to practice the topics from this week's presentation.  

1. Ansible Facts: <https://killercoda.com/het-tanis/course/Ansible-Labs/12-Ansible-System-Facts-Grouping>
2. Ansible Vault: <https://killercoda.com/het-tanis/course/Ansible-Labs/10-Ansible-Vaulting-Password-and-Variables>
3. Ansible API Calls: <https://killercoda.com/het-tanis/course/HashicorpLabs/004-vault-read-secrets-ansible>
4. Stamping servers: <https://killercoda.com/het-tanis/course/Ansible-Labs/07-Ansible-Playbook-Jinja-Templates>
5. Reporting back values: <https://killercoda.com/het-tanis/course/AnsibleLabs/08-Ansible-Playbook-Jinja-Reporting>
6. Generating CSV for management: <https://killercoda.com/hettanis/course/Ansible-Labs/19-Ansible-csv-report>


## Reflection Questions

1. What questions do you still have about this week?
2. How are you going to use what you've learned in your current role?

