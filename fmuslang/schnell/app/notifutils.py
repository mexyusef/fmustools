from constants import sidoarjodir
# kita gunakan istilah pynotif dan notifpy

# https://github.com/YuriyLisovskiy/pynotifier
# pip install py-notifier
from pynotifier import Notification

# https://github.com/ms7m/notify-py
# notify-py --title --message --applicationName --iconPath --soundPath
# https://codingshiksha.com/react/react-js-react-digital-clock-library-example-to-build-a-countdown-digital-alarm-blinking-clock-in-browser-using-javascript-full-project-for-beginners/

# pip install notify-py notify-send
# https://pythonrepo.com/repo/ms7m-notify-py
from notifypy import Notify


from .dirutils import joiner
from .utils import env_get
# pip install py-notifier notify-py notify-send

# plus icon, minus notif bar
def pynotif(judul='judul', pesan='pesan', duration_seconds=5, icon=joiner(sidoarjodir, 'fmus.ico')):
  Notification(
    title=judul,
    description=pesan,
    icon_path=icon,             # On Windows .ico is required, on Linux - .png
    duration=duration_seconds,  # Duration in seconds
    urgency='normal'
  ).send()

# minus icon, plus notif bar
def notifpy(judul='judul', pesan='pesan'):
  notification = Notify(
    default_notification_icon=joiner(sidoarjodir, 'fmus-us.png'),
    default_notification_audio=r'C:\Windows\Media\chord.wav')
  notification.title = judul
  notification.message = pesan
  notification.send()

def notify(title, body, duration=2, mode=1):
  if mode==2:
    notifpy(title, body)
  else:
    pynotif(title, body, duration_seconds=duration)

# pip install --user plyer
from plyer import notification

def notify_plyer():
  notification.notify(
      title='New Pull Request',
      message='PR #123: Fix issue with routing - https://github.com/vercel/next.js/pull/123',
      app_name='GitHub Monitor'
  )
