
import os
import sys
import markdown
import tempfile
import webbrowser

from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QPlainTextEdit, QVBoxLayout, QFrame, QMenu, QFileDialog, QLineEdit, QShortcut
from PyQt5.QtGui import QFont, QKeySequence
from PyQt5.QtGui import QFontDatabase, QFont
from PyQt5.QtCore import Qt


WINDOW_TITLE = 'Distraction Less'
FONT_SIZE = 11
INFO_FONT_SIZE = 11
MAXIMUM_WIDTH = 1280
BACKGROUND_COLOR = '#f3f3e0'


def get_monospaced_font(size):
    '''
    Takes a size and finds a monospaced font from system fonts,
    sets the font size and then returns it
    '''
    monospace_font = QFontDatabase.systemFont(QFontDatabase.FixedFont)
    monospace_font.setPointSize(size)
    return monospace_font


def resize_screen_ratio(object, screenw, screenh, posx_ratio=1/2, ratio=1/6, wratio=0, delta = 60):
    """
    screen_geometry = PyQt5.QtWidgets.QDesktopWidget().screenGeometry(-1)
    screenw, screenh = screen_geometry.width(), screen_geometry.height()
    resize_screen_ratio(w1, screenw, screenh, 1/4, 1/5)
    resize_screen_ratio(w2, screenw, screenh, 3/4, 1/5)

    object hrs punya method resize dan move.
    """
    if not wratio:
        wratio = ratio
    # print('wratio:', wratio)
    lebar, tinggi = int(screenw*wratio),int(screenh*ratio)
    object.resize(lebar, tinggi)
    posx = int((screenw-lebar)*posx_ratio)    
    posy = int((screenh - tinggi)/2) - delta
    object.move(posx, posy)


def resize_screen_ratio_simple(object, posx_ratio=1/2, ratio=1/6, wratio=0, delta = 60):
    from PyQt5.QtWidgets import QDesktopWidget
    screen_geometry = QDesktopWidget().screenGeometry(-1)
    screenw, screenh = screen_geometry.width(), screen_geometry.height()
    resize_screen_ratio(object, screenw, screenh, posx_ratio, ratio, wratio, delta)


