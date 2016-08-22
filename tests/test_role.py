def test_lightdm_installed(Command):
    assert Command('lightdm --version').rc == 0

def test_config_file(File):
    conf = File('/usr/share/lightdm/lightdm.conf.d/70-ansible.conf')

    assert conf.exists
    assert conf.is_file
    assert conf.user == 'root'
    assert conf.group == 'root'
    assert oct(conf.mode) == '0644'

    assert conf.contains('test_usr')
    assert conf.contains('4242')
