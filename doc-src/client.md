On the client, we use Hippo to *'version/backup'* configuration
files into a [Git Repository](client/git.html). With hippo, we can then put a copy 
onto another machine as a precaution (i.e. we want a current versioned 
copy of the configuration on another machine for the event when 
this client dies and we want to rebuild it.)

Most Hippo commands are identical to their Git equivalents, and Hippo needs
root privileges to perform the majority of its functions (and is thus often
executed as root or with sudo.)

Basic preparations of Hippo are:

- [Initialise](#initialise) the new host hippo repository
- [Configure](#configure) git

After which the client is ready for work:

- [Basic Workflow](client/workflow.html)
- [Shortcuts](client/shortcuts.html)
- [Bastion](client/bastion.html)
- [Git](client/git.html)
- [Restore](client/restore.html)

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

## <a name="configure"></a> Configure git

&#91;Ref: [git-config](http://www.kernel.org/pub/software/scm/git/docs/git-config.html "Create an empty git repository or reinitialize an existing one")
]

It is a good idea, at the beginning, to configure Git, with attention to
at least telling git (and as a by-product, hippo) who you are so this
can be detailed in the version message log.

<!--(block|syntax("bash"))-->
$ git --global user.email aldo@example.com
$ git --global user.name Aldo Cortesi
<!--(end)-->
