from ..nfc_protobuf_glue import nfca_proto
from ..nfc_rpc_transport import NfcRpcTransport


class Nfca:
    def __init__(self, transport: NfcRpcTransport) -> None:
        self.nfca_proto = nfca_proto.NfcaProto(transport)

    def read(self) -> dict:
        self.nfca_proto.read_req()
        return self.nfca_proto.read_resp()

    def emulate_start(self, uid: bytes, atqa: bytes, sak: bytes) -> dict:
        self.nfca_proto.emulate_start_req(uid, atqa, sak)
        return self.nfca_proto.emulate_start_resp()

    def emulate_stop(self) -> dict:
        self.nfca_proto.emulate_stop_req()
        return self.nfca_proto.emulate_stop_resp()
