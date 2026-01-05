# Unit 6

## Automating Docker Builds

## Overview

This unit introduces containerization and the tools used to build, deploy, and manage containers in an automated fashion. We learn the principles of release engineering and how they apply to infrastructure automation. Learners will understand the relationship between container image creation, container orchestration, and infrastructure-as-code tools. The core challenge we address is this: infrastructure engineering teams frequently struggle with reliably recreating identical environments and doing so in a timely manner. Through automation, we solve this problem using tools like Docker, Packer, Terraform, and Apptainer.

This unit continues to address the course objective to deploy various automation tools for engineering and operations activities. Specifically, this unit focuses on how we can reliably and repeatably build container images and deploy containerized environments across infrastructure at scale. We apply Google SRE (Site Reliability Engineering) principles to ensure consistency, reliability, and automation in our release pipelines. By the end of this unit, you will understand how to codify infrastructure requirements, automate environment creation, implement version control for infrastructure, and enable repeatable deployments.

## Learning Objectives

1. Container fundamentals and use cases

    - Docker images and container runtime environments
    - Container images as versioned artifacts using semantic versioning
    - The relationship between containers and infrastructure automation
    - Why containers matter for repeatable deployments and use cases (BYOE, reproducible science, static environments, legacy code, custom software)
    - Understand isolated execution environments with all required dependencies

1. Release Engineering Principles

    - Understanding release engineering as the discipline of building and managing software releases in a controlled, reproducible manner
    - Code base management, code changes, and version control strategies
    - Build configuration and the build process (building, branching, and testing)
    - How release engineering principles apply directly to infrastructure automation

1. Container image building tools and decision-making

    - Packer: Building Docker images, VM images, and cloud machine images in an automated fashion
    - Apptainer (formerly Singularity): Lightweight container runtime for HPC and scientific computing
    - When and why to use each tool based on use cases (general-purpose vs. HPC/scientific workloads)
    - Comparison framework for evaluating container technologies

1. Infrastructure-as-Code integration and CI/CD pipelines

    - Using Terraform to deploy container infrastructure
    - Terraform providers and their role in managing platforms and services
    - CI/CD pipelines and build triggers: GitHub Actions, manual triggers, and event-driven systems (Kafka, Event Bridge, Opensearch, Splunk)
    - Testing container images for function and security
    - Integration with version control and automation workflows
    - Tagging and versioning artifacts for deployment readiness

1. Release strategies and deployment patterns

    - Release engineering practices for containers (consistency, reliability, automation)
    - Canary deployments and safe rollout patterns
    - Maintaining consistency across environments
    - Implementing reliable and repeatable releases at scale

## Key Terms and Definitions

|Terms|Definitions|
|:------------------:|:------------------:|
|**Docker**|Container platform for building, shipping, and running applications|
|**Container Image**|A lightweight, standalone, executable package containing code and dependencies|
|**Packer**|Tool for creating machine images and container images in an automated fashion|
|**Apptainer**|Container platform designed for HPC and scientific computing workloads|
|**Terraform**|Infrastructure-as-Code tool for provisioning and managing infrastructure|
|**Release Engineering**|Discipline focused on building and deploying software reliably and repeatedly|
|**Release**|A versioned software package ready for deployment and distribution|
|**Code base**|The complete source code for a project or application|
|**Build Configuration**|Rules and instructions defining how code is compiled, packaged, and tested|
|**CI/CD**|Continuous Integration / Continuous Deployment automated build and deployment pipelines|
|**GitHub Actions**|CI/CD automation platform for triggering builds on code changes and automating workflows|
|**Provisioning**|Configuring and setting up systems and infrastructure, including provisioning containers during builds|
|**Canary Deployment**|Deployment strategy that rolls out changes to a small subset before full release|
|**Container Artifact**|A versioned, immutable container image ready for deployment and distribution|
|**Semantic Versioning**|Versioning scheme (Major.Minor.Patch) for tracking container image changes and compatibility|
|**Build Trigger**|Event or action that initiates an automated container image build (GitHub Actions, manual, event-driven systems like Kafka)|
|**Event-Driven Architecture**|Systems triggered by events from external sources (Kafka, Event Bridge, Opensearch, Splunk) rather than on-demand|
|**Image Testing**|Validation of container images for functional correctness and security vulnerabilities before deployment|
