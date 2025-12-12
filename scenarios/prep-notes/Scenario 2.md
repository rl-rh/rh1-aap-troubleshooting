Scenario #2

    MODE: Easy

    Components: Automation Hub

    Namespace: scenario-2

    Objectives: 
      * Find out why Automation Hub is stuck during the deployment

    Steps:
      ansible-playbook site.yml -t deploy (select scenario 2)
      ansible-playbook site.yml -t break (select scenario 2)
      Note: Automation Hub UI will not be available, just focus on the Hub Operator Logs and Operator Pods
    
    Hints:
      Take a look at the hub operator-manager logs
      Review the errors seen with the hub api pods
      Is there storage for hub?


Answer section:

Hub requires a Read Write Many storage-class in a typical deployment. Change the hub storage class to ocs-external-storagecluster-cephfs , delete the old pvc and let the operator reconcile