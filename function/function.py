# All operations supported in Server side
import os, stat
from stat import *

class Func:
    def __init__(self, name):
        self.name = name;

    # Filesystem methods
    # ==================

    # access - check real user's permissions for a file
    # http://linux.die.net/man/2/access
    def dfs_access(self, path, mode):
        print 'access'
        return os.access(path, mode)

    # chmod - change the mode of path to numeric mode
    # https://docs.python.org/2/library/os.html#os.chmod
    # Mode: http://www.tutorialspoint.com/python/os_chmod.htm
    def dfs_chmod(self, path, mode):
        print 'chmod'
        return os.chmod(path, mode)

    # chown - change the owner and group id of path to the numeric id and gid
    def dfs_chown(self, path, uid, gid):
        print 'chown'
        return os.chown(path, uid, gid)

    # getattr - return the value of the named attribute of the file
    def dfs_getattr(self, path, attr):
        print 'getattr'
        st = os.lstat(os.getcwd() + '/file.txt')
        return dict((key, getattr(st, key)) for key in ('st_mode', 'st_ino', 'st_dev', 'st_nlink', 'st_uid', 'st_gid', 'st_size', 'st_atime', 'st_mtime', 'st_ctime'))

    # readdir - Return a list containing the names of the entries in the directory given by path
    def dfs_readdir(self, path):
        print 'readdir'
        dirents = ['.', '..']
        dirents.extend(os.listdir(path))
        for r in dirents:
            yield r
        # return an object ['.', '..', 'file.txt', 'function.py', 'tempfile.txt']

    # readlink - Return a string representing the path to which the symbolic link points.
    # src = '/usr/bin/python'
    # path = '/tmp/python'
    # lrwxr-xr-x  1 chen  wheel  15 Apr  2 16:38 /tmp/python -> /usr/bin/python
    # create a symbolic link on python in tmp directory
    # os.symlink(src, dst)
    def dfs_readlink(self, path):
        print 'readlink'
        path = os.readlink(path)
        print path

    def dfs_symlink(self, name, target):
        print 'symlink'
        return os.symlink(name, target)
        
    def dfs_unlink(self, path):
        print 'unlink'
        return os.unlink(path)


    # Create a filesystem node (file, device special file or named pipe) named filename. 
    # filename = '/tmp/tmpfile'
    # mode = 0600|stat.S_IRUSR
    # filesystem node specified with different modes
    def dfs_mknod(self, filename, mode):
        print 'mknod'
        os.mknod(filename, mode)

    def dfs_mkdir(self, path, mode):
        print("mkdir")
        return os.mkdir(path, mode)

    # Remove (delete) the directory path.
    def dfs_rmdir(self, path):
        print 'rmdir'
        return os.rmdir(path);

    # Return file system parameters, like fs block size, # of blocks
    # https://docs.python.org/2/library/statvfs.html
    def dfs_statfs(self, path):
        print 'statfs'
        stv = os.statvfs(path)
        return dict((key, getattr(stv, key)) for key in ('f_bsize', 'f_frsize', 'f_blocks', 'f_bfree', 'f_bavail', 'f_files', 'f_ffree', 'f_favail', 'f_flag', 'f_namemax'))

    def dfs_rename(self, old, new):
        print 'rename'
        return os.rename(old, new)

    # The method link() creates a hard link pointing to src named dst.
    def dfs_link(self, old, new):
        print 'link'
        return os.link(old, new)

    # The method utime() sets the access and modified times of the file specified by path.
    def dfs_utime(self, path, times=None):
        print 'utime'
        return os.utime(path, times)

    # File methods
    # ============

    # opens the file file and set various flags according to flags and possibly its mode according to mode.The default mode is 0777 (octal), and the current umask value is first masked out.
    # Flags: http://www.tutorialspoint.com/python/os_open.htm
    def dfs_open(self, path, flags):
        print 'open'
        return os.open(path, flags)

    def dfs_create(self, path, mode, fi=None):
        print 'create'
        return os.open(path, os.O_WRONLY | os.O_CREAT, mode)

    # The method read() reads at most n bytes from file desciptor fd, return a string containing the bytes read
    def dfs_read(self, path, length, offset, fh):
        print 'read'
        os.lseek(fh, offset, os.SEEK_SET)
        return os.read(fh, length)

    def dfs_write(self, path, buf, offset, fh):
        print 'write'
        os.lseek(fh, offset, os.SEEK_SET)
        return os.write(fh, buf)

    def dfs_truncate(self, path, length):
        print 'truncate'
        with open(path, 'r+') as f: f.truncate(length)

    # The method fsync() forces write of file with file descriptor fd to disk
    def dfs_flush(self, path, fh):
        print 'flush'
        return os.fsync(fh)

    def dfs_release(self, path, fh):
        print 'release'
        return os.close(fh)

    # The same as dfs_flush
    def fsync(self, path, fdatasync, fh):
        print 'fsync'
        return self.flush(path, fh)

