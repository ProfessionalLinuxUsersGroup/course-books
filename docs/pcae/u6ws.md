# Unit 6 Worksheet

## Instructions

Fill out the worksheet as you progress through the lab and discussions.
Hold your worksheets until the end to turn them in as a final submission packet.

### Resources / Important Links

- [Apptainer](https://apptainer.org/docs/user/latest/)
    - [Intro to Apptainer](https://apptainer.org/docs/user/latest/introduction.html#why-use-apptainer)
- [Intro to Packer](https://developer.hashicorp.com/packer/docs/intro) 
    - [Packer Tutorial Library](https://developer.hashicorp.com/tutorials/library?product=packer&edition=open_source)
    - [Packer with GitHub Actions](https://developer.hashicorp.com/packer/tutorials/cloud-production/github-actions)
    - [Provisioning](https://developer.hashicorp.com/packer/tutorials/docker-get-started/docker-get-started-provision)
- [Terraform with Docker](https://developer.hashicorp.com/terraform/tutorials/docker-get-started)
- [Release Engineering](https://sre.google/sre-book/release-engineering/)
- ["Canarying" Releases](https://sre.google/workbook/canarying-releases/) 

#### Downloads

The worksheet has been provided below. The document(s) can be transposed to
the desired format so long as the content is preserved. For example, the `.txt`
could be transposed to a `.md` file.

- <a href="../../assets/pcae/downloads/u6/u6_worksheet.md.txt" target="_blank" download="u6_worksheet.md">:material-download: u6_worksheet.md</a>
- <a href="../../assets/pcae/downloads/u6/u6_worksheet.txt" target="_blank" download>:material-download: u6_worksheet.txt</a>
- <a href="../../assets/pcae/downloads/u6/u6_worksheet.pdf" target="_blank" download>:material-download: u6_worksheet.pdf</a>

### Unit 6 Recording

Recording coming soon.  
<!-- Playlist: https://www.youtube.com/playlist?list=PLyuZ_vuAWmpoiB5_fo9zXd_leFwzfbA5o -->
<!-- <iframe -->
<!--     style="width: 100%; height: 100%; border: none; -->
<!--     aspect-ratio: 16/9; border-radius: 1rem; background:black" -->
<!--     src="PLACEHOLDER: Unit Embed Link" -->
<!--     title="PLACEHOLDER: Unit recording title" -->
<!--     frameborder="0" -->
<!--     allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" -->
<!--     referrerpolicy="strict-origin-when-cross-origin" -->
<!--     allowfullscreen> -->
<!-- </iframe> -->

#### Discussion Post #1

Your infrastructure engineering teams have been experiencing problems 
re-creating environments. The main problems have been around reliably building
the exact same environment and also making those builds happen in a timely manner.
Read <https://sre.google/sre-book/release-engineering/> and
<https://sre.google/workbook/canarying-releases/> to answer the following questions.

1. What is release engineering?

2. What are the release engineering principles?

3. How do the tools we've discussed this week, Apptainer, Packer, Terraform, or 
   even Ansible fit into these topics?

#### Discussion Post #2

Your team is trying to decide between the Apptainer and Packer
tools for container deployments. You've been tasked with making the decision between the
two packages.  

Read the following: <https://developer.hashicorp.com/packer/docs/intro> and
<https://apptainer.org/docs/user/latest/introduction.html#why-use-apptainer>

1. Can you describe Apptainer and Packer?

2. How would you make the decision between the two of these tools? (You may want to make a table)

    1. What do they both do?

    2. What do only one or the other do?

    3. What are the strengths and weaknesses of each?

3. Modify or fix the drawing to show how your team will deploy containers.

<img src="../../assets/pcae/images/u6/containerimgworkflow.png" />

!!! note

    Submit your input by following the link below. The discussion posts are done in Discord Forums.

    - [Link to Discussion Posts](https://discord.com/channels/611027490848374811/1365776270800977962)


## Definitions


- Docker Images

- Docker processes

- Container/Runtime Environment

- CI/CD

- Release engineering

    - Releases

    - Code base

    - Code changes

    - Build configuration

        - Building

        - Branching

        - Testing


## Digging Deeper

Read about Terraform providers here:
<https://developer.hashicorp.com/terraform/language/providers>

1. What are Terraform providers?  

2. How would we find a specific provider?

## Reflection Questions


1. What questions do you still have about this week?

2. How are you going to use what you've learned in your current role?

