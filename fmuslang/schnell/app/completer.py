from prompt_toolkit.completion import WordCompleter, FuzzyWordCompleter
from prompt_toolkit.styles import Style
from prompt_toolkit.shortcuts import CompleteStyle

style = Style.from_dict(
	{
		"completion-menu.completion": "bg:#008888 #ffffff",
		"completion-menu.completion.current": "bg:#00aaaa #000000",
		"scrollbar.background": "bg:#88aaaa",
		"scrollbar.button": "bg:#222222",

		"username": "#884444 italic",
		"at": "#00aa00",
		"colon": "#00aa00",
		"pound": "#00aa00",
		"host": "#000088 bg:#aaaaff",
		"path": "#884444 underline",
		# Make a selection reverse/underlined.
		# (Use Control-Space to select.)
		"selected-text": "reverse underline",
	}
)
fake_completer = ['aku', 'bukan', 'cewek', 'durhaka', 'emang', 'fala', 'gue gepeng', 'halah', 'ikutin']

def complete(words, insensitive=True):
	return FuzzyWordCompleter(words)
	# return WordCompleter(words, ignore_case=insensitive)

def create_meta_completer(completer_dict, insensitive=True):
	words = list(completer_dict.keys())
	# return WordCompleter(
	return FuzzyWordCompleter(
		words,
		meta_dict=completer_dict,
		# ignore_case=insensitive,
		# complete_style=CompleteStyle.MULTI_COLUMN,
		# style=style,
	)
