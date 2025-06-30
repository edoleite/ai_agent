import os

def get_files_info(working_directory, directory=None):
    target = os.path.abspath(os.path.join(working_directory, directory))
    base = os.path.abspath(working_directory)

    if directory is None:
        full_path = base
    else:        
        full_path = target

    
    
    

    if not target.startswith(base):
        return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
    
    if not os.path.isdir(full_path):
        return f'Error: "{directory}" is not a directory'
    
    contents = os.listdir(full_path)
    res = '' 

    for item in contents:        
        try:
            
            file_size = os.path.getsize(os.path.join(full_path, item))
            is_dir = os.path.isdir(os.path.join(full_path, item))
            
            res += f"- {item}: file_size={file_size} bytes, is_dir={is_dir}\n"
            
        except Exception as e:
            res += f"Error: {e}\n"

    return res.rstrip("\n")