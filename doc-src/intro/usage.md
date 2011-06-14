Usage
=====

For managing system files, Hippo requires privileged access, so all commands 
below should be run as root. Most Hippo commands are identical to their Git
equivalents:

## Initialise a new host repository

    hippo init

By default, the host-wide git repository lives in __/var/hippo/.git__. 
Metadata is tracked in __/var/hippo/manifest__.
    
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