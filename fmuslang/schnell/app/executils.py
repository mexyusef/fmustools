from .executor import LANGUAGES, ExecFile, FileExecutor
from .printutils import indah4


def execute_code(code):
    code = code.strip()
    if code:
        if code in LANGUAGES:
            indah4(f"executing {code}", warna='green')
            # ExecFile.exec(code)
            FileExecutor().exec(code)
        else:
            indah4(f"{code} not in {LANGUAGES}", warna='red')
