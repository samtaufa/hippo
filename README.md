
Hippo is a host repository for tracking system configuration files.

Overview
========

Hippo is a thin layer built on top of Git that simplifies managing a host-wide
repository of files with metadata (permissions and ownership). Conceptually,
Hippo simply serializes metadata before certain Git commands are run, and
restores file metadata after others. By default, the host-wide git repository
lives in __/var/hippo/.git__, metadata is tracked in __/var/hippo/manifest__.


Usage
=====

Hippo requires privileged access to checked-in files, so all commands below
should be run as root. Most Hippo commands are identical to their Git
equivalents:

## Initialise a new host repository

    hippo init

## Add a file

    hippo add /etc/inetd.conf

It's a good idea to add files and do an initial commit, before making any
modifcations. This gives you a baseline to track changes against.

## Commit

    hippo commit -a 

## Push to a remote host

    hippo push aldo@remotehost:repo

## Inspect a hippo repository with git

A Hippo repository is just a Git repo, with a bit of added structure. You can
check out a hippo repository using Git, and inspect or even modify the included
files and metadata log:

    git clone aldo@remotehost:repo

## Flash a configuration checked into Hippo onto a new system

    hippo clone aldo@remotehost:repo



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




Dependencies
============

* [Git](http://git-scm.com/) v1.7.1 or later.

* [GitPython](http://gitorious.org/git-python) v0.3 or later.

