Scenario #7

    MODE: Easy

    Components: Ansible Lightspeed Intelligent Assistant

    Namespace: aap-rh1    

    Objectives: 
      * Log into gateway UI
      * Chat icon in the top right is missing
      * fix the issue(s)

    Steps:
      ansible-playbook site.yml -t deploy (select scenario 7)
      ansible-playbook site.yml -t break -e chatbot_token='token_value_from_resource_page' (select scenario 7)

    Hints:
      Review lightspeed api and chatbot pod logs to find out why
      Model names and access information are available on the lab resource page

Answer section:
ALIA is currently configured to use a module which it has no access to. 
  * update the chatbot secret (chatbot-configuration-secret) to use this model instead: granite-3-2-8b-instruct
  * delete lightspeed operator pod and wait for reconciliation

Scenario #1

    MODE: Easy

    Steps:

      - Run initialization playbook / role
        - configure ALIA with MaaS

      - Run playbook to mess things up
        - Configures chatbot secret with wrong model

      - Troubleshoot

    Teachings:

      - Learn about ALIA configuration and lightspeed logs