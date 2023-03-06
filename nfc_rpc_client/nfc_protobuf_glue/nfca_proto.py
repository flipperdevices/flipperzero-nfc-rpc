from .nfc_base_proto import NfcBaseProto
from ..nfc_rpc_transport import NfcRpcTransport
from ..nfc_protobuf_compiled import nfca_pb2


class NfcaProto(NfcBaseProto):
    def __init__(self, transport: NfcRpcTransport):
        super().__init__(transport)

    def read_req(self):
        req = nfca_pb2.ReadRequest()
        self.send_cmd(req, "nfca_read_req")

    def read_resp(self):
        resp = self.receive_cmd("nfca_read_resp")
        return {"uid length": resp.uid_len,
                "uid": self.decode_bytes(resp.uid, resp.uid_len),
                "sak": self.decode_bytes(resp.sak, 1),
                "atqa": self.decode_bytes(resp.atqa, 2)}
