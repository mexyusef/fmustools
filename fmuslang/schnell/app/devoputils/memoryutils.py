import os
import psutil


def list_processes_by_memory():
    # Get a list of all running processes
    processes = [proc.info for proc in psutil.process_iter(['pid', 'name', 'memory_info'])]

    # Sort processes based on memory usage
    processes.sort(key=lambda x: x['memory_info'].rss, reverse=True)

    # Print the details of processes
    print("{:<10} {:<30} {:<15}".format("PID", "Name", "Memory Usage (RSS)"))
    print("-" * 60)

    for process in processes:
        pid = process['pid']
        name = process['name']
        memory_usage = process['memory_info'].rss / (1024 * 1024)  # Convert to MB

        print("{:<10} {:<30} {:<15.2f} MB".format(pid, name, memory_usage))


def list_processes_with_path(num_processes=10):
    # Get a list of all running processes
    processes = [proc.info for proc in psutil.process_iter(['pid', 'name', 'memory_info', 'cwd'])]

    # Sort processes based on memory usage
    processes.sort(key=lambda x: x['memory_info'].rss, reverse=True)

    # Print the details of processes
    print("{:<10} {:<30} {:<50} {:<15}".format("PID", "Name", "Working Directory", "Memory Usage (RSS)"))
    print("-" * 120)

    # Determine the number of processes to display
    num_processes_to_display = min(num_processes, len(processes)) if num_processes > 0 else len(processes)

    for process in processes[:num_processes_to_display]:
        pid = process['pid']
        name = process['name']
        working_dir = process['cwd'] if process['cwd'] else "N/A"
        memory_usage = process['memory_info'].rss / (1024 * 1024)  # Convert to MB

        print("{:<10} {:<30} {:<50} {:<15.2f} MB".format(pid, name, working_dir, memory_usage))


if __name__ == "__main__":
    # Set the number of processes to list (default is 10, 0 to list all processes)
    num_processes_to_list = 0

    # Call the function with the specified number of processes
    list_processes_with_path(num_processes_to_list)
