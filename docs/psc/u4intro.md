# Bastion Hosts & Air-Gaps

## Overview

Bastions and airgaps are strategies for controlling how systems connect—or don't connect—to the outside world. They focus on limiting exposure, creating strong boundaries that support a broader security design.
In this unit, we look at how we can seperate systems and create safe disconnects should a problem arise.

## Learning Objectives

1. Understand the role and importance of air-gapped systems.
2. Recognize how to balance strong security with operational efficiency.
3. Learn how bastion hosts can help control and limit system access.
4. Understand methods for automating the jailing and restriction of users.
5. Gain a foundational understanding of `chroot` environments and diversion techniques.

## Key Terms and Definitions

|**Air-gapped**|**Bastion**|
|:------------------:|:------------------:|
|**Jailed process**|**Isolation**|
|**Ingress**|**Egress**|
|**Exfiltration**|**Cgroups**|
|**Namespaces**<br>- Mount, PID, IPC, UTS|
