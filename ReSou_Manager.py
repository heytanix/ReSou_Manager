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

# Function to select resources to monitor
def select_resources_to_monitor():
    print("\nSelect resources to monitor:")
    print("1. RAM")
    print("2. CPU")
    print("3. GPU")
    print("4. All of the above")
    
    choice = input("Enter your choice (comma-separated for multiple): ")
    resources = [int(x.strip()) for x in choice.split(',')]
    return resources