# def main():
func = Func('DFS')
path = os.getcwd() + '/file.txt'
# func.dfs_access(path, os.F_OK)

path = os.getcwd() + '/tempfile.txt'
mode = S_IRUSR
# func.dfs_chmod(path, mode)

path = os.getcwd() + '/file.txt'
uid = 1
gid = 1
# func.dfs_chown(path, uid, gid)

path = os.getcwd() + '/file.txt'
attr = 'name'
# func.dfs_getattr(path, attr)
# print os.lstat(os.getcwd() + '/file.txt')

# path = os.getcwd() + '/file.txt'
path2 = os.getcwd()
# print os.path.isdir(path2)
# dirents = ['.', '..']
# print os.listdir(path2)
# print dirents.extend(os.listdir(path2))
# print dirents
# func.dfs_readdir(path2)

dst = '/tmp/python'
src = '/usr/bin/python'
# func.dfs_readlink(dst)

# func.dfs_unlink(dst)

# func.dfs_symlink(src, dst)

# filename = '/tmp/tmpfile'
# mode = S_IRUSR
# dev = os.makedev(10, 20)
# func.dfs_mknod(filename, mode)    # invalid argument

path = os.getcwd() + '/newDir'
mode = 0755
# func.dfs_mkdir(path, mode)

path = os.getcwd() + '/newDir'
# func.dfs_rmdir(path)

path = os.getcwd()
# func.dfs_statfs(path)

fileOld = os.getcwd() + '/file.txt'
fileNew = os.getcwd() + '/file1.txt'
# func.dfs_rename(fileOld, fileNew)
# func.dfs_rename(fileNew, fileOld)

# func.dfs_link(fileOld, fileNew)

# stinfo = os.stat(fileOld)
# print stinfo
# Using os.stat to recieve atime and mtime of file
# print "access time of a2.py: %s" %stinfo.st_atime
# print "modified time of a2.py: %s" %stinfo.st_mtime
times = (1500000000.0, 1500000000)
# func.dfs_utime(fileOld, times)

# fd = func.dfs_open(fileOld, os.O_RDWR | os.O_CREAT)
# os.write(fd, 'A new file')
# os.close(fd)

# create a file read/write by owner only
# func.dfs_create(fileNew, stat.S_IRUSR | stat.S_IWUSR)

fd = os.open(fileOld, os.O_RDWR)
# ret = os.read(fd, 5)
# print ret
offset = 5
length = 5  # read from 6-10
print func.dfs_read(fileOld, length, offset, fd)
os.close(fd)

# fd = os.open(fileOld, os.O_RDWR)
# offset = 10
# buf = 'LOL'  # read from 6-10
# func.dfs_write(fileOld, buf, offset, fd)
# os.close(fd)

# func.dfs_truncate(fileOld, 10)

# fd = os.open(fileOld, os.O_RDWR)
# func.dfs_flush(fileOld, fd)
# os.close(fd)

