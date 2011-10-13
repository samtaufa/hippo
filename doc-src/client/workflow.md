Most Hippo commands are identical to their Git equivalents, and Hippo needs
root privileges to perform the majority of its functions (and is thus often
executed as root or with sudo.)

After installing the software, the next major workflow item is to

- [Initialise](#initialise) a new host hippo repository

From then on, the standard workflow surrounds general use of archiving a host
configuration, such as: 

1. [Add](#add)ing the files we want to archive/track to the repository queue
2. [Commit](#commit)ting these files and any accepted changes to the repository
3. [Push](#push) the repository to a remote host

## <a name="initialise"></a> Initialise a new host repository

&#91;Ref: [git-init](http://www.kernel.org/pub/software/scm/git/docs/git-init.html "Create an empty git repository or reinitialize an existing one")
]

After installing Hippo onto a host, we create the local repository
for the configuration files using *hippo init*

<!--(block|syntax("bash"))-->
$ sudo hippo init
<!--(end)-->

By default, the host-wide git repository lives in **/var/hippo/.git**. 
Metadata is tracked in **/var/hippo/manifest**.

We now have an empty host configuration repository. There are no 
configuration files in the repository (not even /etc/passwd.)

## <a name="add"></a>1. Add a file

&#91;Ref: [git-add](http://www.kernel.org/pub/software/scm/git/docs/git-add.html "Add file contents to the index")]

Before we can version changes, or backup any of our hosts files, we
need to add these files to the Hippo/Git repository.
The Hippo/Git principles for managing repositories are to:

- 	Take a snapshot of the contents of new or changed
	file(s) to be inserted into the repository. 
	The snapshot is called the *index* and taking the
	snapshot is done by *add*.
- 	Move the *snapshot* in the *index* into the repository
	with a message describing the changes made, using the
	command *commit*.

Select the files you need to track versioning, and use *hippo add file-name*

<!--(block|syntax("bash"))-->
$ sudo hippo add /etc/inetd.conf
<!--(end)-->

We use *sudo* because read/write access to some of the files requires
root privileges.

When learning about configuration archiving, restoration, it is 
interesting to install/configure hippo on a new/pristine system
and add all configuration files. Hippo then becomes a good tool
for detecting/noting changes to your configuration settings as
you install and configure services/applications.

&#91;Ref: [undo git add](http://stackoverflow.com/questions/348170/undo-git-add 
"Is there a way to remove these files from the commit? 'git rm -r --cached <file> ...") | 
[git-status](http://www.kernel.org/pub/software/scm/git/docs/git-status.html "obtain a summary of what is included by any of the above for the next commit") |
[git-rm](http://www.kernel.org/pub/software/scm/git/docs/git-rm.html "Remove files from the working tree and the index") |
[git-commit](http://www.kernel.org/pub/software/scm/git/docs/git-commit.html "Record changes to the repository")
[git-reset](http://www.kernel.org/pub/software/scm/git/docs/git-reset.html "git reset HEAD <file>...")
]

## <a name="commit"></a>3. Commit

&#91;Ref: [git-commit](http://www.kernel.org/pub/software/scm/git/docs/git-commit.html "Record changes to the repository")
]

<blockquote>
Stores the current contents of the index in a new commit along with 
a log message from the user describing the changes
</blockquote>

After we've *'add'* a file/directory into the repository index, we
can remove them, or enshrine/commit these files into the repository
using *commit*

<!--(block|syntax("bash"))-->
$ sudo hippo commit -a 
<!--(end)-->

The above command, including the *-a* tells hippo/Git to commit *all*
index entries.

The commit command is also used to tell the repository that changes
to the existing files can also be committed.

## <a name="push"></a>4. Push to a remote host

&#91;Ref: [git-push](http://www.kernel.org/pub/software/scm/git/docs/git-push.html "Update remote refs along with associated objects")
]

To copy the host configuration files to a separate host (Central Repository)
we use the git-push equivalent.

<!--(block|syntax("bash"))-->
$ hippo push aldo@remotehost:repo master
<!--(end)-->

Of course, this command presumes that the repository has already been created
on the above server/remotehost.

Refer to [Server/Remote host Configuration](../server.html) for configuring your aggregation/central
host.

Refer to [Shortcuts](shortcuts.html) for simplifying the *push* process.

