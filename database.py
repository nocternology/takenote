import sqlite3


class DBWrapper():

    """
    Database wrapper for notes operations
    """

    def __init__(self, dbfile='notes.sqlite'):
        self.db_open(dbfile)

    def db_open(self, file):
        self.conn = sqlite3.connect(file)
        self.cursor = self.conn.cursor()

    def db_create(self, file):
        self.cursor.execute(sql_create_notes)
        self.cursor.execute(sql_create_categories)
        self.cursor.execute(sql_create_paths)

    def create_category(self, category):
        pass

    def create_path(self, path):
        pass

    def create_note(self, note, category, path):
        pass

    def test(self):
        return "OKAY"

sql_create_notes = """
CREATE  TABLE  IF NOT EXISTS "main"."NOTES" (
    "note_id" INTEGER PRIMARY KEY AUTOINCREMENT  NOT NULL  UNIQUE ,
    "cat_id" INTEGER, "path_id" INTEGER NOT NULL,
    "timestamp" DATETIME NOT NULL  DEFAULT CURRENT_TIMESTAMP,
    "content" TEXT)
"""

sql_create_categories = """
CREATE  TABLE "main"."CATEGORIES" (
    "cat_id" INTEGER PRIMARY KEY  AUTOINCREMENT  NOT NULL  UNIQUE ,
    "content" TEXT DEFAULT "no_cat")
"""

sql_create_paths = """
CREATE  TABLE "main"."PATHS" (
    "path_id" INTEGER PRIMARY KEY  AUTOINCREMENT  NOT NULL  UNIQUE ,
    "path" TEXT DEFAULT "/")
"""

sql_add_note = """


"""
