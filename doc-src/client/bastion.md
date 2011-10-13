&#91;<a name="ssh">1.5 Multi-hop SSH</a>]

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
