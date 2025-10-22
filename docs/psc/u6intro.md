# Unit 6 - Monitoring and Parsing Logs

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

## Key terms and Definitions

|**Types of Logs**|**Application Logs**|
|:------------------:|:------------------:|
|**Host Logs**|**Network Logs**|
|**Database Logs**|**Log Structure**|
|**RFC 3164 BSD Syslog**|**RFC 5424 IETF Syslog**|
|**Systemd Journal**|**Log Rotation**|
|**Log Aggregation**|**ELK Stack**|
|**Splunk**|**Loki**|
|**Graylog**|**SIEM (Security Information and Event Management)**|
