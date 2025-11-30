# Unit 4
## Admin Commands and One-Offs

## Overview

This unit explains what are administration and one-off/ad-hoc commands.  We will learn what triggers automation administration commands.  We also clarify how we get into a state where we need to interact with our systems. Once we are in this state we will learn how to interact with our automation using one-off commands.


### What is the skill/tech/concept we are dealing with?

This unit continues to address the course objective to deploy various automation tools for engineering and operations activities.   Our main responsibility on the job is to perform admin and engineering tasks but we ultimately want to use automation to properly fullfil our roles.  A second course objective being addressed is to maintain system configuration and remediating drift via automation.  Remediation of drift is essentially keeping the computing environment in-line with user expectations.



## Learning Objectives

1. What types of admin commands will we use : Commands that change existing and running systems with the goal of keeping systems at 99.999% uptime.

    -  Observe - Check a system and note exactly how it is configured.   Later, ensure nothing has changed, since the last check.
    - Benchmark - Perform a load lest to check the how the system behaves / handles itself.
    - Tune - Change the system configuration then restart the related services for the changes to take effect.

2. What triggers our need to perform admin commands

    - A system event occurs  
        - the server stops responding
        - a log event triggers an alert
        - an event is triggered from an SIEM configured system (e.g. Kafka, SQS, Splunk)
    - A user request is received
        - give access / change permissions
        - fix / configure the environment (as a one-off instead of redeploying)
    - A security event occurs
        - Security findings from an GRC/ISO trigger patching
        - Security incidents requiring fixes to protect CIA
    
3. PPDIOO Deployment methodology

    - focus on Optimize & Operate stages 



## Key Terms and Definitions

SIEM        Security Information and Event Monitoring
PPDIOO      Prepare, Plan, Design, Implement, Operate, Optimize 
KTLO        Keeping the lights on  
GRC         Governance, Risk, and Compliance teams
ISO         Information Security Officer
CIA         Confidentiality, Integrity, and Availability
