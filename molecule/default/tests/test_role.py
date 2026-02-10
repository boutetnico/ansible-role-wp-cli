import pytest


@pytest.mark.parametrize(
    "path,username,groupname,mode",
    [
        ("/usr/local/bin/wp", "root", "root", 0o755),
    ],
)
def test_wp_cli_is_installed(host, path, username, groupname, mode):
    f = host.file(path)
    assert f.exists
    assert f.is_file
    assert f.user == username
    assert f.group == groupname
    assert f.mode == mode


def test_wp_cli_is_executable(host):
    cmd = host.run("wp --version --allow-root")
    assert cmd.rc == 0
    assert "WP-CLI" in cmd.stdout


def test_wp_cli_info_command(host):
    cmd = host.run("wp cli info --allow-root")
    assert cmd.rc == 0
    assert "PHP binary" in cmd.stdout
    assert "WP-CLI root dir" in cmd.stdout
