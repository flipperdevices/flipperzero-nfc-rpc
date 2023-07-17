from ..nfc_protobuf_glue import mf_classic_proto
from ..nfc_rpc_transport import NfcRpcTransport


def ProtoWrapper(fn):
    fn_name = fn.__name__

    def impl(self, *args):
        getattr(self.mf_classic_proto, fn_name + "_req")(*args)
        return getattr(self.mf_classic_proto, fn_name + "_resp")()

    return impl


class MfClassic():
    def __init__(self, transport: NfcRpcTransport) -> None:
        self.mf_classic_proto = mf_classic_proto.MfClassicProto(transport)
    
    @ProtoWrapper
    def auth(self, block: int, key: bytes, key_type: str) -> dict:
        pass

    @ProtoWrapper
    def read_block(self, block: int, key: bytes, key_type: str) -> dict:
        pass

    @ProtoWrapper
    def write_block(self, block: int, key: bytes, key_type: str, data: bytes) -> dict:
        pass

    @ProtoWrapper
    def read_value(self, block: int, key: bytes, key_type: str) -> dict:
        pass

    @ProtoWrapper
    def change_value(self, block: int, key: bytes, key_type: str, data: int) -> dict:
        pass

    

