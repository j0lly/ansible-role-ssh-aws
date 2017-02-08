def test_epel_is_installed(Package):
    epel = Package('epel-release')
    assert epel.is_installed
