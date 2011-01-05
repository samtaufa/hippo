import random, stat, os
import libpry
from libhippo import meta
import utils


class uFile(libpry.AutoTree):
    def test_mode_to_str(self):
        m = meta.Metadata()
        modes = [
            stat.S_ISUID,
            stat.S_ISGID,
            stat.S_ISVTX,

            stat.S_IRUSR,
            stat.S_IWUSR,
            stat.S_IXUSR,

            stat.S_IRGRP,
            stat.S_IWGRP,
            stat.S_IXGRP,

            stat.S_IROTH,
            stat.S_IWOTH,
            stat.S_IXOTH,
        ]
        for i in modes:
            s = m.mode_to_str(i)
            assert m.str_to_mode(s) == i

        for i in range(100):
            n = random.randint(0, len(modes))
            mode = 0
            for i in range(n):
                mode |= random.choice(modes)
                
            s = m.mode_to_str(mode)
            assert m.str_to_mode(s) == mode

    def test_getset_metadata(self):
        m = meta.Metadata()
        md = m.get_metadata("files/one")
        assert md == "r--------"

        d = self.tmpdir()
        p = os.path.join(d, "test")
        utils.touch(p)

        assert m.get_metadata(p) != md
        m.set_metadata(p, md)
        assert m.get_metadata(p) == md

    def test_make_manifest(self):
        m = meta.Metadata()
        paths = utils.touchtree(
            self.tmpdir(),
            [
                "one",
                "dir1/one",
                "dir1/two",
                "dir2/one",
                "dir2/dir3/one",
            ]
        )

        man = m.make_manifest(paths)
        assert m.parse_manifest(man)

        os.chmod(paths[0], 0)
        assert m.make_manifest(paths) != man

        m.apply_manifest(man)
        assert m.make_manifest(paths) == man

    def test_getset_owner(self):
        m = meta.Metadata()
        o = m.get_owner("files/one")
        m.set_owner("files/one", *o)



tests = [
    uFile()
]
        

