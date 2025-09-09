# Contributing to the ProLUG Linux Course Books

The Professional Linux Users Group (ProLUG) provides a set of requirements
and guidelines to contribute to this project. Below are steps to ensure
contributors are adhering to those guidelines and fostering a productive
version control environment.

## How to be a Successful Contributor

To be an effective contributor understanding Git, whether through the command line or an
external tool, will be an important part of contributing. To this effect it is important
that any individual who contributes to this project have a working understanding of committing,
merging, and other fundamental Git workflows.

For clarity this project utilizes GitHub for remote repositories and CI/CD testing
pipeline workflows. Git and GitHub are two separate entities where GitHub provides
the hosting services and Git provides the version control.

Prospective contributors are directed to several resources should they feel their
competency with Git or GitHub falls short:

Git [documentation](https://git-scm.com/doc) and GitHub video tutorials:

- [ByteByteGo's Git Explained in 4 Minutes (4m)](https://www.youtube.com/watch?v=e9lnsKot_SQ) :fontawesome-brands-youtube:{ .youtube }
- [Fireship's How to use Git and Github (12m)](https://youtu.be/HkdAHXoRtos) :fontawesome-brands-youtube:{ .youtube }
- [freeCodeCamp's Git and GitHub Crash Course (1hr)](https://youtu.be/RGOj5yH7evk) :fontawesome-brands-youtube:{ .youtube }

## Signing your Git Commits with SSH

Contributors who elect to contribute through the command line will need
to verify their identities before their commits can be accepted. **This step
is not required if contributors will be submitting changes via GitHub.com itself**
since users will have verified their identities with GitHub's own verification
process.

**To reiterate, individuals contributing via command line will need to sign their
commits through SSH**. Signing GitHub commits helps ProLUG validate incoming commits
from trusted contributors that reside outside the GitHub ecosystem. It can be quite
trivial to impersonate users on GitHub and it is in the best interest of the project
and contributors to observe this security practice.

It should also be noted that GitHub supplies tools like [GitHub CLI](https://cli.github.com/)
that abstract away the process of signing and verifying commits from the command line.
GitHub provides a `gh auth login` function to facilitate the procedure which contributors
can employ without the necessary changes suggested below.

To Sign your Git Commits with SSH:

Generate an SSH key pair if you don't have one:

```bash linenums="1"
ssh-keygen -t ed25519
```

Add SSH public key ('.pub' suffix) to GitHub as "Signing Key".
![addkey](assets/images/addkey.png)

\* GitHub.com -> Profile -> Settings -> GPG and SSH Keys -> Add SSH Key -> Drop down -> Signing Key

Below is a bash script that will attempt to configure signing
Git commits on a localhost:

```bash title="commit-sign.bash" linenums="1"
#!/bin/bash
GH_USERNAME="YourUsername"
git config --global gpg.format ssh
git config --global user.signingkey ~/.ssh/id_ed25519.pub
git config --global tag.gpgSign true
git config --global commit.gpgSign true
mkdir -p ~/.config/git
touch ~/.config/git/allowed_signers
echo "${GH_USERNAME} $(cat ~/.ssh/id_ed25519.pub)" > ~/.config/git/allowed_signers
git config --global gpg.ssh.allowedSignersFile ~/.config/git/allowed_signers
# Make a commit to verify
git log --show-signature -1
```

Make a commit after running those commands and then use `git log --show-signature -1`.
You should see something like `Good "git" signature for <yourname> with ED25519 key SHA256:abcdef...` if it worked.

![verified](assets/images/verified.png)

Your commits should now be verified from your account. This helps us ensure that valid users are
contributing to this project. Unverified commits will be scrutinized and likely discarded.

## Syncing your Fork with the Upstream ProLUG Repo

![syncfork](assets/images/syncfork.png)

In an effort to minimize merge conflicts we strongly suggest forks remain up to date with
the original repository before committing changes. This will help us reduce pull request management overhead.

!!! warning

    Pull requests with substantial merge conflicts may be rejected or marked for change requests.

You can do this from the GitHub web UI easily with the `Sync Fork` button. If you want to do this from the terminal, you can add a new `git remote` called `upstream`.

```bash
git remote add upstream https://github.com/ProfessionalLinuxUsersGroup/course-books.git
```

Then, to sync your local fork with the original repo, do a `git pull` from the `upstream` remote.

```bash
git pull upstream main
```

This fork should now be up to date with the original upstream repository.

## Basic Contribution Workflow

You'll create your own fork of the repository using the GitHub web UI, create a
branch, make changes, push to your fork, then open a pull request.

The basic steps to contribute are outlined below.

### Comment First

If you'd like to work on a specific worksheet or lab, please let us know first by
commenting on the issue so you can be assigned to it.
This way, other contributors can see that someone is already working on it.

This helps the repository maintainers and contributors attain a high degree of
visibility and collaboration before merging changes.

### Create a Fork

Go to the [original repository link](https://github.com/ProfessionalLinuxUsersGroup/course-books).
Click on "Fork" on the top right.

<img src="../assets/images/fork_repo1.png"></img>

Then click "Create Fork" on the next page.

<img src="../assets/images/fork_repo2.png"></img>

Now you'll have your own version of the repository tied to your GitHub account.

### Clone the Fork to your Local Machine

After creating your fork, you'll need to clone it down to your local machine in
order to work on it.

```bash
git clone git@github.com:YOUR_USERNAME/course-books.git
# Or, with https:
git clone https://github.com/YOUR_USERNAME/course-books.git
```

### Create a New Branch

Whenever making changes contributors are highly encouraged to create a branch with an
appropriate name. Switch to that branch, then make changes there.

!!! note "Branch Naming Convention"

    Our branch naming convention is as follows:
    ```plaintext
    <book>-<unit>-<action>
    ```
    If you are making a change to something that affects the entire project rather
    than just a specific book, give it a descriptive name.

For example, if you're working on adding the Unit 1 Worksheet for the Linux
Admin Course book:

```bash
git branch lac-unit1-add-worksheet
git switch lac-unit1-add-worksheet
# Or, simply:
git switch -c lac-unit1-add-worksheet
```

### Make Changes and Commit

Once you're on your new branch, make changes to the `u1ws.md` using the editor
of your choice.

```bash
vi u1ws.md
# Make changes
:wq
```

Once the changes are made, commit them.

```bash
git add u1ws.md
git commit -m "feat: Add lac unit 1 worksheet"
```

!!! note "Commit Message Convention"

    Your commit message should be structured following the conventions laid
    out here: <https://www.conventionalcommits.org/en/v1.0.0/#summary>

### Push the Changes

After making your commit, you can now push the changes to **your fork** on the
**new branch** you created earlier.

```bash
git push origin lac-unit1-add-worksheet
```

This will update your forked repository on GitHub to contain the new branch
with the new changes.

### Create a Pull Request

???+ note "Local Testing"

    We ask that you test your changes locally before opening a pull request.
    Our [development page](./development.md) outlines how to test locally.

Now you'll be able to open a pull request.

GitHub should be smart about detecting new changes and prompt you to open
a pull request upon visiting the original repository or your own fork.

You can also go to the [original repository link](https://github.com/ProfessionalLinuxUsersGroup/course-books), go to the "Pull Requests" tab, and create a new pull request.

After starting your pull request, select your branch `lac-unit1-add-worksheet`,
create a description, and mention an issue by number, prefixed with `#` (e.g., `#5`).

## Consider a few Useful Practices

The practices presented below are not required to contribute to the ProLUG
course books but can streamline contributing to any project and are considered
to some as incredibly useful when engaging in version control with Git.

### Git Worktrees

A notably useful workflow provided by Git is the `git worktree`. This allows the instantion of multiple
working directories within a repository that point to a particular branch for any number of reasons without
needing to clone the base respository separately.

Suppose one worktree is created to work on feature "x" on branch feat, and a separate worktree is implemented
for bug "y" on branch 'bug', all localized in the same repository. A git worktree could even be utilized to quickly
checkout a pull request in its own separate directory within the repository facilitating downstream commands like
pushing over changed files to a host for testing.

Git worktree [documentation](https://git-scm.com/docs/git-worktree).

### Git Rebasing

???+ warning

    Do not rebase commits that exist outside your repository and that people may
    have based work on. Rebase only within your own branches and forks, never onto
    public branches or repos.

In sum, rebasing can be utilized to replay commits onto a currently checked-out branch if
such branch is behind in commits from its upstream branch. This allows circumvention of potentially
hard to read merge commits in a busy repository. As such, proper implementation of rebasing can
leave a clean, and easily readable commit history for all concerned parties. Rebasing can also
facilitate the management of branches and working directories in a notably active project in a myriad
of other ways. Contributors are encouraged to explore the possibilties of rebasing.

```bash title="git-rebase.bash" linenums="1"
git checkout experiment
git rebase master
First, rewinding head to replay your work on top of it...
Applying: added staged command

# Or even a simple pull
git pull --rebase # (1)
```

1.  :pencil: The default `git pull` behavior can be changed to rebase
    instead of merging which won't require a `--rebase` flag; `git config --global pull.rebase true`.
    Find out more here: <https://git-scm.com/docs/git-config#Documentation/git-config.txt-pullrebase>

Rebasing also plays a role in facilitating any commit reverts that may need
to be made in the future. More on that will follow.

Git Rebasing [documentation](https://git-scm.com/book/en/v2/Git-Branching-Rebasing).

### Commit Early, Often, and Squashing Commits

It is great practice to commit early, and often. This however can produce hard
to read commits for repo maintainers and contributors. Squashing commits, which is
a type of rebasing, can be utilized to compress a large number of commits made in
a local repository before being pushed upstream to a remote repository and eventual
pull request.

Below is an example of 4 local commits squashed into a single commit that was pushed
remotely:

![squashing](assets/images/squashing.png)

Squashing commits can improve readability, but its primary utility,
especially for larger projects, may be in addressing an event where
rolling back several commits due to a bug or test can be done with a single
commit revert.

freeCodeCamp has a [great write-up on this procedure](https://www.freecodecamp.org/news/git-squash-commits/).
When done appropriately this can greatly facilitate the development process.
Contributors are strongly encouraged to begin exploring these types of workflows
if they never have.

### Git Stashing

Another useful practice is to employ "stashing" uncommitted files in
a local repository. This is useful in many contexts including stashing
local changes to resolve recently introduced remote vs. local repo conflicts,
or quickly switching working spaces.

Stashing effectively unstages any changes made in the local repo and
saves them to be applied later. This can further help facilitate a rebase
or merge before committing changes upstream for instance.

More on this here:

- <https://www.atlassian.com/git/tutorials/saving-changes/git-stash>
- <https://git-scm.com/book/en/v2/Git-Tools-Stashing-and-Cleaning>

## Adding Assets

If you'd like to add an image to one of the pages, you will need to save that
image into the `docs/assets/` directory.

Each book has its own subdirectory in `assets/`:

```text
assets/
├── deploy
├── downloads
├── images
├── lac
├── pcae
└── psc
```

- Notice the `lac`, `psc`, and `pcae` directories. These are where course-specific
  assets belong.

If you're attempting to add an image to a page in the Linux Admin Course book,
you'd move that image to the `docs/assets/lac/images/` directory.

It's preferable that each unit of each course also has its own directory.

For example, if you're adding a diagram to the intro page in unit 6 of the
Linux Admin Course book, this would go in `/docs/asset/lac/images/u6/`. Giving
the image file a descriptive name also helps (e.g., `firewall-connection-diagram.png`).

This convention helps us keep track of assets and where they belong.

Continuing with that example, this is the path that the image should go in:

```text
docs/
└── assets/
    └── lac/
       └── images/
           └── u6/
               └── firewall-connection-diagram.png
```

---

Once you've added the asset to the appropriate directory, you need to reference
it in the page itself. We're adding a diagram to the Unit 6 Intro of the Linux
Admin Course, so we'd add it to `docs/lac/u6intro.md`.

This can be done with a raw HTML `<img>` element:

```html
<img src="../../assets/lac/images/u6/firewall_connection_diagram.png"></img>
```

This is a **relative path** to the image.

- When determining either the relative or absolute path of the image, use
  `mkdocs build` and examine where the asset file is and where the target page is.

  - For example, `docs/lac/u6intro.md` will end up in `/site/lac/u6intro/index.html`

  - So the relative path from here would be
    `../../assets/lac/image/u6/firewall_connection_diagram.png`

???+ note

    The markdown syntax `![alt text](/path/to/image)` also works. However, to
    maintain consistency, we ask that you use the HTML version.

After adding that, your new asset should be ready to go!

To minimize the strain on maintainers, we ask that you test your change locally
before opening a pull request.

## Supporting Material

Below are links to the necessary materials to build out the course templates:

- Look over the [template pages wiki](https://github.com/ProfessionalLinuxUsersGroup/course-books/wiki), or directly here:
  - Pages: [intro](https://github.com/ProfessionalLinuxUsersGroup/course-books/blob/main/ref/intro.md),
    [bonus](https://github.com/ProfessionalLinuxUsersGroup/course-books/blob/main/ref/ub.md),
    [lab](https://github.com/ProfessionalLinuxUsersGroup/course-books/blob/main/ref/ulab.md),
    [worksheet](https://github.com/ProfessionalLinuxUsersGroup/course-books/blob/main/ref/uws.md)

<!-- TODO: Implement wiki for ref material -->

<!-- - Look over the [template pages wiki](https://github.com/ProfessionalLinuxUsersGroup/lac/wiki), or directly here: -->
<!--   - Pages: [intro](https://github.com/ProfessionalLinuxUsersGroup/lac/blob/main/ref/intro.md), -->
<!--     [bonus](https://github.com/ProfessionalLinuxUsersGroup/lac/blob/main/ref/ub.md), -->
<!--     [lab](https://github.com/ProfessionalLinuxUsersGroup/lac/blob/main/ref/ulab.md), -->
<!--     [worksheet](https://github.com/ProfessionalLinuxUsersGroup/lac/blob/main/ref/uws.md) -->
<!---->
<!-- Ancillary unit videos provided by Scott: -->
<!---->
<!-- - <https://www.youtube.com/watch?v=eHB8WKWz2eQ&list=PLyuZ_vuAWmprPIqsG11yoUG49Z5dE5TDu> -->
<!---->
<!-- PDF and docs directly related to each Unit of the course: -->
<!---->
<!-- - <https://discord.com/channels/611027490848374811/1098309490681598072> -->
