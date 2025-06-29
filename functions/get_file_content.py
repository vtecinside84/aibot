import os

def get_file_content(working_directory, file_path):
    """
    Reads the content of a file located at file_path within the specified working_directory.
    
    Args:
        working_directory (str): The directory where the file is located.
        file_path (str): The path to the file relative to the working_directory.
        
    Returns:
        str: The content of the file.
    """
    full_path = os.path.abspath(os.path.join(working_directory, file_path))
    abs_directory = os.path.abspath(working_directory)
    MAX_CHARS = 10000
    if not abs_directory.startswith(abs_directory):
        raise ValueError(f'Error: Cannot read "{file_path}" as it is outside the permitted working directory')
    if not os.path.isfile(full_path):
        raise FileNotFoundError(f'Error: File not found or is not a regular file: "{file_path}"')
    try:
        with open(full_path, 'r') as file:
            file_string = file.read(MAX_CHARS)
            if os.path.getsize(full_path) > MAX_CHARS:
                file_string += '[...File "{file_path}" truncated at 10000 characters]'
        return file_string
    except Exception as e:
        return (f'Error: {e}')
        