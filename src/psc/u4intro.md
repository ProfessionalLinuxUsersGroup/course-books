<div class="flex-container">
        <img src="https://github.com/ProfessionalLinuxUsersGroup/img/blob/main/Assets/Logos/ProLUG_Round_Transparent_LOGO.png?raw=true" width="64" height="64"></img>
    <p>
        <h1>Bastion Hosts & Air-Gaps</h1>
    </p>
</div>

## Overview

Bastions and airgaps are strategies for controlling how systems connect—or don't connect—to the outside world. They focus on limiting exposure, creating strong boundaries that support a broader security design.
In this unit, we look at how we can seperate systems and create safe disconnects should a problem arise.

## Learning Objectives

1. Understand the role and importance of air-gapped systems.
2. Recognize how to balance strong security with operational efficiency.
3. Learn how bastion hosts can help control and limit system access.
4. Understand methods for automating the jailing and restriction of users.
5. Gain a foundational understanding of `chroot` environments and diversion techniques.

## Relevance and Context

As organizations grow, protecting critical systems becomes more challenging. Air-gapped systems and bastion hosts offer proven ways to limit exposure and manage access securely. Understanding these concepts is essential for building strong security foundations without creating unnecessary barriers to operations.

## Prerequisites

To be successful, students should have a working understanding of skills and tools including:

1. Basic directory navigation skills.
2. Ability to edit and manage configuration files.
3. Understanding of SystemD services and the use of the `sysctl` command.
4. Basic knowledge of Bash scripting.

## Key Terms and Definitions

Air-gapped

Bastion

Jailed process

Isolation

Ingress

Egress

Exfiltration

Cgroups

Namespaces

- Mount
- PID
- IPC
- UTS