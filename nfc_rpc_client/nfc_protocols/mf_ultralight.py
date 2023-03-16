from ..nfc_protobuf_glue import mf_ultralight_proto
from ..nfc_rpc_transport import NfcRpcTransport


class MfUltralight():
    def __init__(self, transport: NfcRpcTransport) -> None:
        self.mf_ul_proto = mf_ultralight_proto.MfUltralightProto(transport)

    def read_page(self, page: int) -> dict:
        self.mf_ul_proto.read_page_req(page)
        return self.mf_ul_proto.read_page_resp()

    def read_version(self) -> dict:
        self.mf_ul_proto.read_version_req()
        return self.mf_ul_proto.read_version_resp()

    def write_page(self, page: int, data: bytes) -> bool:
        self.mf_ul_proto.write_page_req(page, data)
        return self.mf_ul_proto.write_page_resp()
