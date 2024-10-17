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

# Function to monitor RAM usage
def monitor_ram(excluded_processes):
    print("Monitoring RAM usage...")
    while True:
        for proc in psutil.process_iter(['pid', 'name', 'memory_percent']):
            if proc.info['name'] not in essential_processes and proc.info['name'] not in excluded_processes:
                if proc.info['memory_percent'] > 30.0:  # Arbitrary threshold for demonstration
                    print(f"Killing {proc.info['name']} using {proc.info['memory_percent']:.2f}% of RAM")
                    psutil.Process(proc.info['pid']).terminate()
        time.sleep(5)  # Adjust based on monitoring frequency

# Function to monitor CPU usage
def monitor_cpu(excluded_processes):
    print("Monitoring CPU usage...")
    while True:
        for proc in psutil.process_iter(['pid', 'name', 'cpu_percent']):
            if proc.info['name'] not in essential_processes and proc.info['name'] not in excluded_processes:
                if proc.info['cpu_percent'] > 50.0:  # Arbitrary threshold
                    print(f"Killing {proc.info['name']} using {proc.info['cpu_percent']:.2f}% of CPU")
                    psutil.Process(proc.info['pid']).terminate()
        time.sleep(5)
