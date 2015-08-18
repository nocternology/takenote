#!/usr/bin/python

import src.cli as cli
import src.helpers as helpers
import src.database as database


DEFAULT_DB_FILE = "/home/nocternology/Work/takenote/notes.sqlite"


if __name__ == '__main__':
    cli.parse_args()
