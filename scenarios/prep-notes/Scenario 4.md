Scenario #4

    MODE: Easy

    Components: AAP Gateway UI

    Namespace: aap-rh1    

    Objectives: 
      * Find out why Gateway pods are failing
      * Log in to AAP UI to verify things are working again

    Steps:
      ansible-playbook site.yml -t deploy (select scenario 4)
      ansible-playbook site.yml -t break (select scenario 4)

    Hints:
      Are there any pods with errors?

Answer section:

Database has an invalid node_selector, so the pod cannot be scheduled. Either replace the node_selector with a correct label ("kubernetes.io/os": "linux"), or delete the node_selector altogether from the CR in the database section
API pods have an oversized request and limit set that exceeds the resources of the cluster, either reduce the reqeusts/limits to something manageable (500Mi requests, 5Gi limit), or remove the resource_requirements from the CR in the API section
Delete the gateway operator-manager pods and allow for reconciliation


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