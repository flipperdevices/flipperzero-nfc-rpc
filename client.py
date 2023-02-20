#!/usr/bin/env python3

from nfc_rpc_client.base_command import BaseCommand
from nfc_rpc_client.completer import Completer
from nfc_rpc_client.mf_ultralight import MfUltralight

import nfc_rpc_client.nfc_protobuf_compiled.nfc_pb2 as nfc_proto
from flipperzero_protobuf_py.flipperzero_protobuf.flipper_proto import FlipperProto
from flipperzero_protobuf_py.flipperzero_protobuf.cli_helpers import *
from flipperzero_protobuf_py.flipperzero_protobuf.flipper_base import FlipperProtoException

class NfcRpc(BaseCommand):
    def __init__(self):
        super().__init__(name='root')

        nfc_rpc_commands = {
            "quit": self.quit,
            "q": self.quit,
            "nfca": self.nfca,
        }
        self.commands.update(nfc_rpc_commands)

        self.protocols_objects = [MfUltralight()]
        self.commands.update(
            {x.get_name(): x.process for x in self.protocols_objects})

        # Create completer
        self.completer = Completer(self.commands)

    def quit(self):
        return False
    
    def nfca(self, *args):
        pass


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
