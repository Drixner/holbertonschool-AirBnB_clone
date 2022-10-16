#!/usr/bin/python3
""" Console to manage hbnb data """

import cmd
from models import storage
from models.base_model import BaseModel


class HBNBCommand(cmd.Cmd):
    """ Class HBNBCommand CLI, entry command interpreter """
    prompt = '(hbnb) '
    __classes = {
            'BaseModel'
            }

    def emptyline(self):
        """ Method emptyline """
        pass

    def do_quit(self, line):
        """ Quit command to exit the program """
        print()
        return True

    def do_EOF(self, line):
        """ Ctrl+D to exit the program """
        print()
        return True

    def do_create(self, args):
        """ Create instance specified by the user """
        if not args:
            print("** class name missing **")
        elif args not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        else:
            cls_d = {'BaseModel': BaseModel}

            new_obj = cls_d[args]()
            new_obj.save()
            print("{}".format(new_obj.id))
            storage.save()

    def do_show(self, line):
        """ Print string representation: name and id """
        arg = line.split()
        obj_dict = storage.all()  # all() function from file_storage.py
        if len(arg) == 0:
            print("** class name missing **")
        elif arg[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        elif len(arg) == 1:
            print("** instance id missing **")
        elif "{}.{}".format(arg[0], arg[1]) not in obj_dict:
            print("** no instance found **")
        else:
            print(obj_dict["{}.{}".format(arg[0], arg[1])])

    def do_destroy(self, line):
        """ Destroy instance specified by user; save changes to JSON file """
        arg = line.split()
        obj_dict = storage.all()  # all() function from file_storage.py
        if len(arg) == 0:
            print("** class name missing **")
        elif arg[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        elif len(arg) == 1:
            print("** instance id missing **")
        elif "{}.{}".format(arg[0], arg[1]) not in obj_dict:
            print("** no instance found **")
        else:
            del (obj_dict["{}.{}".format(arg[0], arg[1])])
            storage.save()

    def do_all(self, args):
        """ Print all objects or all objects of specified class """
        yes = 0
        all_obj = [str(v) for v in storage.all().values()]
        if not args:
            yes = 1
            print('{}'.format(all_obj))
        elif args:
            arg_list = args.split()
        if args and arg_list[0] in HBNBCommand.__classes:
            yes = 1
            all_obj = storage.all()  # all() function from file_storage.py
            name = arg_list[0]
            all_obj = [str(v) for k, v in all_obj.items()
                       if name == v.__class__.__name__]
            print(all_obj)

        if yes == 0:
            print("** class doesn't exist **")

    def do_update(self, line):
        """Update if given exact object, exact attribute"""
        args = parse(line)
        if len(args) >= 4:
            key = "{}.{}".format(args[0], args[1])
            cast = type(eval(args[2]))
            arg3 = args[3]
            arg3 = arg3.strip('"')
            arg3 = arg3.strip("'")
            setattr(storage.all()[key], args[2], cast(arg3))
            storage.all()[key].save()
        elif len(args) == 0:
            print("** class name missing **")
        elif args[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        elif ("{}.{}".format(args[0], args[1])) not in storage.all().keys():
            print("** no instance found **")
        elif len(args) == 2:
            print("** attribute name missing **")
        else:
            print("** value missing **")


def parse(line):
    """Helper method to parse user typed input"""
    return tuple(line.split())


if __name__ == '__main__':
    HBNBCommand().cmdloop()
