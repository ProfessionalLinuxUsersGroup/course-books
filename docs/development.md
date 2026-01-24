# Local Development and Testing

It is strongly encouraged that contributors test their changes before making commits.

To help facilitate this process, we have provided a local build script that can
be used to test changes locally.

If the contributor prefers to configure their environment on their own, a set
of instructions and guidelines are provided below. These guidelines are by no
means a requirement or the only set of procedures to locally develop on this
project.

The examples, code, and commands provided below were developed using such technologies as containers,
bash scripts, and more.

## Using the Provided Build Script

If you are on a Linux machine or another machine that has access to Bash and
Python, you may use the script provided in the `scripts/` directory.

This script should be run from the root directory of the project:

```bash linenums="1"
git clone https://github.com/ProfessionalLinuxUsersGroup/course-books.git
cd course-books
./scripts/local-build
```

Use the `--help` option to see usage instructions:

```bash linenums="1"
./scripts/local-build --help
```

This is a Bash script that requires Bash version 4.4+, Python 3.10+, as well as the
`venv` and `pip` Python modules.

This script will create a Python virtual environment for the project, install
the necessary dependencies, and serve the site locally via HTTP. A link will be
output to the terminal that you can use to see the local version of the website.

Any changes made while this script is running will reload the website in
real-time.

When you are done testing, use `Ctrl-C` (`SIGINT`) to stop the script.

!!! note "Reporting an Issue"

    Any issues or errors encountered with this script can be reported by [opening an
    issue](https://github.com/ProfessionalLinuxUsersGroup/course-books/issues/new)
    in the project's repository.

## Building Manually

If you prefer to build out your own test environment, you can do so by
following the instructions below.

### Build Dependencies

The ProLUG course books utilize [Material for MkDocs](https://squidfunk.github.io/mkdocs-material/), a friendly
and popular markdown utility that quickly exports static web files for documentation or general website use cases.

Utilizing Material for MkDocs, this course then deploys the exported web
structure to a GitHub Pages workflow and runner that then produces an easily
navigable website.

Below is the current workflow that deploys the Git Page for the courses:

<figure markdown="span">

![workflow](assets/images/workflow.png)

</figure>

To begin developing locally on this project Material for MkDocs has provided a pre-baked Docker image. Or contributors
can utilize a virtual python environment with the required dependencies.

!!! info inline end "Local Dependencies"

    - `httpd` or `apache2`
    - `git`
    - `weasyprint`
    - Python 3.9+
    - Python virtual environment with `mkdoc-material` required pip packages
    - a clone of the [ProLUG course-books repository](https://github.com/ProfessionalLinuxUsersGroup/course-books)

To achieve this deployment locally without deploying the suggested Materials for MkDocs Docker image the following
environment and dependencies are required: A localhost, this could be a container, virtual machine, or local machine,
and the following packages installed on such machine. :material-arrow-right-box:

More information to get started is provided by Material for MkDocs here: <https://squidfunk.github.io/mkdocs-material/getting-started/>

### Building, Deploying, and Developing Locally

Below is a set of scripts that can quickly achieve this environment in an automated fashion if contributors
choose to forgo utilizing the provided build script.

These commands assume a `root` user. These scripts will update host package repositories to
their latest offerings and download missing dependencies, insantiate the python virtual environment
required to build the project, process and produce the necessary `.html` files from the course book
source files, and deploy the website either via `httpd/apache2` or served via the built-in development server.

Outside of system packages all files will be localized to the `/root/course-books` directory
on the container or machine.

Tested on:
Rocky 10.1 LXC (550MB of packages after install)
Ubuntu 25.04 LXC (850MB of packages after install)

=== "APT"
    ```bash linenums="1" title="install.sh"
    #!/bin/bash
    apt-get update && apt-get -y install git python3-full hostname apache2 weasyprint
    git clone https://github.com/ProfessionalLinuxUsersGroup/course-books
    cd course-books
    python3 -m venv venv
    source venv/bin/activate
    pip install -U pip
    pip install -U mkdocs mkdocs-material mkdocs-glightbox mkdocs-to-pdf
    # use for live reloading after changes:
    #   mkdocs serve -a "$(hostname -I | awk '{print $1}'):8000"
    # use for local webserver:
    #   mkdocs build -d /var/www/html/ && systemctl enable --now apache2
    ```

=== "DNF"
    ```bash linenums="1" title="install.sh"
    #!/bin/bash
    dnf install -y git python3 python-pip pango hostname httpd weasyprint
    git clone https://github.com/ProfessionalLinuxUsersGroup/course-books
    cd course-books
    python3 -m venv venv
    source venv/bin/activate
    pip install -U pip
    pip install -U mkdocs mkdocs-material mkdocs-glightbox mkdocs-to-pdf
    # use for live reloading after changes:
    #   mkdocs serve -a "$(hostname -I | awk '{print $1}'):8000"
    # use for local webserver:
    #   mkdocs build -d /var/www/html/ && systemctl enable --now httpd
    ```

The ProLUG Linux Course Books website should now be available from your web browser either at
<http://localhost:{assigned_port}> or its designated IP address and port.

From here you can use such commands from your localhost to implement changes:

```bash linenums="1"
cd "$HOME"/course-books
source venv/bin/activate
mkdocs build -d /var/www/html
systemctl restart {httpd or apache}
```

These commands will switch your shell into the appropriate directory, activate the python
virtual environment, execute the necessary mkdocs binary located in its installed virtual $PATH,
build the site from the source files, and then finally restart the web server.

From there you should be able to see any changes you have made are reflected.

Or send commands over to a networked container or machine:

!!! note

    To minimize complexity and given the nature of commands over SSH,
    these commands will need to utilize absolute paths.

```bash linenums="1"
scp {working directory}/{targeted document} {TARGET_IP}:/root/course-books/{targeted document}
ssh {TARGET_IP} "cd /root/course-books && /root/course-books/venv/bin/mkdocks build -d /var/www/html && systemctl restart httpd"
```
