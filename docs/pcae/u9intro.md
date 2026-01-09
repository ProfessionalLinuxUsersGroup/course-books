# Unit 9

## Build and Deploy Linux Systems

## Overview

You've reached an inflection point in the ProLUG Linux Automation Engineering Course. The units up to this point have prepared you to automate individual components: containers, orchestration platforms, configuration files, and infrastructure resources. This unit brings these concepts together to address one of the most critical challenges in enterprise infrastructure: **building and deploying complete Linux systems at scale with consistency, repeatability, and security**. This unit introduces bare-metal provisioning, immutable infrastructure patterns, and the tools that enable organizations to manage hundreds or thousands of Linux systems from centralized, version-controlled configurations.

The core problem this unit solves is configuration drift and inconsistent environments. When systems are managed manually or through ad-hoc scripts, they diverge over time - package versions differ, configuration files are modified, services are started or stopped inconsistently. These differences create reliability problems, security vulnerabilities, and operational complexity. This unit teaches you how to eliminate drift by treating system images as immutable artifacts, applying infrastructure-as-code principles to entire operating systems, and deploying nodes that are identical, ephemeral, and disposable. These practices align directly with NIST Special Publication 800-223 guidance on High-Performance Computing security and the immutable infrastructure principles championed by Google SRE.

By the end of this unit, you will understand how to use Warewulf for bare-metal provisioning, Apptainer for containerized OS images, and Ansible for automated system configuration within chroot environments. You'll be able to build reproducible Linux system images, deploy them across physical or virtual infrastructure, and implement immutable deployment patterns that enable rapid rollback, consistent security posture, and operational confidence at scale. This is infrastructure automation applied to the operating system itself - the foundation that everything else depends on.

## Learning Objectives

1. **Understand Bare-Metal Provisioning and Diskless Boot Architecture**

    - Comprehend how PXE (Preboot Execution Environment) and iPXE enable network-based operating system delivery
    - Understand the Warewulf provisioning framework architecture: image repository, provisioning server, overlay system, and boot process
    - Recognize when diskless booting is appropriate (HPC clusters, ephemeral compute nodes, high-security environments)
    - Implement network boot infrastructure for delivering OS images to bare metal servers

2. **Build and Manage Containerized Linux System Images**

    - Use Apptainer to create lightweight, single-file container images optimized for system deployment
    - Import OS images from container registries (Docker Hub, GitHub Container Registry) using Warewulf
    - Extract and prepare container filesystems as root OS images for deployment
    - Understand the differences between Docker (application containers) and Apptainer (system containers)
    - Manage image versioning and distribution for large-scale deployments
    - Locate and inspect Warewulf image storage locations for troubleshooting and customization

3. **Automate System Configuration Using Ansible and Chroot Environments**

    - Configure Ansible to interact with chroot environments using the `chroot` connection plugin
    - Write idempotent Ansible playbooks for package installation, service configuration, and system state management
    - Test and validate system configurations locally before deploying to production nodes
    - Implement repeatable, version-controlled system customization workflows
    - Troubleshoot Ansible execution within chroot environments (DNS resolution, package repositories, network access)

4. **Implement Immutable Infrastructure Patterns**

    - Treat deployed nodes as ephemeral resources that are rebuilt rather than patched
    - Separate base OS images from environment-specific overlays (system overlays and runtime overlays)
    - Implement the "build new, deploy, destroy old" pattern for system updates
    - Understand Warewulf terminology: image repository, system overlays, runtime overlays, and wwctl command language
    - Design deployment architectures where configuration changes trigger new image builds
    - Maintain image versioning and rollback capabilities for rapid recovery

## Key Terms and Definitions

|Term|Definition|
|:------------------:|:------------------:|
|**Warewulf**|Open-source bare-metal provisioning and lifecycle management framework for HPC and enterprise Linux systems; delivers operating system images via network boot and manages node configuration through overlays|
|**Apptainer**|Lightweight container format (formerly Singularity) optimized for scientific computing and system deployment; provides single-file, immutable containers without requiring daemon processes|
|**PXE Boot (Preboot Execution Environment)**|Industry-standard network booting protocol (Intel specification) enabling systems to boot operating systems from network-delivered images rather than local disks; foundation for diskless computing|
|**iPXE**|Enhanced open-source PXE implementation supporting HTTP/HTTPS boot sources, scripting capabilities, and advanced network protocols; extends standard PXE functionality|
|**Chroot (Change Root)**|Unix/Linux operation that changes the apparent root directory for a process and its children, creating an isolated filesystem namespace; enables system configuration testing without deployment|
|**Ansible Chroot Connection**|Ansible connection plugin (`ansible_connection=chroot`) enabling playbook execution within chroot environments; allows configuration management of system images before deployment|
|**System Overlay**|Warewulf concept for persistent modifications applied to base OS images; includes configuration files, packages, and customizations shared across node groups|
|**Runtime Overlay**|Warewulf concept for ephemeral, node-specific configurations applied at boot time; enables per-node customization while maintaining shared base images|
|**Immutable Infrastructure**|Infrastructure paradigm where deployed systems are never modified in place; updates require building new images and redeploying nodes, enabling consistent state and rapid rollback|
|**Diskless Booting**|Architecture where compute nodes run operating systems entirely from RAM without local disk storage; OS image delivered via network, enabling stateless, disposable nodes|
|**wwctl**|Warewulf control utility providing command-line interface for image management, node provisioning, overlay configuration, and cluster administration|
|**Configuration Drift**|Gradual divergence of system configurations from their intended state due to manual changes, ad-hoc patches, and inconsistent deployments; eliminated by immutable infrastructure|
|**Bare-Metal Provisioning**|Process of installing and configuring operating systems directly on physical hardware without virtualization; requires network boot infrastructure and automated deployment tools|
|**Idempotent Automation**|Automation that produces identical results regardless of how many times it executes; critical for reliable system deployment where playbooks must safely rerun without unintended side effects|
