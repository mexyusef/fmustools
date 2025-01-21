# import os, pyperclip, sys
# from pprint import pprint
from uuid import uuid4 as u4
# envfile = "c:/users/usef/work/sidoarjo/schnell/.env"
# from dotenv import load_dotenv
# load_dotenv(envfile)
# schnelldir = os.environ['ULIBPY_BASEDIR']
# sys.path.extend([schnelldir, '..'])
# print(schnelldir)
import sys
from pathlib import Path
sidoarjodir = Path(__file__).resolve().parent.parent.parent.parent.parent
#                              file     langs quick app     sch   sid
sys.path.append(sidoarjodir)

from schnell.app.transpiler.frontend.main import process_language
from schnell.app.printutils import indah4
from schnell.app.treeutils import (
    anak,
    data,
    token,
    child1,
    child2,
    child3,
    child4,
    child,
    chdata,
    chtoken,
    ispohon, istoken,
    beranak,
    sebanyak,
    jumlahanak,
)
from schnell.app.dirutils import joiner, joinhere
from schnell.app.fileutils import file_write, file_content
from schnell.app.utils import env_get


from schnell.app.stringutils import tabify_content_tab, tabify_content_space, tabify_contentlist_tab, tabify_contentlist_space

output = {}
hasil = []
layoutcode = ''
final_result = ''

kode_output = """
package main

import (
	"os"

	"github.com/therecipe/qt/widgets"
)

func main() {
	// needs to be called once before you can start using the QWidgets
	app := widgets.NewQApplication(len(os.Args), os.Args)


	// create a window
	// with a minimum size of 250*200
	// and sets the title to "Hello Widgets Example"
	window := widgets.NewQMainWindow(nil, 0)
	window.SetMinimumSize2(250, 200)
	window.SetWindowTitle("Hello Widgets Example")

	// create a regular widget
	// give it a QVBoxLayout
	// and make it the central widget of the window
	widget := widgets.NewQWidget(nil, 0)
	widget.SetLayout(widgets.NewQVBoxLayout()) // akses dg widget.Layout()
	window.SetCentralWidget(widget)


__LAYOUT_CONTENT__



	// make the window visible
	window.Show()

	// start the main Qt event loop
	// and block until app.Exit() is called
	// or the window is closed by the user
	app.Exec()
}
"""


def reset():
    global output, hasil, layoutcode, final_result
    output.clear()
    hasil = []
    layoutcode = ''
    final_result = ''

