<div class="flex-container">
        <img src="https://github.com/ProfessionalLinuxUsersGroup/img/blob/main/Assets/Logos/ProLUG_Round_Transparent_LOGO.png?raw=true" width="64" height="64"></img>
    <p>
        <h1>Unit 6 Worksheet - Monitoring and Parsing Logs</h1>
    </p>
</div>

## Instructions

---

Fill out this sheet as you progress through the lab and discussions. Hold your worksheets until
the end to turn them in as a final submission packet.

### Resources / Important Links

- <https://grafana.com/docs/loki/latest/query/analyzer/>
- <https://www.sans.org/information-security-policy/>
- <https://www.sans.org/blog/the-ultimate-list-of-sans-cheat-sheets/>
- <https://public.cyber.mil/stigs/downloads/>

#### Downloads

The worksheet has been provided below. The document(s) can be transposed to
the desired format so long as the content is preserved. For example, the `.txt`
could be transposed to a `.md` file.

- <a href="./assets/downloads/u6/u6_worksheet.pdf" target="_blank" download>📥 u6_worksheet(`.pdf`)</a>
- <a href="./assets/downloads/u6/u6_worksheet.txt" target="_blank" download>📥 u6_worksheet(`.txt`)</a>

### Unit 6 Recording
  
<iframe style="width: 100%; height: 100%; border: none; aspect-ratio: 16/9; border-radius: 1rem; background:black" src="https://www.youtube.com/embed/pnCC-FX-aag?si=Y9zt3V_f5osfmGYn" title="Unit 6 Recording - ProLUG Linux Security Engineering Course - Free in Discord" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

#### Discussion Post #1

Review chapter 15 of the SRE book:
<https://google.github.io/building-secure-and-reliable-systems/raw/ch15.html#collect_appropriate_and_useful_logs>.
There are 14 references at the end of the chapter. Follow them for more information. One of them:
<https://jvns.ca/blog/2019/06/23/a-few-debugging-resources/> should be reviewed for
question "c".

- a. What are some concepts that are new to you?
- b. There are 5 conclusions drawn, do you agree with them? Would you add or remove anything from the list?
- c. In Julia Evan's debugging blog, which shows that debugging is just another
  form of troubleshooting, what useful things do you learn about the
  relationship between these topics? Are there any techniques you already do
  that this helps solidify for you?

#### Discussion Post #2

Read <https://sre.google/sre-book/monitoring-distributed-systems/>.

- What interesting or new things do you learn in this reading? What may you
  want to know more about?
- What are the "4 golden signals"?
- After reading these, why is immutability so important to logging? What do you
  think the other required items are for logging to be effective?

<div class="warning">
Submit your input by following the link below.

The discussion posts are done in Discord threads. Click the 'Threads' icon on the top right and search for the discussion post.

</div>

- [Link to Discussion Posts](https://discord.com/channels/611027490848374811/1365776270800977962)

## Definitions

---

Types of logs

- Application
- Host
- Network
- DB

Immutable

Structure of Logs

- RFC 3164 BSD Syslog
- RFC 5424 IETF Syslog
- Systemd Journal

Log rotation

Rsyslog

Log aggregation

- ELK
- Splunk
- Graylog
- Loki

SIEM

## Digging Deeper

---

1. Find a cloud service and see what their logging best practices are for security
   incident response. Here is AWS: <https://aws.amazon.com/blogs/security/logging-strategies-for-security-incident-response/>

   - What are the high level concepts mentioned?
   - What are the tools available and what actions do they take?
   - What are the manual and automated query capabilities provided, and how
     they help you rapidly get to a correct assessment of the logged events?

2. Open up that STIG Viewer and filter by "logging" for any of the previous STIGs we've
   worked on. (Mariadb has some really good ones.)

   - What seems to be a common theme?
   - What types of activities MUST be logged in various applications and operating systems?
     - Does it make sense why all logins are tracked?
     - Does it make sense why all admin actions, even just attempted admin actions, are logged?

## Reflection Questions

---

1. What architectures have you used in your career?

   - If you haven't yet worked with any of these, what do you think you would
     architect in the ProLUG lab (~60 virtual machines, 4 physical machines, 1
     NFS share, and 2 Windows laptops?)

2. What questions do you still have about this week?

3. How are you going to use what you've learned in your current role?
