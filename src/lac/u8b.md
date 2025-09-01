<div class="flex-container">
        <img src="https://github.com/ProfessionalLinuxUsersGroup/img/blob/main/Assets/Logos/ProLUG_Round_Transparent_LOGO.png?raw=true" width="64" height="64">
    <p>
        <h1>Unit 8 Bonus - Scripting  </h1>
    </p>
</div>

> **NOTE:** This is an **optional** bonus section. You **do not** need to read it, but if you're interested in digging deeper, this is for you.

## Bash: The Essential Skill for Any Linux Administrator

If you're planning to work with Linux, you’ll use **Bash every day** -- whether troubleshooting servers, automating tasks, or managing system configurations.

### Why is bash important?

- Bash is everywhere:
  - Bash is the default shell on all **major Linux distributions** (RedHat, Debian, etc), and most other distributions
  - It automates common sysadmin tasks (backups, log analysis, deployments)
  - Bash is essential for DevOps and administrative workflows (writing scripts, configuring CI/CD pipelines).

### Why learn Bash?

- You can automate repetitive or complex tasks.
- You can manage anything on your system using Bash (files, processes, services, etc.).
- Bash works across almost all major Linux distributions.

Bash scripting turns **manual commands into powerful, reusable automation**.

## **Writing Your First Script**

Let's create a simple script that prints a message.

- **Create a script file:**
  ```bash
  touch first-script.sh
  ```
- **Make it executable:**
  ```bash
  chmod +x first-script.sh
  # Or, use octal
  chmod 755 first-script.sh
  ```
- **Open it in a text editor (e.g., `vi`):**
  ```bash
  vi first-script.sh
  ```
- **Add the following code:**
  ```bash
  #!/bin/bash
  echo "Hello, admin!"
  ```
- **Run the script:**
  ```bash
  ./first-script.sh
  ```
- **Expected output:**

  ```plaintext
  Hello, admin!
  ```

- **Key Takeaways:**
  - The `#!/bin/bash` **shebang line** tells the system which interpreter to use to
    execute the script.
  - `chmod +x` or `chmod 755` **makes the script executable**.
  - `./` is required because the script is **not in the system’s `PATH`**.

It's worth noting that including a `.sh` file extension is **completely optional**.  
If you decide to replace the Bash script with an executable binary down the line,
having a `.sh` file extension can hurt you (e.g., if any other programs try to
execute it using the `.sh` filename).

## **10 Common Control Operators**

These operators allow you to **chain and control command execution** in Bash.

| Operator | Purpose                                       | Example                         |
| -------- | --------------------------------------------- | ------------------------------- |
| `;`      | Run multiple commands sequentially            | `mkdir test; cd test`           |
| `&&`     | Run second command **only if first succeeds** | `mkdir test && cd test`         |
| `\|\|`   | Run second command **only if first fails**    | `mkdir test \|\| echo "Failed"` |
| `&`      | Run a command **in the background**           | `sleep 60 &`                    |
| `\|`     | Pipe output from one command to another       | `ls \| grep ".txt"`             |
| `()`     | Run commands **in a subshell**                | `(cd /tmp && ls)`               |
| `{}`     | Run commands **in the current shell**         | `{ cd /tmp; ls; }`              |
| `>`      | Redirect output to a file (**overwrite**)     | `echo "log" > file.txt`         |
| `>>`     | Redirect output (**append**)                  | `echo "log" >> file.txt`        |
| `$(...)` | Capture command output (from a subshell)      | `DATE=$(date)`                  |

- **Why does this matter?**
  - These operators **control execution flow** and are fundamental to Bash scripting.

## **10 Common Conditionals**

Bash conditionals allow scripts to **make decisions**.

