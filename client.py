# https://www.stavros.io/posts/python-fuse-filesystem/
#!/usr/bin/env python

from __future__ import with_statement

import os
import sys
import errno
import subprocess
import socket

from common import *
from protocol import *
from fuse import FUSE, FuseOSError, Operations

sock = -1

class Passthrough(Operations):
    # Filesystem methods
    # ==================

    def access(self, path, mode):
        print("access")
        if not send_and_recv(sock, DFS_ACCESS, [path, mode]):
            raise FuseOSError(errno.EACCES)

    def chmod(self, path, mode):
        print("chmod")
        return send_and_recv(sock, DFS_CHMOD, [path, mode])

    def chown(self, path, uid, gid):
        print("chown")
        return send_and_recv(sock, DFS_CHOWN, [path, uid, gid])

    def getattr(self, path, fh=None):
        print("getattr")
        ret = send_and_recv(sock, DFS_GETATTR, [path, fh])
        if ret == False:
            raise FuseOSError(errno.ENOENT)
        return ret
        
    def readdir(self, path, fh):
        print("readdir");
        return send_and_recv(sock, DFS_READDIR, [path, fh])

    def readlink(self, path):
        print("readlink")
        return send_and_recv(sock, DFS_READLINK, [path])

    def mknod(self, path, mode, dev):
        print("mknod")
        return send_and_recv(sock, DFS_MKNOD, [path, mode, dev])

    def rmdir(self, path):
        print("rmdir")
        return send_and_recv(sock, DFS_RMDIR, [path])

    def mkdir(self, path, mode):
        print("mkdir")
        return send_and_recv(sock, DFS_MKDIR, [path, mode])

    def statfs(self, path):
        print("statfs")
        return send_and_recv(sock, DFS_STATFS, [path])

    def unlink(self, path):
        print("unlink")
        return send_and_recv(sock, DFS_UNLINK, [path])

    def symlink(self, name, target):
        print("symlink")
        return send_and_recv(sock, DFS_SYMLINK, [name, path])

    def rename(self, old, new):
        print("rename")
        return send_and_recv(sock, DFS_RENAME, [old, new])

    def link(self, target, name):
        print("link")
        return send_and_recv(sock, DFS_LINK, [target, name])

    def utimens(self, path, times=None):
        print("utimes")
        return send_and_recv(sock, DFS_UTIMENS, [path, times])

    # File methods
    # ============

    def open(self, path, flags):
        print("open")
        return send_and_recv(sock, DFS_OPEN, [path, flags])

    def create(self, path, mode, fi=None):
        print("create")
        return send_and_recv(sock, DFS_CREATE, [path, mode, fi])

    def read(self, path, length, offset, fh):
        print("read")
        return send_and_recv(sock, DFS_READ, [path, length, offset, fh])

    def write(self, path, buf, offset, fh):
        print("write")
        return send_and_recv(sock, DFS_WRITE, [path, buf, offset, fh])

    def truncate(self, path, length, fh=None):
        print("truncate")
        return send_and_recv(sock, DFS_TRUNCATE, [path, length, fh])

    def flush(self, path, fh):
        print("flush")
        return send_and_recv(sock, DFS_FLUSH, [path, fh])

    def release(self, path, fh):
        print("release")
        return send_and_recv(sock, DFS_RELEASE, [path, fh])

    def fsync(self, path, fdatasync, fh):
        print("fsync")
        return send_and_recv(sock, DFS_FSYNC, [path, fdatasync, fh])

def main(mountpoint):
    # Create a socket for communication with the server
    global sock
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((HOST, M_PORT))
    
    # Create mountpoint and directory to mount if they do not exist.
    # We plan to bypass the mounting requirement of FUSE by creating a
    # dummy mount point and mount root.
    if not os.path.exists(mountpoint):
        print("Directory ", mountpoint, "does not exist. Creating it")
        os.mkdir(mountpoint)

    FUSE(Passthrough(), mountpoint, nothreads=True, foreground=True)

    sock.close()

if __name__ == '__main__':
    main(sys.argv[1])