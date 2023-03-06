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

    def read_version_req(self):
        req = mf_ultralight_pb2.ReadVersionRequest()
        self.send_cmd(req, "mf_ultralight_read_version_req")

    def read_version_resp(self):
        resp = self.receive_cmd("mf_ultralight_read_version_resp")
        return {'header': resp.header,
                'vendor_id': resp.vendor_id,
                'prod_type': resp.prod_type,
                'prod_subtype': resp.prod_subtype,
                'prod_ver_major': resp.prod_ver_major,
                'prod_ver_minor': resp.prod_ver_minor,
                'storage_size': resp.storage_size,
                'protocol_type': resp.protocol_type}
