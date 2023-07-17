from .nfc_base_proto import NfcBaseProto
from ..nfc_rpc_transport import NfcRpcTransport
from ..nfc_protobuf_compiled import mf_classic_pb2


class MfClassicProto(NfcBaseProto):
    def __init__(self, transport: NfcRpcTransport) -> None:
        super().__init__(transport)

    def printer(self, var: any) -> str:
        if isinstance(var, bytes):
            return self.decode_bytes(var, len(var))
        elif isinstance(var, int):
            return var
        elif isinstance(mf_classic_pb2.KeyType):
            if var == mf_classic_pb2.KeyTypeA:
                return "A"
            else:
                return "B"
        else:
            return var

    def auth_req(self, block: int, key: bytes, key_type: str) -> None:
        req = mf_classic_pb2.AuthRequest()
        req.block = block
        req.key = key
        if key_type.lower() == "a":
            req.key_type = mf_classic_pb2.KeyTypeA
        elif key_type.lower() == "b":
            req.key_type = mf_classic_pb2.KeyTypeB
        self.send_cmd(req, "mf_classic_auth_req")

    def auth_resp(self) -> dict:
        resp = self.receive_cmd("mf_classic_auth_resp")
        field_names = [f.name for f in resp.DESCRIPTOR.fields]
        return dict((field_name, self.printer(getattr(resp, field_name))) for field_name in field_names)

    def read_block_req(self, block: int, key: bytes, key_type: str) -> None:
        req = mf_classic_pb2.ReadBlockRequest()
        req.block = block
        req.key = key
        if key_type.lower() == "a":
            req.key_type = mf_classic_pb2.KeyTypeA
        else:
            req.key_type = mf_classic_pb2.KeyTypeB
        self.send_cmd(req, "mf_classic_read_block_req")
    
    def read_block_resp(self) -> dict:
        resp = self.receive_cmd("mf_classic_read_block_resp")
        field_names = [f.name for f in resp.DESCRIPTOR.fields]
        return dict((field_name, self.printer(getattr(resp, field_name))) for field_name in field_names)

    def write_block_req(self, block: int, key: bytes, key_type: str, data: bytes) -> None:
        req = mf_classic_pb2.WriteBlockRequest()
        req.block = block
        req.key = key
        if key_type.lower() == "a":
            req.key_type = mf_classic_pb2.KeyTypeA
        else:
            req.key_type = mf_classic_pb2.KeyTypeB
        req.data = data
        self.send_cmd(req, "mf_classic_write_block_req")
    
    def write_block_resp(self) -> dict:
        resp = self.receive_cmd("mf_classic_write_block_resp")
        field_names = [f.name for f in resp.DESCRIPTOR.fields]
        return dict((field_name, self.printer(getattr(resp, field_name))) for field_name in field_names)

    def read_value_req(self, block: int, key: bytes, key_type: str) -> None:
        req = mf_classic_pb2.ReadValueRequest()
        req.block = block
        req.key = key
        if key_type.lower() == "a":
            req.key_type = mf_classic_pb2.KeyTypeA
        else:
            req.key_type = mf_classic_pb2.KeyTypeB
        self.send_cmd(req, "mf_classic_read_value_req")
    
    def read_value_resp(self) -> dict:
        resp = self.receive_cmd("mf_classic_read_value_resp")
        field_names = [f.name for f in resp.DESCRIPTOR.fields]
        return dict((field_name, self.printer(getattr(resp, field_name))) for field_name in field_names)
    
    def change_value_req(self, block: int, key: bytes, key_type: str, data: int) -> None:
        req = mf_classic_pb2.ChangeValueRequest()
        req.block = block
        req.key = key
        if key_type.lower() == "a":
            req.key_type = mf_classic_pb2.KeyTypeA
        else:
            req.key_type = mf_classic_pb2.KeyTypeB
        req.data = data
        self.send_cmd(req, "mf_classic_change_value_req")
    
    def change_value_resp(self) -> dict:
        resp = self.receive_cmd("mf_classic_change_value_resp")
        field_names = [f.name for f in resp.DESCRIPTOR.fields]
        return dict((field_name, self.printer(getattr(resp, field_name))) for field_name in field_names)
