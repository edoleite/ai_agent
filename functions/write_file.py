import os

def write_file(working_directory, file_path, content):
    target = os.path.abspath(os.path.join(working_directory, file_path))
    base = os.path.abspath(working_directory)
    
    if not target.startswith(base):
        return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'

    if not os.path.exists(base):
        try:
            os.makedirs(base)
        except Exception as e:
            return f"Error: {e}"
        
    try:
        with open(target, "w") as f:       
            f.write(content)
            return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'

    except Exception as e:
        return f"Error: {e}"