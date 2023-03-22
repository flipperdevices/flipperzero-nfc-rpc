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

    def write_page(self, page: int, data: bytes) -> dict:
        self.mf_ul_proto.write_page_req(page, data)
        return self.mf_ul_proto.write_page_resp()

    def read_signature(self) -> dict:
        self.mf_ul_proto.read_signature_req()
        return self.mf_ul_proto.read_signature_resp()
    
    def read_counter(self, counter_num: int) -> dict:
        self.mf_ul_proto.read_counter_req(counter_num)
        return self.mf_ul_proto.read_counter_resp()
    
    def read_tearing_flag(self, flag_num: int) -> dict:
        self.mf_ul_proto.read_tearing_flag_req(flag_num)
        return self.mf_ul_proto.read_counter_resp()
    
