<div class="flex-container">
        <img src="https://github.com/ProfessionalLinuxUsersGroup/img/blob/main/Assets/Logos/ProLUG_Round_Transparent_LOGO.png?raw=true" width="64" height="64"></img>
    <p>
        <h1>Unit 6 Bonus - Terminal Multiplexors</h1>
    </p>
</div>

> **NOTE:** This is an **optional** bonus section. You **do not** need to read it, but if you're interested in digging deeper, this is for you.

Enhance productivity by enabling the management of multiple sessions and windows from a single remote session.

## Key Features of Terminal Multiplexors

---

### Create Multiple Windows/Panes 🪟

Split your terminal into panes (or windows) so you can run different commands or tasks simultaneously.

### Detach and Reattach Sessions 🪝

You can detach from a session (e.g., when you log out of a remote server), and later reattach to it exactly as you left it.

### Persistence of Long-Running Tasks

If your network connection drops, the tasks keep running on the server, and you can reattach to them later.

### Collaborate

Some terminal multiplexers allow multiple users to connect to the same session, enabling collaborative work on a single system.

## Popular Terminal Multiplexors

---

### Tmux

- Is widely used by developers and system administrators for its flexible configuration and vibrant community support.
- Its popularity also stems from its straightforward scripting capabilities, making it highly useful for automation.

#### Tmux Resources

Tmux, a terminal multiplexer written in C, emerged around 2007, noted for its customizable configuration and scripting. Despite its popularity and flexibility, users occasionally report stability issues and complex scripting. Tmux, crafted in 2007 by Nicholas Marriott in C, marked an evolution from GNU Screen. Its flexible configuration appeals to system admins, despite some users finding the setup syntax intricate. Tmux, created by Nicholas Marriott in 2007, is a C-based terminal multiplexer famous for its configuration flexibility and scripting prowess, but newcomers often find its syntax intricate.

- [Tmux Wiki](https://github.com/tmux/tmux/wiki)
- [Tmux Cheatsheet](https://tmuxcheatsheet.com/)

### GNU Screen

GNU Screen, created by Oliver Laumann in 1987 and written in C, became one of the first mainstream terminal multiplexers, remaining a staple in many Linux distributions. Praised for its stability and included by default in numerous systems, it can still be considered less intuitive in configuration compared to newer options like tmux.

- is one of the original terminal multiplexers and remains popular due to its reliable, time-tested features.
- It continues to be bundled with many Linux distributions by default, contributing to its enduring user base.

#### GNU Screen Resources

- [GNU Screen Site](https://www.gnu.org/software/screen/)
- [GNU Screen Manual](https://www.gnu.org/software/screen/manual/screen.html)

### Zellij

Zellij, first released in 2020 and written in Rust, is a newcomer to the terminal multiplexer space that focuses on an intuitive UI and easy collaboration. While its modern approach and built-in layout management offer clear advantages over older tools, its relatively small community and limited ecosystem may pose challenges for widespread adoption.

- Although not yet included in the default repositories of all distributions, Zellij is rapidly gaining visibility because of its modern design and user-friendly layout management.
- Its growing ecosystem of plugins and emphasis on collaboration make it an attractive choice for developers seeking a more advanced terminal multiplexer.

#### Zellij Resources

- [Zellij Site](https://zellij.dev/)
 
## Downloads
