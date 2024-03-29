Ansible Role: LightDM
=====================

[![Tests](https://github.com/gantsign/ansible-role-lightdm/workflows/Tests/badge.svg)](https://github.com/gantsign/ansible-role-lightdm/actions?query=workflow%3ATests)
[![Ansible Galaxy](https://img.shields.io/badge/ansible--galaxy-gantsign.lightdm-blue.svg)](https://galaxy.ansible.com/gantsign/lightdm)
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](https://raw.githubusercontent.com/gantsign/ansible-role-lightdm/master/LICENSE)

Role to allow configuration of LightDM, currently limited to configuring the
auto-login preferences and whether to allow users to login using the guest account.

Requirements
------------

* LightDM installed

* Ansible >= 2.9

* Linux Distribution

    * Debian Family

        * Ubuntu

            * Bionic (18.04)
            * Focal (20.04)

        * Note: other versions are likely to work but have not been tested.

Role Variables
--------------

The following variables will change the behavior of this role (default values
are shown below):

```yaml
# Username of user to auto-login on startup
lightdm_autologin_user:

# Time to wait (in seconds) before the user is auto logged in to allow a chance
# to log in as a different user.
lightdm_autologin_user_timeout: 0

# Whether to allow users to login using the guest account
lightdm_greeter_allow_guest: no

# Directory where GLib schemas are located
lightdm_glib_schemas_directory: /usr/share/glib-2.0/schemas

# Directory where LightDM config is located
lightdm_conf_directory: /usr/share/lightdm/lightdm.conf.d

# Name of override file for LightDM config
lightdm_overide_filename: 70-ansible.conf
```

Dependencies
------------

None

Example Playbook
----------------

This role can be used as follows:

```yaml
- hosts: servers
  roles:
    - role: gantsign.lightdm
      lightdm_autologin_user: vagrant
```

More Roles From GantSign
------------------------

You can find more roles from GantSign on
[Ansible Galaxy](https://galaxy.ansible.com/gantsign).

Development & Testing
---------------------

This project uses [Molecule](http://molecule.readthedocs.io/) to aid in the
development and testing; the role is unit tested using
[Testinfra](http://testinfra.readthedocs.io/) and
[pytest](http://docs.pytest.org/).

To develop or test you'll need to have installed the following:

* Linux (e.g. [Ubuntu](http://www.ubuntu.com/))
* [Docker](https://www.docker.com/)
* [Python](https://www.python.org/) (including python-pip)
* [Ansible](https://www.ansible.com/)
* [Molecule](http://molecule.readthedocs.io/)

Because the above can be tricky to install, this project includes
[Molecule Wrapper](https://github.com/gantsign/molecule-wrapper). Molecule
Wrapper is a shell script that installs Molecule and it's dependencies (apart
from Linux) and then executes Molecule with the command you pass it.

To test this role using Molecule Wrapper run the following command from the
project root:

```bash
./moleculew test
```

Note: some of the dependencies need `sudo` permission to install.

License
-------

MIT

Author Information
------------------

John Freeman

GantSign Ltd.
Company No. 06109112 (registered in England)
