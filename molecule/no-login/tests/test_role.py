def test_lightdm_installed(host):
    assert host.run('lightdm --version').rc == 0


def test_config_file(host):
    conf = host.file('/usr/share/lightdm/lightdm.conf.d/70-ansible.conf')

    assert conf.exists
    assert conf.is_file
    assert conf.user == 'root'
    assert conf.group == 'root'
    assert oct(conf.mode) == '0o644'


def test_auto_login(host):
    conf = host.file('/usr/share/lightdm/lightdm.conf.d/70-ansible.conf')

    assert conf.exists
    assert conf.is_file
    assert not conf.contains('autologin-user')
    assert not conf.contains('autologin-user-timeout')


def test_guest_login(host):
    conf = host.file('/usr/share/lightdm/lightdm.conf.d/70-ansible.conf')

    assert conf.exists
    assert conf.is_file
    assert conf.contains('greeter-allow-guest=false')
