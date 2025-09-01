<div class="flex-container">
        <img src="https://github.com/ProfessionalLinuxUsersGroup/img/blob/main/Assets/Logos/ProLUG_Round_Transparent_LOGO.png?raw=true" width="64" height="64"></img>
    <p>
        <h1>Unit 7 Bonus - Package Management & Patching</h1>
    </p>
</div>

> **NOTE:** This is an **optional** bonus section. You **do not** need to read it, but if you're interested in digging deeper, this is for you.

This bonus explores how you can audit and verify software integrity on your system
using package tools, hashes, and file validation -- going deeper into real-world
sysadmin practice.

This is more of a bonus lab. We're going beyond just _installing_ packages.
We're going to audit, validate, and verify that the software on our system is
trustworthy and unmodified.  
We'll explore how to detect unexpected changes using built-in tools, dig into package
metadata, and get a taste of real-world security practices like intrusion detection
and system baselining through package auditing.

In modern enterprise environments, packages may be tampered with, misconfigured, or out-of-date.

A responsible sysadmin needs tools and methods to answer questions like:

- Was this package installed from a trusted source?
- Have any of the installed files been modified?
- Which files belong to which packages?
- Can I detect and recover from unexpected changes?

Let's get into it.

## Verifying Package Integrity

---

Start by finding a package you know is installed and used in your environment -- for example, `sshd`:

```bash
rpm -qi openssh-server
```

Now, check the integrity of the package's files:

```bash
rpm -V openssh-server
```

- `-V`: Stands for **verify**.
  - This option checks timestamps, permissions, ownership, and hashes of installed files.

If you don't see any output, that's a good thing.

`rpm -V` only reports files that have been altered in some way from what the package database expects.
If there is no output, it means all files match the expected checksums, sizes, permissions, etc..

If this command **does** have output, being able to interpret the output is important.
Each character in the output has its own meaning:

- `S` - Size differs.
- `M` - Mode differs (permissions).
- `5` - MD5 checksum mismatch.
- `T` - Modification time differs.

This is a great way to verify the integrity of installed packages.
It's also helpful in troubleshooting when a package isn't working as expected.


## Auditing a File in a Package

---

Let's say you suspect something has been changed or tampered with.
Let's get all files from a package.  

- Run `rpm -ql` to list the files that were installed with a package:

  ```bash
  rpm -ql openssh-server
  ```

- Now pick one file and manually generate its sha256 hash:

  ```bash
  sha256sum /usr/sbin/sshd
  ```

- Download the original `.rpm` package to compare its hash.

  ```bash
  dnf download openssh-server
  ```

  - This will download the `openssh-server-<version>.rpm` package in the current directory.
  - These `.rpm` packages are not stored on the system by default.

- You can inspect the file of your choice with `rpm -qp --dump`:

  ```bash
  rpm -qp --dump openssh-server*.rpm | grep ^/usr/sbin/sshd
  ```

  This will output a bunch of information about the file.  
  The `sha256` hash will be in the fourth column, so we can use `awk` to extract that:

  ```bash
  rpm -qp --dump openssh-server*.rpm | grep ^/usr/sbin/sshd | awk '{print $4}'
  ```

- Compare your version's hash to the original RPM file's hash:

  ```bash
  sha256sum /usr/sbin/sshd
  ```

If the hashes are different, the file has been modified.

## Bonus Challenge 💡

---

1. Run this one-liner to verify all installed packages:
   ```bash
   rpm -Va
   ```
   - This will verify every file from every package and report anything suspicious.
1. Narrow the scope. Only show actual modified files:

   ```bash
   rpm -Va | grep -v '^..5'
   ```

   - This removes lines where only the MD5 checksum differs (which could be expected in some config files).
   - You’ll now see files where size, mode, owner, or timestamp changed — higher confidence indicators of real change.

1. Investigate a suspicious result. If you see something like:

   ```bash
   .M....... c /etc/ssh/sshd_config
   ```

   That means:

   - The permissions (`M`) have changed.
   - It's a config file (`c`).

1. Check the file in question:

   ```bash
   ls -l /etc/ssh/sshd_config
   ```

1. Compare that to what you expected:
   ```bash
   rpm -q --qf '%{NAME} %{VERSION}-%{RELEASE}\n' -f /etc/ssh/sshd_config
   ```

Then you can reinstall the package or extract the original file from the `.rpm` file.

### Reflection Questions

---

- What happens if you manually modify a file, then verify with `rpm -V`?
- Can you identify if changes were made outside of DNF/RPM?
- What types of files are typically most important to verify?


### Example of Real-World Security Tools

---

Large enterprises often use tools like AIDE (Advanced Intrusion Detection Environment) or Tripwire to baseline their systems and detect changes over time.

AIDE can be installed easily with `dnf`, so you can play around with it if you want.
To set up AIDE on your system (as root):

```bash
dnf install aide -y

aide --init

# Copy the default database to use as your database
cp /var/lib/aide/aide.db.new.gz /var/lib/aide/aide.db.gz

# Then, to run a check with aide (this will take a few minutes):
aide --check
```

AIDE compares the current state of the system to a known baseline.

This is foundational to change management, compliance, and intrusion detection.

## Resources

---

- [RPM Man Page](https://man7.org/linux/man-pages/man8/rpm.8.html)
- [AIDE Documentation](https://aide.github.io/)
- [Verifying RPM Packages](https://access.redhat.com/solutions/14303)
- [Using sha256sum](https://man7.org/linux/man-pages/man1/sha256sum.1.html)
 
## Downloads
