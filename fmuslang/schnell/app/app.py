import asyncio
from schnell.app.host import Repl
# from .host import Repl

class Application:

  def __init__(self):
    self.repl = Repl()

  def run(self):
    self.repl.run()
