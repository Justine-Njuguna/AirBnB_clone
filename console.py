#!/usr/bin/python3
"""
This module defines the HBNBCommand class, Console entry point.
"""

import cmd
from models.user import User
from models.base_model import BaseModel
from models.__init__ import storage


class HBNBCommand(cmd.Cmd):
    """
    Custom command interpreter class for HBNB.
    """

    prompt = "(hbnb) "

    def do_create(self, arg):
        """
        Create a new instance of BaseModel or User, save it, and print the ID.
        """
        if not arg:
            print("** class name missing **")
            return

        class_name = arg.split()[0]
        if class_name not in ["BaseModel", "User"]:
            print("** class doesn't exist **")
            return

        if class_name == "BaseModel":
            new_instance = BaseModel()
        elif class_name == "User":
            new_instance = User()

        storage.save()
        print(new_instance.id)

    def do_show(self, arg):
        """
        Print the string representation of an instance.
        """
        args = arg.split()
        if not args:
            print("** class name missing **")
            return

        class_name = args[0]
        if class_name not in ["BaseModel", "User"]:
            print("** class doesn't exist **")
            return

        if len(args) < 2:
            print("** instance id missing **")
            return

        instance_id = args[1]
        key = "{}.{}".format(class_name, instance_id)
        if key not in storage.all():
            print("** no instance found **")
            return

        print(storage.all()[key])

    def do_destroy(self, arg):
        """
        Delete an instance based on the class name and id.
        """
        args = arg.split()
        if not args:
            print("** class name missing **")
            return

        class_name = args[0]
        if class_name not in ["BaseModel", "User"]:
            print("** class doesn't exist **")
            return

        if len(args) < 2:
            print("** instance id missing **")
            return

        instance_id = args[1]
        key = "{}.{}".format(class_name, instance_id)
        if key not in storage.all():
            print("** no instance found **")
            return

        del storage.all()[key]
        storage.save()

    def do_all(self, arg):
        """
        Print all string representations of instances.
        """
        class_name = arg.split()[0] if arg else None
        if class_name and class_name not in ["BaseModel", "User"]:
            print("** class doesn't exist **")
            return

        instances = storage.all().values()
        if class_name:
            instances = [
                    inst for inst in instances
                    if inst.__class__.__name__ == class_name
                    ]

        print([str(inst) for inst in instances])

    def do_update(self, arg):
        """
        Update an instance based on the class name and id.
        Usage: update <class name> <id> <attribute name> "<attribute value>"
        """
        args = arg.split()
        if not args:
            print("** class name missing **")
            return

        class_name = args[0]
        if class_name not in ["BaseModel", "User"]:
            print("** class doesn't exist **")
            return

        if len(args) < 2:
            print("** instance id missing **")
            return

        instance_id = args[1]
        key = "{}.{}".format(class_name, instance_id)
        if key not in storage.all():
            print("** no instance found **")
            return

        if len(args) < 4:
            print("** attribute name missing **")
            return

        attr_name = args[2]
        if len(args) < 5:
            print("** value missing **")
            return

        attr_value = args[3]
        try:
            # Cast the attribute value to the attribute type
            attr_value = eval(attr_value)
        except (NameError, SyntaxError):
            print("** value must be a valid Python data type **")
            return

        # Update the instance's attribute
        setattr(storage.all()[key], attr_name, attr_value)
        storage.save()

    def emptyline(self):
        """
        Do nothing when an empty line is entered.
        """
        pass

    def do_quit(self, arg):
        """
        Quit command to exit the program.
        """
        return True

    def do_EOF(self, line):
        """
        Exit the program when EOF (Ctrl+D) is encountered.
        """
        return True


if __name__ == '__main__':
    HBNBCommand().cmdloop()