class App(QMainWindow):
    '''
    The main Qt application for the writer.
    '''
    def __init__(self):
        super().__init__()
        
        self.working_file_name = ''

        self.InitUI()
        
    def InitUI(self):

        # Set up window & settings
        self.setMinimumSize(300, 200)

        # self.resize(800, 600)
        # self.move(400, 100)
        resize_screen_ratio_simple(self, ratio=0.5, wratio=0.8)

        self.setWindowTitle(WINDOW_TITLE)

        # == Widgets and Layout ==
        # Create the central widget
        self.widget = QWidget(self)
        self.widget.setStyleSheet('background-color:'+ BACKGROUND_COLOR +';')

        # Create default text font
        self.input_font = get_monospaced_font(FONT_SIZE)

        # Create info bar font
        self.info_font = get_monospaced_font(INFO_FONT_SIZE)

        # Create LineEdit for the top info bar
        # This bar is for displaying info about
        # the current file
        self.top_info_bar = QLineEdit(self.widget)
        self.top_info_bar.setReadOnly(True)
        self.top_info_bar.setMaximumWidth(MAXIMUM_WIDTH)

        # Set font and style
        self.top_info_bar.setStyleSheet('qproperty-alignment: AlignCenter; background-color: #d34db33f;')
        self.top_info_bar.setFont(self.info_font)
        self.top_info_bar.setFrame(QFrame.NoFrame)
        self.update_top_info_bar()

        # Create text feild
        self.center_text = QPlainTextEdit(self.widget)
        self.center_text.setMaximumWidth(MAXIMUM_WIDTH)
        self.center_text.setFont(self.input_font)

        # Disable frame style
        self.center_text.setFrameStyle(QFrame.NoFrame)

        # Text feild custom context menu
        self.center_text.setContextMenuPolicy(Qt.CustomContextMenu)
        self.center_text.customContextMenuRequested.connect(self.context_menu_event)

        # Create VBox and set it as layout
        self.widget.setLayout(QVBoxLayout())

        # Layout settings
        self.widget.layout().addWidget(self.top_info_bar)
        self.widget.layout().addWidget(self.center_text)
        self.widget.layout().setContentsMargins(0,0,0,0) 
        self.widget.layout().setAlignment(Qt.AlignCenter)

        self.setCentralWidget(self.widget)

        # Init keyboard shortcuts
        self.InitKeyboard()

    def InitKeyboard(self):
        ''' Init keyboard shortcuts '''
        # == KEYBOARD SHORTCUTS ==

        # Save, (Ctrl+S)
        self.save_keyboard_shortcut = QShortcut(QKeySequence('Ctrl+S'), self)
        self.save_keyboard_shortcut.activated.connect(self.save_text_file)

        self.saveas_keyboard_shortcut = QShortcut(QKeySequence(Qt.SHIFT + Qt.CTRL + Qt.Key_S),self)
        self.saveas_keyboard_shortcut.activated.connect(self.saveas_text_file)

        # Open file (Ctrl+O)
        self.open_keyboard_shortcut = QShortcut(QKeySequence('Ctrl+O'), self)
        self.open_keyboard_shortcut.activated.connect(self.open_text_file)

        # Export to browser
        self.export_keyboard_shortcut = QShortcut(QKeySequence(Qt.SHIFT + Qt.CTRL + Qt.Key_E), self)
        self.export_keyboard_shortcut.activated.connect(self.export_to_browser)

        # Fullscreen toggle (F11)
        self.fullscreen_keyboard_shortcut = QShortcut(QKeySequence(Qt.Key_F11), self)
        self.fullscreen_keyboard_shortcut.activated.connect(self.toggle_fullscreen)

    def save_text_file(self):
        '''
        Saves the written text to a file
        '''
        text_to_save = self.center_text.toPlainText()
        if self.working_file_name:
            with open(self.working_file_name, 'w', encoding='utf-8') as save_file:
                save_file.write(text_to_save)
        else:
            name = QFileDialog.getSaveFileName(self,'Save as...',self.working_file_name,'All Files (*);;Text Files (*.txt)')[0]

            if name:
                with open(name, 'w', encoding='utf-8') as save_file:
                    save_file.write(text_to_save)

                # Show the new file path
                self.working_file_name = name

                # Update info bar
                self.update_top_info_bar()

    def saveas_text_file(self):
        # Set file name to '' to save as new file
        self.working_file_name = ''
        self.save_text_file()

    def open_text_file(self):
        ''' Opens a file and '''
        name = QFileDialog.getOpenFileName(self,'Open a File',self.working_file_name,'All Files (*);;Text Files (*.txt);;HTML Files (*.html)')[0]
        
        if name:
            with open(name, 'r', encoding='utf-8') as new_file:
                new_text = new_file.read()

            self.center_text.setPlainText(new_text)
        
            # Set current file name to the opened one.
            self.working_file_name = name
            
            # Update info bar
            self.update_top_info_bar()

    def export_to_browser(self):
        # Grab the raw markdown text
        markdown_text = self.center_text.toPlainText()
        # Convert it to html using the markdown module
        markdown_html = markdown.markdown(markdown_text)
        
        # Create tempfile for the html
        # The tuple consists of file descriptor and path
        temp_file_descriptor, temp_file_path = tempfile.mkstemp(suffix='.html',text=True)

        # Write html to temp file
        os.write(temp_file_descriptor, markdown_html.encode(encoding='utf-8'))

        # Open the temp file in the browser
        webbrowser.open('file://' + os.path.realpath(temp_file_path))

        # Close the temp file
        os.close(temp_file_descriptor)

    def context_menu_event(self, event):
        '''
        This function defines the context menu that
        appears on right-click. 
        '''

        context_menu = QMenu(self)

        copy_action = context_menu.addAction('Copy\t(Ctrl+C)') # Copy to clipboard
        paste_action = context_menu.addAction('Paste\t(Ctrl+V)') # Paste clipboard

        # Save file
        save_action = context_menu.addAction('Save\t(Ctrl+S)')
        # Save file as...
        save_as_action = context_menu.addAction('Save as...\t(Ctrl+Shift+S)') 
        # Open file
        open_action = context_menu.addAction('Open file\t(Ctrl+O)')

        # Export and open in browser
        export_action = context_menu.addAction('Export to browser\t(Ctrl+Shift+E)')

        action = context_menu.exec_(self.center_text.mapToGlobal(event))

        # Copy and paste actions
        if action == copy_action:
            self.center_text.copy()
        elif action == paste_action:
            self.center_text.paste()

        # File managment actions 
        elif action == save_as_action:
            self.saveas_text_file()
        elif action == save_action:
            self.save_text_file()
        elif action == open_action:
            self.open_text_file()

        # Markdown actions
        elif action == export_action:
            self.export_to_browser()

    def update_top_info_bar(self):
        if self.working_file_name != '':
            self.top_info_bar.setText(self.working_file_name)
        else:
            self.top_info_bar.setText('New File')

    def toggle_fullscreen(self):
        ''' Toggles fullscreen on and off '''

        if self.isFullScreen():
            self.showNormal()
        else:
            self.showFullScreen()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = App()
    w.show()
    sys.exit(app.exec_())
