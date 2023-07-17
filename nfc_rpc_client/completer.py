import readline
from .nfc_commands.base_command import BaseCommand


class Completer():
    def __init__(self, root_cmd: BaseCommand) -> None:
        self.root_cmd = root_cmd
        completer_delims = readline.get_completer_delims()
        readline.set_completer_delims(completer_delims.replace('-', ''))
        readline.set_completer(self.complete)
        readline.parse_and_bind("tab: complete")

    def get_options(self, cmd: BaseCommand, line_buffer: list, new_word: bool) -> list:
        if cmd.has_arguments:
            if len(line_buffer) == 0:
                return [arg + ' ' for arg in cmd.get_arguments()]
            else:
                start_word = '' if new_word else line_buffer[-1]
                options = [arg + ' ' for arg in cmd.get_arguments()
                           if arg.startswith(start_word)]
                for word in line_buffer:
                    if word in cmd.get_arguments():
                        options.remove(word + ' ')
                return options
        elif cmd.has_children:
            child_list = cmd.get_children_list()
            if len(line_buffer) == 0:
                return child_list
            elif line_buffer[0] in child_list:
                return self.get_options(cmd.get_child(line_buffer[0]), line_buffer[1:], new_word)
            else:
                return [child + ' ' for child in cmd.get_children_list() if child.startswith(line_buffer[0])]

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
