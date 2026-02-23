# Red Hat Summit - Session

# Instructions

- Setup a scenario on OpenShift

  ```
  ansible-playbook site.yml
  ```

- Break the environment

  ```
  ansible-playbook site.yml -t break
  ```

- Fix the environment

  ```
  ansible-playbook site.yml -t fix
  ```

- Delete the environment

  ```
  ansible-playbook site.yml -t delete
  ```