<div class="flex-container">
        <img src="https://github.com/ProfessionalLinuxUsersGroup/img/blob/main/Assets/Logos/ProLUG_Round_Transparent_LOGO.png?raw=true" width="64" height="64"></img>
    <p>
        <h1>Unit 6 - Monitoring and Parsing Logs</h1>
    </p>
</div>

## Overview

Monitoring and parsing logs is one of the most essential security engineering
practices in any production environment.

This unit explores how logs are generated, formatted, collected, and analyzed across
various layers of the infrastructure stack, from applications to operating systems
to networks.

Students will gain an operational understanding of how to identify log sources, use
modern tools for log aggregation and search (such as Loki), and develop awareness of
log structure, integrity, and retention requirements.

## Learning Objectives

By the end of Unit 6, students will:

1. Understand the different types of logs and their role in system and security monitoring.
2. Identify log structures (e.g., RFC 3164, RFC 5424, `journald`) and apply
   appropriate parsing techniques.
3. Explore and configure log aggregation pipelines using modern tools like Grafana Loki.
4. Analyze real-world security events using log data and query languages.
5. Learn how log immutability and integrity contribute to reliable forensics and compliance.

## Relevance & Context

Logs are often the first and best source of truth when diagnosing an incident,
auditing a system, or responding to a breach.  
Without well-structured, searchable, and preserved logs, response teams are blind to
what actually happened.

This unit trains students to think like operators and defenders -- ensuring logs are
complete, available, immutable, and actionable.

It builds directly on previous units around compliance and auditing, preparing
learners to create scalable observability strategies that support both security and
performance goals.

## Prerequisites

Before beginning Unit 6, students should:

1. Be comfortable working at the command line using `journalctl`, `grep`, `less`, and
   related tools.
2. Understand system service management with `systemctl`.
3. Have basic familiarity with syslog, log rotation, and the concept of standard
   input/output streams.
4. Be able to interact with YAML and JSON-formatted configuration files.
5. Have installed or downloaded STIG Viewer 2.18 for compliance reference.

## Key terms and Definitions

Types of Logs
- Application Logs  
- Host Logs  
- Network Logs  
- Database Logs

Log Structure

- RFC 3164 BSD Syslog
- RFC 5424 IETF Syslog
- Systemd Journal

Log Rotation

Log Aggregation

- ELK Stack
- Splunk
- Loki
- Graylog

SIEM (Security Information and Event Management)
