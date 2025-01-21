import socket, struct
from colorama import init, Fore

"""
https://stackoverflow.com/questions/19196105/how-to-check-if-a-network-port-is-open
https://www.geeksforgeeks.org/port-scanner-using-python/
https://resources.infosecinstitute.com/topic/write-a-port-scanner-in-python/
https://www.thepythoncode.com/article/make-port-scanner-python
"""

init()
GREEN = Fore.GREEN
RESET = Fore.RESET
GRAY = Fore.LIGHTBLACK_EX

def is_port_open(port, host='localhost'):
  """
  https://www.thepythoncode.com/article/make-port-scanner-python
  determine whether `host` has the `port` open
  """
  # creates a new socket
  s = socket.socket()
  try:
    # tries to connect to host using that port
    s.connect((host, port))
    # make timeout if you want it a little faster ( less accuracy )
    # s.settimeout(0.2)
  except:
    # cannot connect, port is closed
    # return false
    return False
  else:
    # the connection was established, port is open!
    return True

def is_ports_open(ports=[], host='localhost'):
  for port in ports:
    if is_port_open(host, port):
      print(f"{GREEN}[+] {host}:{port} is open     {RESET}")
    else:
      print(f"{GRAY}[!] {host}:{port} is closed    {RESET}", end="\r")


def get_ip(interface='eth0'):
  try:
    import fcntl
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    alamat = socket.inet_ntoa(fcntl.ioctl(s.fileno(), 0x8915, struct.pack('256s', 'eth0'[:15].encode('utf-8') ))[20:24])
  except Exception as err:
    alamat = 'localhost'
  return alamat

def write_ip(filepath='/mnt/c/Users/user/ip'):
  from schnell.app.fileutils import file_write
  from schnell.app.printutils import indah4
  alamat = get_ip()
  file_write(filepath, alamat)
  indah4(f"Selesai menulis ip '{alamat}' ke file '{filepath}'", warna='green')

CURRENT_IP_ETH0 = get_ip()
