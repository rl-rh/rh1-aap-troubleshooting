 1. Log in to the OCP Cluster UI, obtain cli auth token
 2. Install the AAP Operator
     ```
    ansible-playbook -e aap_ns=aap1 step2.yml
    ```
 3. Configure AAP components and find whats failing. (Quotas wrong and hub SC wrong)
     ```
     ansible-playbook -e aap_ns=aap1 step3.yml
     ```
 4. Upgrade to the latest AAP version. View Product versions in gateway UI. Should be Controller ver: x.x, Hub Version x.x, EDA version x.x
    ```
    ansible-playbook -e aap_ns=aap1 step4.yml
    ```
 5. Run this one and run the job template called RH1-T1
    ```
    ansible-playbook -e aap_ns=aap1 step5.yml
    ```