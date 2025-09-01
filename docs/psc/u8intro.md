<div class="flex-container">
        <img src="https://github.com/ProfessionalLinuxUsersGroup/img/blob/main/Assets/Logos/ProLUG_Round_Transparent_LOGO.png?raw=true" width="64" height="64"></img>
    <p>
        <h1>Unit 8 - Configuration Drift and Remediation</h1>
    </p>
</div>

## Overview

Configuration drift is the silent enemy of consistent, secure infrastructure.  
When systems slowly deviate from their intended state, whether that be through manual 
changes, failed updates, or misconfigured automation, security risks increase and 
reliability suffers.

In this unit, we focus on identifying, preventing, and correcting configuration drift.  
Students will explore concepts like Infrastructure as Code (IaC), immutable 
infrastructure, and centralized configuration management.  
We will also look at how drift can be detected through tools like AIDE and remediated 
through automation platforms like Ansible.

Students will not only understand why drift happens, but also learn how to build
resilient systems that can identify and self-correct unauthorized changes.

## Learning Objectives

1. Define configuration drift and understand its impact on security and operations.
2. Explore change management frameworks, including CMDBs and baselines.
3. Implement detection tools like AIDE to monitor file system integrity.
4. Use Ansible to remediate drift and enforce configuration state.
5. Connect drift management to compliance, auditability, and incident response.

## Relevance & Context

Configuration drift undermines both security and operational goals.  
Whether through silent config changes or forgotten test artifacts, drift introduces 
uncertainty and risk.  
In enterprise environments, undocumented changes can void audits, invalidate incident 
investigations, or introduce vulnerabilities unnoticed.

Security engineers must treat configuration as code and enforce strong change control
policies. By learning to detect, document, and automatically remediate drift, 
students will be equipped to reduce their organization's attack surface and ensure 
long-term consistency.

This unit ties together principles of monitoring, logging, and automation into a 
unified practice: configuration control.

## Prerequisites

To succeed in this unit, students should be comfortable with:

1. Basic command line navigation and editing skills (`vi`, `cat`, `grep`)
2. Experience using Ansible or YAML-based automation (basic playbook structure)
3. Familiarity with STIGs and the use of the STIG Viewer

## Key terms and Definitions

Configuration Drift  

System Lifecycle  

Change Management  
- CMDB (Configuration Management Database)  
- CI (Configuration Item)  
- Baseline  

Build Book / Run Book  

Immutable Infrastructure  

Hashing  
- `md5sum`, `sha256sum`, etc.  

IaC (Infrastructure as Code)  

Orchestration  

Automation  

AIDE (Advanced Intrusion Detection Environment)  

