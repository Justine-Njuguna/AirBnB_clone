#!/usr/bin/python3
"""
This module defines the HBNBCommand class, Console entry point.
"""

import cmd


class HBNBCommand(cmd.Cmd):
    """
    Custom command interpreter class for HBNB.
    """

    prompt = "(hbnb) "

    def do_quit(self, arg):
        """
        Exit the program.
        """
        return True

    def do_EOF(self, arg):
        """
        Exit the program on EOF (Ctrl-D).
        """
        print()  # Print a newline before exiting
        return True

    def emptyline(self):
        """
        Do nothing when an empty line is entered.
        """
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
