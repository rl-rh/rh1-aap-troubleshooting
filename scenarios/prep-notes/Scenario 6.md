Scenario #6

    MODE: Easy

    Components: Automation Controller

    Namespace: aap-rh1    

    Objectives: 
      * Log into gateway UI
      * Browse to Automation Execution (Automation Controller) -> Job Templates
      * Launch the four job templates
      * fix the issue(s)

    Steps:
      ansible-playbook site.yml -t deploy (select scenario 6)
      ansible-playbook site.yml -t break (select scenario 6)

    Hints:
      Review automation-job pod logs

Answer section:
The Job Template references an Execution Environment in a private quay repo which has no matching credential in it. Switch the EE to match the other Job Templates

Scenario #6

    MODE: Easy

    Steps:

      - Run initialization playbook / role
        - run playbook to add job templates

      - Run playbook to mess things up
        - Adds EE that is missing credential
        - Create custom route


      - Troubleshoot

    Teachings:

      - View errors when job launches with EE missing credential
      - Add CSRF option into CR