# Molecule test this role

## Scenario - `default`
This will test the role installing Certbot and Adding Cron job, Certificate generation and Modifying Apache config is not tested.

Run Molecule test
```
molecule test
```

Run test with variable example
```
MOLECULE_DISTRO=centos7 molecule test
```

### Molecule variables
 - `MOLECULE_DISTRO` OS of docker container to test, default `ubuntu2204`
   - Tested distros;
    - `ubuntu2204`
    - `ubuntu2004`
    - `centos7`
    - `rockylinux8`
    - `rockylinx9`
    - `rhel7`
    - `rhel8`
    - `rhel9`
 - `MOLECULE_ANSIBLE_VERBOSITY` `0-3`, sets ansible verbosity for debugging, default `0`