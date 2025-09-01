<div class="flex-container">
        <img src="https://github.com/ProfessionalLinuxUsersGroup/img/blob/main/Assets/Logos/ProLUG_Round_Transparent_LOGO.png?raw=true" width="64" height="64"></img>
    <p>
        <h1>Unit 8 Worksheet - Scripting</h1>
    </p>
</div>

## Instructions

---

Fill out the worksheet as you progress through the lab and discussions.
Hold your worksheets until the end to turn them in as a final submission packet.

### Resources / Important Links

- [TLDP Bash Beginner's Guide](https://tldp.org/LDP/Bash-Beginners-Guide/html/chap_01.html)
- [devhints.io - Bash Scripting Cheatsheet](https://devhints.io/bash)
- [Bash Hacker's Wiki](https://web.archive.org/web/20230406205817/https://wiki.bash-hackers.org/)

#### Downloads

The worksheet has been provided below. The document(s) can be transposed to
the desired format so long as the content is preserved. For example, the `.txt`
could be transposed to a `.md` file.

- <a href="./assets/downloads/u8/u8_worksheet.txt" target="_blank" download>📥 u8_worksheet(`.txt`)</a>
- <a href="./assets/downloads/u8/u8_worksheet.docx" target="_blank" download>📥 u8_worksheet(`.docx`)</a>

### Unit 8 Recording

<iframe
    style="width: 100%; height: 100%; border: none;
    aspect-ratio: 16/9; border-radius: 1rem; background:black"
    src="https://www.youtube.com/embed/sn_LwfIObQw?si=aBqkZL1RIzKN9mWx"
    title="Unit 7: Package Management on Linux - System Administrator Course"
    frameborder="0"
    allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share"
    referrerpolicy="strict-origin-when-cross-origin"
    allowfullscreen>
</iframe>

#### Discussion Post #1

Scenario:

<blockquote>

It’s a 2 week holiday in your country and most of the engineers and architects who designed the system are out of town.

You’ve noticed a pattern of logs filling up on a set of web servers from increased traffic.
Your research shows, and then you verify, that the logs are being sent off real time to Splunk.
Your team has just been deleting the logs every few days, but one of the 3rd shift engineers didn’t
read the notes and your team suffered downtime.

How might you implement a simple fix to stop gap the problem before all the engineering resources come back next week?

</blockquote>

1. What resources helped you answer this?

2. Why can’t you just make a design fix and add space in /var/log on all these systems?

3. Why can’t you just make a design change and logrotate more often so this doesn’t happen?

4. For 2,3 if you are ok with that, explain your answer. (This isn’t a trick, maybe there is a valid reason.)

#### Discussion Post #2

Scenario:

<blockquote>

You are the only Linux Administrator at a small healthcare company.
The engineer/admin before you left you a lot of scripts to untangle.
This is one of our many tasks as administrators, so you set out to accomplish it.
You start to notice that he only ever uses nested `if` statements in bash.

You also notice that every loop is a conditional `while true`, and then he breaks the loop after a decision test each loop.
You know his stuff works, but you think it could be more easily written for supportability, for you and future admins.
You decide to write up some notes by reading some google, AI, and talking to your peers.

</blockquote>

1. Compare the use of nested if versus case statement in bash.

2. Compare the use of conditional and counting loops. Under what circumstances would you use one or the other?

<div class="warning">

Submit your input by following the link below.

The discussion posts are done in Discord Forums.

</div>

- [Link to Discussion Forum](https://discord.com/channels/611027490848374811/1365776270800977962)


## Definitions

---

Variables:

Interpreted program:

Compiled program:

Truth table:

AND/OR logic:

Single/Dual/Multiple alternative logic:

## Digging Deeper

---

1. Read:

- <https://tldp.org/LDP/Bash-Beginners-Guide/html/sect_07_01.html>
- <https://tldp.org/LDP/Bash-Beginners-Guide/html/sect_07_02.html>
- <https://tldp.org/LDP/Bash-Beginners-Guide/html/sect_07_03.html>

What did you learn about capabilities of bash that can help you in your scripting?

2.  If you want to dig more into truth tables and logic, this is a good start: <https://en.wikipedia.org/wiki/Truth_table>

## Reflection Questions

---

1. What questions do you still have about this week?

2. Just knowing a lot about scripting doesn’t help much against actually doing it in
   a practical sense.
   What things are you doing currently at work or in a lab that you can apply some of
   this logic to?
