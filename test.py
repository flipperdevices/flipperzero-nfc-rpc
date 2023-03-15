#!/usr/bin/env python3

import readline
import argparse
import sys


class MyArgParse(argparse.ArgumentParser):
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
        self.parser = MyArgParse()

    def add_child(self, child):
        self.children.append(child)
        self.has_children = True

    def get_child(self, child_name):
        ret = None
        for child in self.children:
            if child_name == child.get_name():
                ret = child
        return ret

    def get_child_list(self):
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

class QuitCommand(BaseCommand):
    def __init__(self):
        super().__init__(name='q')

    def execute(self, args):
        return False


class NfcaCommand(BaseCommand):
    class NfcaReadCommand(BaseCommand):
        def __init__(self):
            super().__init__(name='read')

        def process(self, args):
            print('Nfca read')

    def __init__(self):
        super().__init__(name='nfca')
        self.add_child(self.NfcaReadCommand())


class MfUltralightCommand(BaseCommand):
    class MfUltralightReadCommand(BaseCommand):
        def __init__(self):
            super().__init__(name='read')
            self.add_argument('-p', '--page', type=int, required=True)

        def execute(self, args):
            print(f'Mf Ul Read page {args.page}')

    class MfUltralightWriteCommand(BaseCommand):
        def __init__(self):
            super().__init__(name='write')
            self.add_argument('-p', '--page', type=int, required=True)
            self.add_argument('-d', '--data')


        def execute(self, args):
            print(f'MfUl write page {args.page} data: {args.data}')

    def __init__(self):
        super().__init__(name='mfu')
        self.add_child(self.MfUltralightWriteCommand())
        self.add_child(self.MfUltralightReadCommand())


class RootComand(BaseCommand):
    def __init__(self):
        super().__init__(name='root')
        self.add_child(QuitCommand())
        self.add_child(NfcaCommand())
        self.add_child(MfUltralightCommand())


class Completer():
    def __init__(self, root_cmd):
        self.root_cmd = root_cmd
        completer_delims = readline.get_completer_delims()
        readline.set_completer_delims(completer_delims.replace('-', ''))
        readline.set_completer(self.complete)
        readline.parse_and_bind("tab: complete")

    def get_options(self, cmd, line_buffer, new_word):
        if cmd.has_arguments:
            if len(line_buffer) == 0:
                return [arg + ' ' for arg in cmd.get_arguments()]
            else:
                start_word = '' if new_word else line_buffer[-1]
                options = [arg + ' ' for arg in cmd.get_arguments() if arg.startswith(start_word)]
                for word in line_buffer:
                    if word in cmd.get_arguments():
                        options.remove(word + ' ')
                return options
        elif cmd.has_children:
            child_list = cmd.get_child_list()
            if len(line_buffer) == 0:
                return child_list
            elif line_buffer[0] in child_list:
                return self.get_options(cmd.get_child(line_buffer[0]), line_buffer[1:], new_word)
            else:
                return [child + ' ' for child in cmd.get_child_list() if child.startswith(line_buffer[0])]

    def complete(self, text, state):
        line_buffer = readline.get_line_buffer()
        new_word = False
        if line_buffer == '':
            new_word = True
        elif line_buffer[-1] == ' ':
            new_word = True

        options = self.get_options(
            self.root_cmd, line_buffer.split(), new_word)

        try:
            return options[state]
        except IndexError:
            return None


class Client():
    def __init__(self) -> None:
        self.root_cmd = RootComand()
        self.completer = Completer(self.root_cmd)

    def run(self):
        while True:
            command = input("> ").strip()
            if not command:
                continue

            if self.root_cmd.process(command.split()) == False:
                break


if __name__ == '__main__':
    Client().run()
