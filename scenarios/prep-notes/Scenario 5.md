Scenario #5

    MODE: Easy

    Components: Automation Hub

    Namespace: aap-rh1    

    Objectives: 
      * Log into gateway UI
      * Browse to Automation Content (Automation Hub) -> Repositories
      * Sync the "Community" repository
      * fix the issue(s)

    Steps:
      ansible-playbook site.yml -t deploy (select scenario 5)
      ansible-playbook site.yml -t break (select scenario 5)

    Hints:
      Review hub content pod logs

Answer section:
There are two issues here:
* Content limits are too low, they need to be increased quite a bit or removed. You can update the CR with these values for Hub Content:
          spec:
            hub:
              content:
                resource_requirements:
                  limits:
                    cpu: 1000m
                    memory: 8Gi
                  requests:
                    cpu: 100m
                    memory: 200Mi
* PVC for hub file storage is too low, increase the size of the PVC
  * increase size to 10Gi in the AAP CR: hub_file_storage_size: 25Mi
  * increase the size on the pvc directly
  spec:
  resources:
    requests:
      storage: 10Gi


Scenario #5

    MODE: Easy

    Steps:

      - Run initialization playbook / role

      - Run playbook to mess things up
        - Hub limits too low when going to sync community.general
        - PVC too small to sync community.general

      - Troubleshoot

    Teachings:

      - Grow PVC
      - remove or update limits for hub pods