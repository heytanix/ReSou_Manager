import psutil
import platform
import time
import GPUtil
from threading import Thread

# Detect system platform - helps detect the Operating system of user's system
system_platform = platform.system()

# Exclude essential system processes based on OS - Avoids elimination of necessary OS processes
if system_platform == 'Windows':
    essential_processes = ['System', 'Registry', 'csrss.exe']
elif system_platform == 'Linux':
    essential_processes = ['init', 'systemd']
elif system_platform == 'Darwin':  # MacOS
    essential_processes = ['kernel_task', 'launchd']
else:
    essential_processes = []

