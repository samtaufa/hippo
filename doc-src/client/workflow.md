Most Hippo commands are identical to their Git equivalents, and Hippo needs
root privileges to perform the majority of its functions (and is thus often
executed as root or with sudo.)

After installing the software, general workflow is: 

1. [Add](#add)ing the files we want to archive/track to the repository queue
2. [Review](#status) the files indexed
3. [Commit](#commit)ting these files and any accepted changes to the repository
4. [Push](#push) the repository to a remote host

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

### Oops, don't add that file

&#91;Ref: [undo git add](http://stackoverflow.com/questions/348170/undo-git-add 
"Is there a way to remove these files from the commit? 'git rm -r --cached <file> ...") | 
[git-rm](http://www.kernel.org/pub/software/scm/git/docs/git-rm.html "Remove files from the working tree and the index") |
[git-reset](http://www.kernel.org/pub/software/scm/git/docs/git-reset.html "git reset HEAD <file>...")
]

More often than not, I've jumped in and [add]()ed files that I do not
want to version. *DO NOT* use *'git rm <file>'* to get rid of the 
index entry. The documentation is quite clear that this will
*remove* the index entry and *the file*. To *remove only the index*
entry, use something such as the below:

<!--(block|syntax("bash"))-->
$ sudo su
# cd /var/hippo
# git rm -r --cached <file>...
<!--(end)-->

Refer the above referenced documentation for more details.

## <a name="status"></a>2. Status

&#91; [git-status](http://www.kernel.org/pub/software/scm/git/docs/git-status.html "obtain a summary of what is included by any of the above for the next commit")]

You can always review what is currently 'snapshotted' or 'staged'
into hippo/git index, by using the *status* command.

<!--(block|syntax("bash"))-->
$ sudo hippo status
<!--(end)-->

From the displayed list, you take note of the files that have changed
and then make decisions for committing/removing indexed files.

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

