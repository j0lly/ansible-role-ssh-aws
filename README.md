ssh aws sync
=========

This Role provides a setup for an ssh aws pub key based lookup for ec2 instances

This role enhance the job done by [widdix](https://github.com/widdix/aws-ec2-ssh)

[![Ansible Role](https://img.shields.io/ansible/role/15479.svg)](https://galaxy.ansible.com/j0lly/ssh-keys/)
[![Build Status](https://travis-ci.org/j0lly/ansible-role-ssh-aws.svg?branch=master)](https://travis-ci.org/j0lly/ansible-role-ssh-aws)

Requirements
------------

The ec2 instance need to be able to perform iam calls, possibly via an instance profile:
 - "iam:GetSSHPublicKey"
 - "iam:ListSSHPublicKeys"
 - "iam:ListUsers"
 - "iam:GetGroup"

**role should look like:**
```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "Stmt1471562879000",
      "Effect": "Allow",
      "Action": [
        "iam:ListUsers",
        "iam:GetGroup"
      ],
      "Resource": [
        "*"
      ]
    },
    {
      "Sid": "Stmt1471562943000",
      "Effect": "Allow",
      "Action": [
        "iam:GetSSHPublicKey",
        "iam:ListSSHPublicKeys"
      ],
      "Resource": [
        "arn:aws:iam::<YOUR_ACCOUNT_ID_HERE>:user/*"
      ]
    }
  ]
}
```

Role Variables
--------------

The variables that can be passed to this role and a brief description about
them are as follows. (For all variables, take a look at [defaults/main.yml](defaults/main.yml))

```yaml
# define if we want to create [iam] users during provisioning
ssh_aws_first_sync: false

# runcommand for pub key retrival
ssh_aws_authkey_command_path: '/opt/authorized_key_command.sh'
ssh_aws_user: 'nobody'

# path for import user command
ssh_aws_import_user_path: '/opt/import_users.sh'
```

Example Playbook
----------------

```yaml
- hosts: all
  roles:
    - {role: j0lly.ssh-aws,
       ssh_aws_first_sync: true}
```

License
-------

[BSD](LICENSE)
