import os

def touch(path):
    head, tail = os.path.split(path)
    os.makedirs(head)
    open(path, "w").close()


def allpaths(path):
    """
        Returns a list of all component directories for a given path. For
        "/var/log/messages", we return the list ["/var", "/var/log",
        "/var/log/messages"]. Note we always exclude the root directory.
    """
    lst = []
    current = ""
    for i in path.split(os.path.sep):
        if i:
            current = current + "/" + i
            if path[0] == os.path.sep:
                lst.append(current)
            else:
                lst.append(current[1:])
    return lst


