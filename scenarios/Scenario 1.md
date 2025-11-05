Scenario #1

    MODE: Easy

    Steps:

      - Run initialization playbook / role

        - Deploy Automation Controller successfully but with auto_upgrade: false and
          no_log: true

      - Run playbook to mess things up
        - Adds ResourceQuota and LimitRange to namespace (these cannot be removed) so that
          OCP will start to OOM kill the database
        - Deletes the database postgres service for Automation Controller
        - Restarts the web/task pods

      - Troubleshoot

    Teachings:

      - Learn how Automation Controller connects to the database pod

      - Learn how to enable logging within Automation Controller operator
        (same principles will apply to the other operators)

      - Learn about Automation Controller's auto_upgrade: false which shouldn't be used
        in production.

      - Learn about troubleshooting the resource_requirements