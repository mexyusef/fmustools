class AutoIncrement:
  """
  ai = AutoIncrement(5)
  ai = AutoIncrement()
  ai()
  ai()
  """
  def __init__(self, start=1):
    self.initial = start
    self.start = start
    self.used = False

  def set_used(self, nilai=True):
    self.used = nilai

  def get_used(self):
    return self.used
    
  def __call__(self):
    # if not self.used:
    #   self.used = True
    self.start += 1
    return str(self.start)
    
  def reset(self):
    self.start = 0

  def init(self, initial_value=None):
    self.start = initial_value if initial_value is not None else self.initial
    return str(self.start)

