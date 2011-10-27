
As Hippo is based on GIT, your *Central Repository* may be multiple
hosts, or if you are running a small site, distribute your
repository amongst your servers or a workstation.

Installing/configuring the **Central Repository** involves the following:

- Host [User Group](#group)
- Repository [Path](server/repository.html#path)
- Adding a [New Repository](server/repository.html#new)

## <a name="group"></a> Host User Group

We set up a host 'group' for users with read/write access to the
Hippo Repository: for our example *_hippo*.

Members of this group will include all administrators
pushing updates to the repositories.

On OpenBSD you will do something such as the below:

<!--(block|syntax("bash"))-->
# group add _hippo
# usermod -G _hippo samt
# usermod -G _hippo charlie
<!--(end)-->
