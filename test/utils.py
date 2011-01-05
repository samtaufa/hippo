import os


def touchtree(path, paths):
    fullpaths = [os.path.join(path, i) for i in paths]
    for i in fullpaths:
        touch(i)
    return fullpaths



def touch(path):
    head, tail = os.path.split(path)
    try:
        os.makedirs(head)
    except OSError, e:
        pass
    open(path, "w").close()

