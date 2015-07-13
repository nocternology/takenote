import cli
import helpers
import database

# Defines
DEFAULT_DB_FILE = "/home/ghandalf/Work/projects/takenote/notes.sqlite"

# Main Handler
if __name__ == '__main__':
    # Debugging
    cli.parse_args()
    print helpers.get_current_directory()
    db = database.DBWrapper(DEFAULT_DB_FILE)
    print db.create_path("/home/lol")
    print db.create_category("TODO")
    print db.create_note("This is a test note", "TODO", "/home/testing")
    db.close()
