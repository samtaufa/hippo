For our sample repository, we create a path that matches
our *local standard* repository configurations. 

<!--(block|syntax("bash"))-->
# mkdir -p /var/repos
# chown root:_hippo /var/repos
<!--(end)-->

## <a name="new"></a> Adding a New Repository

To add a new host to the repository

- Create the necessary path
- Push updates from the client

### Create the necessary path

Create the path, and then initialise the GIT repository within the path.

<!--(block|syntax("bash"))-->
# mkdir /var/repos/hostname.git
# cd /var/repos/hostname.git
# git init --bare --shared=group
<!--(end)-->

Note that the *--shared=group* uses the keyword *group*, not the
*group-name* used for the server user/group.

If you are new to Git, it will be useful to edit the repo
file ./description which is a short-line summary of the contents
of the repo. This is used in tools such as [GitWeb](../gitweb.html).

### Push updates from the client.

On the client host:

To get our data across from the client to the server, we *hippo push*

<!--(block|syntax("bash"))-->
$ hippo push username@server:/var/repos/hostname.git master
<!--(end)-->

