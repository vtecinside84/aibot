import os

def get_files_info(working_directory, directory=None):
    directory = os.path.join(working_directory, directory)
    if not os.path.isdir(directory):
        return f'Error: "{directory}" is not a directory'
    abs_working_directory = os.path.abspath(working_directory)
    abs_directory = os.path.abspath(directory)
    if not abs_directory.startswith(abs_working_directory):
        return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
    files = os.listdir(directory)
    fileslist = []
    for file in files:
        file_path = os.path.join(directory, file)
        fileslist.append(f"- {file}: file_size={os.path.getsize(file_path)} bytes, is_dir={os.path.isdir(file_path)}")
    return "\n".join(fileslist)