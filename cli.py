#!/bin/python

import argparse


# def parse_args():
#     """
#     Parses the arguments
#     """
#     parser = argparse.ArgumentParser()
#     list_parser = argparse.ArgumentParser(add_help=False)
#     group_actions = parser.add_mutually_exclusive_group()
#
#     group_actions.add_argument(
#         "-r", "--remove", help="removes a note", action="store_true")
#     group_actions.add_argument(
#         "-m", "--modify", help="modifies a note", action="store_true")
#     group_actions.add_argument(
#         "-a", "--add", help="adds a note", action="store_true")
#     group_actions.add_argument(
#         "-n", "--note", help="the note you want to add/remove/modify",
#         type=str)
#
#     parser.add_argument(
#         "-l", "--list", help="list notes for current path",
#         action="store_true")
#     parser.add_argument(
#         "-lr", "--listrecursive", help="list notes for current path \
#         and subpaths", action="store_true")
#
#     args = parser.parse_args()

#
#     return args

def parse_args():
    """
    Parses the arguments
    """
    parser = argparse.ArgumentParser()

    subparsers = parser.add_subparsers(help='commands')

    # List notes
    list_parser = subparsers.add_parser('list', help='List notes')
    list_parser.add_argument(
        '-lr', action='store_true', help='Lists notes recursively')

    # Add note
    add_parser = subparsers.add_parser('add', help='Add note')
    add_parser.add_argument(
        '-c', action='store', help='Specifies a category for the note (TODO, \
        FIXME, ...)')
    add_parser.add_argument(
        'note', action='store', help='Note to be added')

    # Delete note
    del_parser = subparsers.add_parser('del', help='Deletes a note')
    del_parser.add_argument(
        'note', action='store', help='Hash of the note to be deleted')

    results = parser.parse_args()

    return results


def parse_add_note():
    """
    Generates the subsequencial calls when a -a command is issued
    """
    pass
