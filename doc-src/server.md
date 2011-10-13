Installing/configuring the **Central Repository** involves the following:

- Host [User Group](#group)
- Repository [Path](#path)
- Adding a [New Repository](#new)

### <a name="group"></a> Host User Group

Set up a host 'group' for our example *hippo*.

Members of this group will include all administrators
pushing updates to the repositories. For example,
a group called *hippo* will have at least your name?

<!--(block|syntax("bash"))-->
# group add _hippo
# usermod -G _hippo samt
# usermod -G _hippo charlie
<!--(end)-->

### <a name="path"></a> Repository Path

For our sample repository, we create a path that matches
our *local standard* repository configurations. 

<!--(block|syntax("bash"))-->
# mkdir -p /var/repos
# chown root:_hippo /var/repos
<!--(end)-->

### <a name="new"></a> Adding a New Repository

To add a new host to the repository

- Create the necessary path
- Push updates from the client

#### Create the necessary path

Create the path, and then initialise the GIT repository within the path.

<!--(block|syntax("bash"))-->
# mkdir /var/repos/hostname.git
# cd /var/repos/hostname.git
# git init --bare --shared=group
<!--(end)-->

Note that the *--shared=group* uses the keyword *group*, not the
*group-name* used for the server user/group.

#### Push updates from the client.

On the client host:

To get our data across from the client to the server, we *hippo push*

<!--(block|syntax("bash"))-->
$ hippo push username@server:/var/repos/hostname.git master
<!--(end)-->

