[![tests](https://github.com/boutetnico/ansible-role-wp-cli/workflows/Test%20ansible%20role/badge.svg)](https://github.com/boutetnico/ansible-role-wp-cli/actions?query=workflow%3A%22Test+ansible+role%22)
[![Ansible Galaxy](https://img.shields.io/badge/galaxy-boutetnico.wp_cli-blue.svg)](https://galaxy.ansible.com/boutetnico/wp_cli)

ansible-role-wp-cli
===================

This role installs and configures [WP-CLI](https://wp-cli.org/).

Requirements
------------

Ansible 2.10 or newer.

Supported Platforms
-------------------

- [Debian - 11 (Bullseye)](https://wiki.debian.org/DebianBullseye)
- [Debian - 12 (Bookworm)](https://wiki.debian.org/DebianBookworm)
- [Ubuntu - 20.04 (Focal Fossa)](http://releases.ubuntu.com/20.04/)
- [Ubuntu - 22.04 (Jammy Jellyfish)](http://releases.ubuntu.com/22.04/)

Role Variables
--------------

| Variable            | Required | Default             | Choices   | Comments                                 |
|---------------------|----------|---------------------|-----------|------------------------------------------|
| wp_cli_path         | true     | `/usr/local/bin/wp` | string    |                                          |
| wp_cli_keep_updated | true     | `false`             | bool      |                                          |

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
