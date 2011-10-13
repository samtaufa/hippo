In a shared environment, we can't store the origin repository information
directly in the hippo repository, because different administrators may need a
different repository URL string. The easiest way around this, is to configure
the remote branches in the individual administrator gitconfigs instead. 

For example, file: __~/.gitconfig__:

<pre class="config-file">
[branch "master"]
	remote = origin
	merge = refs/heads/master

[remote "origin"]
	url = aldo@remotehost:/path/to/repo
	fetch = +refs/heads/*:refs/remotes/origin/*
</pre>

With the above configuration, you can connect to each host and simply
use:

<!--(block|syntax("bash"))-->
$ hippo push origin master
<!--(end)-->

This *~/.gitconfig* change simplifies maintenance significantly, 
because each site can be *backed-up* with the same command-line 
instruction.

