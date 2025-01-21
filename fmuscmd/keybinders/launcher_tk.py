import tkinter as tk
from tkinter import ttk, messagebox
import subprocess
import os
import configparser

# Path to Firefox executable and URL
FIREFOX_PATH = r"C:/Program Files/Mozilla Firefox/firefox.exe"
URL = "https://hailuoai.video"

# Basic applications
applications = {
    "Notepad": "notepad.exe",
    "Notepad++": "C:/Program Files/Notepad++/notepad++.exe",
    "Chrome": "C:/Program Files/Google/Chrome/Application/chrome.exe",
    "Edge": "msedge.exe",
    "Windows Terminal": "wt.exe",
    "PowerShell": "powershell.exe",
    "VLC Media Player": "C:/Program Files/VideoLAN/VLC/vlc.exe",
    "Paint": "mspaint.exe",
    "VS Code": "code.exe"
}

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
            profiles[name] = config.get(section, 'Path')
    
    return profiles

# Include Firefox profiles in the applications list
firefox_profiles = get_firefox_profiles()
for profile_name in firefox_profiles.keys():
    applications[f"Firefox - {profile_name}"] = ("firefox", profile_name)  # Store as tuple to distinguish profile launch

class AppLauncher(tk.Tk):
    def __init__(self):
        super().__init__()

        # Window setup
        self.title("App Launcher")
        self.geometry("800x100")
        self.overrideredirect(True)
        self.attributes("-topmost", True)

        # Background and styling
        self.configure(bg="#1E1E2F")
        self.style = ttk.Style()
        self.style.theme_use("clam")
        self.style.configure("TButton", font=("Helvetica", 10), background="#2B3D52", foreground="white")
        self.style.configure("TCombobox", font=("Helvetica", 10), background="#2B3D52", foreground="white")

        # Draggable window
        self.bind("<B1-Motion>", self.move_window)
        self.bind("<ButtonPress-1>", self.click_window)

        # App selector
        self.app_var = tk.StringVar()
        self.app_selector = ttk.Combobox(self, textvariable=self.app_var, values=list(applications.keys()), state="readonly")
        self.app_selector.set("Select Application")
        self.app_selector.grid(row=0, column=0, padx=10, pady=10)

        # Launch button
        self.launch_button = ttk.Button(self, text="Launch", command=self.launch_app)
        self.launch_button.grid(row=0, column=1, padx=10)

        # Close button
        self.close_button = ttk.Button(self, text="✖", command=self.quit_app)
        self.close_button.grid(row=0, column=2, padx=10)

        # Alignment customization
        self.alignment_menu = tk.Menu(self, tearoff=0)
        self.alignment_menu.add_command(label="Align Top", command=lambda: self.align("top"))
        self.alignment_menu.add_command(label="Align Bottom", command=lambda: self.align("bottom"))
        self.alignment_menu.add_command(label="Align Left", command=lambda: self.align("left"))
        self.alignment_menu.add_command(label="Align Right", command=lambda: self.align("right"))

        self.bind("<Button-3>", self.show_menu)

    def launch_app(self):
        app_name = self.app_var.get()
        if app_name in applications:
            cmd = applications[app_name]
            try:
                if isinstance(cmd, tuple) and cmd[0] == "firefox":  # Firefox profile launch
                    profile_path = firefox_profiles[cmd[1]]
                    subprocess.Popen([FIREFOX_PATH, '-no-remote', '-P', cmd[1], URL], creationflags=subprocess.DETACHED_PROCESS)
                else:
                    subprocess.Popen(cmd, creationflags=subprocess.DETACHED_PROCESS)
            except Exception as e:
                messagebox.showerror("Launch Error", f"Could not launch {app_name}: {e}")
        else:
            messagebox.showwarning("Select Application", "Please select an application to launch.")

    def quit_app(self):
        self.quit()

    def show_menu(self, event):
        self.alignment_menu.post(event.x_root, event.y_root)

    def align(self, position):
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()

        if position == "top":
            self.geometry(f"{self.winfo_width()}x100+0+0")
        elif position == "bottom":
            self.geometry(f"{self.winfo_width()}x100+0+{screen_height - 100}")
        elif position == "left":
            self.geometry(f"100x{self.winfo_height()}+0+0")
        elif position == "right":
            self.geometry(f"100x{self.winfo_height()}+{screen_width - 100}+0")

    def move_window(self, event):
        x = self.winfo_pointerx() - self._offset_x
        y = self.winfo_pointery() - self._offset_y
        self.geometry(f"+{x}+{y}")

    def click_window(self, event):
        self._offset_x = event.x
        self._offset_y = event.y

def run_launcher():
    app = AppLauncher()
    app.mainloop()

if __name__ == "__main__":
    run_launcher()
