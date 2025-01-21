
from prompt_toolkit.auto_suggest import Suggestion, AutoSuggest, ThreadedAutoSuggest

class UlibSuggestion(AutoSuggest):
  def __init__(self, entries):
    self.entries = entries

  def get_suggestion(self, buff, document):
    # Consider only the last line for the suggestion.
    text = document.text.rsplit("\n", 1)[-1]
    if text.strip():
      for word_lines in self.entries:
        for word in word_lines.splitlines():
          if word.startswith(text):
            return Suggestion(word[len(text) :])

    return None
