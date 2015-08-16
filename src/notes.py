import database

# Defines
EMPTY_LIST_ERROR = "Nothing to list :/"
EMPTY_NOTE_ERROR = "Your note is empty :/"
NOTE_ADDED = "Your note has been added !"
UNKNOWN_ERROR = "Something went very wrong ..."

db_handler = database.DBWrapper()


def list_all_notes():
    """
    List all stored notes
    """
    pretty_print(db_handler.get_all_notes())


def list_by_category(category):
    """
    List notes of a given category
    """
    pretty_print(db_handler.get_by_category(category))


def add_note(note, category):
    """
    Adds a note given its category
    """
    if (note is None or len(note) == 0):
        print EMPTY_NOTE_ERROR
        return False

    if (category is None):
        category = "DEFAULT"

    if (db_handler.create_note(note, category) > 0):
        print NOTE_ADDED
    else:
        print UNKNOWN_ERROR


def pretty_print(list):
    """
    Pretifies the printing of the notes
    """
    print "ID\tTimestamp\t\tCategory\tNote"
    print "--\t---------\t\t--------\t----"

    if (len(list) == 0):
        print EMPTY_LIST_ERROR
        return False

    for note in list:
        print str(note[0]) + "\t" + note[3] + "\t" + note[1] + "\t\t" + note[2]
