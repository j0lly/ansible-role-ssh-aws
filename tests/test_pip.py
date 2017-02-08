import pytest


@pytest.fixture()
def AnsibleDistribution(Ansible):
    """ Grab Os specific values """
    return Ansible("setup")["ansible_facts"]["ansible_distribution"]


def test_pip_is_installed(Package, AnsibleDistribution):
    # This is sub-optimal, need better way to parametrize
    if AnsibleDistribution == 'CentOS':
        pip = Package('python2-pip')
    elif AnsibleDistribution == 'Amazon':
        pip = Package('python27-pip')
    else:
        raise ValueError("Unsupported distribution: " + AnsibleDistribution)

    assert pip.is_installed
