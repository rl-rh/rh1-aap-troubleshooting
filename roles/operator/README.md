# Introduction

I created this operator role to help simplify the installation / possible deletion of the AAP operator between each step. The role-specific variables that can be specified at the playbook-level can be found in the `defaults/main.yml` file.

# Usage

- Install the latest version of the AAP 2.6 operator

  ```
  - name: Install Ansible Automation Platform operator
    hosts: all
    gather_facts: false

    tasks:
        - name: Install Ansible Automation Platform operator
        vars:
            install_channel: "stable-2.6"
        ansible.builtin.import_role:
            name: operator
  ```

- Install the earlier version of the AAP 2.5 operator

  ```
  - name: Install Ansible Automation Platform operator
    hosts: all
    gather_facts: false

    tasks:
        - name: Install Ansible Automation Platform operator
        vars:
            install_channel: "stable-2.5"
            install_starting_csv: "aap-operator.v2.5.0-0.1727240614"
            install_plan_approval: "Manual"
        ansible.builtin.import_role:
            name: operator
  ```