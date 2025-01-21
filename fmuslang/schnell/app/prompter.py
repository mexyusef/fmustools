import sys

from prompt_toolkit.shortcuts import confirm
from prompt_toolkit.shortcuts import message_dialog
from prompt_toolkit.shortcuts import input_dialog
from prompt_toolkit.shortcuts import button_dialog
from prompt_toolkit.formatted_text import HTML
from prompt_toolkit.shortcuts import radiolist_dialog
from prompt_toolkit.completion import PathCompleter

class Prompter:
  def __init__(self, flavor=1):
    self.flavor = flavor

  def run(self):
    if self.flavor == 1:
      answer = confirm("Should we do that?")
      print("You said: %s" % answer)
    elif self.flavor == 2:
      message_dialog(
        title="Example dialog window",
        text="Do you want to continue?\nPress ENTER to quit.",
      )
    elif self.flavor == 3:
      result = input_dialog(
        title="Input dialog example", text="Please type your name:"
      )
      print("Result = {}".format(result))
    elif self.flavor == 4:
      result = button_dialog(
        title="Button dialog example",
        text="Are you sure?",
        buttons=[("Yes", True), ("No", False), ("Maybe...", None)],
      )
      print("Result = {}".format(result))
    elif self.flavor == 5:
      # result = radiolist_dialog(
      #   values=[
      #     ("red", HTML('<style bg="red" fg="white">Red</style>')),
      #     ("green", HTML('<style bg="green" fg="white">Green</style>')),
      #     ("blue", HTML('<style bg="blue" fg="white">Blue</style>')),
      #     ("orange", HTML('<style bg="orange" fg="white">Orange</style>')),
      #   ],
      #   title=HTML("Radiolist dialog example <reverse>with colors</reverse>"),
      #   text="Please select a color:",
      # )
      result = radiolist_dialog(
        values=[
          ("red", "Red"),
          ("green", "Green"),
          ("blue", "Blue"),
          ("orange", "Orange"),
        ],
        title="Radiolist dialog example",
        text="Please select a color:",
      )
      print("Result = {}".format(result))


from .lexerlist import lexer_list

class RadioInput:
  def run(self):
    result = radiolist_dialog(
      values=[
        # (value, label), result akan menerima value=str
        # di sini value kit a set ke tuple
        (item, item[1]) for item in lexer_list
      ],
      title="Radiolist dialog example",
      text="Please select a color:",
    )
    # print("Result = {}".format(result))
    return result

class GetFilename:
  def run(self):
    result = input_dialog(
      title="Input dialog example", 
      text="Please type your name:",
      completer=PathCompleter(),
    )
    # print("Result = {}".format(result))
    return result

if __name__ == '__main__':
  arg = 1
  if len(sys.argv) == 2:
    arg = int(sys.argv[1])

  Prompter(arg).run()
