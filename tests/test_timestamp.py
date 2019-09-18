from _repobee import plugin

from repobee_timestamp import timestamp


def test_register():
    """Just test that there is no crash"""
    plugin.register_plugins([timestamp])
