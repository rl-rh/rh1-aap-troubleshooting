# Red Hat One - Session

# Instructions

- Setup a scenario on OpenShift

  ```
  ansible-playbook -i inventory.yml site.yml -e 'namespace=$NAMESPACE'
  ```
  **NOTE**: Change `$NAMESPACE` to namespace you want work with

- Break the environment

  ```
  ansible-playbook -i inventory.yml site.yml -e 'namespace=$NAMESPACE' -t break
  ```