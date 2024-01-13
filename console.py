#!/usr/bin/python3
"""
Console main
"""
import cmd
import json
import shlex
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models.state import State
from models.city import City


class HBNBCommand(cmd.Cmd):
    """HBNBCommand class"""
    prompt = "(hbnb) "
    vClass = {
        "BaseModel": BaseModel,
        "User": User,
        "Amenity": Amenity,
        "Place": Place,
        "Review": Review,
        "State": State,
        "City": City
        }
    def emptyline(self):
        """do nothing when enter empty"""
        pass

    def do_nothing(self, arg):
        """do_nothing"""
        pass

    def do_EOF(self, arg):
        """EOF to exit"""
        print("")
        return True

    def do_quit(self, arg):
        """Close and saves"""
        return True

    def do_create(self, arg):
        """
        create BaseMOdel and save json
        Usage: create <className>
        """
        cmds = shlex.split(arg)
        if len(cmds) == 0:
            print("** class name missing **")
            return
        if cmds[0] not in HBNBCommand.vClass.keys():
            print("** class doesn't exist **")
            return
        newInst = HBNBCommand.vClass[cmds[0]]()
        newInst.save()
        print(newInst.id)

    def do_show(self, arg):
        """
        print str representation
        Usage: show <className> <id>
        """
        cmds = shlex.split(arg)
        if len(cmds) == 0:
            print("** class name missing **")
            return
        if cmds[0] not in HBNBCommand.vClass.keys():
            print("** class doesn't exist **")
            return
        if len(cmds) < 2:
            print("** instance id missing **")
            return
        storage.reload()
        objects = storage.all()
        key = "{}.{}".format(cmds[0], cmds[1])
        if key in objects:
            print(str(objects[key]))
        else:
            print("** no instance found **")

    def do_destroy(self, arg):
        """
        delete specefic object
        Usage: destroy <className> <id>
        """
        cmds = shlex.split(arg)
        if len(cmds) == 0:
            print("** class name missing **")
            return
        if cmds[0] not in HBNBCommand.vClass.keys():
            print("** class doesn't exist **")
            return
        if len(cmds) <= 1:
            print("** instance id missing **")
            return
        storage.reload()
        objects = storage.all()
        key = "{}.{}".format(cmds[0], cmds[1])
        if key in objects:
            del objects[key]
            storage.save()
        else:
            print("** no instance found **")

    def do_all(self, arg):
        """
        Prints all representation of instances on the class
        Usage: <User>.all() or <User>.show()
        """
        storage.reload()
        cmds = shlex.split(arg)
        jsonStr = []
        objects = storage.all()
        if not arg:
            for key in objects:
                jsonStr.append(str(objects[key]))
            print(json.dumps(jsonStr))
            return
        if cmds[0] not in HBNBCommand.vClass.keys():
            print("** class doesn't exist **")
        else:
            for key in objects:
                if cmds[0] in key:
                    jsonStr.append(str(objects[key]))
            print(json.dumps(jsonStr))

    def do_count(self, arg):
        """
        counts number of instances
        usage: <class name>.count()
        """
        objects = storage.all()
        cmds = shlex.split(arg)
        if arg:
            className = cmds[0]
        count = 0
        if cmds:
            if className in self.vClass:
                for obj in objects.values():
                    if obj.__class__.__name__ == className:
                        count += 1
                print(count)
            else:
                print("** invalid class name **")
        else:
            print("** class name missing **")

    def do_update(self, arg):
        """
        Updates specefic instance
        Usage: update <className> <id> <attribute_name> "<attribute_value>"
        """
        cmds = shlex.split(arg)
        if not arg:
            print("** class name missing **")
            return
        if len(cmds) == 0:
            print("** class name missing **")
        elif cmds[0] not in self.vClass:
            print("** class doesn't exist **")
        elif len(cmds) < 2:
            print("** instance id missing **")
        else:
            storage.reload()
            objects = storage.all()
            key = "{}.{}".format(cmds[0], cmds[1])
            if key not in objects:
                print("** no instance found **")
            elif len(cmds) < 3:
                print("** attribute name missing **")
            elif len(cmds) < 4:
                print("** value missing **")
            else:
                inst = objects[key]
                if hasattr(inst, cmds[2]):
                    typeNew = type(getattr(inst, cmds[2]))
                    setattr(inst, cmds[2], typeNew(cmds[3]))
                else:
                    setattr(inst, cmds[2], cmds[3])
                storage.save()

    def reformatUpdate(self, arg):
        """
        reformat update instance
        """
        if not arg:
            print("** class name missing **")
            return
        frmtName = "{" + arg.split("{")[1]
        cmds = shlex.split(arg)
        storage.reload()
        objects = storage.all()
        if cmds[0] not in HBNBCommand.vClass.keys():
            print("** class doesn't exist **")
            return
        if (len(cmds) == 1):
            print("** instance id missing **")
            return
        key = "{}.{}".format(cmds[0], cmds[1])
        if key not in objects:
            print("** no instance found **")
        if (frmtName == "{"):
            print("** attribute name missing **")
            return
        frmtName = frmtName.replace("\'", "\"")
        frmtName = json.loads(frmtName)
        inst = objects[key]
        for my_key in frmtName:
            if hasattr(inst, my_key):
                typeNew = type(getattr(inst, my_key))
                setattr(inst, my_key, frmtName[my_key])
            else:
                setattr(inst, my_key, frmtName[my_key])
        storage.save()

    def default(self, arg):
        """defualt when input invalid"""
        validCmd = {
            "all": self.do_all,
            "show": self.do_show,
            "destroy": self.do_destroy,
            "count": self.do_count,
            "update": self.do_update
        }
        arg = arg.strip()
        cmds = arg.split(".")
        if len(cmds) != 2:
            cmd.Cmd.default(self, arg)
            return
        className = cmds[0]
        cmd = cmds[1].split("(")[0]
        frmt = ""
        if (cmd == "update" and cmds[1].split("(")[1][-2] == "}"):
            paras = cmds[1].split("(")[1].split(",", 1)
            paras[0] = shlex.split(paras[0])[0]
            frmt = "".join(paras)[0:-1]
            frmt = className + " " + frmt
            self.reformatUpdate(frmt.strip())
            return
        try:
            paras = cmds[1].split("(")[1].split(",")
            for i in range(len(paras)):
                if (i != len(paras) - 1):
                    frmt = frmt + " " + shlex.split(paras[i])[0]
                else:
                    frmt = frmt + " " + shlex.split(paras[i][0:-1])[0]
        except IndexError:
            frmt = ""
        frmt = className + frmt
        if (cmd in validCmd.keys()):
            validCmd[cmd](frmt.strip())

if __name__ == '__main__':
    HBNBCommand().cmdloop()
