<div class="flex-container">
        <img src="https://github.com/ProfessionalLinuxUsersGroup/img/blob/main/Assets/Logos/ProLUG_Round_Transparent_LOGO.png?raw=true" width="64" height="64"></img>
    <p>
        <h1>Unit 2 Worksheet - Securing the Network Connection</h1>
    </p>
</div>

## Instructions

---

Fill out this sheet as you progress through the lab and discussions. Hold your worksheets until
the end to turn them in as a final submission packet.

### Resources / Important Links

- <https://www.sans.org/information-security-policy/>
- <https://www.sans.org/blog/the-ultimate-list-of-sans-cheat-sheets/>
- <https://docs.rockylinux.org/gemstones/core/view_kernel_conf/>
- <https://ciq.com/blog/demystifying-and-troubleshooting-name-resolution-in-rocky-linux/>
- <https://www.activeresponse.org/wp-content/uploads/2013/07/diamond.pdf>

#### Downloads

The worksheet has been provided below. The document(s) can be transposed to
the desired format so long as the content is preserved. For example, the `.txt`
could be transposed to a `.md` file.

- <a href="./assets/downloads/u2/u2_worksheet.txt" target="_blank" download>📥 u2_worksheet(`.txt`)</a>
- <a href="./assets/downloads/u2/u2_worksheet.docx" target="_blank" download>📥 u2_worksheet(`.docx`)</a>

### Unit 2 Recording

<!-- <img src="./assets/images/under-construction.jpg" style="border-radius:2%"></img> -->

<iframe
    style="width: 100%; height: 100%; border: none;
    aspect-ratio: 16/9; border-radius: 1rem; background:black"
    src="https://www.youtube.com/embed/x1kgXOWv-eM"
    title="Unit 2 Recording - ProLUG Linux Security Engineering Course - Free in Discord"
    frameborder="0"
    allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share"
    referrerpolicy="strict-origin-when-cross-origin"
    allowfullscreen>
</iframe>

#### Discussion Post #1

There are 401 stigs for RHEL 9. If you filter in your STIG viewer for
`sysctl` there are 33 (mostly network focused), ssh - 39, and network - 58. Now there are
some overlaps between those, but review them and answer these questions

1. As systems engineers why are we focused on protecting the network portion of our
   server builds?
2. Why is it important to understand all the possible ingress points to our servers that
   exist?
   - Why is it so important to understand the behaviors of processes that are
     connecting on those ingress points?

#### Discussion Post #2

Read this: <https://ciq.com/blog/demystifying-and-troubleshooting-name-resolution-in-rocky-linux/>
or similar blogs on DNS and host file configurations.

1. What is the significance of the nsswitch.conf file?

2. What are security problems associated with DNS and common exploits? (May have
   to look into some more blogs or posts for this)

<div class="warning">
Submit your input by following the link below.

The discussion posts are done in Discord threads. Click the 'Threads' icon on the top right and search for the discussion post.

</div>

- [Link to Discussion Posts](https://discord.com/channels/611027490848374811/1098309490681598072)

## Definitions

---

sysctl:

nsswitch.conf:

DNS:

Openscap:

CIS Benchmarks:

ss/netstat:

tcpdump:

ngrep:

## Digging Deeper

---

1. See if you can find any DNS exploits that have been used and written up in the
   diamond model of intrusion analysis format. If you can, what are the primary actors
   and actions that made up the attack?

## Reflection Questions

---

1. What questions do you still have about this week?

2. How are you going to use what you've learned in your current role?
