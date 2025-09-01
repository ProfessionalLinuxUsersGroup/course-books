<div class="flex-container">
        <img src="https://github.com/ProfessionalLinuxUsersGroup/img/blob/main/Assets/Logos/ProLUG_Round_Transparent_LOGO.png?raw=true" width="64" height="64"></img>
    <p>
        <h1>Unit 2 - Securing the Network Connection</h1>
    </p>
</div>

## Overview

Understanding and implementing network standards and compliance measures can make security controls of critical importance very effective.

This unit introduces foundational knowledge on analyzing, configuring, and hardening networking components using tools and frameworks like STIGs, OpenSCAP, and DNS configurations.

## Learning Objectives

By the end of Unit 2 students will have foundational knowledge and skills of
the concepts below:

1. Identifying and analyzing STIGs related to Linux networking.
2. Understand and configure secure name resolution using nsswitch.conf and DNS.
3. Utilizing tools like tcpdump, ngrep, ss, and netstat to monitor network behavior.
4. Applying OpenSCAP and SCC tools for network compliance assessments.
5. Exploring known network-based exploits and understanding their anatomy via the Diamond Model of Intrusion Analysis.

## Relevance and Context

Networks represent one of the most common attack vectors in enterprise systems. Misconfigured name
resolution, open ports, and insecure protocols are all doorways to intrusion. As system engineers,
building resilient systems requires a deep understanding of how data flows through these pathways
and what tools can monitor and secure them.

By learning to assess and remediate network-related STIGs and implementing structured standards,
students will gain the skills to reduce ingress risk and respond effectively to threats. These skills
are not only crucial for compliance but also for real-world defense.

## Prerequisites

To be successful, students should have a working understanding of skills and tools including:

1. The Command Line Interface and BASH shell skills
2. Installing and Updating Linux System Packages
3. Network concepts including TCP/IP, DNS, and more
4. Interacting with command line tools such as: `sysctl`, `firewalld`, `grep`, and `oscap`
5. Ability to edit files with `vim`
6. Students will need to download the latest STIG viewer, v2.18

## Key Terms and Definitions

sysctl  
nsswitch.conf  
DNS  
Openscap  
CIS Benchmarks  
ss/netstat  
tcpdump  
ngrep
