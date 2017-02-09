import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    '.molecule/ansible_inventory').get_hosts('all')


def test_pip_is_installed(Package, SystemInfo):
    # This is sub-optimal, need better way to parametrize
    if SystemInfo.distribution == 'centos':
        pip = Package('python2-pip')
    elif SystemInfo.distribution == 'amzn':
        pip = Package('python27-pip')
    else:
        raise ValueError(
                "Unsupported distribution: " + SystemInfo.distribution)

    assert pip.is_installed
