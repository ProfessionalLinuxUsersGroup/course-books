<head>
    <style> .flex-container { display: flex; align-items: center; gap: 20px; } </style>
</head>
<div class="flex-container">
        <img src="https://github.com/ProfessionalLinuxUsersGroup/img/blob/main/Assets/Logos/ProLUG_Round_Transparent_LOGO.png?raw=true" width="64" height="64">
    <p>
        <h1>Unit 8 Worksheet - Configuration Drift and Remediation</h1>
    </p>
</div>

## Instructions

---

Fill out this sheet as you progress through the lab and discussions. Hold your worksheets until
the end to turn them in as a final submission packet.

### Resources / Important Links

- <https://google.github.io/building-secure-and-reliable-systems/raw/ch14.html#treat_configuration_as_code>
- <https://en.wikipedia.org/wiki/Configuration_management>
- <https://www.sans.org/information-security-policy/>
- <https://www.sans.org/blog/the-ultimate-list-of-sans-cheat-sheets/>

#### Downloads

The worksheet has been provided below. The document(s) can be transposed to
the desired format so long as the content is preserved. For example, the `.txt`
could be transposed to a `.md` file.

- <a href="./assets/downloads/u8/u8_worksheet.txt" target="_blank" download>📥 u8_worksheet(`.txt`)</a>
- <a href="./assets/downloads/u8/u8_worksheet.pdf" target="_blank" download>📥 u8_worksheet(`.pdf`)</a>

### Unit 8 Recording

<iframe
    style="width: 100%; height: 100%; border: none; aspect-ratio: 16/9; border-radius: 1rem; background:black;"
    src="https://www.youtube.com/embed/C5F6i9zDgJ4?si=rHKecMF9MDg3tmGl"
    title="Unit 8 Recording - ProLUG Linux Security Engineering Course - Free in Discord;
    frameborder="0;
    allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share;
    referrerpolicy="strict-origin-when-cross-origin;
    allowfullscreen;>
</iframe>

#### Discussion Post #1

Read about configuration management here:
<https://en.wikipedia.org/wiki/Configuration_management>

- What overlap of terms and concepts do you see from this week’s meeting?

- What are some of the standards and guidelines organizations involved with
  configuration management?

  - Do you recognize them from other IT activities?

#### Discussion Post #2

Review the SRE guide to treating configurations as code.  
Read as much as you like, but focus down on the “Practical Advice” section:
<https://google.github.io/building-secure-and-reliable-systems/raw/ch14.html#treat_configuration_as_code>

- What are the best practices that you can use in your configuration management adherence?

- What are the security threats and how can you mitigate them?

- Why might it be good to know this as you design a CMDB or CI/CD pipeline?

---

<div class="warning">

Submit your input by following the link below.

The discussion posts are done in Discord Forums.

</div>

- [Link to Discussion Forum](https://discord.com/channels/611027490848374811/1365776270800977962)

## Definitions

---

System Lifecycle

Configuration Drift

Change management activities

- CMDB
- CI
- Baseline

Build book

Run book

Hashing

- `md5sum`
- `sha<x>sum`

IaC

Orchestration

Automation

AIDE

## Digging Deeper

---

1. Review more of the SRE books from Google: <https://sre.google/books/> to try to find
   more useful change management practices and policies.

## Reflection Questions

---

1. How does the idea of control play into configuration management? Why is it so important?

2. What questions do you still have about this week?

3. How are you going to use what you’ve learned in your current role?
