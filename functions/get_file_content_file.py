import os

def get_file_content(working_directory, file_path):
    target = os.path.abspath(os.path.join(working_directory, file_path))
    base = os.path.abspath(working_directory)
    
    if not target.startswith(base):
        return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
    
    if not os.path.isfile(target):
        return f'Error: File not found or is not a regular file: "{file_path}"'
    
    MAX_CHARS = 10000

    with open(target, "r") as f:
        file_content_string = f.read()
        
    if len(file_content_string) > MAX_CHARS:
        with open(target, "r") as f:
            file_content_string = f.read(MAX_CHARS) + f'[...File "{file_path}" truncated at 10000 characters]'
    
    return file_content_string
