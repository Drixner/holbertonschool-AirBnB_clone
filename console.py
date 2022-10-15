#!/usr/bin/python3
""" Console to manage hbnb data """

import cmd


class HBNBCommand(cmd.Cmd):
    """ Class HBNBCommand CLI, entry command interpreter """
    prompt = '(hbnb) '

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

if __name__ == '__main__':
    HBNBCommand().cmdloop()
