# Unit 5 Worksheet - Repos & Patching

## Instructions

Fill out this sheet as you progress through the lab and discussions. Hold your worksheets until
the end to turn them in as a final submission packet.

### Resources / Important Links

- <https://public.cyber.mil/stigs/downloads/>
- <https://httpd.apache.org/>
- <https://docs.rockylinux.org/books/admin_guide/13-softwares/>
- <https://sig-core.rocky.page/documentation/patching/patching/>
- <https://wiki.rockylinux.org/rocky/repo/>
- <https://www.sans.org/information-security-policy/>
- <https://www.redhat.com/en/blog/whats-epel-and-how-do-i-use-it/>

#### Downloads

The worksheet has been provided below. The document(s) can be transposed to
the desired format so long as the content is preserved. For example, the `.txt`
could be transposed to a `.md` file.

- <a href="https://professionallinuxusersgroup.github.io/course-books/assets/psc/downloads/u5/u5_worksheet.txt" target="_blank">📥 u5_worksheet(`.txt`)</a>
- <a href="https://professionallinuxusersgroup.github.io/course-books/assets/psc/downloads/u5/u5_worksheet.pdf" target="_blank">📥 u5_worksheet(`.pdf`)</a>

### Unit 5 Recording

<iframe
    style="width: 100%; height: 100%; border: none;
    aspect-ratio: 16/9; border-radius: 0.25rem; background:black"
    src="https://www.youtube.com/embed/YyK5doWENY8"
    title="Unit 5 Recording - ProLUG Linux Security Engineering Course - Free in Discord"
    frameborder="0"
    allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share"
    referrerpolicy="strict-origin-when-cross-origin"
    allowfullscreen>
</iframe>

Link: <https://www.youtube.com/watch?v=YyK5doWENY8>

#### Discussion Post #1

Review the rocky documentation on Software management in Linux.

- <https://docs.rockylinux.org/books/admin_guide/13-softwares/>

1. What do you already understand about the process?
2. What new things did you learn or pick up?
3. What are the DNF plugins?
   What is the use of the versionlock plugin?
4. What is an EPEL?
   Why do you need to consider this when using one?

#### Discussion Post #2

Do a google search for "patching enterprise Linux" and try to
wade through all of the noise.

1. What blogs (or AI) do you find that enumerates a list of steps or checklists to
   consider?
2. After looking at that, how does patching a fleet of systems in the enterprise differ
   from pushing "update now" on your local desktop?
   What seems to be the major considerations?
   What seems to be the major roadblocks?

!!! info

    Submit your input by following the link below. The discussion posts are done in Discord Forums.
    [Link to Discussion Forum](https://discord.com/channels/611027490848374811/1365776270800977962)

## Definitions

Patching

Repos

Software

EPEL

BaseOS v. Appstream (in RHEL/Rocky)

Other types you can find?

- httpd
- patching
- GPG Key
- DNF/YUM

## Digging Deeper

1. After completing the lab and worksheet, draw out how you would deploy a software
   repository into your system.
   How are you going to update it?
   What tools do you find that are useful in this space?

## Reflection Questions

1. Why is it that repos are controlled by root/admin functions and not any user,
   developer, or manager?

2. What questions do you still have about this week?

3. How are you going to use what you've learned in your current role?
