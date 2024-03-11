#!/usr/bin/python3
""" Module for console.py"""

import cmd
from models.base_model import BaseModel
from models.user import User
from models import storage
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State


class HBNBCommand(cmd.Cmd):
    """
    Class for command interpreter.
    Attributes:
        prompt (str): The prompt displayed to the user.
        Cls (dict): a dictionary containing the Classes' names
            as keys, and the object thy represents as value.
    """
    prompt = "(hbnb) "
    Cls = {"BaseModel": BaseModel, "User": User, "Amenity": Amenity,
           "City": City, "Place": Place, "Review": Review, "State": State}

    def do_quit(self, arg):
        """
        Quit command to exit the program
        """
        return True

    def do_EOF(self, arg):
        """
        EOF command to exit the program
        """
        print()
        return True

    def emptyline(self):
        """
        Empty line should not execute anything
        """
        pass

    def do_create(self, arg):
        """
        Create an instance of the specified class
        """
        args = arg.split()
        if not args:
            print("** class name missing **")
        elif args[0] not in HBNBCommand.Cls:
            print("** class doesn't exist **")
        else:
            storage.reload()
            instance = HBNBCommand.Cls[args[0]]()
            instance.save()
            print(instance.id)

    def do_show(self, arg):
        """
        Show a specific object
        """
        args = arg.split()
        if not args:
            print("** class name missing **")
        elif args[0] not in HBNBCommand.Cls:
            print("** class doesn't exist **")
        elif not arg.split()[1:]:
            print("** instance id missing **")
        else:
            input_id = arg.split()[1:]
            storage.reload()
            all_objs = storage.all()
            counter = 0
            for obj_id in all_objs.keys():
                if obj_id.split('.')[1:] == input_id:
                    if obj_id.split('.')[0] == args[0]:
                        counter = 1
                        print(all_objs[obj_id])
            if counter == 0:
                print("** no instance found **")

    def do_all(self, arg):
        """
        Prints all string representation of all instances
        based or not on the class name
        """
        storage.reload()
        all_objs = storage.all()
        my_list = []
        if not arg:
            for obj_key in all_objs.keys():
                my_list.append(str(all_objs[obj_key]))
            if len(my_list) > 0:
                print(my_list)
        else:
            if arg in HBNBCommand.Cls:
                for obj_key in all_objs.keys():
                    if obj_key.split('.')[0] == arg:
                        my_list.append(str(all_objs[obj_key]))
                if len(my_list) > 0:
                    print(my_list)
            else:
                print("** class doesn't exist **")

    def do_destroy(self, arg):
        """
        Delete an instance based on
        the class name and id
        """
        args = arg.split()

        if not args:
            print("** class name missing **")
        elif args[0] not in HBNBCommand.Cls:
            print("** class doesn't exist **")
        elif not arg.split()[1:]:
            print("** instance id missing **")
        else:
            input_id = arg.split()[1:]
            storage.reload()
            all_objs = storage.all()
            counter = 0
            d_instance = ""
            for obj_id in all_objs.keys():
                if obj_id.split('.')[1:] == input_id:
                    if obj_id.split('.')[0] == args[0]:
                        d_instance = obj_id
                        counter = 1
                        break

            if counter != 0:
                del storage.all()[d_instance]
                storage.save()
            else:
                print("** no instance found **")

    def do_update(self, arg):
        """
        Updates an instance based on the class name
        and id by adding or updating attribute
        """
        args = arg.split()

        if not args:
            print("** class name missing **")
        elif args[0] not in HBNBCommand.Cls:
            print("** class doesn't exist **")
        elif not args[1:]:
            print("** instance id missing **")
        elif not args[2:]:
            print("** attribute name missing **")
        elif not args[3:]:
            print("** value missing **")
        else:
            storage.reload()
            all_objs = storage.all()
            input_id = args[1]
            counter = 0
            for obj_id in all_objs.keys():
                if obj_id.split('.')[1] == input_id:
                    if obj_id.split('.')[0] == args[0]:
                        storage.reload()
                        my_model = HBNBCommand.Cls[args[0]]()
                        print(type(args[3]))
                        setattr(my_model, args[2], args[3])
                        my_model.save()
                        counter = 1
                        break

            if counter == 0:
                print("** no instance found **")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
