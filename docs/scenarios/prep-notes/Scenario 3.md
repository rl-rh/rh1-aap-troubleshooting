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


Answer section:

Database service was deleted. Create a new service using this YAML (replacing the variables with the correct names), then wait for the pods to come back online and healthy
```
    api_version: v1
    kind: Service
    name: "{{ _scenario_name }}-aap-postgres-15"
    namespace: "{{ namespace }}" 
    state: present
    definition:
      apiVersion: v1
      kind: Service
      metadata:
        name: "{{ _scenario_name }}-aap-postgres-15"
        namespace: "{{ namespace }}" 
        ownerReferences:
          - apiVersion: aap.ansible.com/v1alpha1
            kind: AnsibleAutomationPlatform
            name: "{{ _scenario_name }}-aap"
            uid: "{{ aap_cr_info.resources[0].metadata.uid }}"
        labels:
          app.kubernetes.io/component: database
          app.kubernetes.io/instance: "postgres-15-{{ _scenario_name }}-aap"
          app.kubernetes.io/managed-by: aap-gateway-operator
          app.kubernetes.io/name: postgres-15
      spec:
        clusterIP: None
        ipFamilies:
          - IPv4
        ports:
          - name: '5432'
            protocol: TCP
            port: 5432
            targetPort: 5432
        internalTrafficPolicy: Cluster
        clusterIPs:
          - None
        type: ClusterIP
        ipFamilyPolicy: SingleStack
        sessionAffinity: None
        selector:
          app.kubernetes.io/component: database
          app.kubernetes.io/instance: "postgres-15-{{ _scenario_name }}-aap"
          app.kubernetes.io/managed-by: aap-gateway-operator
          app.kubernetes.io/name: postgres-15   
```          

Gateway password was changed. Use the aap-gateway-manage command to set the password back to what is defined in the CR
```aap-gateway-manage update_password --username admin --password```

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