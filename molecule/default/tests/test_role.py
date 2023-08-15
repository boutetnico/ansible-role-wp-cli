import pytest


@pytest.mark.parametrize(
    "path,username,groupname,mode",
    [
        ("/usr/local/bin/wp", "root", "root", 0o755),
    ],
)
def test_wp_cli_is_installed(host, path, username, groupname, mode):
    path = host.file(path)
    assert path.exists
    assert path.is_file
    assert path.user == username
    assert path.group == groupname
    assert path.mode == mode
