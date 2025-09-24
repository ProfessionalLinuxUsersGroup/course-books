  
# ProLUG Linux Automation
# Lab Guide  

## Acceptable Use Policy

The acceptable use policy is presented during login through the Bastion node:  

!!! “You are entering the ProLUG lab environment. All activities may be monitored. By entering you agree to use the lab for the stated purpose of learning Linux.”

Violations of this Acceptable Use Policy (AUP) or deliberate misuse of lab resources will result in immediate termination of access privileges and removal from ProLUG.

## Access to Lab Enviornments

> Insert link to picture

Prolug Automation server mapping to target nodes.
Auto1 -> user: svc_ansible, password: ansible1234 -> target nodes: target1-1, target1-2
Auto2 -> user: svc_ansible, password: ansible1234 -> target nodes: target2-1, target2-2
Auto3 -> user: svc_ansible, password: ansible1234 -> target nodes: target3-1, target3-2
Auto4 -> user: svc_ansible, password: ansible1234 -> target nodes: target4-1, target4-2
Auto5 -> user: svc_ansible, password: ansible1234 -> target nodes: target5-1, target5-2

For additional lab capacity use Killercoda.com. That lab mapping is as follows:
Controlplane -> user: root, key -> target node: node01

## Public Keys

Public keys are dropped in the prolug_lab_environment channel where they can be added to the jump
server for bastion access.
Note: The password method is unreliable as it changes often.

## Lab Best Practices

Reboot servers when you are done with them. This will ensure a clean server for the next user to log in.
