from .base import base_grammar
from .browse import browse_languages
from .chart import chart_languages
from .data import data_languages
from .decl import declarative_languages
from .gui import gui_languages
from .lang import main_languages
from .video import video_languages

from .frontend import frontend_languages
from .mobile import mobile_languages

bahasa = f"""
keseluruhan: insn+

insn: dirspec* filespec*
  | programs
  | browse_program
  | video_program

dirspec: "dir" dirconfig?
  | "dir" dirconfig? "(" dirspec* filespec* ")"
dirconfig: "[" HURUF_FOLDER "]"

dirname: HURUF_FOLDER

// sementara declarative dan imperative/functional terpisah
filespec: "F" fileconfig? programs?
  | "f" fileconfig? programs?
  | "DF" fileconfig? declaratives___?      -> declarative_program

fileconfig: "[" HURUF_FOLDER "]"

// --------------------- declarative programs
{declarative_languages}

// --------------------- video programs
{video_languages}

// --------------------- browse directory programs
{browse_languages}

// main languages
{main_languages}

// base grammar
{base_grammar}
"""
