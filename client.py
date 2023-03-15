#!/usr/bin/env python3

from nfc_rpc_client.base_command import BaseCommand
from nfc_rpc_client.completer import Completer
from nfc_rpc_client.nfca import Nfca
from nfc_rpc_client.mf_ultralight import MfUltralight
from nfc_rpc_client.nfc_rpc_transport import NfcRpcTransport


class NfcRpcRootCommand(BaseCommand):
    def __init__(self, transport):
        super().__init__(name='root')
        root_commands = {
            "quit": self.quit,
            "q": self.quit,
        }
        self.commands.update(root_commands)
        self.children = [
            Nfca(transport),
            MfUltralight(transport),
        ]

        self.commands.update({x.get_name(): x.process for x in self.children})

    def quit(self):
        return False
    
    def get_children(self):
        return self.children



class NfcRpc():
    def __init__(self):
        # self.transport = NfcRpcTransport()
        self.transport = None
        self.root_cmd = NfcRpcRootCommand(self.transport)

        # Create completer
        self.completer = Completer(self.root_cmd)

    def run(self):
        while True:
            command = input("> ").strip()
            if not command:
                continue

            # Split command and arguments
            parts = command.split()
            func_name = parts[0].lower()

            if func_name in self.root_cmd.get_commands().keys():
                func = self.root_cmd.get_commands()[func_name]
                if func(*parts[1:]) == False:
                    break
            else:
                print("Unknown command:", command)


if __name__ == "__main__":
    nfc_rpc = NfcRpc()
    nfc_rpc.run()
