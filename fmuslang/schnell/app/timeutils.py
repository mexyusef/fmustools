import datetime
import time
from datetime import datetime, timedelta


def timestamp(formatter='%Y%m%d_%H%M%S'):
    return datetime.datetime.now().strftime(formatter)


def diary_time(formatter='[%a, %d %b %Y %H:%M:%S]'):
    return datetime.datetime.now().strftime(formatter)


def time_ago_to_datetime(time_ago):
    current_datetime = datetime.utcnow()

    if time_ago[-1] == 'Y':
        delta = timedelta(days=int(time_ago[:-1]) * 365)
    elif time_ago[-1] == 'M':
        delta = timedelta(days=int(time_ago[:-1]) * 30)
    elif time_ago[-1] == 'W':
        delta = timedelta(weeks=int(time_ago[:-1]))
    elif time_ago[-1] == 'D':
        delta = timedelta(days=int(time_ago[:-1]))
    elif time_ago[-1] == 'H':
        delta = timedelta(hours=int(time_ago[:-1]))
    else:
        raise ValueError("Invalid time ago specification")

    new_datetime = current_datetime - delta
    return new_datetime.strftime('%Y-%m-%dT%H:%M:%SZ')


def test_time_ago_to_datetime():
    print(time_ago_to_datetime('2Y'))  # 2 years ago
    print(time_ago_to_datetime('3M'))  # 3 months ago
    print(time_ago_to_datetime('7W'))  # 7 weeks ago
    print(time_ago_to_datetime('2D'))  # 2 days ago
    print(time_ago_to_datetime('5H'))  # 5 hours ago

    # 2022-06-12T17:42:23Z
    # 2024-03-13T17:42:23Z
    # 2024-04-23T17:42:23Z
    # 2024-06-09T17:42:23Z
    # 2024-06-11T12:42:23Z
