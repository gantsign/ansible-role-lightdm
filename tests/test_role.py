from testinfra.utils.ansible_runner import AnsibleRunner

testinfra_hosts = AnsibleRunner('.molecule/ansible_inventory').get_hosts('all')


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
    assert conf.contains('autologin-user=test_usr')
    assert conf.contains('autologin-user-timeout=4242')

def test_guest_login(File):
    conf = File('/usr/share/lightdm/lightdm.conf.d/70-ansible.conf')

    assert conf.exists
    assert conf.is_file
    assert conf.contains('greeter-allow-guest=true')
