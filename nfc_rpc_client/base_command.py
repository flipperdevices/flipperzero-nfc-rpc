class BaseCommand():
    def __init__(self, name):
        self.name = name
        self.commands = {
            "help": self.help,
            "?": self.help,
        }

    def get_name(self):
        return self.name

    def get_commands(self):
        return self.commands

    def get_arguments(self, command_name):
        return {}

    def help(self):
        print("Available commands:", ", ".join(self.commands.keys()))
        
    def process(self, *args):
        if not args:
            self.help()
            return True

        command = args[0].lower()
        if command in self.commands:
            func = self.commands[command]
            func(*args[1:])
        else:
            print("Unknown command:", command)
