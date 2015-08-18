#!/bin/python

import argparse
import notes


def parse_args():
    """
    Parses the arguments
    """
    # Parsers declaration
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
        'note', metavar='note', nargs='+', help='Note to be added')

    # Delete note
    del_parser = subparsers.add_parser('del', help='Deletes a note')
    del_parser.add_argument(
        '-n', '--note', action='store', help='Hash of the note to be deleted')
    del_parser.add_argument(
        '-c', '--cat', action='store', help='Delete a whole category')

    # Actual parsing
    args = parser.parse_args()
    parse_callback(args)


def parse_callback(args):
    """
    Callback to handle correct function call of command line
    """

    if (args.subparser == 'list'):
        if args.all is True:
            notes.list_all_notes()
        elif args.cat is not None:
            notes.list_by_category(args.cat)
        else:
            print "Nothing to do ..."

    if (args.subparser == 'del'):
        if args.cat is not None:
            notes.delete_category(args.cat)
        elif args.note is not None:
            notes.delete_note(args.note)
        else:
            print "Nothing to do ..."

    if (args.subparser == 'add'):
        notes.add_note(' '.join(args.note), args.cat)
