Because Hippo is a thin-layer on top of git, many of it's commands
have equivalents in Hippo, as well as the standard Git command-line
still being relevant for interrogating, reviewing the Hippo 
repository. Simplified maintenance, monitoring include:

1. [Review](#review) repository
2. [Standardised](#standardised) Commits
3. [Flash](#flash) onto new host


## <a name="review"></a> 1. Review Repository

&#91;Ref: [git-clone](http://www.kernel.org/pub/software/scm/git/docs/git-clone.html "Clone a repository into a new directory")
]

A Hippo repository is just a Git repo, with a bit of added structure. You can
check out a hippo repository using Git, and inspect or even modify the included
files and metadata log:

<!--(block|syntax("bash"))-->
git clone aldo@remotehost:repo
<!--(end)-->

## <a name="standardised"></a> 2. Standardised Commits

&#91;Ref: [git-config](http://www.kernel.org/pub/software/scm/git/docs/git-config.html "commit.template: Specify a file to use as the template for new commit messages")
]

Commit Templates provide a framework for consistent documentation to
be included with each commit. You can use git's built-in commit template 
functionality with hippo. 

First, create the template file - in this example: */etc/hippo-commit-template*

Then, set the commit template like this:

<!--(block|syntax("bash"))-->
$ sudo hippo config commit.template /etc/hippo-commit-template
<!--(end)-->

## <a name="flash"></a> 3. Flash/Restore configuration

&#91;Ref: [git-clone](http://www.kernel.org/pub/software/scm/git/docs/git-clone.html "Clone a repository into a new directory")
]

Restore a configuration checked into Hippo onto a new system

<!--(block|syntax("bash"))-->
hippo clone aldo@remotehost:repo
<!--(end)-->
