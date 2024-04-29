#!/usr/bin/python3
"""
This module contains the entry point of the command interpreter
"""

import cmd
import sys
from models import storage
from models.state import State
from models.city import City

class HBNBCommand(cmd.Cmd):
    """
    This class contains the command interpreter methods
    """
    prompt = '(hbnb) '
    intro = 'Welcome to the Holberton Airbnb command interpreter!\n'

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """Exit the program using EOF (Ctrl + D)"""
        print()
        return True

    def emptyline(self):
        """Do nothing on empty input"""
        pass

    def do_create(self, arg):
        """Create a new instance of a specified class"""
        if not arg:
            print("** class name missing **")
            return
        try:
            new_instance = eval(arg)()
            new_instance.save()
            print(new_instance.id)
        except NameError:
            print("** class doesn't exist **")

    def do_show(self, arg):
        """Show the string representation of an instance"""
        args = arg.split()
        if not arg:
            print("** class name missing **")
            return
        if args[0] not in ['BaseModel', 'User', 'State', 'City', 'Amenity',
                           'Place', 'Review']:
            print("** class doesn't exist **")
            return
        if len(args) == 1:
            print("** instance id missing **")
            return
        key = args[0] + '.' + args[1]
        if key not in storage.all():
            print("** no instance found **")
            return
        print(storage.all()[key])

    def do_destroy(self, arg):
        """Delete an instance"""
        args = arg.split()
        if not arg:
            print("** class name missing **")
            return
        if args[0] not in ['BaseModel', 'User', 'State', 'City', 'Amenity',
                           'Place', 'Review']:
            print("** class doesn't exist **")
            return
        if len(args) == 1:
            print("** instance id missing **")
            return
        key = args[0] + '.' + args[1]
        if key not in storage.all():
            print("** no instance found **")
            return
        del storage.all()[key]
        storage.save()

    def do_all(self, arg):
        """Print all string representation of all instances"""
        args = arg.split()
        objects = storage.all()
        if not arg:
            print([str(value) for value in objects.values()])
            return
        if args[0] not in ['BaseModel', 'User', 'State', 'City', 'Amenity',
                           'Place', 'Review']:
            print("** class doesn't exist **")
            return
        print([str(value) for key, value in objects.items() if args[0] in key])

    def do_update(self, arg):
        """Update an instance by adding or updating an attribute"""
        args = arg.split()
        if not arg:
            print("** class name missing **")
            return
        if args[0] not in ['BaseModel', 'User', 'State', 'City', 'Amenity',
                           'Place', 'Review']:
            print("** class doesn't exist **")
            return
        if len(args) == 1:
            print("** instance id missing **")
            return
        key = args[0] + '.' + args[1]
        if key not in storage.all():
            print("** no instance found **")
            return
        if len(args) == 2:
            print("** attribute name missing **")
            return
        if len(args) == 3:
            print("** value missing **")
            return
        setattr(storage.all()[key], args[2], args[3])
        storage.save()

    def do_count(self, arg):
        """Count the number of instances of a class"""
        args = arg.split()
        if not arg:
            print("** class name missing **")
            return
        if args[0] not in ['BaseModel', 'User', 'State', 'City', 'Amenity',
                           'Place', 'Review']:
            print("** class doesn't exist **")
            return
        objects = storage.all()
        count = sum(1 for key in objects.keys() if args[0] in key)
        print(count)

    def default(self, line):
        """Called on an input line when the command prefix is not recognized"""
        args = line.split('.')
        class_name = args[0]
        if class_name not in ['BaseModel', 'User', 'State', 'City', 'Amenity',
                              'Place', 'Review']:
            print("** class doesn't exist **")
            return
        if len(args) < 2 or args[1] == '':
            print("** missing attribute **")
            return
        if args[1][:6] == 'count(' and args[1][-1] == ')':
            self.do_count(class_name)
            return
        if args[1][:5] == 'show(' and args[1][-1] == ')':
            args[1] = args[1][5:-1]
            self.do_show(class_name + ' ' + args[1])
            return
        if args[1][:8] == 'destroy(' and args[1][-1] == ')':
            args[1] = args[1][8:-1]
            self.do_destroy(class_name + ' ' + args[1])
            return
        if args[1][:7] == 'update(' and args[1][-1] == ')':
            args[1] = args[1][7:-1]
            self.do_update(class_name + ' ' + args[1])
            return
        if args[1][:4] == 'all(' and args[1][-1] == ')':
            args[1] = args[1][4:-1]
            self.do_all(class_name)
            return
        print("** invalid command **")

if __name__ == '__main__':
    HBNBCommand().cmdloop()
