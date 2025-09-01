<div class="flex-container">
        <img src="https://github.com/ProfessionalLinuxUsersGroup/img/blob/main/Assets/Logos/ProLUG_Round_Transparent_LOGO.png?raw=true" width="64" height="64"></img>
    <p>
        <h1>Unit 11 Worksheet - Monitoring</h1>
    </p>
</div>

## Instructions

---

Fill out the worksheet as you progress through the lab and discussions.
Hold your worksheets until the end to turn them in as a final submission packet.

### Resources / Important Links

- [How to easily monitor your Linux server | Grafana Labs](https://grafana.com/solutions/linux-node/monitor/)
- [30 Linux System Monitoring Tools Every SysAdmin Should Know](https://www.cyberciti.biz/tips/top-linux-monitoring-tools.html)
- [Monitoring Linux Using SNMP - Nagios](https://www.nagios.com/solutions/linux-monitoring/)

#### Downloads

The worksheet has been provided below. The document(s) can be transposed to
the desired format so long as the content is preserved. For example, the `.txt`
could be transposed to a `.md` file.

- <a href="./assets/downloads/u11/u11_worksheet.txt" target="_blank" download>📥 u11_worksheet(`.txt`)</a>
- <a href="./assets/downloads/u11/u11_worksheet.docx" target="_blank" download>📥 u11_worksheet(`.docx`)</a>

### Unit 11 Recording

<iframe
    style="width: 100%; height: 100%; border: none;
    aspect-ratio: 16/9; border-radius: 1rem; background:black"
    src="https://www.youtube.com/embed/6VOHFYkptOw"
    title="Unit 11 Recording - ProLUG Linux Systems Administration Course - Free in Discord"
    frameborder="0"
    allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share"
    referrerpolicy="strict-origin-when-cross-origin"
    allowfullscreen>
</iframe>

#### Discussion Post #1

<blockquote>

You’ve heard the term “loose coupling” thrown around the
office about a new monitoring solution coming down the pike. You find a good resource and
read the section on “Prefer Loose Coupling” <https://sre.google/workbook/monitoring/>.

</blockquote>

1. What does “loose coupling” mean, if you had to summarize to your junior team
   members?

2. What is the advantage given for why you might want to implement this type of
   tooling in your monitoring? Do you agree? Why or why not?

3. They mention “exposing metrics” what does it mean to expose metrics? What
   happens to metrics that are exposed but never collected?

#### Discussion Post #2

<blockquote>

Your HPC team is asking for more information about how CPU0
is behaving on a set of servers. Your team has node exporter writing data out to Prometheus
(Use this to simulate <https://promlabs.com/promql-cheat-sheet/>).

</blockquote>

1. Can you see the usage of CPU0 and what is the query?

2. Can you see the usage of CPU0 for just the last 5 minutes and what is the query?

3. You know that CPU0 is excluded from Slurm, can you exclude that and only pull the
   user and system for the remaining CPUs and what is that query?

<div class="warning">

Submit your input by following the link below.

The discussion posts are done in Discord Forums.

</div>

- [Link to Discussion Forum](https://discord.com/channels/611027490848374811/1365776270800977962)


## Definitions

---

SLO

SLA

SLIKPI

Span

Trace

Prometheus

Node_Exporter

Grafana

Dashboard

Heads up Display

## Digging Deeper

---

1. Read the rest of the chapter <https://sre.google/workbook/monitoring/>
   and note anything else of interest when it comes to monitoring and dashboarding.

2. Look up the “ProLUG Prometheus Certified Associate Prep 2024” in Resources ->
   Presentations in our ProLUG Discord. Study that for a deep dive into Prometheus.

3. Complete the project section of “Monitoring Deep Dive Project Guide” from the
   prolug-projects section of the Discord. We have a Youtube video on that project as
   well. <https://www.youtube.com/watch?v=54VgGHr99Qg>

## Reflection Questions

---

1. What questions do you still have about this week?

2. How can you apply this now in your current role in IT? If you’re not in IT, how can you
   look to put something like this into your resume or portfolio?
