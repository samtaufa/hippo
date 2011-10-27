## Multi-hop Transport

&#91; [ssh(1)](
http://www.openbsd.org/cgi-bin/man.cgi?query=ssh_config&sektion=5&arch=&apropos=0&manpath=OpenBSD+Current),
[ssh_config(5)](
http://www.openbsd.org/cgi-bin/man.cgi?query=ssh_config&sektion=5&arch=&apropos=0&manpath=OpenBSD+Current),
[SSH Productivity Tips](
http://blogs.perl.org/users/smylers/2011/08/ssh-productivity-tips.html)
]

You sometimes have hosts for which you want to maintain configuration versioning
(using Hippo) but the client cannot connect directly to your aggregate
repository (central-host.) 

To get our configuration files from the client to the final-destination, 
we must pass-through an intermediary/bastion host. We want to be able to copy 
the configuration from the client host through the intermediary.

<pre>
[ Client ] |---ssh---> [ Bastion ] >>---ssh---> [ Destination ]
</pre>

This guide discusses multi-hop ssh, where we
proxy the ssh transport through an intermediate (or bastion) host. 

1. [Configuration](#config)
2. [Verification](#verify)
3. [Shortcuts](#shortcut)

### <a name="config">1.</a> Configuration

Because we use git/hippo to push to a URL that is using SSH as 
the default transport, we can use SSH's aliasing and proxying
features to simplify our command-line, such that we can
*hippo push* updates to a URL that we are not directly connected
to. The SSH transport's *alias* is used to reference a tunneled
(proxied) connection through the bastion (intermediary) host.

We set up our SSH Alias (tunnel) such as in the following
configuration:

In your _~/.ssh/config_ file add a section as follows:

<!--(block|syntax("apache"))-->
Host DestinationAlias
	ProxyCommand ssh -Aq IntermediateHost nc -w 10 %h %p
	Hostname DestinationHost
    ForwardAgent no
    ForwardX11 no
<!--(end)-->

Where the above options are discussed below:

<table>
	<tr><th>Config Entry</th>
		<th>More Information</th>
	</tr>
	<tr><td>DestinationAlias</td>
		<td>The alias we will use in our ssh user@hostname command-line
		for connecting to the host behind the intermediate host.</td>
	</tr>
	<tr><td>IntermediateHost</td>
		<td>The DNS or IP Address for you Bastion Host</td>
	</tr>
	<tr><td>nc -w 10 %h %p</td>
		<td>The <a href="http://www.openbsd.org/cgi-bin/man.cgi?query=nc&sektion=1">nc(1)</a>
            (or <strong>netcat</strong>) 
        </td>
        
	</tr>
	<tr><td>DestinationHost</td>
		<td>The final target host.</td>
	</tr>
</table>

With the [OpenSSH 5.4](http://marc.info/?l=openssh-unix-dev&m=126801438509606&w=2) release,
OpenSSH provides the -W 'netcat mode' to 'route connections via intermediate servers.

<!--(block|syntax("apache"))-->
Host DestinationAlias
	ProxyCommand ssh -W %h:%p IntermediateHost
	Hostname DestinationHost
    ForwardAgent no
    ForwardX11 no
<!--(end)-->

### <a name="verify">2.</a> Verification

We can now confirm (and accept ssh prompts) to the above hosts with standard
ssh connections:

-   make sure we can connect to the *IntermediateHost*
-   on the  *IntermediateHost*, make sure you can connect to the *DestinationHost*

<!--(block|syntax("bash"))-->
$ ssh -Aq IntermediateHost
<!--(end)-->
<pre class="screen-output">

Welcome ...
</pre>

Verify that the connection is successful on the  *IntermediateHost*.

From the  *IntermediateHost*, verify the connection is successful to
the destination host:

<!--(block|syntax("bash"))-->
$ ssh DestinationHost
<!--(end)-->
<pre class="screen-output">

Welcome ...
</pre>

The above verifies that the steps from our client to the 
destination host, is succesfully stepped through.

-   make sure we can connect to the *DestinationHost* directly
    (with ProxyCommand creating a through tunnel for us)

<!--(block|syntax("bash"))-->
$ ssh DestinationAlias
<!--(end)-->

If things work correctly, you should get a prompt that this is a 
new host, and whether to accept the host ssh signature.

Accept, and you can now push or pull to the destination host, using the 
assigned shortcut name.

<!--(block|syntax("bash"))-->
$ hippo push DestinationAlias:repo_path master
<!--(end)-->

<table>
	<tr><th>Command-Line Entry</th>
		<th>More Information</th>
	</tr>
	<tr><td>repo_path</td>
		<td>The full path on the remote host to the repository</td>
	</tr>
</table>

### <a name="shortcut">3.</a> Shortcut

The above example show that we have to explicitly enter the full repository
path (for the GIT/Hippo repo) at the destination host. This can lead to
a number of typing errors if you are versioning a large number of hosts.
Fortunately, Git's [shortcuts](shortcuts.html] facility allows the transport 
(which by default we're using SSH) to resolve the URL. We can use this
to standardise our command-line for all hosts.

File extract: ~/.gitconfig

<pre class="config-file">

[branch "master"]
    remote = origin
    merge = refs/heads/master
    
[remote "origin"]
    url = DestinationAlias:repo_path
    fetch = +refs/heads/*:refs/remotes/origin/*
</pre>

The *DestinationAlias* is resolved by *SSH* using *~.ssh/config* and we can
now use the same command-line on all hosts to [push](workflow.html#push) updates
to the central repository.

<!--(block|syntax("bash"))-->
$ hippo push origin master
<!--(end)-->
