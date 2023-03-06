from .base_command import BaseCommand
from .nfc_protobuf_glue.nfca_proto import NfcaProto
from .nfc_rpc_transport import NfcRpcTransport
from .nfc_protobuf_compiled import nfca_pb2


class Nfca(BaseCommand):
    def __init__(self, transport: NfcRpcTransport):
        super().__init__("nfca")
        self.transport = transport
        nfca_commands = {
            "read": self.read,
        }
        self.commands.update(nfca_commands)

    def read(self):
        nfca_proto = NfcaProto(self.transport)
        nfca_proto.read_req()
        resp = nfca_proto.read_resp()
        print(f"Nfca detected!")
        print(f"Uid: {resp['uid'].decode('utf-8')}")
        print(f"ATQA: {resp['atqa'].decode('utf-8')}")
        print(f"SAK: {resp['sak'].decode('utf-8')}")
        
