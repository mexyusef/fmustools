from configuration_values import config_app
from schnell.app.clipboardutils import trycopy, trypaste
from schnell.app.dirutils import isfile
from schnell.app.fileutils import file_content, file_write
from schnell.app.printutils import indah4

# kita coba juga berbagai progressbar...
import os, random, signal, time, threading
from prompt_toolkit.shortcuts import ProgressBar
from prompt_toolkit.styles import Style
from prompt_toolkit.shortcuts.progress_bar import formatters
from prompt_toolkit.formatted_text import HTML
from prompt_toolkit.output import ColorDepth
from prompt_toolkit.key_binding import KeyBindings
from prompt_toolkit.patch_stdout import patch_stdout

def progress1():
    with ProgressBar() as pb:
        for i in pb(range(800)):
            time.sleep(0.01)

style2 = Style.from_dict(
    {
        "title": "#4444ff underline",
        "label": "#ff4400 bold",
        "percentage": "#00ff00",
        "bar-a": "bg:#00ff00 #004400",
        "bar-b": "bg:#00ff00 #000000",
        "bar-c": "#000000 underline",
        "current": "#448844",
        "total": "#448844",
        "time-elapsed": "#444488",
        "time-left": "bg:#88ff88 #000000",
    }
)

def progress2():
    with ProgressBar(
        style=style2,
        title="Progress bar example with custom styling."
    ) as pb:
        for i in pb(range(1600), label="Downloading..."):
            time.sleep(0.01)

style3 = Style.from_dict(
    {
        "progressbar title": "#0000ff",
        "item-title": "#ff4400 underline",
        "percentage": "#00ff00",
        "bar-a": "bg:#00ff00 #004400",
        "bar-b": "bg:#00ff00 #000000",
        "bar-c": "bg:#000000 #000000",
        "tildes": "#444488",
        "time-left": "bg:#88ff88 #ffffff",
        "spinning-wheel": "bg:#ffff00 #000000",
    }
)

# C:\work\ciledug\ciledug\fmusperintah\vendor\python-prompt-toolkit\examples\progress-bar\styled-2.py
def progress3():
    custom_formatters = [
        formatters.Label(),
        formatters.Text(" "),
        formatters.SpinningWheel(),
        formatters.Text(" "),
        formatters.Text(HTML("<tildes>~~~</tildes>")),
        formatters.Bar(sym_a="#", sym_b="#", sym_c="."),
        formatters.Text(" left: "),
        formatters.TimeLeft(),
    ]
    with ProgressBar(
        title="Progress bar example with custom formatter.",
        formatters=custom_formatters,
        style=style3,
    ) as pb:
        for i in pb(range(20), label="Downloading..."):
            time.sleep(1)

from fpprogress import progress_rainbow
# # C:\work\ciledug\ciledug\fmusperintah\vendor\python-prompt-toolkit\examples\progress-bar\styled-rainbow.py
# def progress4():
#     # true_color = confirm("Yes true colors? (y/n) ")
#     # true_color = True
#     custom_formatters = [
#         # C:\work\ciledug\ciledug\fmusperintah\vendor\python-prompt-toolkit\src\prompt_toolkit\shortcuts\progress_bar\formatters.py
#         # formatters.Label(),
#         formatters.SpinningWheel(),
#         # formatters.Text(" "),
#         formatters.Rainbow(formatters.Bar()),
#         # formatters.Text(" left: "),
#         # formatters.Rainbow(formatters.TimeLeft()),
#     ]

#     color_depth = ColorDepth.DEPTH_24_BIT
#     # color_depth = ColorDepth.DEPTH_8_BIT

#     with ProgressBar(formatters=custom_formatters, color_depth=color_depth) as pb:
#         for i in pb(range(20), label="Fmusing..."):
#             time.sleep(1)


# C:\work\ciledug\ciledug\fmusperintah\vendor\python-prompt-toolkit\examples\progress-bar\styled-tqdm-1.py
style4 = Style.from_dict({"": "cyan"})

