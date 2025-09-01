<head>
    <style> .flex-container { display: flex; align-items: center; gap: 20px; } </style>
</head>
<div class="flex-container">
        <img src="https://github.com/ProfessionalLinuxUsersGroup/img/blob/main/Assets/Logos/ProLUG_Round_Transparent_LOGO.png?raw=true" width="64" height="64">
    <p>
        <h1>Unit 7 Worksheet - Monitoring and Alerting</h1>
    </p>
</div>

## Instructions

---

Fill out this sheet as you progress through the lab and discussions. Hold your worksheets until
the end to turn them in as a final submission packet.

### Resources / Important Links

- <https://promlabs.com/promql-cheat-sheet/>
- <https://www.sans.org/information-security-policy/>
- <https://www.sans.org/blog/the-ultimate-list-of-sans-cheat-sheets/>

#### Downloads

The worksheet has been provided below. The document(s) can be transposed to
the desired format so long as the content is preserved. For example, the `.txt`
could be transposed to a `.md` file.

- <a href="./assets/downloads/u7/u7_worksheet.txt" target="_blank" download>📥 u7_worksheet(`.txt`)</a>
- <a href="./assets/downloads/u7/u7_worksheet.pdf" target="_blank" download>📥 u7_worksheet(`.pdf`)</a>

### Unit 7 Recording

 <iframe
     style="width: 100%; height: 100%; border: none;
     aspect-ratio: 16/9; border-radius: 1rem; background:black"
     src="https://www.youtube.com/embed/2yhCRQ-QmlE?si=mAZH3NRoJmnnopif"
     title="Unit 7 Recording - Monitoring and Alerting"
     frameborder="0"
     allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share"
     referrerpolicy="strict-origin-when-cross-origin"
     allowfullscreen>
 </iframe>

#### Discussion Post #1

Read about telemetry, logs, and traces. Ther are many good sources, even from
Microsoft:
<https://microsoft.github.io/code-with-engineering-playbook/observability/log-vs-metric-vs-trace/>

1. How does the usage guidance of that blog (at bottom) align with your
   understanding of these three items?

2. What other useful blogs or AI write-ups were you able to find?

3. What is the usefulness of this in securing your system?

#### Discussion Post #2

When we think of our systems, sometimes an airgapped system is simple to think about
because everything is closed in. The idea of alerting or reporting is the opposite.
We are trying to get the correct, timely, and important information out of the system
when and where it is needed.

Read the summary at the top of:
<https://docs.google.com/document/d/199PqyG3UsyXlwieHaqbGiWVa8eMWi8zzAn0YfcApr8Q/edit?tab=t.0>

1. What is the litmus test for a page? (Sending something out of the system?)

2. What is over-monitoring v. under-monitoring?
   Do you agree with the assessment of the paper?
   Why or why not, in your experience?

3. What is cause-based v. symptom-based and where do they belong? Do you agree?

<div class="warning">

Submit your input by following the link below.

The discussion posts are done in Discord Forums.

</div>

- [Link to Discussion Forum](https://discord.com/channels/611027490848374811/1365776270800977962)

## Definitions

---

Telemetry

Tracing

- Span
- Label

Time Series Database (TSDB)

Queue

Upper control limit / Lower control limit (UCL/LCL)

Aggregation

SLO, SLA, SLI

Push v. Pull of data

Alerting rules

Alertmanager

- Alert template
- Routing
- Throttling

Monitoring for defensive operations

- SIEM
- Intrusion Detection Systems - IDS
- Intrusion Prevention Systems - IPS

## Digging Deeper

---

1. Look into Wazuh: [Security Information and Event Management (SIEM). Real Time Monitoring | Wazuh](https://wazuh.com/platform/siem/)

   1. What are their major capabilities and features (what they advertise)?
   1. What are they doing with logs that increases visibility and usefulness in the security space?
      [Log data analysis - Use cases · Wazuh documentation](https://documentation.wazuh.com/current/getting-started/use-cases/log-analysis.html)

## Reflection Questions

---

1. What do I mean when I say that security is an art and not an engineering practice?

2. What questions do you still have about this week?

3. How are you going to use what you've learned in your current role?
