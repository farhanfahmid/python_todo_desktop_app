

def get_todos(filepath='todos_file.txt'):
    """Read a text file and return list of to-do items"""
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local

def write_todos(todos_arg, filepath='todos_file.txt'):
    """Write the to-do items list in the text file"""
    with open(filepath, 'w') as file_local:
        file_local.writelines(todos_arg)


# # Function to get the correct file path for images
# def resource_path(relative_path):
#     """ Get absolute path to resource, works for dev and PyInstaller .exe """
#     if getattr(sys, 'frozen', False):  # If running as a PyInstaller bundle
#         base_path = sys._MEIPASS  # Extracted temp folder for PyInstaller
#     else:
#         base_path = os.path.abspath(".")  # Running as script
#
#     return os.path.join(base_path, relative_path)