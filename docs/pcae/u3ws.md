# Unit 3 Worksheet

## Instructions

Fill out the worksheet as you progress through the lab and discussions.
Hold your worksheets until the end to turn them in as a final submission packet.

### Resources / Important Links

- <https://killercoda.com/hettanis/course/Ansible-Labs/02-Ansible-Host-File>
- <https://docs.ansible.com/ansible/latest/inventory_guide/intro_inventory.html>

#### Downloads

The worksheet has been provided below. The document(s) can be transposed to
the desired format so long as the content is preserved. For example, the `.txt`
could be transposed to a `.md` file.

- <a href="https://professionallinuxusersgroup.github.io/course-books/assets/pcae/downloads/u3/u3_worksheet.md.txt" target="_blank">📥 u3_worksheet(`.md`)</a>
- <a href="https://professionallinuxusersgroup.github.io/course-books/assets/pcae/downloads/u3/u3_worksheet.txt" target="_blank">📥 u3_worksheet(`.txt`)</a>
- <a href="https://professionallinuxusersgroup.github.io/course-books/assets/pcae/downloads/u3/u3_worksheet.pdf" target="_blank">📥 u3_worksheet(`.pdf`)</a>

### Unit 3 Recording

<iframe
    style="width: 100%; height: 100%; border: none;
    aspect-ratio: 16/9; border-radius: 0.25rem; background:black"
    src="https://www.youtube.com/embed/Xsz7MXJPU58"
    title="Unit 3 Recording - ProLUG Linux Automation Engineering Course - Free in Discord"
    frameborder="0"
    allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share"
    referrerpolicy="strict-origin-when-cross-origin"
    allowfullscreen>
</iframe>

Link: <https://www.youtube.com/watch?v=acKjnxuGjVI>

#### Discussion Post #1

Find a blog post or open source tool that focuses on IT inventory management.  

1. What is meant by the term “inventory” in an IT context?
2. What are some of the issues with inventories in a company?
    - How have people attempted to overcome these issues?
3. What different formats of inventories can you find for IT management?
    - Why would formatting matter?


#### Discussion Post #2

You are a system administrator for a small company with ~100 total Linux 
systems. The security engineer approaches you and shows you vulnerabilities in 
your 110 total Linux systems. He then asserts, "without a good inventory, you 
cannot have security in the system."  

1. Do you agree with him, why or why not?

    1. How do you plan to start to “true up” your inventories?

    2. How can you prevent this type of problem (if you think it is one) in the future?

2. We often say in engineering, “Or you can do nothing”. This speaks to the possibility
   of just accepting the situation and allowing a system to keep running.

    1. Can you do that in this situation, or must this be corrected? Why or why not?


!!! info

    Submit your input by following the link below. The discussion posts are done in Discord Forums.
    [Link to Discussion Posts](https://discord.com/channels/611027490848374811/1365776270800977962)


## Definitions

- IT Inventory

- File formats (be able to identify and parse them with your tools)
    - `.csv`
    - `.ini`
    - `.yaml`

- Grouping

- Variables (in relation to inventories)

- Ranges (and their usefulness)
    - `[01:50]`
    - `[01:50:2]`


## Digging Deeper

1. Build some inventories like the ones here:
   <https://docs.ansible.com/ansible/latest/inventory_guide/intro_inventory.html>

    1. Parse these down using ansible-inventory to see if you understand the syntax
       and formatting.

    2. Run through this lab for understanding:
       <https://killercoda.com/hettanis/course/Ansible-Labs/02-Ansible-Host-File>



## Reflection Questions

1. What questions do you still have about this week?

2. How are you going to use what you’ve learned in your current role?

