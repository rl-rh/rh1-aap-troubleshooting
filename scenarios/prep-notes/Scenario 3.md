Scenario #3

    MODE: Easy

    Components: AAP Gateway UI

    Namespace: aap-rh1

    Objectives: 
      * Find out why Gateway pods are failing
      * Log in to AAP UI to verify things are working again

    Steps:
      ansible-playbook site.yml -t deploy (select scenario 3)
      ansible-playbook site.yml -t break (select scenario 3)
      Once you find the first issue (you don't need to know exactly how to fix it), run the ansible-playbook site.yml -t fix (select scenario 3) to fix the first issue
      Once you find the second issue (you don't need to know exactly how to fix it), run the ansible-playbook site.yml -t fix (select scenario 3) to fix the second issue

    Hints:
      Does the database have connection to the Gateway API pod?
      What OpenShift resource is needed for one pod to talk to another?
      Having issues logging in? Take a look at the Gateway API pod logs


Scenario #3

    MODE: Easy

    Steps:

      - Run initialization playbook / role
        - sets up full aap deployments

      - Run playbook to mess things up
        - gateway password changed
        - delete database service

      - Troubleshoot

    Teachings:

      - Learn about aap-gateway manage commands

      - Learn about gateway services and reviewing gateway logs