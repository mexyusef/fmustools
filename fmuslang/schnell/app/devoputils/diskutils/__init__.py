import psutil
# pip install psutil


def get_free_memory_size():
    # Get the system memory information
    memory_info = psutil.virtual_memory()

    # Get the free memory size in bytes
    free_memory_bytes = memory_info.available

    # Define the units for better readability
    units = ['B', 'KB', 'MB', 'GB', 'TB']

    # Convert the size to human-readable format
    for unit in units:
        if free_memory_bytes < 1024:
            return f"{free_memory_bytes:.2f}{unit}"
        free_memory_bytes /= 1024


def test_get_free_memory_size():
    free_memory_size = get_free_memory_size()
    print(f"Free Memory Size: {free_memory_size}")


def get_available_disk_space(path='c:'):
    try:
        disk_space = psutil.disk_usage(path)
        available_space = disk_space.free
        # return available_space
        # Convert bytes to human-readable format
        for unit in ['B', 'KB', 'MB', 'GB', 'TB']:
            if available_space < 1024.0:
                break
            available_space /= 1024.0

        return f"{available_space:.2f}{unit}"

    except Exception as e:
        print(f"Error: {e}")
        return None


# #reflect#schnell.app.devoputils.diskutils/test_get_available_disk_space
def test_get_available_disk_space():
    path_to_check = "c:"  # You can specify a different path if needed
    available_space = get_available_disk_space(path_to_check)

    if available_space is not None:
        print(f"Available disk space on '{path_to_check}': {available_space}.")
    else:
        print("Failed to retrieve disk space information.")


def get_cpu_usage_percent():
    # Get CPU usage percentage
    cpu_percent = psutil.cpu_percent(interval=1)

    return cpu_percent


def test_get_cpu_usage_percent():
    cpu_percent = get_cpu_usage_percent()
    print(f"CPU Usage: {cpu_percent}%")


def has_other_drives():
    partitions = psutil.disk_partitions()

    for partition in partitions:
        drive = partition.device
        if drive != 'C:':
            return True

    return False


def test_has_other_drives():
    if has_other_drives():
        print("There are drives other than C: drive.")
    else:
        print("There are no drives other than C: drive.")


def get_disk_drives():
    drives = []
    partitions = psutil.disk_partitions()

    for partition in partitions:
        drive = partition.device
        drives.append(drive)

    return drives


def test_get_disk_drives():
    disk_drives = get_disk_drives()
    if disk_drives:
        print("Available Disk Drives:")
        for drive in disk_drives:
            print(drive)
    else:
        print("No disk drives found.")
