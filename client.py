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

        self.proto = FlipperProto()

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
    
    def bytes_to_hex(self, bytes, length=0):
        if length == 0:
            length = len(bytes)
        return ':'.join('{:02x}'.format(x) for x in bytes[:length])

    def nfca(self, *args):
        req = nfc_proto.NfcaReadRequest()
        req.ok = True
        self.proto.rpc_app_data_exchange_send(req.SerializeToString())
        resp = self.proto.rpc_app_data_exchange_recv()
        nfc_resp = nfc_proto.NfcaReadResponse()
        try:
            nfc_resp.ParseFromString(resp)
        except:
            print("Error parsing response")
            return
        uid = self.bytes_to_hex(nfc_resp.uid, nfc_resp.uid_len)
        print(f"UID: {uid}")
        sak = self.bytes_to_hex(nfc_resp.sak)
        print(f"SAK: {sak}")
        atqa = self.bytes_to_hex(nfc_resp.atqa)
        print(f"ATQA: {atqa}")

    def run(self):
        self.proto.rpc_app_start("NfcRpc", "RPC")

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
