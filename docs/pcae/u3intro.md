# Unit 3

## Making and Using Inventories

## Overview

This unit describes best practices for inventory management. It will clarify details about our inventory sources such as flat files and API calls from other programs. We learn that we cannot do anything properly without a good inventory and are guided on how best to achieve this goal.

We learn that a good inventory is complete, accurate and properly formatted. Inventories must use consistent identifiers of the same type such as IP vs FQDN values. The semi-structured nature of our inventory must be readable and properly formatted for use by our tool of choice (e.g. bash, python, ansible).

## Learning Objectives

1. Inventory Sources

    - Flat files
    - API calls

1. Aspects of a good inventory

    - Accurate
    - Readable
    - Useful

1. Inventories are structured and useful lists of items.

    - With the goal of being 100% complete
     (otherwise the missing 2% will become your focus)
    - Commonly maintained with bash, python & ansible.
     (this course focuses on ansible)
    - Understanding the various types of semi-structured lists
        - flat files
        - CSV files
        - json files
        - yaml files

## Key Terms and Definitions

|Terms|Definitions|||
|:------------------:|:------------------:|:------------------:|:------------------:|
|**Flat files**|Just a list of servers or a basic list of tab/space separated values|||
|**IP address**|Internet Protocol address|[RFC 1918]||
|**FQDN**|Fully Qualified Domain Name|[RFC 1034]|(note: RFC 1035 and many later updates)|
|**CSV**|Comma Separated Values|[RFC 4180]||
|**JSON**|JavaScript Object Notation|[RFC 8259]|(note: language independent)|
|**YAML**|Yet Another Markup Language|[RFC 9512]|(note: language independent)|
