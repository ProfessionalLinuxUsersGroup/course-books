# Unit 3 Worksheet - LVM and Raid

## Instructions

Fill out the worksheet as you progress through the lab and discussions.
Hold your worksheets until the end to turn them in as a final submission packet.

### Resources / Important Links

- [Google SRE Book - Implementing SLOs](https://sre.google/workbook/implementing-slos/)
- [AWS High Availability Architecture Guide](https://docs.aws.amazon.com/pdfs/whitepapers/latest/real-time-communication-on-aws/real-time-communication-on-aws.pdf)
- [Red Hat High Availability Cluster Configuration](https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/9/html/configuring_and_managing_high_availability_clusters/index)

#### Downloads

The worksheet has been provided below. The document can be transposed to
the desired format so long as the content is preserved. For example, the `.txt`
could be transposed to a `.md` file.

- <a href="https://professionallinuxusersgroup.github.io/course-books/assets/lac/downloads/u3/u3_worksheet.txt" target="_blank">📥 u3_worksheet(`.txt`)</a>
- <a href="https://professionallinuxusersgroup.github.io/course-books/assets/lac/downloads/u3/u3_worksheet.docx" target="_blank">📥 u3_worksheet(`.docx`)</a>
- <a href="https://professionallinuxusersgroup.github.io/course-books/assets/lac/downloads/u3/u3_worksheet.pdf" target="_blank">📥 u3_worksheet(`.pdf`)</a>

### Unit 3 Recording

<iframe
    style="width: 100%; height: 100%; border: none;
    aspect-ratio: 16/9; border-radius: 0.25rem; background:black"
    src="https://www.youtube.com/embed/NYL85ndQLbc"
    title="Unit 3 Recording - ProLUG Linux Systems Administration Course - Free in Discord"
    frameborder="0"
    allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share"
    referrerpolicy="strict-origin-when-cross-origin"
    allowfullscreen>
</iframe>

Link: <https://www.youtube.com/watch?v=NYL85ndQLbc>

#### Discussion Post #1

Scan the chapter [here](https://google.github.io/building-secure-and-reliable-systems/raw/ch17.html) for keywords and pull out what you think will help you to better understand how to triage an incident.

Read the section called "Operation Security" in this same chapter: [Building Secure and Reliable Systems](https://google.github.io/building-secure-and-reliable-systems/raw/ch17.html)

1. What important concepts do you learn about how we behave during an
    operational response to an incident?

#### Discussion Post #2

Ask Google, find a blog, or ask an AI about high availability. (Here's one if you need it: [AWS Real-Time Communication Whitepaper](https://docs.aws.amazon.com/pdfs/whitepapers/latest/real-time-communication-on-aws/real-time-communication-on-aws.pdf#high-availability-and-scalability-on-aws)

1. What are some important terms you read about? Why do you think understanding
    HA will help you better in the context of triaging incidents?


!!! info

    Submit your input by following the link below. The discussion posts are done in Discord forums.
    - [Link to Discussion Posts](https://discord.com/channels/611027490848374811/1365776270800977962)

## Definitions

Five 9's:

Single Point of Failure (SPOF):

Key Performance Indicators (KPIs):

Service Level Indicator (SLI):

Service Level Objective (SLO):

Service Level Agreement (SLA):

Active-Standby:

Active-Active:

Mean Time to Detect (MTTD):

Mean Time to Recover/Restore (MTTR):

Mean Time Between Failures (MTBF):

## Digging Deeper

1. If uptime is so important to us, why is it so important to us to also understand how our systems can fail? Why would we focus on the thing that does not drive uptime?

2. Start reading about SLOs: [Implementing SLOs](https://sre.google/workbook/implementing-slos/)
   How does this help you operationally?
   Does it make sense that keeping systems within defined parameters will help keep
   them operating longer?

## Reflection Questions

1. What questions do you still have about this week?

2. How are you going to use what you've learned in your current role?
