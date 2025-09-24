# Getting Started

Welcome to the Professional Linux Users Group! You're likely here because you
want to take a structured approach to learning Linux. Our community is
passionate about sharing knowledge. We come together voluntarily to create
these web-books as companion materials for our interactive courses.

We call them interactive because participation with your peers during the
course time frame is required to earn a certificate. That said, you are also
free to follow along with the materials at your own pace. Inside each book,
you'll find everything you need: labs, worksheets, and recorded lecture videos.

### A Bit About Linux

Linux, a **UNIX-like operating system**, is built around the **kernel**—the
core component that acts as a bridge between hardware and software. The kernel
manages resources such as memory, processes, and devices, while we as users
interact with it indirectly through a **shell**, entering commands that the
system interprets and executes.

On top of the Linux kernel sit many different **distributions (distros)**. A
distribution is a curated package that typically includes:

- The Linux kernel
- A collection of software tools and utilities (typically called the Operating System)
- Package management systems
- Optionally, a desktop environment for graphical interaction

These distributions vary in design and purpose -- some focus on ease of use,
others on performance, stability, or security. Whether you choose Ubuntu,
Fedora, Arch, or another distro, the underlying kernel remains the same.

Once you learn Linux fundamentals, your skills are portable across nearly all
distributions.

## 1. Learning Basic Linux Skills

The best way to understand Linux is through hands-on practice. This is
sometimes called Time on Tools (TOT)—the time you spend directly working with
the commands, files, and systems yourself. Reading guides and watching
tutorials are helpful, but it’s the act of typing commands, troubleshooting
mistakes, and seeing the results that makes the knowledge stick.

### Killercoda

Killercoda is a website that hosts interactive labs developed by many different
creators. Scott Champine (Het Tanis) has created a number of labs including the
basics of Linux. By creating an account on `Killercoda` you will be able to
gain hands on experience with the `Linux Command Line Terminal` through your
web browser on any computer free of charge.

[:octicons-arrow-right-24: Linux Labs by Het](https://killercoda.com/het-tanis/course/Linux-Labs)

### Joining the Discord

Our Discord server holds regular scheduled events where one can actively or passively
participate. It is also a place to ask questions or get involved in projects.

[:octicons-arrow-right-24: Link to Discord](https://discord.gg/vrbMr3ct)

### "Beginners Start Here" Playlist

<iframe
    style="
        width: 100%;
        height: 100%;
        border: none;
        aspect-ratio: 16/9;
        border-radius: 1rem;
        background:black"
    src="https://www.youtube.com/embed/alcsTPQsruM?si=Dluz0h-UCgg9YfsW"
    title="Beginners Start Here"
    frameborder="0"
    allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share"
    referrerpolicy="strict-origin-when-cross-origin"
    allowfullscreen>
</iframe>

[:fontawesome-brands-youtube:{ .youtube } :octicons-arrow-right-24: Het_Tanis' Full "Beginners Start Here" Playlist](https://www.youtube.com/watch?v=alcsTPQsruM&list=PLyuZ_vuAWmpqHEm-Js2gZleKzUY5uBWcM)

## 2. Setting Up a Local Linux Install

Killercoda is a great way for newcomers to dip their toes into Linux. However,
because Killercoda creates **ephemeral virtual environments**, everything is
temporary — you can't keep your progress or return to the same setup later. The
next logical step is to set up something more **permanent**.

There are several ways you can run Linux at home:

- **Virtual Machine (VM)**: Run Linux inside Windows or macOS using software like VirtualBox or VMware.
- **Windows Subsystem for Linux (WSL)**: A convenient way to run Linux alongside Windows without a full VM.
- **HomeLab with a Type 1 Hypervisor (e.g., Proxmox)**: Run multiple virtual machines or containers on one dedicated server.
- **Direct Install**: Put Linux on an old desktop, laptop, or single-board computer (like a Raspberry Pi).
- **Virtual Private Server (VPS)**: Rent a remote Linux server from a hosting provider.

Each approach has pros and cons depending on your goals:

- Some setups include a **desktop environment** (a Graphical User Interface/GUI),
  while others are **headless** (no graphical interface, only command-line).
- A dedicated hypervisor can host **multiple test environments**, while a
  direct install gives you a **single dedicated machine**.

Take some time to research which option best fits your needs, budget, and
comfort level.

Some resources to get you started with a local Linux installation:

- Ubuntu Server Install (no GUI): <https://ubuntu.com/tutorials/install-ubuntu-server#1-overview>
- Ubuntu Desktop Install (with a GUI): <https://ubuntu.com/tutorials/install-ubuntu-desktop#1-overview>
- Rocky Linux Install (with a GUI): <https://krython.com/post/installing-rocky-linux-9-complete-installation-guide>

## 3. Participation in a Course

The ProLUG Certified Enterprise Linux Administration Course is meant to teach
you the fundamentals of Linux. It is a long and involved course at 16 weeks
with roughly 160 hours of contact time. Each unit has worksheets and labs to
complete, along with discussion posts to participate in.

To see when the course is actively running, check the events in Discord.

The course book is available for anyone to complete at any time. However,
participation during an active course run is the only way to receive the
certification.

[:octicons-arrow-right-24: Linux Admin Course Book](/course-books/lac/syllabus/)
