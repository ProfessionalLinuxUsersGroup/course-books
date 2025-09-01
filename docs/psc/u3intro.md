<div class="flex-container">
        <img src="https://github.com/ProfessionalLinuxUsersGroup/img/blob/main/Assets/Logos/ProLUG_Round_Transparent_LOGO.png?raw=true" width="64" height="64"></img>
    <p>
        <h1>Unit 3 - User Access and System Integration</h1>
    </p>
</div>

## Overview

User access in an larger organizations requires more sophisticated controls. For this purpose Active Directory (AD) and Lightweight Directory Access Protocol (LDAP) have become popular choices as they offer more sophisticated and robust ways of controlling access.
In this chapter, you will learn why AD and LDAP are popular choices.

## Learning Objectives

1. Understand how LDAP or AD works and why it is beneficial.
2. High level understanding of hardening Rocky Linux, a RHEL adjacent distro.
3. Gain a basic understanding of PAM.

## Relevance and Context

In enterprise environments, managing user identities and system access at scale is critical for security, compliance, and operational efficiency. Lightweight Directory Access Protocol (LDAP) and Active Directory (AD) provide centralized authentication, authorization, and account management capabilities that far surpass local account management methods. 

Understanding these systems is foundational for administrators working with Rocky Linux, a Red Hat Enterprise Linux (RHEL) derivative, especially when implementing compliance standards such as DISA STIGs or CIS Benchmarks. Mastering integration points like PAM (Pluggable Authentication Modules) and services like `sssd` allows administrators to ensure secure and scalable authentication across diverse systems.

## Prerequisites

To be successful, students should have a working understanding of skills and tools including:

1. Basic Directory navigation.
2. Knowledge of editing config files.
3. Basic knowledge of StigViewer.
4. Understanding of SystemD services and the SysCTL command.

## Key Terms and Definitions

PAM  

AD  

LDAP  

sssd  

oddjob  

krb5  

realm/realmd  

wheel (system group in RHEL)

