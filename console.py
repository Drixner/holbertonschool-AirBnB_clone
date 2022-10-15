#!/usr/bin/python3
""" Console to manage hbnb data """

import cmd


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
            rint("** class doesn't exist **")
        else:
            cls_d = {'BaseModel': BaseModel}

            new_obj = cls_d[args]()
            new_obj.save()
            print("{}".format(new_obj.id))
            storage.save()

    def do_show(self, line):
        """ Print string representation: name and id """
        arg = line.split()
        obj_dict = storage.all()  # all function from file_storage.py
        if len(arg) == 0:
            print("** class name missing **")
        elif arg[0] not in HBNBCommand.classes:
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
        obj_dict = storage.all()  # all function from file_storage.py
        if len(arg) == 0:
            print("** class name missing **")
        elif arg[0] not in HBNBCommand.classes:
            print("** class doesn't exist **")
        elif len(arg) == 1:
            print("** instance id missing **")
        elif "{}.{}".format(arg[0], arg[1]) not in obj_dict:
            print("** no instance found **")
        else:
            del (obj_dict["{}.{}".format(arg[0], arg[1])])
            storage.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
