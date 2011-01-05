import libpry
from libhippo import utils



class uAllpaths(libpry.AutoTree):
    def test_all(self):
        expected = ["/var", "/var/log", "/var/log/messages"]
        assert utils.allpaths("/var/log/messages") == expected


        expected = ["var", "var/log", "var/log/messages"]
        assert utils.allpaths("var/log/messages") == expected

        expected = ["var"]
        assert utils.allpaths("var") == expected

        expected = []
        assert utils.allpaths("/") == expected



tests = [
    uAllpaths(),
]
