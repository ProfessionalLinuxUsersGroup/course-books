<div class="flex-container">
        <img src="https://github.com/ProfessionalLinuxUsersGroup/img/blob/main/Assets/Logos/ProLUG_Round_Transparent_LOGO.png?raw=true" width="64" height="64"></img>
    <p>
        <h1>Repos & Patching</h1>
    </p>
</div>

## Overview

Where software originates—and how and when it is updated (patched)—is essential to maintaining system stability and security. Every patch applied to a system must come from a known and trusted source, as introducing changes into a stable environment can have significant consequences. Administrators and engineers ensure that patching is planned and scheduled using verified, trackable repositories and resources.

In this unit, we will examine how this process is implemented in adjacent distributions, where administrators can apply granular control to Red Hat Package Manager (RPM) packages and maintain internal repositories of vetted packages.

## Learning Objectives

1. Understand the importance of package integrity.
2. Understand patching techniques and routines.
3. Understanding automated methods of patching.
4. Understanding custom internal package repositories.

## Relevance and Context

For security engineers, controlling the origin and integrity of software updates is a foundational practice for minimizing attack surfaces. By managing internal repositories and applying strict control over RPM packages, organizations can enforce compliance, prevent supply chain attacks, and ensure only trusted, audited software enters production environments.

## Prerequisites

To be successful, students should have a working understanding of skills and tools including:

1. Basic directory navigation skills.
2. Ability to edit and manage configuration files.
3. Basic knowledge of STIG.
4. Basic knowledge of Ansible.

## Key Terms and Definitions

Patching

Repos

Software

- EPEL
- BaseOS v. Appstream (in RHEL/Rocky)
- Other types you can find?

httpd

patching

GPG Key

DNF/YUM
