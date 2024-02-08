#!/usr/bin/python3
"""
Console module
"""
import cmd
from models.base_model import BaseModel
from models.user import User
from models import storage


class HBNBCommand(cmd.Cmd):
    """
    HBNBCommand class
    """
    prompt = "(hbnb) "

    def do_quit(self, line):
        """
        Quit the program
        """
        return True

    def do_EOF(self, line):
        """
        Exit the program
        """
        return True

    def emptyline(self):
        """
        Empty line
        """
        pass

    def do_help(self, input):
        """
        Help command
        """
        if input:
            cmd.Cmd.do_help(self, input)
        else:
            print("\nDocumented commands (type help <topic>):")
            print("========================================")
            print("EOF  help  quit\n")

    def do_create(self, line):
        """
        Creating a new instance of BaseModel
        """
        if not line:
            print("** class name missing **")
        elif line not in globals():
            print("** class doesn't exist **")
        else:
            new_instance = globals()[line]()
            new_instance.save()
            print(new_instance.id)

    def do_show(self, line):
        """
        Prints the string representation of an instance
        """
        args = line.split()
        if not line:
            print("** class name missing **")
        elif args[0] not in globals():
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        else:
            key = args[0] + "." + args[1]
            all_objs = storage.all()
            if key in all_objs:
                print(all_objs[key])
            else:
                print("** no instance found **")

    def do_destroy(self, line):
        """
        Deletes an instance
        """
        args = line.split()
        if not line:
            print("** class name missing **")
        elif args[0] not in globals():
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        else:
            key = args[0] + "." + args[1]
            all_objs = storage.all()
            if key in all_objs:
                del all_objs[key]
                storage.save()
            else:
                print("** no instance found **")

    def do_all(self, line):
        """
        Prints all string representation of all instances
        """
        args = line.split()
        all_objs = storage.all()
        if not line:
            print([str(all_objs[obj]) for obj in all_objs])
        elif args[0] not in globals():
            print("** class doesn't exist **")
        else:
            print([str(all_objs[obj]) for obj in all_objs
                   if args[0] in obj])

    def do_update(self, line):
        """
        Updates an instance based on the class name and id
        """
        args = line.split()
        all_objs = storage.all()
        if not line:
            print("** class name missing **")
        elif args[0] not in globals():
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        elif len(args) == 2:
            print("** attribute name missing **")
        elif len(args) == 3:
            print("** value missing **")
        else:
            key = args[0] + "." + args[1]
            if key in all_objs:
                setattr(all_objs[key], args[2], args[3])
                storage.save()
            else:
                print("** no instance found **")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
