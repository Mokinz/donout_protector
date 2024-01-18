# system_commands.py

import ctypes

def lock_computer():
    # Use ctypes to execute the Windows lock command
    ctypes.windll.user32.LockWorkStation()
