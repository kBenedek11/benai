import os

def write_file(working_directory, file_path, content):
    full_path = os.path.abspath(os.path.join(working_directory, file_path))
    valid_path = full_path.startswith(os.path.abspath(working_directory))

    if not valid_path:
        return f'Error: Cannot write "{file_path}" as it is outside the permitted working directory'
    if not os.path.exists(os.path.dirname(full_path)):
        try:
            os.makedirs(os.path.dirname(full_path))
        except Exception as e:
            return f"Error: {e}"
    try:   
        with open(full_path, "w") as f:
            f.write(content)
    except Exception as exc:
        return f"Error: {exc}"

    return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'