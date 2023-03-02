#!/usr/bin/env python3

from nfc_rpc_client.base_command import BaseCommand
from nfc_rpc_client.completer import Completer
from nfc_rpc_client.nfca import Nfca
from nfc_rpc_client.mf_ultralight import MfUltralight
from nfc_rpc_client.nfc_rpc_transport import NfcRpcTransport


class NfcRpc(BaseCommand):
    def __init__(self):
        super().__init__(name='root')

        self.transport = NfcRpcTransport()

        nfc_rpc_commands = {
            "quit": self.quit,
            "q": self.quit,
        }
        self.commands.update(nfc_rpc_commands)

        self.protocols_objects = [
            Nfca(self.transport),
            MfUltralight(self.transport),
        ]
        self.commands.update(
            {x.get_name(): x.process for x in self.protocols_objects})

        # Create completer
        self.completer = Completer(self.commands)

    def quit(self):
        return False

    def bytes_to_hex(self, bytes, length=0):
        if length == 0:
            length = len(bytes)
        return ':'.join('{:02x}'.format(x) for x in bytes[:length])

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
