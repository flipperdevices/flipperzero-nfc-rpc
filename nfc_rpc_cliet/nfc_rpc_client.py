#!/usr/bin/env python3

from base_command import BaseCommand
from completer import Completer
from mf_ultralight import MfUltralight


class NfcRpc(BaseCommand):
    def __init__(self):
        super().__init__(name='root')

        nfc_rpc_commands = {
            "quit": self.quit,
            "q": self.quit,
        }
        self.commands.update(nfc_rpc_commands)

        self.protocols_objects = [MfUltralight()]
        self.commands.update(
            {x.get_name(): x.process for x in self.protocols_objects})

        # Create completer
        self.completer = Completer(self.commands)

    def quit(self):
        return False

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


if __name__ == "__main__":
    nfc_rpc = NfcRpc()
    nfc_rpc.run()
