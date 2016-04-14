# Echo server program
import socket
import os

from common import *

HOST = ''                 # Symbolic name meaning all available interfaces
PORT = 50007              # Arbitrary non-privileged port
DIR = "/Users/vsrao/ws/sdir"

class dfs:

    def _full_path(self, partial):
        if partial.startswith("/"):
            partial = partial[1:]
        path = os.path.join(DIR, partial)
        return path

    # Filesystem methods
    # ==================

    # access - check real user's permissions for a file
    # http://linux.die.net/man/2/access
    def dfs_access(self, param_list):
        log.debug('dfs_access')
        log.debug(param_list)
        path = self._full_path(param_list[0])
        return os.access(path, param_list[1])

    # chmod - change the mode of path to numeric mode
    # https://docs.python.org/2/library/os.html#os.chmod
    # Mode: http://www.tutorialspoint.com/python/os_chmod.htm
    def dfs_chmod(self, param_list):
        log.debug('dfs_chmod')
        log.debug(param_list)
        path = self._full_path(param_list[0])
        return os.chmod(path, param_list[1])

    # chown - change the owner and group id of path to the numeric id and gid
    def dfs_chown(self, param_list):
        log.debug('dfs_chown')
        log.debug(param_list)
        path = self._full_path(param_list[0])
        return os.chown(path, param_list[1], param_list[2])

    # getattr - return the value of the named attribute of the file
    def dfs_getattr(self, param_list):
        log.debug('dfs_getattr')
        log.debug(param_list)
        path = self._full_path(param_list[0])
        if os.path.exists(path):
            st = os.lstat(path)
            return dict((key, getattr(st, key)) for key in ('st_mode', 'st_ino', 'st_dev', 'st_nlink', 'st_uid', 'st_gid', 'st_size', 'st_atime', 'st_mtime', 'st_ctime'))
        else:
            return False

    # readdir - Return a list containing the names of the entries in the directory given by path
    def dfs_readdir(self, param_list):
        log.debug('dfs_readdir')
        log.debug(param_list)
        path = self._full_path(param_list[0])
        dirents = ['.', '..']
        dirents.extend(os.listdir(path))
        return dirents

    # readlink - Return a string representing the path to which the symbolic link points.
    def dfs_readlink(self, param_list):
        log.debug('dfs_readlink')
        log.debug(param_list)
        path = self._full_path(param_list[0])
        path = os.readlink(path)
        return path

    def dfs_symlink(self, param_list):
        log.debug('dfs_symlink')
        log.debug(param_list)
        path = self._full_path(param_list[1])
        return os.symlink(param_list[1], path)
        
    def dfs_unlink(self, param_list):
        log.debug('dfs_unlink')
        log.debug(param_list)
        path = self._full_path(param_list[0])
        return os.unlink(path)

    # Create a filesystem node (file, device special file or named pipe) named filename.
    def dfs_mknod(self, param_list):
        log.debug('dfs_mknod')
        log.debug(param_list)
        path = self._full_path(param_list[0])
        return os.mknod(path, param_list[1])

    def dfs_mkdir(self, param_list):
        log.debug('dfs_mkdir')
        log.debug(param_list)
        path = self._full_path(param_list[0])
        return os.mkdir(path, param_list[1])

    # Remove (delete) the directory path.
    def dfs_rmdir(self, param_list):
        log.debug('dfs_rmdir')
        log.debug(param_list)
        path = self._full_path(param_list[0])
        return os.rmdir(path);

    # Return file system parameters, like fs block size, # of blocks
    # https://docs.python.org/2/library/statvfs.html
    def dfs_statfs(self, param_list):
        log.debug('dfs_statfs')
        log.debug(param_list)
        path = self._full_path(param_list[0])
        stv = os.statvfs(path)
        return dict((key, getattr(stv, key)) for key in ('f_bsize', 'f_frsize', 'f_blocks', 'f_bfree', 'f_bavail', 'f_files', 'f_ffree', 'f_favail', 'f_flag', 'f_namemax'))

    def dfs_rename(self, param_list):
        log.debug('dfs_rename')
        log.debug(param_list)
        old = self._full_path(param_list[0])
        new = self._full_path(param_list[1])
        return os.rename(old, new)

    # The method link() creates a hard link pointing to src named dst.
    def dfs_link(self, param_list):
        log.debug('dfs_link')
        log.debug(param_list)
        target = self._full_path(param_list[0])
        name = self._full_path(param_list[1])
        return os.link(target, name)

    # The method utime() sets the access and modified times of the file specified by path.
    def dfs_utime(self, param_list):
        log.debug('dfs_utime')
        log.debug(param_list)
        path = self._full_path(param_list[0])
        return os.utime(path, (param_list[1][0], param_list[1][1]))

    # File methods
    # ============

    # opens the file file and set various flags according to flags and possibly its mode according to mode.The default mode is 0777 (octal), and the current umask value is first masked out.
    # Flags: http://www.tutorialspoint.com/python/os_open.htm
    def dfs_open(self, param_list):
        log.debug('dfs_open')
        log.debug(param_list)
        path = self._full_path(param_list[0])
        return os.open(path, param_list[1])

    def dfs_create(self, param_list):
        log.debug('dfs_create')
        log.debug(param_list)
        path = self._full_path(param_list[0])
        return os.open(path, os.O_WRONLY | os.O_CREAT, param_list[1])

    # The method read() reads at most n bytes from file desciptor fd, return a string containing the bytes read
    def dfs_read(self, param_list):
        log.debug('dfs_read')
        log.debug(param_list)
        #path = self._full_path(param_list[0])
        os.lseek(param_list[3], param_list[2], os.SEEK_SET)
        return os.read(param_list[3], param_list[1])

    def dfs_write(self, param_list):
        log.debug('dfs_write')
        log.debug(param_list)
        os.lseek(param_list[3], param_list[2], os.SEEK_SET)
        return os.write(param_list[3], param_list[1])

    def dfs_truncate(self, param_list):
        log.debug('dfs_truncate')
        log.debug(param_list)
        path = self._full_path(param_list[0])
        with open(path, 'r+') as f: f.truncate(param_list[1])

    # The method fsync() forces write of file with file descriptor fd to disk
    def dfs_flush(self, param_list):
        log.debug('dfs_flush')
        log.debug(param_list)
        return os.fsync(param_list[1])

    def dfs_release(self, param_list):
        log.debug('dfs_release')
        log.debug(param_list)
        return os.close(param_list[1])

    # The same as dfs_flush
    def dfs_fsync(self, param_list):
        log.debug('dfs_fsync')
        log.debug(param_list)
        path = self._full_path(param_list[0])
        return self.dfs_flush(path, param_list[1])
    
    dfs_oper = {DFS_ACCESS : dfs_access, DFS_CHMOD : dfs_chmod, DFS_CHOWN : dfs_chown, DFS_GETATTR : dfs_getattr, DFS_READDIR : dfs_readdir,
            DFS_READLINK : dfs_readlink, DFS_MKNOD : dfs_mknod, DFS_RMDIR : dfs_rmdir, DFS_MKDIR : dfs_mkdir, DFS_STATFS : dfs_statfs,
            DFS_UNLINK : dfs_unlink, DFS_SYMLINK: dfs_symlink, DFS_RENAME : dfs_rename, DFS_LINK : dfs_link, DFS_UTIMENS : dfs_utime,
            DFS_OPEN : dfs_open, DFS_CREATE : dfs_create, DFS_READ : dfs_read, DFS_WRITE : dfs_write, DFS_TRUNCATE : dfs_truncate,
            DFS_FLUSH : dfs_flush, DFS_RELEASE : dfs_release, DFS_FSYNC : dfs_fsync
    }

dfsObj = dfs()

def execute_json_command(conn, command_string):
    commandObj = json.loads(command_string)
    param_list = commandObj['param_list']
    command = commandObj['command']

    ret = dfsObj.dfs_oper[command](dfsObj, param_list)
    result_string = stringify_result(ret)
    conn.send(result_string)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(1)
conn, addr = s.accept()
print 'Connected by ', addr

while 1:
    data = conn.recv(1024)
    execute_json_command(conn, data)
    
conn.close()

s.close()