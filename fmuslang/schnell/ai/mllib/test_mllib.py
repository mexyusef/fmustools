# term
import os, sys
sys.path.append(os.path.dirname(__file__))
from mllib import main

def test_answer():
  assert main() == 'OK'
