#!/usr/bin/python3
"""
This module define a consule.py
    that contains the entry point of the command interpreter.
"""

import cmd
import json
import shlex
from datetime import datetime
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models import storage
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """
    Class that use a command interpreter class.
    """

    prompt = "(hbnb)"
    __classes_dict = {
        "BaseModel": BaseModel,
        "User": User,
        "Place": Place,
        "State": State,
        "City": City,
        "Amenity": Amenity,
        "Review": Review
    }

    def emptyline(self):
        """
        Empty line to do nothing.
            an empty line + ENTER shouldn’t execute anything
        """

        pass

    def do_nothing(self, arg):
        """
        Method to do nothing.
        """

        pass

    def do_EOF(self, arg):
        """
        Quit of programme in non-interactive mode.
        Quit command CTRL+D to exit the program.
        """

        print("")
        return True

    def do_quit(self, arg):
        """
        Quit command that used exit of program.
        """

        return True

    def do_create(self, args):
        """
        Method to creates a new instance,
            it saves and prints its id.
        """

        if args == "":
            print("** class name missing **")
            return

        arg = shlex.split(args)

        if arg[0] not in HBNBCommand. __classes_dict:
            print("** class doesn't exist **")
            return

        new_instance = HBNBCommand.__classes_dict[arg[0]]()
        new_instance.save()
        print(new_instance.id)

    def do_show(self, args):
        """
        Prints the string representation of\
                an instance based on the class name and id.
        Ex: $ show BaseModel 1234-1234-1234.
        """
        arg = shlex.split(args)

        if len(arg) == 0:
            print("** class name missing **")
            return

        if arg[0] not in HBNBCommand.__classes_dict:
            print("** class doesn't exist **")
            return

        if len(arg) < 2:
            print("** instance id missing **")
            return

        storage.reload()
        obj = storage.all()
        ObjDict = arg[0] + "." + arg[1]

        if ObjDict in obj:
            print(str(obj[ObjDict]))
        else:
            print("** no instance found **")

    def do_destroy(self, args):
        """
        Deletes an instance based on the class name and id.
        (save the change into the JSON file).

        Ex: $ destroy BaseModel 1234-1234-1234.
        """

        arg = shlex.split(args)

        if len(arg) == 0:
            print("** class name missing **")
            return

        if arg[0] not in HBNBCommand.__classes_dict:
            print("** class doesn't exist **")
            return

        if len(arg) < 2:
            print("** instance id missing **")
            return

        storage.reload()
        obj = storage.all()
        ObjDict = arg[0] + "." + arg[1]

        if ObjDict in obj:
            del obj[ObjDict]
            storage.save()
        else:
            print("** no instance found **")

    def do_all(self, args):
        """
        Prints all string representation of
            all instances based or not on the class name.

        Ex: $ all BaseModel or $ all.
        """

        storage.reload()
        JsonDict = []
        ObjDict = storage.all()

        if args == "":
            for k, v in ObjDict.items():
                JsonDict.append(str(v))
            print(json.dumps(JsonDict))
            return

        arg = shlex.split(args)

        if arg[0] in HBNBCommand.__classes_dict.keys():
            for i, j in ObjDict.items():
                if arg[0] in i:
                    JsonDict.append(str(j))
            print(json.dumps(JsonDict))
            return
        else:
            print("** class doesn't exist **")

    def do_update(self, args):
        """
        Updates an instance based on the class name and id:
            by adding or updating attribute
            (save the change into the JSON file).

        Ex: $ update BaseModel 1234-1234-1234 email "aibnb@mail.com".
        """

        if not args:
            print("** class name missing **")
            return

        arg = shlex.split(args)
        storage.reload()
        obj = storage.all()

        if arg[0] not in HBNBCommand.__classes_dict.keys():
            print("** class doesn't exist **")
            return

        if len(arg) == 1:
            print("** instance id missing **")
            return

        try:
            ObjKey = arg[0] + "." + arg[1]
            obj[ObjKey]

        except KeyError:
            print("** no instance found **")
            return

        if (len(arg) == 2):
            print("** attribute name missing **")
            return

        if (len(arg) == 3):
            print("** value missing **")
            return

        ObjDict = obj[ObjKey].__dict__

        if arg[2] in ObjDict.keys():
            DictType = type(ObjDict[arg[2]])
            print(DictType)
            ObjDict[arg[2]] = type(ObjDict[arg[2]])(arg[3])
        else:
            ObjDict[arg[2]] = arg[3]

        storage.save()

    def do_update_help(self, args):
        """
        Updates an instance based on the class name and id:
            by adding or updating attribute.
            (save the change into the JSON file).

        Ex: $ update BaseModel 1234-1234-1234 email "aibnb@mail.com".
        """

        if not args:
            print("** class name missing **")
            return

        NewDict = "{" + args.split("{")[1]
        arg = shlex.split(args)
        storage.reload()
        obj = storage.all()

        if arg[0] not in HBNBCommand.__class_dict.keys():
            print("** class doesn't exist **")
            return

        if len(arg) == 1:
            print("** instance id missing **")
            return

        try:
            ObjKey = arg[0] + "." + arg[1]
            obj[ObjKey]

        except KeyError:
            print("** no instance found **")
            return

        if (NewDict == "{"):
            print("** attribute name missing **")
            return

        NewDict = my_dict.replace("\'", "\"")
        NewDict = json.loads(NewDict)
        ObjInst = obj[ObjKey]

        for i in NewDict:
            if hasattr(ObjInst, i):
                DictType = type(getattr(ObjInst, i))
                setattr(ObjInst, i, NewDict[i])
            else:
                setattr(ObjInst, i, NewDict[i])

        storage.save()

    def do_count(self, args):
        """
        Method that count the current number of class instances.
        """

        obj = storage.all()
        c = 0

        for i in obj:
            if (args in i):
                c += 1

        print(c)

    def all_features(self, args):
        """
        Method that  defines an actions on objects.
        """

        CmdDict = {
            "all": self.do_all, "count": self.do_count,
            "show": self.do_show, "destroy": self.do_destroy,
            "update": self.do_update,
        }

        arg = args.strip()
        v = arg.split(".")

        if len(v) != 2:
            cmd.Cmd.all_features(self, arg)
            return

        ClassName = v[0]
        Cmnd = val[1].split("(")[0]
        ln = ""

        if (Cmnd == "update" and v[1].split("(")[1][-2] == "}"):
            i = v[1].split("(")[1].split(",", 1)
            i[0] = shlex.split(i[0])[0]
            ln = "".join(i)[0:-1]
            ln = ClassName + " " + l
            self.do_help_update(ln.strip())
            return

        try:
            i = v[1].split("(")[1].split(",")

            for n in range(len(i)):
                if (n != len(i) - 1):
                    ln = ln + " " + shlex.split(i[n])[0]
                else:
                    ln = ln + " " + shlex.split(i[n][0:-1])[0]

        except IndexError:
            i = ""
            ln = ""

        ln = ClassName + ln

        if (Cmnd in CmdDict.keys()):
            CmdDict[Cmnd](l.strip())


if __name__ == '__main__':
    HBNBCommand().cmdloop()
