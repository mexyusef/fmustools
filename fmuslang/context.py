global_context = {
    # 'current_chart'               : Chartlang.HIGHCHART.value,
    "current_chart": "highchart",
    # 'current_gui'                 : Guilang.PYQT5.value,
    "current_gui": "pyqt5",
    # 'current_language'            : Lang.PY.value,
    "current_language": "py",
    # mestinya jk invoke flutter program, nilai ini jg langsung berubah
    # 'current_mobile'              : Mobilelang.FLUTTER.value,
    "current_mobile": "flutter",
    # 'current_declarative'         : Declang.REACT.value,
    "current_declarative": "react",
    "override_language": None,
    # ini utk `react itu hasilkan baris entry react utk vscode atau tampilkan entry bahasa react?
    "petik_vscode": True,
    "pyautogui_input": None,
    # 'print_after_process'         : True,
    # tujuannya utk generate file dll
    "working_folder": None,
    # $$link= dan $$img= apakah diaktifkan
    "fmus_expansion_mode": True,
    "fmus_editor_folding": True,
    # 'fmus_expansion_mode'         : False,
    "clock_reminder": False,
    "quick_viewer_folding": True,
    # /ketik)
    "characters_per_minute": 8000,
    # ctrl alt p di fmus editor
    "current_active_language": "py",
    "current_tab": " " * 2,
}

# biar gampang importnya
from schnell.app.appconfig import command_prompt_data, command_prompt_data_extension

redis_context = {
    "active": None,
    "db": -1,
}
