import os
from functions.config import *
from google import genai
from google.genai import types

def get_file_content(working_directory, file_path):
    full_path = os.path.abspath(os.path.join(working_directory, file_path))
    valid_path = full_path.startswith(os.path.abspath(working_directory))
    if not valid_path:
        return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
    
    if not os.path.isfile(full_path): 
        return f'Error: File not found or is not a regular file: "{file_path}"'
    
    try:

        with open(full_path, "r") as f:
            file_content_string = f.read(MAX_CHARS)
        if len(file_content_string) >= MAX_CHARS:
            file_content_string += f"[...File '{file_path}' truncated at 10000 characters]"
        return file_content_string
    except Exception as e:
        return f"Error: {e}"
    

schema_get_file_content = types.FunctionDeclaration(
    name="get_file_content",
    description="Lists the content of a file, constrained to the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The path of the file which contents will be listed, constrained to files inside the working directory.",
            ),
        },
    ),
)