## Installation Sequence

Dependencies

-   [Git](#git) v1.7.1 or later.
-   [GitPython](#gitpython) v0.3 or later

Base System

- hippo

<a name="git"></a>

### GIT

Install GIT v1.7.1 or later for your platform from the [GIT Pages](http://git-scm.com/)

Git is a free & open source, distributed version control system designed 
to handle everything from small to very large projects with speed and 
efficiency.

Every Git clone is a full-fledged repository with complete history and full 
revision tracking capabilities, not dependent on network access or a 
central server. Branching and merging are fast and easy to do.

<a name="gitpython"></a>

### GitPython

Install [GitPython](http://gitorious.org/git-python) v0.3 or later. You
should be able to use 


__On most Unix-like systems, you'll probably need to run these commands as root or using sudo__

Install GitPython using setuptools/distribute

<!--(block | syntax("bash"))-->
$ sudo easy_install GitPython
<!--(end)-->

Or pip:

<!--(block | syntax("bash"))-->
$ sudo pip install GitPython
<!--(end)-->

Or, if you do not have setuptools/distribute installed, use the download link
to download the source package, and install it in the normal fashion. The
following procedures install GitPython and immediate dependencies.

-   GitDB 
-   async
-   GitPython

#### GitDB 

[GitDB](https://github.com/gitpython-developers/gitdb) 
allows you to access bare git repositories for reading and writing. 
It aims at allowing full access to loose objects as well as packs with 
performance and scalability in mind. It operates exclusively on streams, 
allowing to operate on large objects with a small memory footprint.

<!--(block | syntax("bash"))-->
$ cd /path-to-my-local-src
$ git clone git://github.com/gitpython-developers/gitdb.git
$ cd gitdb
$ sudo python setup.py install
<!--(end)-->

#### async

[Async](https://github.com/gitpython-developers/async) aims to make 
writing asyncronous processing easier. It provides a task-graph with 
interdependent tasks that communicate using blocking channels, allowing 
to delay actual computations until items are requested. Tasks will automatically 
be distributed among 0 or more threads for the actual computation.

<!--(block | syntax("bash"))-->
$ cd /path-to-my-local-src
$ git clone git://github.com/gitpython-developers/async.git
$ cd async
<!--(end)-->

Review whether the following diff applies:

<!--(block | syntax("bash"))-->
diff --git a/setup.py b/setup.py
--- a/setup.py
+++ b/setup.py
@@ -76,7 +76,7 @@ setup(cmdclass={'build_ext':build_ext_nofail},
       url = "http://gitorious.org/git-python/async",
       packages = ('async', 'async.mod', 'async.test', 'async.test.mod'),
       package_dir = {'async':'async'},
-      ext_modules=[Extension('async.mod.zlib', ['async/mod/zlibmodule.c'])],
+      ext_modules=[Extension('async.mod.zlib', ['async/mod/zlibmodule.c'], libraries=["z"])],
       license = "BSD License",
       zip_safe=False,
       long_description = """Async is a framework to process interdependent tasks in a pool of workers"""
<!--(end)-->

Modify the setup.py file as appropriate and install.

<!--(block | syntax("bash"))-->
$ sudo python setup.py install
<!--(end)-->

#### GitPython

[GitPython](https://github.com/gitpython-developers/gitpython) is a python
library used to interact with git repositories, high-level like git-porcelain, or 
low-level like git-plumbing.

<!--(block | syntax("bash"))-->
$ cd /path-to-my-local-src
$ git clone git://github.com/gitpython-developers/GitPython.git
$ cd GitPython
$ sudo python setup.py install
<!--(end)-->

### Hippo

Install Hippo from the source at [github.com](https://github.com/cortesi/hippo)

<!--(block | syntax("bash"))-->
$ cd /path-to-my-local-src
$ git clone https://github.com/cortesi/hippo.git
$ cd hippo
$ sudo python setup.py install
<!--(end)-->
