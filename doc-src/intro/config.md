Configuration
=============

## Configuring an origin repository

In a shared environment, we can't store the origin repository information
directly in the hippo repository, because different administrators may need a
different repository URL string. The easiest way around this, is to configure
the remote branches in the individual administrator gitconfigs instead. For
example, I have this in my __~/.gitconfig__:

    [branch "master"]
        remote = origin
        merge = refs/heads/master

    [remote "origin"]
        url = aldo@remotehost:/path/to/repo
        fetch = +refs/heads/*:refs/remotes/origin/*


## Commit templates

You can use git's built-in commit template functionality with hippo. First,
create the template file - in this example, I use _/etc/hippo-commit-template_.
Then, set the commit template like this:

    hippo config commit.template /etc/hippo-commit-template


## Multi-hop SSH

Often, you will want to push or pull from a repo that is not directly reachable
from the current system. In this case, you can set up multi-hop SSH. In your
_~/.ssh/config_ file add a section as follows:

    Host destination_host_name
        ProxyCommand ssh -Aq intermediate_host_address nc -q0 %h 22
        Hostname destination_host_address

Here, __destination_host_name__ is the shortcut name you want to use for the
destination host. The intermediate and destination host addresses are either IP
addresses or resolvable hostnames.

You can now push or pull to the destination host, using the assigned shortcut
name.
