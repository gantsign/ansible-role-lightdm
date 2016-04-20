Ansible Role: LightDM
=====================

[![Build Status](https://travis-ci.org/gantsign/ansible-role-lightdm.svg?branch=master)](https://travis-ci.org/gantsign/ansible-role-lightdm)

Role to allow configuration of LightDM, currently limited to configuring the
auto-login preferences.

Requirements
------------

Ubuntu with LightDM installed.

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
     - { role: gantsign.lightdm, lightdm_autologin_user: vagrant }
```

License
-------

MIT

Author Information
------------------

John Freeman

GantSign Ltd.
Company No. 06109112 (registered in England)
