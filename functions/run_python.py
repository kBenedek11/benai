import os
import subprocess
import sys

def run_python_file(working_directory, file_path, args=[]):
    full_path = os.path.abspath(os.path.join(working_directory, file_path))
    valid_path = full_path.startswith(os.path.abspath(working_directory))
    
    if not valid_path:
        return f'   Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
    
    if not os.path.exists(full_path):
        return f'Error: File "{file_path}" not found.'
    
    if not full_path.endswith(".py"):
        return f'Error: "{file_path}" is not a Python file.'
    try:
        completed_process = subprocess.run([sys.executable, full_path] + args, capture_output = True, timeout = 30)
        if not completed_process.returncode == 0:
            return f"STDOUT: {completed_process.stdout}, STDERR: {completed_process.stderr}, Process exited with code {completed_process.returncode}"
        if not completed_process.stdout:
            return "No output produced"
        return f"STDOUT: {completed_process.stdout}, STDERR: {completed_process.stderr} "
    except Exception as e:
        return f"Error: executing Python file: {e}"
    

