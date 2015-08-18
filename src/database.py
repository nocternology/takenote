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

    def db_create(self):
        self.cursor.execute(sql_create_notes)
        self.cursor.execute(sql_create_categories)

    def create_category(self, category):
        self.cursor.execute(sql_get_category, [category])
        tcat = self.cursor.fetchone()

        if tcat is None:
            self.cursor.execute(sql_add_category, [category])
            self.conn.commit()
            return self.cursor.lastrowid
        else:
            return tcat[0]

    def create_note(self, note, category):
        cat_id = self.create_category(category)

        self.cursor.execute(sql_add_note, [cat_id, note])
        self.conn.commit()

        return self.cursor.lastrowid

    def get_all_notes(self):
        """
        Gets all the stored notes
        """
        self.cursor.execute(sql_get_all_notes)
        return self.cursor.fetchall()

    def get_by_category(self, category):
        """
        Gets all notes for a category
        """
        self.cursor.execute(sql_get_by_cat, [category])
        return self.cursor.fetchall()

    def delete_category(self, category):
        """
        Deletes a hole category
        """
        self.cursor.execute(sql_get_category, [category])
        tcat = self.cursor.fetchone()

        if tcat is None:
            return -1
        else:
            try:
                self.cursor.execute(sql_delete_category_notes, [tcat[0]])
                self.cursor.execute(sql_delete_category, [tcat[0]])
                self.conn.commit()

                return 0
            except Exception as e:
                return 1

    def delete_note(self, note):
        """
        Deletes a note given its ID
        """
        try:
            self.cursor.execute(sql_delete_note, [note])
            self.conn.commit()

            return 0
        except Exception as e:
            print e.message
            return -1

    def close(self):
        self.conn.close()


# SQL Queries
sql_create_notes = """
CREATE  TABLE  IF NOT EXISTS "main"."NOTES" (
    "note_id" INTEGER PRIMARY KEY AUTOINCREMENT  NOT NULL  UNIQUE ,
    "cat_id" INTEGER,
    "timestamp" DATETIME NOT NULL  DEFAULT CURRENT_TIMESTAMP,
    "content" TEXT)
"""

sql_create_categories = """
CREATE  TABLE "main"."CATEGORIES" (
    "cat_id" INTEGER PRIMARY KEY  AUTOINCREMENT  NOT NULL  UNIQUE ,
    "content" TEXT DEFAULT "no_cat")
"""

sql_add_note = """
INSERT INTO "main"."NOTES" ("cat_id","content") VALUES (?,?)
"""

sql_add_category = """
INSERT INTO "main"."CATEGORIES" ("content") VALUES (?)
"""

sql_get_category = """
SELECT * FROM "main"."CATEGORIES" WHERE "content" = ?
"""

sql_get_all_notes = """
SELECT N.note_id, C.content, N.content, N.timestamp FROM NOTES N, CATEGORIES C
WHERE
    N.cat_id = C.cat_id
ORDER BY
    C.cat_id
    DESC;
"""

sql_get_by_cat = """
SELECT N.note_id, C.content, N.content, N.timestamp FROM NOTES N, CATEGORIES C
WHERE
    N.cat_id = C.cat_id AND
    C.content = ?
    GROUP BY
    C.cat_id;
"""

sql_delete_category = """
DELETE FROM CATEGORIES WHERE CATEGORIES.cat_id = ?
"""

sql_delete_category_notes = """
DELETE FROM NOTES WHERE NOTES.cat_id = ?
"""

sql_delete_note = """
DELETE FROM NOTES WHERE NOTES.note_id = ?
"""
