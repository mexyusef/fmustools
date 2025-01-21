import sys
import subprocess
import tempfile
import os
import configparser
from PyQt6.QtWidgets import (
    QApplication, QWidget, QPushButton, QVBoxLayout, QComboBox, 
    QHBoxLayout, QLabel
)
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QIcon, QFont
from PyQt6.QtSvgWidgets import QSvgWidget

# Firefox executable path and URL to open
FIREFOX_PATH = r"C:/Program Files/Mozilla Firefox/firefox.exe"
URL = "https://hailuoai.video/"

# Function to fetch Firefox profiles
def get_firefox_profiles():
    profiles = {}
    appdata_path = os.getenv('APPDATA')  # Gets the %APPDATA% path
    profiles_ini_path = os.path.join(appdata_path, "Mozilla", "Firefox", "profiles.ini")

    if not os.path.exists(profiles_ini_path):
        print("profiles.ini not found. Ensure Firefox is installed.")
        return profiles

    config = configparser.ConfigParser()
    config.read(profiles_ini_path)

    for section in config.sections():
        if section.startswith('Profile'):
            name = config.get(section, 'Name')
            path = config.get(section, 'Path')
            profiles[name] = path

    return profiles

# Create temporary SVG icons
def create_temp_svgs():
    svg_dir = tempfile.mkdtemp()
    icons = {
        "notepad_icon.svg": """<svg width="64" height="64" xmlns="http://www.w3.org/2000/svg"><rect width="100%" height="100%" fill="#1E3A8A"/><text x="32" y="40" font-size="24" fill="#FFF" text-anchor="middle">N</text></svg>""",
        "firefox_icon.svg": """<svg width="64" height="64" xmlns="http://www.w3.org/2000/svg"><rect width="100%" height="100%" fill="#1F2937"/><text x="32" y="40" font-size="24" fill="#F97316" text-anchor="middle">F</text></svg>""",
    }
    icon_paths = {}
    for icon_name, svg_data in icons.items():
        icon_path = os.path.join(svg_dir, icon_name)
        with open(icon_path, 'w') as svg_file:
            svg_file.write(svg_data)
        icon_paths[icon_name] = icon_path
    return icon_paths

class LauncherApp(QWidget):
    def __init__(self, icon_paths):
        super().__init__()
        self.setWindowTitle("Application Launcher with Firefox Profiles")
        self.setWindowFlags(Qt.WindowType.FramelessWindowHint | Qt.WindowType.WindowStaysOnTopHint)
        self.setFixedSize(600, 120)
        
        # Main layout with gradient background
        main_layout = QVBoxLayout()
        main_layout.setContentsMargins(0, 0, 0, 0)
        self.setStyleSheet("""
            QWidget {
                background: qlineargradient(
                    spread:pad, x1:0, y1:0, x2:1, y2:1, 
                    stop:0 #2B3D52, stop:1 #1E1E2F
                );
                border-radius: 10px;
            }
        """)

        # Header layout for the title and close button
        header_layout = QHBoxLayout()
        
        # Header label
        header_label = QLabel("Select and Launch Applications")
        header_label.setFont(QFont("Arial", 14))
        header_label.setStyleSheet("color: #A8C0FF;")
        header_label.setAlignment(Qt.AlignmentFlag.AlignLeft)
        header_layout.addWidget(header_label)
        
        # Close button
        close_button = QPushButton("✖")
        close_button.setFixedSize(30, 30)
        close_button.setStyleSheet("color: #FF4D4D; font-size: 16px; background-color: transparent;")
        close_button.clicked.connect(self.close)
        header_layout.addWidget(close_button)
        
        # Add header layout to main layout
        main_layout.addLayout(header_layout)
        
        # Horizontal layout for app dropdown and launch button
        button_layout = QHBoxLayout()
        
        # Applications to launch with SVG icons
        self.applications = {
            "Notepad": ("notepad.exe", icon_paths["notepad_icon.svg"]),
        }

        # Fetch and add Firefox profiles
        firefox_profiles = get_firefox_profiles()
        for profile_name in firefox_profiles.keys():
            self.applications[f"Firefox - {profile_name}"] = (("firefox", profile_name), icon_paths["firefox_icon.svg"])
        
        # Application dropdown with icon preview
        self.app_dropdown = QComboBox()
        for app_name, (cmd, icon_path) in self.applications.items():
            icon = QIcon(icon_path)
            self.app_dropdown.addItem(icon, app_name)
        button_layout.addWidget(self.app_dropdown)
        
        # Launch button
        launch_button = QPushButton("Launch")
        launch_button.clicked.connect(self.launch_application)
        button_layout.addWidget(launch_button)

        main_layout.addLayout(button_layout)
        self.setLayout(main_layout)

    def launch_application(self):
        app_name = self.app_dropdown.currentText()
        cmd, icon_path = self.applications[app_name]

        # Launch the app without tracking it by Python process (no ResourceWarning)
        if isinstance(cmd, tuple) and cmd[0] == "firefox":
            profile_name = cmd[1]
            subprocess.Popen([FIREFOX_PATH, '-no-remote', '-P', profile_name, URL],
                             creationflags=subprocess.DETACHED_PROCESS | subprocess.CREATE_NEW_PROCESS_GROUP)
        else:
            subprocess.Popen(cmd, creationflags=subprocess.DETACHED_PROCESS | subprocess.CREATE_NEW_PROCESS_GROUP)

def run_launcher():
    icon_paths = create_temp_svgs()
    app = QApplication.instance() or QApplication(sys.argv)
    launcher = LauncherApp(icon_paths)
    launcher.show()
    
    if not QApplication.instance():
        app.exec()

# def run_launcher():
#     icon_paths = create_temp_svgs()
#     app = QApplication.instance() or QApplication(sys.argv)
#     launcher = LauncherApp(icon_paths)
#     launcher.show()
#     app.exec() if not QApplication.instance() else None

def run_launcher2():
    app = QApplication(sys.argv)
    icon_paths = create_temp_svgs()
    launcher = LauncherApp(icon_paths)
    launcher.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    run_launcher2()
