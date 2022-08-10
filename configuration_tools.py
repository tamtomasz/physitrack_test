import os
import time
from sys import platform
import subprocess
import shutil

from pathlib import Path, WindowsPath

VENV_NAME = 'venv123'

def _wait_for_file(file_path: Path):
    start_time = time.time()


def create_venv():
    print("Creating virtual env...")
    current_path = Path(__file__).parent
    if platform == "linux" or platform == "linux2":
        script_file = current_path.joinpath('setup_and_run_linux.sh')
        os.chmod(str(script_file), 0o755)
        subprocess.call(f'./{script_file.name}')
    elif platform == "darwin":
        #  Mac OS config
        ...
    elif platform == "win32":
        script_file = current_path.joinpath('setup_and_run_win.bat')
        subprocess.Popen([f'{str(script_file)}'])


def activate_venv():
    print("Activating virtual env...")
    current_path = Path(__file__).parent
    activate_this_file = current_path.joinpath('activate_this.py')
    activate_this_file_destination = current_path.joinpath(f'{VENV_NAME}/Scripts/activate_this.py')
    shutil.copy(str(activate_this_file), str(activate_this_file_destination))
    exec(open(str(activate_this_file_destination)).read())




