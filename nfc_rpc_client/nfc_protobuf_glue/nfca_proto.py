from .nfc_base_proto import NfcBaseProto
from ..nfc_rpc_transport import NfcRpcTransport
from ..nfc_protobuf_compiled import nfca_pb2


class NfcaProto(NfcBaseProto):
    def __init__(self, transport: NfcRpcTransport) -> None:
        super().__init__(transport)

    def read_req(self) -> None:
        req = nfca_pb2.ReadRequest()
        self.send_cmd(req, "nfca_read_req")

    def read_resp(self) -> dict:
        resp = self.receive_cmd("nfca_read_resp")
        return {"error": resp.error,
                "uid length": resp.uid_len,
                "uid": self.decode_bytes(resp.uid, resp.uid_len),
                "sak": self.decode_bytes(resp.sak, 1),
                "atqa": self.decode_bytes(resp.atqa, 2)}

    def emulate_start_req(self, uid: bytes, atqa: bytes, sak: bytes) -> None:
        req = nfca_pb2.EmulateStartRequest()
        req.uid = uid
        req.uid_len = len(uid)
        req.atqa = atqa
        req.sak = sak
        self.send_cmd(req, "nfca_emulate_start_req")

    def emulate_start_resp(self) -> dict:
        resp = self.receive_cmd("nfca_emulate_start_resp")
        return {"error": resp.error}

    def emulate_stop_req(self) -> None:
        req = nfca_pb2.EmulateStopRequest()
        self.send_cmd(req, "nfca_emulate_stop_req")

    def emulate_stop_resp(self) -> dict:
        resp = self.receive_cmd("nfca_emulate_stop_resp")
        return {"error": resp.error}