def progress5():
    custom_formatters = [
        formatters.Label(suffix=": "),
        formatters.Bar(start="|", end="|", sym_a="#", sym_b="#", sym_c="-"),
        formatters.Text(" "),
        formatters.Progress(),
        formatters.Text(" "),
        formatters.Percentage(),
        formatters.Text(" [elapsed: "),
        formatters.TimeElapsed(),
        formatters.Text(" left: "),
        formatters.TimeLeft(),
        formatters.Text(", "),
        formatters.IterationsPerSecond(),
        formatters.Text(" iters/sec]"),
        formatters.Text("  "),
    ]
    with ProgressBar(style=style4, formatters=custom_formatters) as pb:
        for i in pb(range(1600), label="Installing"):
            time.sleep(0.01)

# C:\work\ciledug\ciledug\fmusperintah\vendor\python-prompt-toolkit\examples\progress-bar\styled-tqdm-2.py
style5 = Style.from_dict({"bar-a": "reverse"})

def progress6():
    custom_formatters = [
        formatters.Label(suffix=": "),
        formatters.Percentage(),
        formatters.Bar(start="|", end="|", sym_a=" ", sym_b=" ", sym_c=" "),
        formatters.Text(" "),
        formatters.Progress(),
        formatters.Text(" ["),
        formatters.TimeElapsed(),
        formatters.Text("<"),
        formatters.TimeLeft(),
        formatters.Text(", "),
        formatters.IterationsPerSecond(),
        formatters.Text("it/s]"),
    ]
    with ProgressBar(style=style5, formatters=custom_formatters) as pb:
        for i in pb(range(1600), label="Installing"):
            time.sleep(0.01)

# C:\work\ciledug\ciledug\fmusperintah\vendor\python-prompt-toolkit\examples\progress-bar\two-tasks.py

def progress7():
    with ProgressBar() as pb:
        # Two parallal tasks.
        def task_1():
            for i in pb(range(100)):
                time.sleep(0.05)

        def task_2():
            for i in pb(range(150)):
                time.sleep(0.08)

        # Start threads.
        t1 = threading.Thread(target=task_1)
        t2 = threading.Thread(target=task_2)
        t1.daemon = True
        t2.daemon = True
        t1.start()
        t2.start()

        # Wait for the threads to finish. We use a timeout for the join() call,
        # because on Windows, join cannot be interrupted by Control-C or any other
        # signal.
        for t in [t1, t2]:
            while t.is_alive():
                t.join(timeout=0.5)

# C:\work\ciledug\ciledug\fmusperintah\vendor\python-prompt-toolkit\examples\progress-bar\unknown-length.py

def progress8_data():
    """
    A generator that produces items. len() doesn't work here, so the progress
    bar can't estimate the time it will take.
    """
    yield from range(1000)

def progress8():
    with ProgressBar() as pb:
        for i in pb(progress8_data()):
            time.sleep(0.1)

# C:\work\ciledug\ciledug\fmusperintah\vendor\python-prompt-toolkit\examples\progress-bar\styled-apt-get-install.py
style_apt = Style.from_dict(
    {
        "label": "bg:#ffff00 #000000",
        "percentage": "bg:#ffff00 #000000",
        "current": "#448844",
        "bar": "",
    }
)
def progress9():
    custom_formatters = [
        formatters.Label(),
        formatters.Text(": [", style="class:percentage"),
        formatters.Percentage(),
        formatters.Text("]", style="class:percentage"),
        formatters.Text(" "),
        formatters.Bar(sym_a="#", sym_b="#", sym_c="."),
        formatters.Text("  "),
    ]

    with ProgressBar(
        style=style_apt,
        formatters=custom_formatters) as pb:
        for i in pb(range(1600), label="Installing"):
            time.sleep(0.01)

