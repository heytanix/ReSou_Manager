# ReSou_Manager - System Resource Optimizer

This project is a Python-based system resource optimizer designed to monitor and manage the usage of RAM, CPU, and GPU. It can automatically terminate processes that exceed a specified resource threshold, helping to optimize system performance by excluding essential or user-defined processes.

## Features

- **Platform Detection**: Automatically detects the operating system (Windows, Linux, or macOS) and excludes essential system processes from being terminated.
- **Custom Process Exclusion**: Users can input specific processes to exclude from monitoring and termination.
- **Resource Monitoring**:
  - **RAM**: Monitors and terminates processes consuming more than 30% of available memory.
  - **CPU**: Monitors and terminates processes consuming more than 50% of CPU power.
  - **GPU**: Monitors GPU usage and reports when the load exceeds 80%.
- **Multi-threaded**: The tool runs separate threads to monitor RAM, CPU, and GPU simultaneously based on user selection.

## Requirements

- **Python 3.x**
- Required Python libraries:
  - `psutil`
  - `GPUtil`
  - `platform`
  
Install the required libraries using pip:
```bash
pip install psutil GPUtil
