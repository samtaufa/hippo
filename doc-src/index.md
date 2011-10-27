Hippo is a distributed version control repository for tracking 
system configuration files.

$!Image("hippo.png", title="Hippo", klass="imgcenter")!$

Use Hippo when you want versioning to allow you to do things 
such as:

1. Document changes and retain history of
changes to your configuration file.
2. Retain the above mentioned history on copies
you maintain external to the host.
3. Restore your configuration onto the same other hosts,
while maintaining the history of your changes.

## sGittish

<blockquote>
<strong>skittish</strong>

a: lively or frisky in action
</blockquote>

Hippo is a thin layer built on top [Git](http://git-scm.com/ "Git is 
a free and open source, distributed version control system") to
simplify managing files with metadata (permissions and ownership). 
By maintaining and managing file metadata, the repository can be used to 
archive and restore a host configuration.

Conceptually, Hippo serializes metadata before certain Git commands are run, 
and restores file metadata after others. 

Because Hippo is a thin layer (wrapper) around [Git](http://git-scm.com/ "Git is 
a free & open source, distributed version control system"), the terminology
used in Hippo is very much that used in Git. Likewise, *git* and related support 
tools can be used in many parts of the Hippo repository.

## Up and Running

To effectively use Hippo, you will generally have Hippo installed
and running on each host, including the host that you designate
to archive copies of configurations from all the hosts.

Each host will have a standard installation, with a designated
'central repository' configured with **bare** repos that all
administrators can *push* or *pull* configurations.