#!/usr/bin/python3
import cmd
from models.base_model import BaseModel
from models import storage
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

    def do_create(self, arg):
        """Creates a new instance of BaseModel, saves it (to the JSON file)
        and prints the id"""
        if not arg:
            print("**class name missing**")
            return
        try:
            #check if the name exists
            model_class = eval(arg)
        except NameError:
            print("**class doesn't exist**")
            return
        #create a new instance
        new_instace = model_class()
        new_instace.save()
        print(new_instace.id)

    def help_create(self):
        """displays the help information for create command"""
        print("Create a new instance of BaseModel, save it to the JSON file, and print the id")
        print("usage: create <class name>")

    def do_show(self, arg):
        """ Prints the string representation of an instance based on the
        class name and id"""
        arguments = arg.split()

        if len(arguments) == 0:
            print("***class name missing**")
            return
        class_name = arguments[0]

        try:
            model_class = eval(class_name)
        except NameError:
            print("**class doesn't exist**")
        if len(arguments) < 2:
            print("**instance id missing**")
            return
        
        id_instance = arguments[1]
        key = f'{class_name}.{id_instance}'
        if key not in storage.all():
            print("**no instance found**")
            return
        print(storage.all()[key])



    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id
        (save the change into the JSON file)"""
        arguments = arg.split()

        if len(arguments) == 0:
            print("***class name missing**")
            return
        class_name = arguments[0]

        try:
            model_class = eval(class_name)
        except NameError:
            print("**class doesn't exist**")
        if len(arguments) < 2:
            print("**instance id missing**")
            return

        id_instance = arguments[1]
        key = f'{class_name}.{id_instance}'
        if key not in storage.all():
            print("**no instance found**")
            return
        #deletes the instance and save the changes
        del storage.all()[key]
        storage.save()

    def do_all(self, arg):



if __name__ == '__main__':
    HBNBCommand().cmdloop()
