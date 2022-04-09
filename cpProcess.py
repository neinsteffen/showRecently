import ctypes
import contextlib
import time,sys
from _ctypes import _SimpleCData
from _ctypes import sizeof, byref, addressof, alignment, resize
from ctypes import c_size_t, sizeof, c_wchar_p, get_errno, c_wchar

CF_UNICODETEXT = 13
GMEM_MOVEABLE = 0x0002

@contextlib.contextmanager
def clipboard(hwnd):
    t = time.time() + 0.5
    success = False
    while time.time() < t:
        success = OpenClipboard(hwnd)
        if success:
            break
        time.sleep(0.01)
    if not success:
        pass
        #raise PyperclipWindowsException("Error calling OpenClipboard")

    try:
        yield
    finally:
        safeCloseClipboard()
@contextlib.contextmanager
def window():
    hwnd = safeCreateWindowExA(0, b"STATIC", None, 0, 0, 0, 0, 0,
                                None, None, None, None)
    try:
        yield hwnd
    finally:
        safeDestroyWindow(hwnd)
PY2 = sys.version_info[0] == 2
STR_OR_UNICODE = unicode if PY2 else str 

def _stringifyText(text):
    if PY2:
        acceptedTypes = (unicode, str, int, float, bool)
    else:
        acceptedTypes = (str, int, float, bool)
    if not isinstance(text, acceptedTypes):
        pass
        #raise PyperclipException('only str, int, float, and bool values can be copied to the clipboard, not %s' % (text.__class__.__name__))
    return STR_OR_UNICODE(text)


def _check_size(typ, typecode=None):
    from struct import calcsize
    if typecode is None:
        typecode = typ._type_
    actual, required = sizeof(typ), calcsize(typecode)
    if actual != required:
        raise SystemError("sizeof(%s) wrong: %d instead of %d" % \
                          (typ, actual, required))

class c_void_p(_SimpleCData):
    _type_ = "P"
c_voidp = c_void_p 
_check_size(c_void_p)

class c_wchar_p(_SimpleCData):
    _type_ = "Z"
    def __repr__(self):
        return "%s(%s)" % (self.__class__.__name__, c_void_p.from_buffer(self).value)
class CheckedCall(object):
    def __init__(self, f):
        super(CheckedCall, self).__setattr__("f", f)
    def __call__(self, *args):
        ret = self.f(*args)
        if not ret:
            pass
            #raise PyperclipWindowsException("Error calling " + self.f.__name__)
        return ret

    def __setattr__(self, key, value):
        setattr(self.f, key, value)
def copy_windows(text):

        text = _stringifyText(text) # Converts non-str values to str.

        with window() as hwnd:
            with clipboard(hwnd):
                safeEmptyClipboard()

                if text:
                    count = wcslen(text) + 1
                    handle = safeGlobalAlloc(GMEM_MOVEABLE,
                                            count * sizeof(c_wchar))
                    locked_handle = safeGlobalLock(handle)

                    ctypes.memmove(c_wchar_p(locked_handle), c_wchar_p(text), count * sizeof(c_wchar))
                    
                    
                    safeSetClipboardData(CF_UNICODETEXT, handle)
def paste_windows():
    with clipboard(None):
        handle = safeGetClipboardData(CF_UNICODETEXT)
        if not handle:
            return ""       
        return c_wchar_p(handle).value

    return copy_windows, paste_windows


from ctypes.wintypes import (HGLOBAL, LPVOID, DWORD, LPCSTR, INT, HWND,
                                HINSTANCE, HMENU, BOOL, UINT, HANDLE)

windll = ctypes.windll
msvcrt = ctypes.CDLL('msvcrt')
safeGetClipboardData = CheckedCall(windll.user32.GetClipboardData)
safeGetClipboardData.argtypes = [UINT]
safeGetClipboardData.restype = HANDLE
handle = safeGetClipboardData(CF_UNICODETEXT)


safeCreateWindowExA = CheckedCall(windll.user32.CreateWindowExA)
safeCreateWindowExA.argtypes = [DWORD, LPCSTR, LPCSTR, DWORD, INT, INT,
                                    INT, INT, HWND, HMENU, HINSTANCE, LPVOID]
safeCreateWindowExA.restype = HWND

safeSetClipboardData = CheckedCall(windll.user32.SetClipboardData)
safeSetClipboardData.argtypes = [UINT, HANDLE]
safeSetClipboardData.restype = HANDLE

safeCloseClipboard = CheckedCall(windll.user32.CloseClipboard)
safeCloseClipboard.argtypes = []
safeCloseClipboard.restype = BOOL

safeDestroyWindow = CheckedCall(windll.user32.DestroyWindow)
safeDestroyWindow.argtypes = [HWND]
safeDestroyWindow.restype = BOOL

OpenClipboard = windll.user32.OpenClipboard
OpenClipboard.argtypes = [HWND]
OpenClipboard.restype = BOOL

safeEmptyClipboard = CheckedCall(windll.user32.EmptyClipboard)
safeEmptyClipboard.argtypes = []
safeEmptyClipboard.restype = BOOL

safeGlobalLock = CheckedCall(windll.kernel32.GlobalLock)
safeGlobalLock.argtypes = [HGLOBAL]
safeGlobalLock.restype = LPVOID

safeGlobalUnlock = CheckedCall(windll.kernel32.GlobalUnlock)
safeGlobalUnlock.argtypes = [HGLOBAL]
safeGlobalUnlock.restype = BOOL

safeGlobalAlloc = CheckedCall(windll.kernel32.GlobalAlloc)
safeGlobalAlloc.argtypes = [UINT, c_size_t]
safeGlobalAlloc.restype = HGLOBAL

wcslen = CheckedCall(msvcrt.wcslen)
wcslen.argtypes = [c_wchar_p]
wcslen.restype = UINT
