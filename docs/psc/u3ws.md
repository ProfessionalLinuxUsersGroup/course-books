<div class="flex-container">
        <img src="https://github.com/ProfessionalLinuxUsersGroup/img/blob/main/Assets/Logos/ProLUG_Round_Transparent_LOGO.png?raw=true" width="64" height="64"></img>
    <p>
        <h1>Unit 3 Worksheet - User Access and System Integration</h1>
    </p>
</div>

## Instructions

---

Fill out this sheet as you progress through the lab and discussions. Hold your worksheets until
the end to turn them in as a final submission packet.

### Resources / Important Links

- <https://www.sans.org/information-security-policy/>
- <https://www.sans.org/blog/the-ultimate-list-of-sans-cheat-sheets/>
- <https://docs.rockylinux.org/guides/security/pam/>
- <https://docs.rockylinux.org/guides/security/authentication/active_directory_authentication/>
- <https://docs.rockylinux.org/books/admin_guide/06-users/>

#### Downloads

The worksheet has been provided below. The document(s) can be transposed to
the desired format so long as the content is preserved. For example, the `.txt`
could be transposed to a `.md` file.

- <a href="./assets/downloads/u3/u3_worksheet.pdf" target="_blank" download>📥 u3_worksheet(`.pdf`)</a>
- <a href="./assets/downloads/u3/u3_worksheet.txt" target="_blank" download>📥 u3_worksheet(`.txt`)</a>
<!-- - <a href="./assets/downloads/u3/u3_worksheet.docx" target="_blank" download>📥 u3_worksheet(`.docx`)</a> -->

### Unit 3 Recording

<!-- <img src="./assets/images/under-construction.jpg" style="border-radius:2%"></img> -->

<iframe
    style="width: 100%; height: 100%; border: none;
    aspect-ratio: 16/9; border-radius: 1rem; background:black"
    src="https://www.youtube.com/embed/-4FhZ2q4RSo"
    title="Unit 3 Recording - ProLUG Linux Security Engineering Course - Free in Discord"
    frameborder="0"
    allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share"
    referrerpolicy="strict-origin-when-cross-origin"
    allowfullscreen>
</iframe>

#### Discussion Post #1

There are 16 Stigs that involve PAM for RHEL 9.
Read the guide from Rocky Linux here: <https://docs.rockylinux.org/guides/security/pam/>

1. What are the mechanisms and how do they affect PAM functionality?
   - Review `/etc/pam.d/sshd` on a Linux system.  
     What is happening in that file relative to these functionalities?
2. What are the common PAM modules?
   - Review `/etc/pam.d/sshd` on a Linux system.  
     What is happening in that file relative to these functionalities?
3. Look for a blog post or article about PAM that discusses real world application.  
   Post it here and give us a quick synopsis. (Bonus arbitrary points if you find one of our ProLUG members blogs on the subject.)

#### Discussion Post #2

Read about active directory (or LDAP) configurations of Linux via `sssd` here:
<https://docs.rockylinux.org/guides/security/authentication/active_directory_authentication>

1. Why do we not want to just use local authentication in Linux? Or really any system?
2. There are 4 SSSD STIGS.
   - What are they?
   - What do they seek to do with the system?

<div class="warning">
Submit your input by following the link below.

The discussion posts are done in Discord threads. Click the 'Threads' icon on the top right and search for the discussion post.

</div>

- [Link to Discussion Posts](https://discord.com/channels/611027490848374811/1098309490681598072)

## Definitions

---

PAM:

AD:

LDAP:

sssd:

oddjob:

krb5:

realm/realmd:

wheel (system group in RHEL):

## Digging Deeper

---

1. How does `/etc/security/access.conf` come into play with pam_access?
   Read up on it here: <https://man7.org/linux/man-pages/man8/pam_access.8.html>
   - Can you find any other good resources?
   - What is the structure of the access.conf file directives?
2. What other important user access or user management information do you learn by
   reading this? <https://docs.rockylinux.org/books/admin_guide/06-users/>
   - What is the contents of the `/etc/login.defs` file? Why do you care?

## Reflection Questions

---

1. What questions do you still have about this week?

2. How are you going to use what you've learned in your current role?
