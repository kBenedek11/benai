import os

def get_files_info(working_directory, directory="."):
    full_path = os.path.abspath(os.path.join(working_directory, directory))
    valid_path = full_path.startswith(os.path.abspath(working_directory))
    result = []
    if not valid_path:
        return f'   Error: Cannot list "{directory}" as it is outside the permitted working directory'
    
    if not os.path.isdir(full_path): 
        return f'   Error: "{directory}" is not a directory'
    try:
        dir_contents = os.listdir(full_path)
        for file in dir_contents:
            file_path = os.path.join(full_path, file)
            is_file = os.path.isfile(file_path)
            file_size = os.path.getsize(file_path)
            is_dir = os.path.isdir(file_path)
            result.append(f"- {file}: file_size={file_size} bytes, is_dir={is_dir}")
        return "\n".join(result)
    except Exception as exc:
        return f'   Error listing files: "{exc}"'
    