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
        # Category exists ?
        self.cursor.execute(sql_get_category, [category])
        tcat = self.cursor.fetchone()

        if tcat is None:
            self.cursor.execute(sql_add_category, [category])
            self.conn.commit()
            return self.cursor.lastrowid
        else:
            return tcat[0]

    def create_path(self, path):
        # Path exists ?
        self.cursor.execute(sql_get_path, [path])
        tpath = self.cursor.fetchone()

        if tpath is None:
            self.cursor.execute(sql_add_path, [path])
            self.conn.commit()
            return self.cursor.lastrowid
        else:
            return tpath[0]

    def create_note(self, note, category, path):
        cat_id = self.create_category(category)
        path_id = self.create_path(path)

        self.cursor.execute(sql_add_note, [cat_id, path_id, note])
        self.conn.commit()

        return self.cursor.lastrowid

    def close(self):
        self.conn.close()


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
INSERT INTO "main"."NOTES" ("cat_id","path_id","content") VALUES (?,?,?)
"""

sql_add_category = """
INSERT INTO "main"."CATEGORIES" ("content") VALUES (?)
"""

sql_add_path = """
INSERT INTO "main"."PATHS" ("path") VALUES (?)
"""

sql_get_category = """
SELECT * FROM "main"."CATEGORIES" WHERE "content" = ?
"""

sql_get_path = """
SELECT * FROM "main"."PATHS" WHERE "path" = ?
"""
