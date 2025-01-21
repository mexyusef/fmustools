import asyncio
from .host import HostContainer as Repl

class Application:
  def __init__(self):
    self.repl = Repl()

  def run(self):
    self.repl.run()
