
Hippo is a distributed version control repository for tracking 
system configuration files.

Overview
========

Hippo is a thin layer built on top of [GIT](http://git-scm.com/ "Git is 
a free & open source, distributed version control system") that 
simplifies managing files with metadata (permissions and ownership). 
By maintaining and managing file metadata, the repository can be used to 
archive and restore a host configuration.

Conceptually, Hippo serializes metadata before certain Git commands are run, 
and restores file metadata after others. 