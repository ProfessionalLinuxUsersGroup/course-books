<div class="flex-container">
        <img src="https://github.com/ProfessionalLinuxUsersGroup/img/blob/main/Assets/Logos/ProLUG_Round_Transparent_LOGO.png?raw=true" width="64" height="64"></img>
    <p>
        <h1>Unit 4 Worksheet - Bastions and Jailing Users</h1>
    </p>
</div>

## Instructions

---

Fill out this sheet as you progress through the lab and discussions. Hold your worksheets until
the end to turn them in as a final submission packet.

### Resources / Important Links

- <https://www.sans.org/information-security-policy/>
- <https://www.sans.org/blog/the-ultimate-list-of-sans-cheat-sheets/>
- <https://aws.amazon.com/search/?searchQuery=air+gapped#facet_type=blogs&page=1>
- <https://aws.amazon.com/blogs/security/tag/bastion-host/>

#### Downloads

The worksheet has been provided below. The document(s) can be transposed to
the desired format so long as the content is preserved. For example, the `.txt`
could be transposed to a `.md` file.

- <a href="./assets/downloads/u4/u4_worksheet.pdf" target="_blank" download>📥 u4_worksheet(`.pdf`)</a>
- <a href="./assets/downloads/u4/u4_worksheet.txt" target="_blank" download>📥 u4_worksheet(`.txt`)</a>

### Unit 4 Recording

<!-- <img src="./assets/images/under-construction.jpg" style="border-radius:2%"></img> -->

<iframe
    style="width: 100%; height: 100%; border: none;
    aspect-ratio: 16/9; border-radius: 1rem; background:black"
    src="https://www.youtube.com/embed/dnz92v71Tr4?si=tKBN9rcjWLBtecPO"
    title="Security Engineering Unit 4: Bastions and Air-Gapped Systems"
    frameborder="0"
    allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share"
    referrerpolicy="strict-origin-when-cross-origin"
    allowfullscreen>
</iframe>

#### Discussion Post #1

Review some of the blogs here:

- <https://aws.amazon.com/search/?searchQuery=air+gapped#facet_type=blogs&page=1>

- <https://aws.amazon.com/blogs/security/tag/bastion-host/>

Or find some on your own about air-gapped systems.

1. What seems to be the theme of air-gapped systems?
2. What seems to be their purpose?
3. If you use google, or an AI, what are some of the common themes that come up when
   asked about air-gapped or bastion systems?

#### Discussion Post #2

Do a Google or AI search of topics around jailing a user or processes in Linux.

1. Can you enumerate the methods of jailing users?
2. Can you think of when you've been jailed as a Linux user?  
   If not, can you think of the useful ways to use a jail?

<div class="warning">
Submit your input by following the link below.

The discussion posts are done in Discord threads. Click the 'Threads' icon on the top right and search for the discussion post.

</div>

- [Link to Discussion Posts](https://discord.com/channels/611027490848374811/1098309490681598072)

## Definitions

---

Air-gapped

Bastion

Jailed process

Isolation

Ingress

Egress

Exfiltration

Cgroups

Namespaces

- Mount
- PID
- IPC
- UTS

## Digging Deeper

---

1. While this isn't, strictly speaking, an automation course there is some value in
   looking at automation of the bastion deployments. Check out this ansible code:  
   <https://github.com/het-tanis/stream_setup/blob/master/roles/bastion_deploy/tasks/main.yml>

   - Does the setup make sense to you with our deployment?
   - What can improve and make this better?

2. Find a blog or github where someone else deploys a bastion. Compare it to our
   process.

3. Knowing what you now know about bastions, jails, and air-gapped systems. Reflect
   on the first 3 weeks, all the STIGs you've reviewed and touched. Do any of them
   seem moot, or less necessary if applied in an air-gapped environment?

   - Does your answer change if you read about Zero Trust and know how much of a hot
     topic that is in the security world now?
     1. Why or why not?

4. Think of a Linux system where you would like to deploy a bastion (If you cannot think
   of one, use ProLUG Lab). Draw out how you think the system works in
   excalidraw.com.

## Reflection Questions

---

1. Does it matter if the user knows that they are jailed? Why or why not?

2. What questions do you still have about this week?

3. How are you going to use what you've learned in your current role?
