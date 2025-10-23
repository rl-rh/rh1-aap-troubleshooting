 1. Log in to the OCP Cluster UI, obtain cli auth token, then install the AAP Operator and AAP CR. Figure out whats failing with Hub
     ```
    ansible-playbook -e install_namespace=aap1 step1.yml
    ```
 2. Update the AAP CR. Look at the logs to figure out whats going wrong. Hint, take a look at the DB pod
     ```
    ansible-playbook -e install_namespace=aap1 step2.yml
    ```
 3. Configure AAP components and find whats failing. (Quotas wrong and hub SC wrong)
     ```
     ansible-playbook -e install_namespace=aap1 step3.yml
     ```
 4. Upgrade to the latest AAP version. View Product versions in gateway UI. Should be Controller ver: 4.6.21, Hub Version 4.10.9, EDA version 1.1.13
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