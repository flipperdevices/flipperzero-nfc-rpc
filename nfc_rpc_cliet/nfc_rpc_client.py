#!/usr/bin/env python3

import readline


import readline


class NfcRpc:
    def __init__(self):
        self.commands = {
            "help": self.help,
            "?": self.help,
            "quit": self.quit,
            "q": self.quit,
            "mfu": self.mfu_command,
        }

        readline.set_completer(self.completer)
        readline.parse_and_bind("tab: complete")

    def completer(self, text, state):
        options = [c for c in self.commands.keys() if c.startswith(text)]
        try:
            return options[state]
        except IndexError:
            return None

    def help(self):
        print("Available commands:", ", ".join(self.commands.keys()))

    def quit(self):
        return False

    def mfu_command(self, *args):
        if not args:
            # Print help for MfUltralight commands
            mfu = MfUltralight()
            mfu.help()
            return

        command = args[0].lower()
        mfu = MfUltralight()

        if command in mfu.commands:
            # Call MfUltralight command with arguments
            func = mfu.commands[command]
            func(*args[1:])
        else:
            print("Unknown command: mfu", command)

    def run(self):
        while True:
            command = input("> ").strip()
            if not command:
                continue

            # Split command and arguments
            parts = command.split()
            func_name = parts[0].lower()

            if func_name in self.commands:
                func = self.commands[func_name]
                if func(*parts[1:]) == False:
                    break
            else:
                print("Unknown command:", command)


class MfUltralight:
    def __init__(self):
        self.commands = {
            "help": self.help,
            "info": self.info,
            "dump": self.dump,
            "read": self.read,
            "write": self.write,
        }

    def help(self):
        print("Available commands:", ", ".join(self.commands.keys()))

    def info(self):
        print("MfUltralight info")

    def dump(self, page):
        print(f"MfUltralight dump page {page}")

    def read(self, page):
        print(f"MfUltralight read page {page}")

    def write(self, page, data):
        print(f"MfUltralight write {data} to page {page}")


if __name__ == "__main__":
    nfc_rpc = NfcRpc()
    nfc_rpc.run()
