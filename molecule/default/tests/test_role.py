import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_lightdm_installed(host):
    assert host.run('lightdm --version').rc == 0


def test_config_file(host):
    conf = host.file('/usr/share/lightdm/lightdm.conf.d/70-ansible.conf')

    assert conf.exists
    assert conf.is_file
    assert conf.user == 'root'
    assert conf.group == 'root'
    assert oct(conf.mode) == '0644'


def test_auto_login(host):
    conf = host.file('/usr/share/lightdm/lightdm.conf.d/70-ansible.conf')

    assert conf.exists
    assert conf.is_file
    assert conf.contains('autologin-user=test_usr')
    assert conf.contains('autologin-user-timeout=4242')


def test_guest_login(host):
    conf = host.file('/usr/share/lightdm/lightdm.conf.d/70-ansible.conf')

    assert conf.exists
    assert conf.is_file
    assert conf.contains('greeter-allow-guest=true')
