from ..nfc_protobuf_glue import mf_ultralight_proto
from ..nfc_rpc_transport import NfcRpcTransport

def ProtoWrapper(fn):
    fn_name = fn.__name__

    def impl(self, *args):
        getattr(self.mf_ul_proto, fn_name + "_req")(*args)
        return getattr(self.mf_ul_proto, fn_name + "_resp")()

    return impl


class MfUltralight():
    def __init__(self, transport: NfcRpcTransport) -> None:
        self.mf_ul_proto = mf_ultralight_proto.MfUltralightProto(transport)

    @ProtoWrapper
    def read_page(self, page: int) -> dict:
        pass

    @ProtoWrapper
    def read_version(self) -> dict:
        pass

    def read_version_(self) -> dict:
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

    def emulate_start(self, data: bytes) -> dict:
        self.mf_ul_proto.emulate_start_req(data)
        return self.mf_ul_proto.emulate_start_resp()

    def emulate_stop(self) -> dict:
        self.mf_ul_proto.emulate_stop_req()
        return self.mf_ul_proto.emulate_stop_resp()    
