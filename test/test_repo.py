import os
import libpry
from libhippo import repo
import utils



class uRepo(libpry.AutoTree):
    def _mkrepo(self):
        t = self.tmpdir()
        paths = utils.touchtree(
            t, 
            [
                "one",
                "dir/two",
            ]
        )
        r = repo.Hippo(
            os.path.join(t, "hippo"),
            t,
        )
        r.init([])
        r.add(["one"])
        r.add(["dir/two"])
        r.commit(["-q", "-a", "-m", "testing"])
        return r

    def test_init(self):
        r = self._mkrepo()
        r.refresh([])
        r.checkout(["-q", "master"])

    def test_file_move(self):
        r = self._mkrepo()
        r.mv(["dir/two", "dir/three"])
        r.commit(["-q", "-a", "-m", "testing"])

    def test_rm(self):
        r = self._mkrepo()
        r.rm(["-q", "dir/two"])
        r.commit(["-q", "-a", "-m", "testing"])

        gr = r.repo()
        lst = []
        for i in gr.head.commit.tree.traverse():
            lst.append(i.path)
        assert not "dir/two" in lst



tests = [
    uRepo()
]

