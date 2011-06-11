import os, time, sys, subprocess
import git
import utils, meta

HIPPO_DIR = "/var/hippo"
HIPPO_BASE = "/"

COMMANDS = [
    "init", "add", "commit", "clone", "status", "rm", "mv",
    "log", "refresh", "show", "push", "checkout", "diff", "remote", "config"
]

class Hippo:
    """
        Hippo is essentially a thin layer over the top of the git command-line
        tool. At the moment, we support a small sensible subset of the git
        command repertoire, but we plan to expand that to 

        The hippo repository directory structure looks like this:

            /var/hippo/manifest
            /var/hippo/.git
    """
    def __init__(self, datadir, base):
        self.datadir, self.base = datadir, base
        self.gitdir = os.path.join(self.datadir, ".git")
        self.manifest = os.path.join(self.datadir, "manifest")

    def repo(self):
        """
            Return a gitpython repo object.
        """
        return git.Repo(self.gitdir)

    def refresh_manifest(self):
        r = self.repo()

        paths = set()

        # Now look at the files in the index, which may not be committed yet
        for (path, stage), entry in r.index.entries.iteritems(): 
            for i in utils.allpaths(os.path.join(self.base, path)):
                paths.add(i)

        m = meta.Metadata()

        data = m.make_manifest(paths)
        f = open(self.manifest, "w")
        f.write(data)
        f.close()

    def apply_manifest(self):
        data = open(self.manifest).read()
        m = meta.Metadata()
        m.apply_manifest(data)

    def _git(self):
        os.environ["GIT_WORK_TREE"] = self.base
        os.environ["GIT_DIR"] = os.path.join(self.datadir, ".git")
        return git.Git(self.base)

    # Commands
    def init(self, args):
        g = self._git()
        utils.touch(self.manifest)
        g.init()
        g.add(self.manifest)

    def add(self, args):
        g = self._git()
        g.add(*args)

    def commit(self, args):
        self.refresh_manifest()
        # We invoke git directly with Popen, because git-python has no
        # mechanism to return interactive controll to the user so we can use
        # the editor.
        os.environ["GIT_WORK_TREE"] = self.base
        os.environ["GIT_DIR"] = os.path.join(self.datadir, ".git")
        tail = ""
        if args:
            tail = " " + " ".join(args)
        p = subprocess.Popen(
            "git commit" + tail,
            shell=True
        )
        p.wait()

    def _cmd(self, cmd, args):
        g = self._git()
        print getattr(g, cmd)(*args),

    #
    # hippo commands
    # 
    def refresh(self, args):
        self.refresh_manifest()

    #
    # git commands
    #

    # begin nocover
    def status(self, args):
        # Suppress untracked files display. Eventually, we should re-implement
        # this to make the status command output nicer.
        self.refresh_manifest()
        args.append("-uno")
        self._cmd("status", args)

    def log(self, args):
        self._cmd("log", args)

    def diff(self, args):
        self.refresh_manifest()
        self._cmd("diff", args)

    def show(self, args):
        self._cmd("show", args)

    def push(self, args):
        self._cmd("push", args)

    def remote(self, args):
        self._cmd("remote", args)

    def config(self, args):
        self._cmd("config", args)

    # end nocover

    def rm(self, args):
        self._cmd("rm", args)

    def mv(self, args):
        self._cmd("mv", args)

    def checkout(self, args):
        self._cmd("checkout", args)
        self.apply_manifest()

    def clone(self, args):
        self._cmd("clone", args)
        self.apply_manifest()
