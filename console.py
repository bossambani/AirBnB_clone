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


    '''def parse(arg):
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
'''
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
        elif commands[0] not in self.__classes:
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
        elif commands[0] not in self.__classes:
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
        elif commands[0] not in self.__classes:
            print("** class doesn't exist **")
        else:
            for key, value in objects.items():
                if key.split('.')[0] == commands[0]:
                    print(str(value))

    def do_count(self, arg):
        """
        Counts and retrieves the number of instances of a class
        usage: <class name>.count()
        """
        objects = storage.all()

        commands = shlex.split(arg)

        if arg:
            cls_nm = commands[0]

        count = 0

        if commands:
            if cls_nm in self.__classes:
                for obj in objects.values():
                    if obj.__class__.__name__ == cls_nm:
                        count += 1
                print(count)
            else:
                print("** invalid class name **")
        else:
            print("** class name missing **")

    def do_update(self, arg):
       """
       Update an instance by adding or updating an attribute.
       Usage: update <class_name> <id> <attribute_name> "<attribute_value>"
       """
       commands = shlex.split(arg)

       if len(commands) == 0:
           print("** class name missing **")
       elif commands[0] not in self.__classes:
           print("** class doesn't exist **")
       elif len(commands) < 2:
           print("** instance id missing **")
       else:
           objects = storage.all()

           key = "{}.{}".format(commands[0], commands[1])
           if key not in objects:
               print("** no instance found **")
           elif len(commands) < 3:
               print("** attribute name missing **")
           elif len(commands) < 4:
               print("** value missing **")
           else:
               obj = objects[key]
               curly_braces = re.search(r"\{(.*?)\}", arg)

               if curly_braces:
                   try:
                       str_data = curly_braces.group(1)

                       arg_dict = ast.literal_eval("{" + str_data + "}")

                       attribute_names = list(arg_dict.keys())
                       attribute_values = list(arg_dict.values())
                       try:
                           attr_name1 = attribute_names[0]
                           attr_value1 = attribute_values[0]
                           setattr(obj, attr_name1, attr_value1)
                       except Exception:
                           pass
                       try:
                           attr_name2 = attribute_names[1]
                           attr_value2 = attribute_values[1]
                           setattr(obj, attr_name2, attr_value2)
                       except Exception:
                           pass
                   except Exception:
                       pass
               else:

                   attr_name = commands[2]
                   attr_value = commands[3]

                   try:
                       attr_value = eval(attr_value)
                   except Exception:
                       pass
                   setattr(obj, attr_name, attr_value)

               obj.save()

    def default(self, arg):
        """
        Default behavior for cmd module when input is invalid
        """
        arg_list = arg.split('.')

        cls_nm = arg_list[0]  # incoming class name

        command = arg_list[1].split('(')

        cmd_met = command[0]  # incoming command method

        e_arg = command[1].split(')')[0]  # extra arguments

        method_dict = {
                'all': self.do_all,
                'show': self.do_show,
                'destroy': self.do_destroy,
                'update': self.do_update,
                'count': self.do_count
                }

        if cmd_met in method_dict.keys():
            if cmd_met != "update":
                return method_dict[cmd_met]("{} {}".format(cls_nm, e_arg))
            else:
                if not cls_nm:
                    print("** class name missing **")
                    return
                try:
                    obj_id, arg_dict = split_curly_braces(e_arg)
                except Exception:
                    pass
                try:
                    call = method_dict[cmd_met]
                    return call("{} {} {}".format(cls_nm, obj_id, arg_dict))
                except Exception:
                    pass
        else:
            print("*** Unknown syntax: {}".format(arg))
            return False

if __name__ == "__main__":
    HBNBCommand().cmdloop()
