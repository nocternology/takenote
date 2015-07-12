#!/bin/python

import argparse


def parse_args():
    parser = argparse.ArgumentParser()
    group_actions = parser.add_mutually_exclusive_group()

    group_actions.add_argument(
        "-r", "--remove", help="removes a note", action="store_true")
    group_actions.add_argument(
        "-m", "--modify", help="modifies a note", action="store_true")
    group_actions.add_argument(
        "-a", "--add", help="adds a note", action="store_true")
    group_actions.add_argument(
        "-n", "--note", help="the note you want to add/remove/modify",
        type=str)

    parser.add_argument(
        "-l", "--list", help="list notes", action="store_true")

    args = parser.parse_args()


if __name__ == '__main__':
    parse_args()
