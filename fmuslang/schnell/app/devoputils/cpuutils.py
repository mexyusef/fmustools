import psutil


def get_cpu_usage_percent():
    # Get CPU usage percentage
    cpu_percent = psutil.cpu_percent(interval=1)

    return cpu_percent


def test_get_cpu_usage_percent():
    cpu_percent = get_cpu_usage_percent()
    print(f"CPU Usage: {cpu_percent}%")

