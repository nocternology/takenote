import os


def get_current_directory():
    """
    Returns current execution directory (where the script is called)
    """
    return os.getcwd()


def check_file(db_file):
    """
    Checks if a file exists
    """
    return os.path.isfile(db_file)
