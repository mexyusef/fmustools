
from __future__ import absolute_import

try:
    import fcntl
    import errno
    has_fcntl = True
except ImportError:
    has_fcntl = False

try:
    import msvcrt
    import os
    has_msvcrt = True
except ImportError:
    has_msvcrt = False


class BaseLock(object):
    """Base class for file locking
    """

    def __init__(self, fileobj, mode=None, filename=None):
        self.fileobj = fileobj
        self.locked = False

    def acquire(self):
        pass

    def release(self):
        pass

    def __enter__(self):
        self.acquire()
        return self

    def __exit__(self, *args):
        if self.locked:
            self.release()

    def __del__(self):
        if self.locked:
            self.release()


class UnixFileLock(BaseLock):
    """Simple file locking for Unix using fcntl
    """

    def __init__(self, fileobj, mode=None, filename=None):
        super(UnixFileLock, self).__init__(fileobj)

        if mode is None:
            mode = fcntl.LOCK_EX
        self.mode = mode

    def acquire(self):
        try:
            fcntl.flock(self.fileobj, self.mode)
            self.locked = True
        except IOError as e:
            if e.errno != errno.ENOLCK:
                raise e

    def release(self):
        self.locked = False
        fcntl.flock(self.fileobj, fcntl.LOCK_UN)


class WindowsFileLock(BaseLock):
    """Simple file locking for Windows using msvcrt
    """

    def __init__(self, fileobj, mode=None, filename=None):
        super(WindowsFileLock, self).__init__(None)
        self.filename = "{}.lock".format(filename)

    def acquire(self):
        # create a lock file and lock it
        self.fileobj = os.open(self.filename, os.O_RDWR | os.O_CREAT | os.O_TRUNC)
        msvcrt.locking(self.fileobj, msvcrt.LK_NBLCK, 1)

        self.locked = True

    def release(self):
        self.locked = False

        # unlock lock file and remove it
        msvcrt.locking(self.fileobj, msvcrt.LK_UNLCK, 1)
        os.close(self.fileobj)
        self.fileobj = None

        try:
            os.remove(self.filename)
        except OSError:
            pass


if has_fcntl:
    FileLock = UnixFileLock
elif has_msvcrt:
    FileLock = WindowsFileLock
else:
    FileLock = BaseLock
