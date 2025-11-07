Scenario #1

    MODE: Easy

    Steps:

      - Run initialization playbook / role

      - Run playbook to mess things up
        - Adjusts the postgresql resource requirements to cause OOMkill
        - Sets auto_upgrade: false

      - Troubleshoot

    Teachings:

      - Learn about Automation Controller's auto_upgrade: false which shouldn't be used
        in production.

      - Learn about troubleshooting the resource_requirements