# C:\work\ciledug\ciledug\fmusperintah\vendor\python-prompt-toolkit\examples\progress-bar\nested-progress-bars.py
def progress10():
    with ProgressBar(
        title=HTML('<b fg="#aa00ff">Nested progress bars</b>'),
        bottom_toolbar=HTML(" <b>[Control-L]</b> clear  <b>[Control-C]</b> abort"),
    ) as pb:
        for i in pb(range(6), label="Main task"):
            for j in pb(range(200), label=f"Subtask <{i + 1}>", remove_when_done=True):
                time.sleep(0.01)

# C:\work\ciledug\ciledug\fmusperintah\vendor\python-prompt-toolkit\examples\progress-bar\many-parallel-tasks.py
def progress11():
    with ProgressBar(
        title=HTML("<b>Example of many parallel tasks.</b>"),
        bottom_toolbar=HTML("<b>[Control-L]</b> clear  <b>[Control-C]</b> abort"),
    ) as pb:

        def run_task(label, total, sleep_time):
            for i in pb(range(total), label=label):
                time.sleep(sleep_time)

        threads = [
            threading.Thread(target=run_task, args=("First task", 50, 0.1)),
            threading.Thread(target=run_task, args=("Second task", 100, 0.1)),
            threading.Thread(target=run_task, args=("Third task", 8, 3)),
            threading.Thread(target=run_task, args=("Fourth task", 200, 0.1)),
            threading.Thread(target=run_task, args=("Fifth task", 40, 0.2)),
            threading.Thread(target=run_task, args=("Sixth task", 220, 0.1)),
            threading.Thread(target=run_task, args=("Seventh task", 85, 0.05)),
            threading.Thread(target=run_task, args=("Eight task", 200, 0.05)),
        ]

        for t in threads:
            t.daemon = True
            t.start()

        # Wait for the threads to finish. We use a timeout for the join() call,
        # because on Windows, join cannot be interrupted by Control-C or any other
        # signal.
        for t in threads:
            while t.is_alive():
                t.join(timeout=0.5)

# C:\work\ciledug\ciledug\fmusperintah\vendor\python-prompt-toolkit\examples\progress-bar\colored-title-and-label.py
def progress12():
    title = HTML('Downloading <style bg="yellow" fg="black">4 files...</style>')
    label = HTML("<ansired>some file</ansired>: ")

    with ProgressBar(title=title) as pb:
        for i in pb(range(800), label=label):
            time.sleep(0.01)

# C:\work\ciledug\ciledug\fmusperintah\vendor\python-prompt-toolkit\examples\progress-bar\a-lot-of-parallel-tasks.py
def progress13():
    with ProgressBar(
        title=HTML("<b>Example of many parallel tasks.</b>"),
        bottom_toolbar=HTML("<b>[Control-L]</b> clear  <b>[Control-C]</b> abort"),
    ) as pb:

        def run_task(label, total, sleep_time):
            """Complete a normal run."""
            for i in pb(range(total), label=label):
                time.sleep(sleep_time)

        def stop_task(label, total, sleep_time):
            """Stop at some random index.

            Breaking out of iteration at some stop index mimics how progress
            bars behave in cases where errors are raised.
            """
            stop_i = random.randrange(total)
            bar = pb(range(total), label=label)
            for i in bar:
                if stop_i == i:
                    bar.label = f"{label} BREAK"
                    break
                time.sleep(sleep_time)

        threads = []

        for i in range(160):
            label = "Task %i" % i
            total = random.randrange(50, 200)
            sleep_time = random.randrange(5, 20) / 100.0

            threads.append(
                threading.Thread(
                    target=random.choice((run_task, stop_task)),
                    args=(label, total, sleep_time),
                )
            )

        for t in threads:
            t.daemon = True
            t.start()

        # Wait for the threads to finish. We use a timeout for the join() call,
        # because on Windows, join cannot be interrupted by Control-C or any other
        # signal.
        for t in threads:
            while t.is_alive():
                t.join(timeout=0.5)

