#!/bin/python

import argparse
import notes


def parse_args():
    """
    Parses the arguments
    """

    parser = argparse.ArgumentParser()

    subparsers = parser.add_subparsers(help='commands', dest='subparser')

    # List notes
    list_parser = subparsers.add_parser('list', help='List notes')
    list_parser.add_argument(
        '-c', '--cat', action='store', help='Category of notes to list')
    list_parser.add_argument(
        '-a', '--all', action='store_true', help='All stored notes')

    # Add note
    add_parser = subparsers.add_parser('add', help='Add note')
    add_parser.add_argument(
        '-c', '--cat', action='store', help='Category of the new note')
    add_parser.add_argument(
        '-n', '--note', action='store', help='Note to be added')

    # Delete note
    del_parser = subparsers.add_parser('del', help='Deletes a note')
    del_parser.add_argument(
        '-n', '--note', action='store', help='Hash of the note to be deleted')
    del_parser.add_argument(
        '-c', '--cat', action='store', help='Delete a whole category')

    args = parser.parse_args()

    parse_callback(args)

    return args


def parse_callback(args):
    """
    Callback to handle correct function call of command line
    """

    if (args.subparser == 'list'):
        if args.all is True:
            notes.list_all_notes()
        if args.cat is not None:
            notes.list_by_category(args.cat)

    if (args.subparser == 'del'):
        pass
    if (args.subparser == 'add'):
        notes.add_note(args.note, args.cat)
