# All operations supported in Server side
import os
from stat import *

class Func:

    # Filesystem methods
    # ==================
    def dfs_access(self, path, mode):
        # access - check real user's permissions for a file
        # http://linux.die.net/man/2/access
        path = os.getcwd() + '/file.txt'
        print os.access(path, os.F_OK)

    def dfs_chmod(self, path, mode):
        # chmod - change the mode of path to numeric mode
        # https://docs.python.org/2/library/os.html#os.chmod
        path = os.getcwd() + '/tempfile.txt'
        mode = S_IRUSR
        print os.chmod(path, mode)

    def dfs_chown(self, path, uid, gid):
        # chown - change the owner and group id of path to the numeric id and gid
        # path = os.getcwd() + '/file.txt'
        # uid = 1
        # gid = 1
        # os.chown(path, uid, gid)

    def dfs_getattr(self, path):
        # getattr - return the value of the named attribute of the file
        f = open(os.getcwd() + '/file.txt')
        filename = getattr(f, "name")
        # filetype = getattr(f, "__doc__")
        print filename
        # print filetype
        print ST_GID
        # print dir()

    def dfs_readdir(self, path):
        # readdir - Return a list containing the names of the entries in the directory given by path
        print os.listdir(os.getcwd())

    def dfs_readlink(self, path):
        # readlink - Return a string representing the path to which the symbolic link points.
        src = '/usr/bin/python'
        path = '/tmp/python'
        # lrwxr-xr-x  1 chen  wheel  15 Apr  2 16:38 /tmp/python -> /usr/bin/python
        # create a symbolic link on python in tmp directory
        # os.symlink(src, dst)
        path = os.readlink(path)
        print path

    def mknod(self, path)

def main():
    Func.def_access("", os.F_OK)
