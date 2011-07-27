# Client

Most Hippo commands are identical to their Git equivalents, and Hippo needs
root privileges to perform the majority of its functions (and is thus often
executed as root or with sudo.)

A <a href="#workflow">standard workflow</a> for Hippo would be similar to the below:

1. [Initialise](#initialise) a new host repository
2. [Add](#add) files
3. [Commit](#commit)
4. [Push](#push) to a remote host
5. [Multi-hop SSH](#ssh)

<a href="#maintenance">General Maintenance</a> will include some inspection such as:

- Standardised Commits
- Remote Repository
- Inspection
- Flash onto new host


## <a name="workflow"></a>1. Standard Workflow

The standard workflow surrounds general use of archiving a host
configuration, such as: (a) initialising the hippo repository, (b)
adding relevant files, (c) committing these changes, and then (d)
pushing these changes to a remote host.

1. Initialise a new host repository
2. Add files
3. Commit above Changes
4. Push to a remote host

### <a name="initialise"></a> 1.1 Initialise a new host repository

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

### <a name="add"></a> 1.2 Add a file

&#91;Ref: [git-add](http://www.kernel.org/pub/software/scm/git/docs/git-add.html "Add file contents to the index")]

Using the same principles for adding files to Git, we use *hippo add* 
to add files for inclusion into the repository index.

<!--(block|syntax("bash"))-->
$ sudo hippo add /etc/inetd.conf
<!--(end)-->

It's a good idea to add pristine files (files untouched other than the initial
Operating System install) before making any modifcations. 
This gives you a baseline to track changes against.

### <a name="commit"></a> 1.3 Commit

&#91;Ref: [git-commit](http://www.kernel.org/pub/software/scm/git/docs/git-commit.html "Record changes to the repository")
]

"Stores the current contents of the index in a new commit along with 
a log message from the user describing the changes "

<!--(block|syntax("bash"))-->
$ sudo hippo commit -a 
<!--(end)-->

### <a name="push"></a> 1.4 Push to a remote host

&#91;Ref: [git-push](http://www.kernel.org/pub/software/scm/git/docs/git-push.html "Update remote refs along with associated objects")
]

To copy the host configuration files to a separate host (Central Repository)
we use the git-push equivalent.

<!--(block|syntax("bash"))-->
$ hippo push aldo@remotehost:repo master
<!--(end)-->

Of course, this command presumes that the repository has already been created
on the above server/remotehost.

### <a name="ssh"></a>1.5 Multi-hop SSH

Often, you will want to push or pull from a repo that is not directly reachable
from the current system. In this case, you can set up multi-hop SSH, where we
proxy through an intermediate (or bastion) host. 

<pre>
      [ Host-A ] oo---ssh---> [ Bastion ] >>---ssh---> [ Destination ]
</pre>

In your _~/.ssh/config_ file add a section as follows:

<!--(block|syntax("apache"))-->
Host destination_host_name_alias
	ProxyCommand ssh -Aq intermediate_host_address nc -w 10 %h %p
	Hostname destination_host_address
<!--(end)-->

Here, **destination_host_name_alias** is the shortcut alias you want to use for the
destination host. The intermediate and destination host addresses are either IP
addresses or resolvable hostnames.

You can now push or pull to the destination host, using the assigned shortcut
name.

<!--(block|syntax("bash"))-->
$ hippo push aldo@destination_host_name_alias:repo master
<!--(end)-->

<table>
	<tr><th>Config Entry</th>
		<th>More Information</th>
	</tr>
	<tr><td>destination_host_name_alias</td>
		<td>The alias we will use in our ssh user@hostname command-line
		for connecting to the host behind the intermediate host.</td>
	</tr>
	<tr><td>intermediate_host_address</td>
		<td>The DNS or IP Address for you Bastion Host</td>
	</tr>
	<tr><td>nc -w 10 %h %p</td>
		<td>Refer the 'manpage' 
		<a href="http://www.openbsd.org/cgi-bin/man.cgi?query=nc&apropos=0&sektion=0&manpath=OpenBSD+Current&arch=i386&format=html">nc(1)</a></td>
	</tr>
	<tr><td>destination_host_address</td>
		<td>The final target host.</td>
	</tr>
</table>

## <a name="maintenance"></a> 2 Maintenance / Monitoring

Because Hippo is a thin-layer on top of git, many of it's commands
have equivalents in Hippo, as well as the standard Git command-line
still being relevant for interrogating, reviewing the Hippo 
repository. Simplified maintenance, monitoring include:

1. [Standardised](#standardised) Commits
2. A [Remote Repository](#remote)
3. [Review](#review) repository
4. [Flash](#flash) onto new host

### <a name="standardised"></a> 2.1 Standardised Commits

&#91;Ref: [git-config](http://www.kernel.org/pub/software/scm/git/docs/git-config.html "commit.template: Specify a file to use as the template for new commit messages")
]

Commit Templates provide a framework for consistent documentation to
be included with each commit. You can use git's built-in commit template 
functionality with hippo. 

First, create the template file - in this example: */etc/hippo-commit-template*

Then, set the commit template like this:

<!--(block|syntax("bash"))-->
$ sudo hippo config commit.template /etc/hippo-commit-template
<!--(end)-->

### <a name="remote"></a> 2.2 A Remote Repository

In a shared environment, we can't store the origin repository information
directly in the hippo repository, because different administrators may need a
different repository URL string. The easiest way around this, is to configure
the remote branches in the individual administrator gitconfigs instead. 

For example, file: __~/.gitconfig__:

<!--(block|syntax("bash"))-->
[branch "master"]
	remote = origin
	merge = refs/heads/master

[remote "origin"]
	url = aldo@remotehost:/path/to/repo
	fetch = +refs/heads/*:refs/remotes/origin/*
<!--(end)-->

### <a name="review"></a> 2.3 Inspect a hippo repository with git

&#91;Ref: [git-clone](http://www.kernel.org/pub/software/scm/git/docs/git-clone.html "Clone a repository into a new directory")
]

A Hippo repository is just a Git repo, with a bit of added structure. You can
check out a hippo repository using Git, and inspect or even modify the included
files and metadata log:

<!--(block|syntax("bash"))-->
git clone aldo@remotehost:repo
<!--(end)-->

### <a name="flash"></a> 2.4 Flash/Restore configuration

&#91;Ref: [git-clone](http://www.kernel.org/pub/software/scm/git/docs/git-clone.html "Clone a repository into a new directory")
]

Restore a configuration checked into Hippo onto a new system

<!--(block|syntax("bash"))-->
hippo clone aldo@remotehost:repo
<!--(end)-->
