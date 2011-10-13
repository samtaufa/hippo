Hippo is a distributed version control repository for tracking 
system configuration files.

Hippo is a thin layer built on top of the open source, distributed
version control system: [Git](http://git-scm.com/ "Git is 
a free & open source, distributed version control system") to
simplify managing files with metadata (permissions and ownership). 
By maintaining and managing file metadata, the repository can be used to 
archive and restore a host configuration.

Conceptually, Hippo serializes metadata before certain Git commands are run, 
and restores file metadata after others. 

## sGittish

<blockquote>
<strong>skittish</strong>

a: lively or frisky in action
</blockquote>

Because Hippo is a thin layer (wrapper) around [Git](http://git-scm.com/ "Git is 
a free & open source, distributed version control system"), the terminology
used in Hippo is very much that used in Git.

Likewise, *git* and related support tools can be used in many parts of the 
Hippo repository.

## Up and Running

To effectively use Hippo, you will generally have Hippo installed
and running on each host, including the host that you designate
to archive copies of configurations from all the hosts.

Each host will have a standard installation, with a designated
'central repository' configured with **bare** repos that all
administrators can *push* or *pull* configurations.