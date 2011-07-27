# Installation

Hippo installation is straight forward, with few dependencies that 
can be installed using standard packages for your System
of choice.

The major dependencies to get Hippo working are:

-	[Python](#python) 2.5, 2.6, 2.7
-   [Git](#git) v1.7.1 or later.
-   [GitPython](#gitpython) v0.3 or later
	* [setuptools](http://pypi.python.org/pypi/setuptools) 0.6c11 or later

Then of course, the installation of Hippo itself.

- hippo

## <a name="python"></a> Python

Hippo works happily using Python 2.6, 2.7. Other versions may
also be compatible.

Install the [Python of Choice](http://www.python.org) for your host.

## <a name="git"></a> Git

&#91;Ref: [Git Community Book - Installing Git](http://book.git-scm.com/2_installing_git.html)
]

Install Git v1.7.1 or later for your platform from the [Git Pages](http://git-scm.com/)

Git is a free & open source, distributed version control system designed 
to handle everything from small to very large projects with speed and 
efficiency.

Every Git clone is a full-fledged repository with complete history and full 
revision tracking capabilities, not dependent on network access or a 
central server. Branching and merging are fast and easy to do.

### Setup and Initialisation

&#91;Ref: [Pro Git: Getting Started](http://progit.org/book/ch1-5.html) ]

For the new Git user, a few house-keeping things are useful for shared 
administration environments to ease tracking of who commits changes
to the Hippo repository.  If you haven't already configured your Git
environment, keep a reference handy such as: [A tour of git: the basics](http://cworth.org/hgbook-git/tour/)
or [Git Community Book: Setup and Initialization](http://book.git-scm.com/2_setup_and_initialization.html) 
and configure Git such as the below example:

<!--(block|syntax("bash"))-->
$ git config --global user.name "Your Name"
$ git config --global user.email "you@example.com"
<!--(end)-->
 
Which should update/create your standard Git configuration file, usually
stored at ~/.gitconfig.

If your configuration is sane, you should get a sane result from the below
command-line

<!--(block|syntax("bash"))-->
$ git config user.name
<!--(end)-->


## <a name="gitpython"></a> GitPython

Install [GitPython](https://github.com/gitpython-developers/GitPython) v0.3 or later.

__On most Unix-like systems, you'll probably need to run these commands as root or using sudo__

Install GitPython using setuptools/distribute

<!--(block | syntax("bash"))-->
$ sudo easy_install GitPython
<!--(end)-->

Or pip:

<!--(block | syntax("bash"))-->
$ sudo pip install GitPython
<!--(end)-->

### Source Install

If the above doesn't work for you, the following
are the dependencies for a source install. Obviously, if you can install any of
the dependencies from your OS binary packages, then that may be preferable for
compatability, maintenance.

The following procedures install immediate dependencies, and GitPython.

-   GitDB 
-   async
-	setuptools
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

#### setuptools

The GitPython installation process is dependent on setuptools.

Download the [source](http://pypi.python.org/pypi/setuptools#files) and
install per software configuration.

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

## Hippo

&#91;Ref: [https://github.com/cortesi/hippo)](https://github.com/cortesi/hippo)]

Install Hippo from the source at [github.com](https://github.com/cortesi/hippo)

<!--(block | syntax("bash"))-->
$ cd /path-to-my-local-src
$ git clone https://github.com/cortesi/hippo.git
$ cd hippo
$ sudo python setup.py install
<!--(end)-->