| Test                  | Meaning                         | Example                     |
| --------------------- | ------------------------------- | --------------------------- |
| `[[ -f FILE ]]`       | File exists                     | `[[ -f /etc/passwd ]]`      |
| `[[ -d DIR ]]`        | Directory exists                | `[[ -d /home/user ]]`       |
| `[[ -n STR ]]`        | String is **non-empty**         | `[[ -n "$USER" ]]`          |
| `[[ -z STR ]]`        | String is **empty**             | `[[ -z "$VAR" ]]`           |
| `[[ "$A" = "$B" ]]`   | Strings are **equal**           | `[[ "$USER" = "root" ]]`    |
| `[[ "$A" != "$B" ]]`  | Strings are **not equal**       | `[[ "$USER" != "admin" ]]`  |
| `[[ NUM1 -eq NUM2 ]]` | Numbers are **equal**           | `[[ 5 -eq 5 ]]`             |
| `[[ NUM1 -gt NUM2 ]]` | NUM1 is **greater than** NUM2   | `[[ 10 -gt 5 ]]`            |
| `[[ "$?" -eq 0 ]]`    | Last command **was successful** | `command && echo "Success"` |
| `[[ -x FILE ]]`       | File is **executable**          | `[[ -x script.sh ]]`        |

- **Why does this matter?**

  - These tests are used in `if`-statements and loops.

- **Single brackets vs. double brackets?**
  - Single brackets `[ ... ]` are used in POSIX shell scripts. Using single
    brackets is equivalent to using the `test` command (see `help test` and `help [`)
    - These are generally more subject to shell injection attacks, since they
      allow anything to expand within them.
    - You **must** quote all variables and subshell command (i.e., `"$(...)"`)
      within single brackets.
  - Double brackets `[[ ... ]]` are **keywords** (also builtins) in bash (see `help [[`).
    - These do not require you to quote variables, and provide some extended
      functionality.
    - If you're writing a **Bash** script, there's no reason to use single
      brackets for conditionals.

## 10 Bash Scripting Scenarios

Below are 10 **real-world examples** of using bash from the command line.

| Scenario                                   | Solution                                                    | Cont'd.                                |
| ------------------------------------------ | ----------------------------------------------------------- | -------------------------------------- |
| **Check if a file exists before deleting** | `if [ -f "data.txt" ]; then rm data.txt; fi`                |
| **Backup a file before modifying**         | `cp config.conf config.bak`                                 |
| **Create a log entry every hour**          | `echo "$(date): Check OK" >> log.txt`                       |
| **Monitor disk space**                     | `df -h`                                                     | `awk '$5 > 90 {print "Low disk: "$1}'` |
| **Check if a service is running**          | `systemctl is-active nginx`                                 | `systemctl restart nginx`              |
| **List large files in a directory**        | `find /var/log -size +100M -exec ls -lh {} \;`              |
| **Change all `.txt` files to `.bak`**      | `for file in *.txt; do mv "$file" "${file%.txt}.bak"; done` |
| **Check if a user is logged in**           | `who`                                                       | `grep "admin"`                         |
| **Kill a process by name**                 | `pkill -f "python server.py"`                               |
| **Find and replace text in files**         | `sed -i 's/old/new/g' file.txt`                             |

- **Why does this matter?**
  - These scenarios show **how Bash automates real-world tasks**.

## Debugging Bash Scripts

**Debugging tools** help troubleshoot Bash scripts.

| Command                | Purpose                                             |
| ---------------------- | --------------------------------------------------- |
| `set -x`               | Print each command **before execution**             |
| `set -e`               | Exit script **if any command fails**                |
| `trap '...' ERR`       | Run a custom **error handler** when a command fails |
| `echo "$VAR"`          | Print variable values **for debugging**             |
| `printf "%s\n" "$VAR"` | Print variable values **for debugging**             |
| `bash -x script.sh`    | Run script **with debugging enabled**               |

Using `set -x` and `echo` (or `printf`) are some of the most common methods of
troubleshooting.

### Example Debugging Script

```bash
#!/bin/bash
set -xe  # Enable debugging and exit on failure
mkdir /tmp/mydir
cd /tmp/mydir
rm -rf /tmp/mydir
```

## Next Steps

Now that you understand the fundamentals, here’s what to do next:

- Practice writing scripts:
  - Automate a daily task (e.g., installing a program, creating backups, user management)
- Master error handling:
  - Learn signals and `trap`, and learn about logging techniques.
- Explore advanced topics:
  - Look into writing functions, using arrays, and job control.
- Read `man bash`:
  - The ultimate built-in reference.
  - This resource has everything you need to know about Bash and then some!
- Join ProLUG community:
  - Learn from others, contribute, and improve your Linux skillset.

🚀 **Happy scripting!**

## Downloads
