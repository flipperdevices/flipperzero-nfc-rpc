from .nfc_base_proto import NfcBaseProto
from ..nfc_rpc_transport import NfcRpcTransport
from ..nfc_protobuf_compiled import mf_ultralight_pb2


class MfUltralightProto(NfcBaseProto):
    def __init__(self, transport: NfcRpcTransport):
        super().__init__(transport)

    def read_page_req(self, page: int = 0):
        req = mf_ultralight_pb2.ReadPageRequest()
        req.page = page
        self.send_cmd(req, "mf_ultralight_read_page_req")

    def read_page_resp(self):
        resp = self.receive_cmd("mf_ultralight_read_page_resp")
        return {'page': resp.page, 'data': resp.data}
