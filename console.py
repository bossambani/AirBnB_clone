#!/usr/bin/python3
import cmd
import re
import shlex
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review
"""Defines a class that contains the entry point of the command interpreter"""


class HBNBCommand(cmd.Cmd):
    """HBNBCommand class"""
    prompt = "(hbnb) "
    __classes = {"BaseModel","User", "State", "City", "Place", "Amenity", "Review"}


    def parse(arg):
        curly_braces = re.search(r"\{(.*?)\}", arg)
        brackets = re.search(r"\[(.*?)\]", arg)
        if curly_braces is None:
            if brackets is None:
                return [i.strip(",") for i in split(arg)]
            else:
                lexer = split(arg[:brackets.span()[0]])
                retl = [i.strip(",") for i in lexer]
                retl.append(brackets.group())
                return retl
        else:
            lexer = split(arg[:curly_braces.span()[0]])
            retl = [i.strip(",") for i in lexer]
            retl.append(curly_braces.group())
            return retl

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

    def do_create(self, arg):
        """Creates a new instance of BaseModel, saves it (to the JSON file)
        and prints the id"""
        commands = shlex.split(arg)

        if len(commands) == 0:
            print("**class name missing**")
        elif commands[0] not in self.__classes:
            print("** class doesn't exist **")
        else:
            new_instance = BaseModel()
            new_instance.save()
            print(new_instance.id)

    def help_create(self):
        """displays the help information for create command"""
        print("Create a new instance of BaseModel, save it to the JSON file, and print the id")
        print("usage: create <class name>")

    def do_show(self, arg):
        """ Prints the string representation of an instance based on the
        class name and id"""
        commands = shlex.split(arg)

        if len(commands) == 0:
            print("** class name missing **")
        elif commands[0] not in self.valid_classes:
            print("** class doesn't exist **")
        elif len(commands) < 2:
            print("** instance id missing **")
        else:
            objects = storage.all()

            key = "{}.{}".format(commands[0], commands[1])
            if key in objects:
                print(objects[key])
            else:
                print("** no instance found **")



    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id
        (save the change into the JSON file)"""
        commands = shlex.split(arg)

        if len(commands) == 0:
            print("** class name missing **")
        elif commands[0] not in self.valid_classes:
            print("** class doesn't exist **")
        elif len(commands) < 2:
            print("** instance id missing **")
        else:
            objects = storage.all()
            key = "{}.{}".format(commands[0], commands[1])
            if key in objects:
                del objects[key]
                storage.save()
            else:
                print("** no instance found **")
                #deletes the instance and save the changes

    def do_all(self, arg):
        """Usage: all or all <class> or <class>.all()
        Display string representations of all instances of a given class.
        If no class is specified, displays all instantiated objects."""
        objects = storage.all()

        commands = shlex.split(arg)

        if len(commands) == 0:
            for key, value in objects.items():
                print(str(value))
        elif commands[0] not in self.valid_classes:
            print("** class doesn't exist **")
        else:
            for key, value in objects.items():
                if key.split('.')[0] == commands[0]:
                    print(str(value))
if __name__ == "__main__":
    HBNBCommand().cmdloop()