# C:\work\ciledug\ciledug\fmusperintah\vendor\python-prompt-toolkit\examples\progress-bar\custom-key-bindings.py
def progress14():
    bottom_toolbar = HTML(
        ' <b>[f]</b> Print "f" <b>[q]</b> Abort  <b>[x]</b> Send Control-C.'
    )

    # Create custom key bindings first.
    kb = KeyBindings()
    cancel = [False]

    @kb.add("f")
    def _(event):
        print("You pressed `f`.")

    @kb.add("q")
    def _(event):
        "Quit by setting cancel flag."
        cancel[0] = True

    @kb.add("x")
    def _(event):
        "Quit by sending SIGINT to the main thread."
        os.kill(os.getpid(), signal.SIGINT)

    # Use `patch_stdout`, to make sure that prints go above the
    # application.
    with patch_stdout():
        with ProgressBar(key_bindings=kb, bottom_toolbar=bottom_toolbar) as pb:
            for i in pb(range(800)):
                time.sleep(0.01)
                if cancel[0]:
                    break

def handle_minus(text, self_session, self_refresh_completer):
    """
    -c
        clear
    -n
        newline
    ->
        copy from text_area, ini percuma krn jk kita ngetik -> maka text_area berubah content
    ->filename
        save to file
    -50
        tinggi jadi 50
    -:filename
    -@
        clipboard to editor
    ???
        editor to clipboard
    """
    if text == 'c':
        self_session.text_area_editor.text = ''
    elif text.startswith('+'):  # append literal to editor
        content = text.removeprefix('+')
        self_session.text_area_editor.text += content.replace('\\n', '\n').replace('\\t', '\t')
    elif text == '@':  # clipboard => editor
        content = trypaste()
        self_session.text_area_editor.text = content
    elif text == '>@':  # editor => clipboard
        trycopy(self_session.text_area_editor.text)
    elif text.startswith('>'):  # ->filename, save to file
        # self_session.text_area_editor.text = self_session.text_area.text
        filepath = text.removeprefix('>').strip()
        if isfile(filepath):
            file_write(filepath, self_session.text_area_editor.text)
    elif text.startswith(':'):  # -:filename, load from file
        filepath = text.removeprefix(':').strip()
        if isfile(filepath):
            self_session.text_area_editor.text = file_content(filepath)
    elif text.isdigit():  # ganti tinggi
        nilai = int(text)
        if 0<nilai<100:
            config_app['text_area_height'] = nilai
            self_refresh_completer()
    elif text == '-':  # -- utk toggle show editor
        config_app['show_textarea_editor'] = not config_app['show_textarea_editor']
        self_refresh_completer()
    elif text == '-1':  # --1 utk toggle show editor
        config_app['show_textarea_editor'] = not config_app['show_textarea_editor']
        self_refresh_completer()
    elif text == '--':  # --- utk toggle show textarea+editor
        config_app['show_textarea'] = not config_app['show_textarea']
        self_refresh_completer()
    elif text == '-2':  # --2 utk toggle show textarea+editor
        config_app['show_textarea'] = not config_app['show_textarea']
        self_refresh_completer()
    elif text == '-3':  # --3 utk toggle show show_editor_toolbar
        config_app['show_editor_toolbar'] = not config_app['show_editor_toolbar']
        self_refresh_completer()
    elif text.startswith('#'):
        # coba berbagai progress bar
        pb = text.removeprefix('#').strip()
        pb = int(pb)
        if pb == 1:
            # print('progress1')
            progress1()
        elif pb == 2:
            progress2()
        elif pb == 3:
            progress3()
        elif pb == 4:
            progress_rainbow()
        elif pb == 5:
            progress5()
        elif pb == 6:
            progress6()
        elif pb == 7:
            progress7()
        elif pb == 8:
            progress8()
        elif pb == 9:
            progress9()
        elif pb == 10:
            progress10()
        elif pb == 11:
            progress11()
        elif pb == 12:
            progress12()
        elif pb == 13:
            progress13()
        elif pb == 14:
            progress14()
        else:
            indah4('-#<antara 1 dan 14>', warna='magenta')
