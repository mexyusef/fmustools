
class Debug:
  def __init__(self, isDebug=True):
    self.isDebug = isDebug
  def __call__(self, *args):
    if self.isDebug:
      print(*args)

