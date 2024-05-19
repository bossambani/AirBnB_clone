#!/usr/bin/python3
import cmd
"""Defines a class that contains the entry point of the command interpreter"""


class HBNBCommand(cmd.Cmd):
    """HBNBCommand class"""
    prompt = "(hbnb) "

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def help_quit(self):
        """Display help information for quit command"""
        print("Quit command to exit the program")
        print('\n')

    def do_EOF(self, arg):
        """EOF command to exit the program"""
        print()
        return True

    def help_EOF(self):
        """displays the help information for EOF command"""
        print("EOF command to exit the progrma")

    def emptyline(self):
        """Does not execute anything"""
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
