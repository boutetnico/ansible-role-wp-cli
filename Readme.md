ansible-role-wp-cli
===================

This role installs and configures [WP-CLI](https://wp-cli.org/).

Requirements
------------

Ansible 2.6 or newer.

Supported Platforms
-------------------

- [Debian - 9 (Stretch)](https://wiki.debian.org/DebianStretch)
- [Debian - 10 (Buster)](https://wiki.debian.org/DebianBuster)
- [Ubuntu - 16.04 (Xenial Xerus)](http://releases.ubuntu.com/16.04/)
- [Ubuntu - 18.04 (Bionic Beaver)](http://releases.ubuntu.com/18.04/)

Role Variables
--------------

| Variable            | Required | Default             | Choices   | Comments                                      |
|---------------------|----------|---------------------|-----------|-----------------------------------------------|
| wp_cli_path         | true     | `/usr/local/bin/wp` | string    |                                               |
| wp_cli_keep_updated | true     | `false`             | bool      |                                               |

Dependencies
------------

None

Example Playbook
----------------

    - hosts: all
      roles:
        - role: ansible-role-wp-cli

Testing
-------

    molecule test

License
-------

MIT

Author Information
------------------

[@boutetnico](https://github.com/boutetnico)
