# Unit 8 Worksheet

## Instructions

Fill out the worksheet as you progress through the lab and discussions.
Hold your worksheets until the end to turn them in as a final submission packet.

### Resources / Important Links

- <https://sre.google/sre-book/release-engineering/>
- <https://sre.google/workbook/canarying-releases/>
- <https://docs.ansible.com/projects/ansible/latest/collections/kubernetes/core/k8s_module.html>
- <https://killercoda.com/het-tanis/course/Automation-Labs/Unit8_Kubernetes_Automation>
- <https://killercoda.com/het-tanis/course/Kubernetes-Labs/blue-green-deployments>
- <https://killercoda.com/het-tanis/course/Kubernetes-Labs/canary-deployments>

#### Downloads

The worksheet has been provided below. The document(s) can be transposed to
the desired format so long as the content is preserved. For example, the `.txt`
could be transposed to a `.md` file.

- <a href="https://professionallinuxusersgroup.github.io/course-books/assets/pcae/downloads/u8/u8_worksheet.md.txt" target="_blank">📥 u8_worksheet(`.md`)</a>
- <a href="https://professionallinuxusersgroup.github.io/course-books/assets/pcae/downloads/u8/u8_worksheet.txt" target="_blank">📥 u8_worksheet(`.txt`)</a>
- <a href="https://professionallinuxusersgroup.github.io/course-books/assets/pcae/downloads/u8/u8_worksheet.pdf" target="_blank">📥 u8_worksheet(`.pdf`)</a>

### Unit 8 Recording

<iframe
    style="width: 100%; height: 100%; border: none;
    aspect-ratio: 16/9; border-radius: 0.25rem; background:black"
    src="https://www.youtube.com/embed/C4dzRI_bFCQ"
    title="Unit 8 Recording - ProLUG Linux Automation Engineering Course - Free in Discord"
    frameborder="0"
    allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share"
    referrerpolicy="strict-origin-when-cross-origin"
    allowfullscreen>
</iframe>

Link: <https://www.youtube.com/watch?v=C4dzRI_bFCQ>

#### Discussion Post #1

Your infrastructure engineering teams have been experiencing problems re-creating environments. The main problems
have been around reliably building the exact same environment and also making those builds happen in a timely manner. Last week you read <https://sre.google/sre-book/release-engineering/> and <https://sre.google/workbook/canarying-releases/> to answer the following questions.

1. How is a Kubernetes environment different, in release context from a virtual or
   physical server environment?
    1. What does the term ephemeral mean, and are all Kubernetes environments
      ephemeral? Why or why not?
    1. How does blue/green or canary deployments help maintain uptime in release management?
        1. What is the use case of each?

#### Discussion Post #2

Your team needs to develop a “push button” solution for deploying Kubernetes for a number of different development
teams. You have a development cluster that they can use and capacity is not a consideration for this discussion.

1. What pieces of information will you need to supply on your side for this type of
   automation?
1. What pieces of information will the team need to supply on their side for each
   deployment?
    1. How can the different dev teams feed this into your automation?
    1. What do you prefer?
1. What are some potential default variables you would want to use for this
   deployment?

!!! info

    Submit your input by following the link below. The discussion posts are done in Discord Forums.
    [Link to Discussion Posts](https://discord.com/channels/611027490848374811/1365776270800977962)

## Definitions

- Kubernetes
    - Namespaces
    - Pods
    - Deployments
    - Labels

## Digging Deeper

1. Read other use cases for the Kubernetes module in Ansible:
   https://docs.ansible.com/projects/ansible/latest/collections/kubernetes/core/k8s_module.html
    1. How might you use these other use cases in your environments?
    1. Do you have another tool you’d use instead of this? Does it have the same, or
    more functionality?
1. Deployment practices with Kubernetes blue/green and canary labs:
    1. <https://killercoda.com/het-tanis/course/Kubernetes-Labs/blue-green-deployments>
    1. <https://killercoda.com/het-tanis/course/Kubernetes-Labs/canary-deployments>

## Reflection Questions

1. What questions do you still have about this week?
1. How are you going to use what you’ve learned in your current role?
