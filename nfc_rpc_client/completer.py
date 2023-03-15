import readline
import sys

# root = {'?', 'help', 'nfca', 'q', 'quit', 'mfu'}

# mfu = {'read', 'write', 'version', '?', 'help'}

# nfca = {'read', 'info', '?', 'help'}


class Completer():
    def __init__(self, root_cmd):
        self.root_cmd = root_cmd
        readline.set_completer(self.complete)
        readline.parse_and_bind("tab: complete")

        self.root_cmd_list = root_cmd.get_commands().keys()
        

    def complete(self, text, state):
        cmd = readline.get_line_buffer().split()
        cmd_len = len(cmd)

        if cmd_len < 2:
            options = [c for c in self.root_cmd.get_commands().keys() if c.startswith(text)]
        elif cmd_len == 2:
            children = self.root_cmd.get_children()
            partly_typed = False
            for child in children:
                if cmd[0] in child.get_commands():
                    partly_typed = False
                else:
                
                

        # try:
        #     cmd = readline.get_line_buffer().split()[0]
        # except IndexError:
        #     cmd = ''

        # if cmd == 'nfca':
        #     options = [c for c in nfca if c.startswith(text)]
        # elif cmd == 'mfu':
        #     options = [c for c in mfu if c.startswith(text)]
        # else:
        #     options = [c for c in root if c.startswith(text)]

        try:
            return options[state] + ' '
        except IndexError:
            return None
