import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_lightdm_installed(Command):
    assert Command('lightdm --version').rc == 0


def test_config_file(File):
    conf = File('/usr/share/lightdm/lightdm.conf.d/70-ansible.conf')

    assert conf.exists
    assert conf.is_file
    assert conf.user == 'root'
    assert conf.group == 'root'
    assert oct(conf.mode) == '0644'


def test_auto_login(File):
    conf = File('/usr/share/lightdm/lightdm.conf.d/70-ansible.conf')

    assert conf.exists
    assert conf.is_file
    assert not conf.contains('autologin-user')
    assert not conf.contains('autologin-user-timeout')


def test_guest_login(File):
    conf = File('/usr/share/lightdm/lightdm.conf.d/70-ansible.conf')

    assert conf.exists
    assert conf.is_file
    assert conf.contains('greeter-allow-guest=false')
