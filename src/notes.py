import database

# Defines
EMPTY_LIST_ERROR = "Nothing to list :/"
EMPTY_NOTE_ERROR = "Your note is empty :/"
NOTE_ADDED = "Your note has been added !"
NOTE_DELETED = "Your note has been deleted !"
UNKNOWN_ERROR = "Something went very wrong ..."
ERROR_CATEGORY = "Category doesn't exist :/"
CATEGORY_DELETED = "Category deleted !"


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


def delete_category(category):
    """
    Deletes a hole category
    """
    return_code = db_handler.delete_category(category)

    if (return_code == -1):
        print ERROR_CATEGORY
        return False
    if (return_code == 0):
        print CATEGORY_DELETED
        return True
    else:
        print UNKNOWN_ERROR
        return False


def delete_note(note_id):
    """
    Deletes a note given its ID
    """
    return_code = db_handler.delete_note(note_id)

    if (return_code == 0):
        print NOTE_DELETED
        return True
    else:
        print UNKNOWN_ERROR
        return False


def pretty_print(list):
    """
    Pretifies the printing of the notes
    """
    if (len(list) == 0):
        print EMPTY_LIST_ERROR
        return False

    print "ID\tTimestamp\t\tCategory\tNote"
    print "--\t---------\t\t--------\t----"

    for note in list:
        print "%s\t%s\t%s\t\t%s" % (note[0], note[3], note[1], note[2])
        # print str(note[0]) + "\t" + note[3] + "\t" + note[1] + "\t\t" + note[2]
