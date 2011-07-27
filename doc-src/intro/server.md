# Server Configuration

Installing/configuring the **Central Repository** involves the following:

- Host [User Group](#group)
- Repository [Path](#path)
- Adding a [New Repository](#new)

### <a name="group"></a> Host User Group

Set up a host 'group' for our example *hippo*.

Members of this group will include all administrators
pushing updates to the repositories. For example,
a group called *hippo* will have at least your name?

### <a name="path"></a> Repository Path

For our sample repository, we create a path that matches
our standard repository configurations. 

<!--(block|syntax("bash"))-->
# mkdir -p /var/data/repos
# chown root:hippo /var/data/repos
<!--(end)-->

### <a name="new"></a> Adding a New Repository

To add a new host to the repository

- Create the necessary path

<!--(block|syntax("bash"))-->
# mkdir /var/data/repos/hostname.git
# cd /var/data/repos/hostname.git
# git init --bare --shared=group
<!--(end)-->

On the client host:

To get our data across from the client to the server, we *hippo push*

<!--(block|syntax("bash"))-->
$ hippo push username@server:/var/data/repos/hostname.git master
<!--(end)-->

