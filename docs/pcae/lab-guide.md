# ProLUG Linux Automation
## Lab Guide

Students will be granted access to the ProLUG lab environment upon request.  
If you would like access, join us on Discord and ask in the
`#prolug_lab_environment` channel.  

Outlined below is the Acceptable Use Policy and layout of the lab used for the
Linux Automation Course.  


## Acceptable Use Policy

The acceptable use policy is presented during login through the Bastion node:

"You are entering the ProLUG lab environment. All activities may be monitored.
By entering you agree to use the lab for the stated purpose of learning Linux."

!!! warning

    Willful violations of this AUP, or intentional destruction will result in removal from ProLUG.

## Access to Lab

<img src="../../assets/pcae/images/lab-guide-bastion-process.png" />

Auto server mapping to target nodes is as follows.
```plaintext
Auto1 -> user: svc_ansible, password: ansible1234 -> target nodes: target1-1, target1-2
Auto2 -> user: svc_ansible, password: ansible1234 -> target nodes: target2-1, target2-2
Auto3 -> user: svc_ansible, password: ansible1234 -> target nodes: target3-1, target3-2
Auto4 -> user: svc_ansible, password: ansible1234 -> target nodes: target4-1, target4-2
Auto5 -> user: svc_ansible, password: ansible1234 -> target nodes: target5-1, target5-2
```

For additional lab capacity, use [Killercoda.com](https://killercoda.com).  

That lab mapping is as follows:
```plaintext
Controlplane -> user: root, key -> target node: node01
```

## Public Keys

Public keys are dropped in the `#prolug_lab_environment` channel in Discord, 
where they can be added to the jump server for bastion access.

!!! note

    The password method is unreliable, as it changes often.

## Lab Best Practices

Reboot servers when you are done with them.  
This will ensure a clean server for the next user to log in.
