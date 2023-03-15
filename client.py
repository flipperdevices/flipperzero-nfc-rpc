#!/usr/bin/env python3

from nfc_rpc_client.nfc_rpc_transport import NfcRpcTransport
from nfc_rpc_client.nfc_commands.root_command import RootCommand
from nfc_rpc_client.completer import Completer


class Client:
    def __init__(self) -> None:
        self.transport = NfcRpcTransport()
        self.root_cmd = RootCommand(self.transport)
        self.completer = Completer(self.root_cmd)

    def run(self) -> None:
        while True:
            command = input("> ").strip()
            if not command:
                continue

            if self.root_cmd.process(command.split()) == False:
                break


if __name__ == '__main__':
    Client().run()
