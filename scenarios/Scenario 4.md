Scenario #1

    MODE: Easy

    Steps:

      - Run initialization playbook / role
        - going to reuse the aap from scenario 3
        - set node_selector on db pod
        - set bonkers limits on gateway api pod
        - 

      - Troubleshoot

    Teachings:

      - Learn about Automation Controller's auto_upgrade: false which shouldn't be used
        in production.

      - Learn about troubleshooting the resource_requirements