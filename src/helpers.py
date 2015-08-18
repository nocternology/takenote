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


def fatal_exit():
    """
    Self explanatory is guess
    """
    print "Somethign went VERY bad !"
    exit(-1)


def expand_to_home(filename):
    """
    Gets the current user's path and return the absolute filepath to
    the DB file
    """
    home_path = os.path.expanduser("~")

    return home_path + "/" + filename
