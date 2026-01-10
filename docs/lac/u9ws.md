# Unit 9 Worksheet - Containerization on Linux

## Instructions

Fill out the worksheet as you progress through the lab and discussions.
Hold your worksheets until the end to turn them in as a final submission packet.

### Resources / Important Links

- [Dockerfile Reference Page](https://docs.docker.com/reference/dockerfile/)
- [Podman Command List](https://docs.podman.io/en/latest/Commands.html)

#### Downloads

The worksheet has been provided below. The document(s) can be transposed to
the desired format so long as the content is preserved. For example, the `.txt`
could be transposed to a `.md` file.

- <a href="https://professionallinuxusersgroup.github.io/course-books/assets/lac/downloads/u9/u9_worksheet.txt" target="_blank">📥 u9_worksheet(`.txt`)</a>
- <a href="https://professionallinuxusersgroup.github.io/course-books/assets/lac/downloads/u9/u9_worksheet.docx" target="_blank">📥 u9_worksheet(`.docx`)</a>
- <a href="https://professionallinuxusersgroup.github.io/course-books/assets/lac/downloads/u9/u9_worksheet.pdf" target="_blank">📥 u9_worksheet(`.pdf`)</a>

### Unit 9 Recording

<iframe
    style="width: 100%; height: 100%; border: none;
    aspect-ratio: 16/9; border-radius: 0.25rem; background:black"
    src="https://www.youtube.com/embed/_lo50mgERJY"
    title="Unit 9 Recording - ProLUG Linux Systems Administration Course - Free in Discord"
    frameborder="0"
    allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share"
    referrerpolicy="strict-origin-when-cross-origin"
    allowfullscreen>
</iframe>

Link: <https://www.youtube.com/watch?v=_lo50mgERJY>

#### Discussion Post #1

It’s a slow day in the NOC and you have heard that a new system of container deployments are being used by your developers. Do some reading about containers, docker, and podman.

1.  What resources helped you answer this?

2.  What did you learn about that you didn’t know before?

3.  What seems to be the major benefit of containers?

4.  What seems to be some obstacles to container deployment?

#### Discussion Post #2

!!! abstract "Scenario"

    You get your first ticket about a problem with containers. One of the engineers is trying to move his container up to the Dev environment shared server. He sends you over this information about the command he’s trying to run.

    ```plaintext
    [developer1@devserver read]$ podman ps
    CONTAINER ID  IMAGE       COMMAND     CREATED     STATUS      PORTS       NAMES
    [developer1@devserver read]$ podman images
    REPOSITORY                TAG                IMAGE ID      CREATED      SIZE
    localhost/read_docker     latest             2c0728a1f483  5 days ago   68.2 MB
    docker.io/library/python  3.13.0-alpine3.19  9edd75ff93ac  3 weeks ago  47.5 MB
    [developer1@devserver read]$ podman run -dt -p 8080:80/tcp docker.io/library/httpd
    ```

    You decide to check out the server

    ```plaintext
    [developer1@devserver read] ss -ntulp
    Netid   State    Recv-Q   Send-Q      Local Address:Port        Peer Address:Port         Process
    udp     UNCONN   0        0           127.0.0.53%lo:53               0.0.0.0:*             users:(("systemd-resolve",pid=166693,fd=13))
    tcp     LISTEN   0        80              127.0.0.1:3306             0.0.0.0:*             users:(("mariadbd",pid=234918,fd=20))
    tcp     LISTEN   0        128               0.0.0.0:22               0.0.0.0:*             users:(("sshd",pid=166657,fd=3))
    tcp     LISTEN   0        4096        127.0.0.53%lo:53               0.0.0.0:*             users:(("systemd-resolve",pid=166693,fd=14))
    tcp     LISTEN   0        4096                    *:8080                   *:*             users:(("node_exporter",pid=662,fd=3))
    ```


1. What do you think the problem might be?

    -  How will you test this?

2. The developer tells you that he’s pulling a local image. Do you find this to be
   true, or is something else happening in their `run` command?

!!! info

    Submit your input by following the link below. The discussion posts are done in Discord forums.
    [Link to Discussion Posts](https://discord.com/channels/611027490848374811/1365776270800977962)

## Definitions

Container:

Docker:

Podman:

CI/CD:

Dev/Prod Environments (Development/Production Environments):

Dockerfile:

Docker/Podman images:

Repository:

## Digging Deeper

1. Find a blog on deployment of some service or application in a container that interests you.  
    See if you can get the deployment working in the lab.

    -  What worked well?
    -  What did you have to troubleshoot?
    -  What documentation can you make to be able to do this faster next time?

2. Run this scenario and play with K3s: <https://killercoda.com/k3s/scenario/intro>

## Reflection Questions

1. What questions do you still have about this week?

2. How can you apply this now in your current role in IT? If you’re not in IT, how
   can you look to put something like this into your resume or portfolio?
