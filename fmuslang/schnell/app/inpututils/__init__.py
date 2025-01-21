import sys
from prompt_toolkit import PromptSession, prompt
from prompt_toolkit.application import run_in_terminal
from prompt_toolkit.auto_suggest import AutoSuggest, AutoSuggestFromHistory, Suggestion
from prompt_toolkit.clipboard.pyperclip import PyperclipClipboard
from prompt_toolkit.completion import WordCompleter, FuzzyWordCompleter, NestedCompleter, FuzzyCompleter
from prompt_toolkit.formatted_text import ANSI, HTML
from prompt_toolkit.history import FileHistory
from prompt_toolkit.key_binding import KeyBindings
from prompt_toolkit.shortcuts import CompleteStyle, confirm, set_title
from prompt_toolkit.validation import Validator


ciledugdir = r'c:\work\ciledug'
sys.path.extend([ciledugdir])
from ciledug.palsu.palsu import process_palsu_language


def give_me(default_value=None, prompter='Give me the value:', palsu_request=':name', warna='#e296ea'):
    if not default_value:
        default_value_spaced = process_palsu_language(palsu_request, returning=True)
        default_value = default_value_spaced.replace(' ', '_').lower()
    masukan = prompt(
        HTML(f'<style color="{warna}">{prompter}: </style>'),
        default=default_value,
        placeholder=HTML(f'<style color="#888888">({default_value})</style>'),
    )
    return masukan


def test_give_me():
    # terima = give_me('hello, lovers')
    terima = give_me()
    if terima:
        print(terima)


def give_me_prefix_value(default_value='', prompter='Give me the value:', palsu_request=':name', warna='#e296ea'):
    # if not default_value:
    default_value_spaced = process_palsu_language(palsu_request, returning=True)
    default_value += ('-' if default_value else '') + default_value_spaced.replace(' ', '-').lower()  # fly gak terima _ tapi -

    masukan = prompt(
        HTML(f'<style color="{warna}">{prompter}: </style>'),
        default=default_value,
        placeholder=HTML(f'<style color="#888888">({default_value})</style>'),
    )
    return masukan

if __name__ == '__main__':
    test_give_me()
