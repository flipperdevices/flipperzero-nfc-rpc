import argparse
import sys

class MyArgumentParser(argparse.ArgumentParser):
    def error(self, message):
        self.print_usage(sys.stderr)
        print(f'{message}')
        raise Exception()

class BaseCommand:
    def __init__(self, name):
        self.name = name
        self.children = []
        self.has_children = False
        self.arguments = []
        self.has_arguments = False
        self.parser = MyArgumentParser()

    def add_child(self, child):
        self.children.append(child)
        self.has_children = True

    def get_child(self, child_name):
        ret = None
        for child in self.children:
            if child_name == child.get_name():
                ret = child
        return ret

    def get_children_list(self) -> list:
        return [child.get_name() for child in self.children]

    def get_name(self):
        return self.name

    def help(self):
        if self.has_children:
            children_commands = [child.get_name() for child in self.children]
            print("Available commands: ", ", ".join(children_commands))
        elif self.has_arguments:
            print("Usage:")
            print(f"{self.name}", " ".join(self.arguments))

    def add_argument(self, short_name: str, full_name: str, type=str, required=False):
        self.arguments.append(full_name)
        self.parser.add_argument(short_name, full_name, type=type, required=required)
        self.has_arguments = True

    def get_arguments(self):
        return self.arguments

    def execute(self, args):
        pass

    def process(self, args):
        if self.has_children:
            if len(args) > 0:
                child_cmd = self.get_child(args[0])
                if child_cmd is not None:
                    return child_cmd.process(args[1:])
                else:
                    self.help()
            else:
                self.help()
        elif self.has_arguments:
            try:
                parsed_args = self.parser.parse_args(args)
                return self.execute(parsed_args)
            except:
                pass
        else:
            return self.execute(None)
