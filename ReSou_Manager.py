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

# Function to get processes to monitor
def get_processes_to_exclude():
    excluded_processes = input("Enter processes to exclude (comma-separated): ").split(',')
    return [proc.strip() for proc in excluded_processes]
