Scenario #1

    MODE: Easy

    Namespace: cenario-1

    Components: Automation Controller

    Objectives: 
      * Find out why there are pod errors
      * Check the version of controller

    Steps:
      ansible-playbook site.yml -t deploy (select scenario 1)
      ansible-playbook site.yml -t break (select scenario 1)