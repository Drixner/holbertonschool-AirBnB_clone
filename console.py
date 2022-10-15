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
        """ Exit the shell """
        return True

    def do_EOF(self, line):
        """ Exit the shell """
        print()
        retur True

if __name__ == '__main__':
    HBNBCommand().cmdloop()
