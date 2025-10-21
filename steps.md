 1. Log in to the OCP Cluster UI, obtain cli auth token
 2. Install the AAP Operator
     ```
    ansible-playbook -e install_namespace=aap1 step2.yml
    ```
 3. Configure AAP components and find whats failing. (Quotas wrong and hub SC wrong)
     ```
     ansible-playbook -e install_namespace=aap1 step3.yml
     ```
 4. Upgrade to the latest AAP version. View Product versions in gateway UI. Should be Controller ver: x.x, Hub Version x.x, EDA version x.x
    ```
    ansible-playbook -e install_namespace=aap1 step4.yml
    ```
 5. Run this one and run the job template called RH1-T1
    ```
    ansible-playbook -e install_namespace=aap1 step5.yml
    ```
 6. Run this one and run the job template called RH1-T2
    ```
    ansible-playbook -e install_namespace=aap1 step6.yml
    ```
 7. Create cutom route for aap and log in then run a job template called RH1-T3
    ```
    ansible-playbook -e install_namespace=aap1 step7.yml
    ```