import os

def run_python_file(working_directory, file_path, args=[]):
    full_path = os.path.abspath(os.path.join(working_directory, file_path))
    valid_path = full_path.startswith(os.path.abspath(working_directory))
    
    if not valid_path:
        return f'   Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
    
    if not os.path.exists(full_path):
        return f'Error: File "{file_path}" not found.'