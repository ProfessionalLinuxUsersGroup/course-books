<div class="flex-container">
    <img src="https://github.com/ProfessionalLinuxUsersGroup/img/blob/main/Assets/Logos/ProLUG_Round_Transparent_LOGO.png?raw=true" width="64" height="64"></img>
    <p>
        <h1>Unit 13 - System Hardening</h1>
    </p>
</div>

## Overview

---

In this unit, we focus on **system hardening** — the process of configuring Linux systems to meet defined security standards. As threats evolve, system administrators play a key role in ensuring confidentiality, integrity, and availability by reducing attack surfaces and enforcing secure configurations.

We will explore industry benchmarks like **STIGs and CIS**, implement hardening techniques for services like SSH, identify unneeded software, and analyze system security posture using tools like the **SCC Tool**. You’ll also revisit baselining and documentation as part of security validation and compliance.

## Learning Objectives

---

**By the end of this unit, you will be able to**:

- Define system hardening and understand its role in securing Linux servers
- Scan systems using the **SCC Tool** to assess security compliance
- Apply remediation steps based on **STIG** reports
- Harden services such as **SSHD**, remove unnecessary software, and lock down ports
- Rescan and verify improvements in your system’s security posture
- Understand the importance of documentation and change management in security

## Relevance & Context

---

Security hardening helps ensure that systems are not only functional but also resilient against misuse and attacks. Whether aligning with **PCI DSS, CIS benchmarks, or STIGs**, hardening turns general-purpose Linux installs into mission-ready infrastructure.

This unit emphasizes **security vs. accessibility**, change management, and shared responsibility between security and operations. You’ll experience real-world practices like scanning, remediating, and verifying — essential skills for any administrator tasked with system security.

## Prerequisites

---

**Before starting Unit 13, you should have**:

- A solid understanding of **Linux system administration and services**
- Comfort using the terminal and managing services with `systemctl`
- Ability to inspect ports, services, and installed software
- Familiarity with tools like `ss`, `rpm`, `dnf`, and `ssh`
- Access to a **Rocky Linux system with root/sudo privileges**
- **_(Optional but recommended)_**: Experience from Unit 12 on baselining and benchmarking

## Key Terms and Definitions

---

**Hardening**

**Pipeline**

**Change Management**

**Security Standard**

**Security Posture**

**Acceptable Risk**

- **NIST 800-53**

**STIG**

**CIS Benchmark**

**OpenSCAP**

**SCC Tool**

**HIDS**

**HIPS**
