"""
    This module captures and applies file metadata. We assume, for the moment,
    that all filenames are ascii, with no special characters.
"""
import os, stat, pwd, grp

class Metadata:
    def mode_to_str(self, mode):
        """
            Returns a string representation of a numeric mode. This is an
            abbreviated form the the mode specification output.
        """
        m = [
            "r" if mode&stat.S_IRUSR else "-",
            "w" if mode&stat.S_IWUSR else "-",
            "x" if mode&stat.S_IXUSR else "-",

            "r" if mode&stat.S_IRGRP else "-",
            "w" if mode&stat.S_IWGRP else "-",
            "x" if mode&stat.S_IXGRP else "-",

            "r" if mode&stat.S_IROTH else "-",
            "w" if mode&stat.S_IWOTH else "-",
            "x" if mode&stat.S_IXOTH else "-",
        ]
        if mode&stat.S_ISUID:
            if mode&stat.S_IXUSR:
                m[2] = "s"
            else:
                m[2] = "S"
        if mode&stat.S_ISGID:
            if mode&stat.S_IXGRP:
                m[5] = "s"
            else:
                m[5] = "S"
        if mode&stat.S_ISVTX:
            if mode&stat.S_IXOTH:
                m[8] = "t"
            else:
                m[8] = "T"
        return "".join(m)

    def str_to_mode(self, s):
        """
            Returns a numeric mode, generated from a string.
        """
        m = 0
        if s[0] != "-": m |= stat.S_IRUSR
        if s[1] != "-": m |= stat.S_IWUSR
        if s[2] in ["x", "s"]:
            m |= stat.S_IXUSR
        if s[2] in ["s", "S"]:
            m |= stat.S_ISUID
            
        if s[3] != "-": m |= stat.S_IRGRP
        if s[4] != "-": m |= stat.S_IWGRP
        if s[5] in ["x", "s"]:
            m |= stat.S_IXGRP
        if s[5] in ["s", "S"]:
            m |= stat.S_ISGID

        if s[6] != "-": m |= stat.S_IROTH
        if s[7] != "-": m |= stat.S_IWOTH
        if s[8] in ["x", "t"]:
            m |= stat.S_IXOTH
        if s[8] in ["t", "T"]:
            m |= stat.S_ISVTX
        return m

    def get_owner(self, path):
        s = os.stat(path)
        username = pwd.getpwuid(s.st_uid).pw_name
        group = grp.getgrgid(s.st_gid).gr_name
        return username, group

    def set_owner(self, path, username, group):
        if (username, group) != self.get_owner(path):
            # begin nocover
            uid = pwd.getpwnam(username).pw_uid
            gid = grp.getgrnam(group).gr_gid
            os.chown(path, uid, gid)
            # end nocover
    
    def get_metadata(self, path):
        """
            Returns a string representation of the file metadata.
        """
        s = os.stat(path)
        return self.mode_to_str(s.st_mode)

    def set_metadata(self, path, meta):
        """
            Applies a string metadata specification to a file.
        """
        # We compare metadata representations rather than modes, because we
        # want to ignore things like directory and device flags in the
        # comparison.
        if self.get_metadata(path)!= meta:
            mode = self.str_to_mode(meta)
            os.chmod(path, mode)

    def make_manifest(self, paths):
        parts = []
        for i in sorted(paths):
            u, g = self.get_owner(i)
            l = "%s %s %s %s"%(self.get_metadata(i), u, g, i)
            parts.append(l)
        return "\n".join(parts)

    def parse_manifest(self, data):
        paths = []
        for i in data.splitlines():
            mode, user, group, path = i.split(" ", 3)
            paths.append((path, mode, user, group))
        return paths

    def apply_manifest(self, data):
        paths = self.parse_manifest(data)
        for i in paths:
            self.set_metadata(i[0], i[1])
            self.set_owner(i[0], i[2], i[3])


