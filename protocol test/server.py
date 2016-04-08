# Echo server program
import socket
import os

from common import *

HOST = ''                 # Symbolic name meaning all available interfaces
PORT = 50007              # Arbitrary non-privileged port

class dfs:


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
        #return os.mkdir(path, mode)
        return os.mkdir('/home/freeradical/Documents',mode)

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
    def dfs_fsync(self, path, fdatasync, fh):
        print 'fsync'
        return self.dfs_flush(path, fh)
    
    dfs_oper = {DFS_ACCESS : dfs_access, DFS_CHMOD : dfs_chmod, DFS_CHOWN : dfs_chown, DFS_GETATTR : dfs_getattr, DFS_READDIR : dfs_readdir,
            DFS_READLINK : dfs_readlink, DFS_MKNOD : dfs_mknod, DFS_RMDIR : dfs_rmdir, DFS_MKDIR : dfs_mkdir, DFS_STATFS : dfs_statfs, 
            DFS_UNLINK : dfs_unlink, DFS_SYMLINK: dfs_symlink, DFS_RENAME : dfs_rename, DFS_LINK : dfs_link, DFS_UTIMES : dfs_utime, 
            DFS_OPEN : dfs_open, DFS_CREATE : dfs_create, DFS_READ : dfs_read, DFS_WRITE : dfs_write, DFS_TRUNCATE : dfs_truncate, 
            DFS_FLUSH : dfs_flush, DFS_RELEASE : dfs_release, DFS_FSYNC : dfs_fsync
    }

def execute_json_command(conn, command_string):
    commandObj = json.loads(command_string)
    param_list = commandObj['param_list']
    command = commandObj['command']
    print command
    print param_list

    dfsObj = dfs()
    #ret = dfsObj.dfs_oper[command](param_list)
    ret = eval('dfsObj.'+command)(*param_list)
    print ret
    result_string = stringify_result(ret)
    print result_string
    conn.send(result_string)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(1)

while 1:
    conn, addr = s.accept()
    print 'Connected by ', addr
    data = conn.recv(1024)
    print data, len(data)
    execute_json_command(conn, data)
    conn.close()

s.close()