from .nfc_base_proto import NfcBaseProto
from ..nfc_rpc_transport import NfcRpcTransport
from ..nfc_protobuf_compiled import mf_ultralight_pb2


class MfUltralightProto(NfcBaseProto):
    def __init__(self, transport: NfcRpcTransport) -> None:
        super().__init__(transport)

    def read_page_req(self, page: int = 0) -> None:
        req = mf_ultralight_pb2.ReadPageRequest()
        req.page = page
        self.send_cmd(req, "mf_ultralight_read_page_req")

    def read_page_resp(self) -> dict:
        resp = self.receive_cmd("mf_ultralight_read_page_resp")
        return {'error': resp.error, 'page': resp.page, 'data': self.decode_bytes(resp.data, 4)}

    def read_version_req(self) -> None:
        req = mf_ultralight_pb2.ReadVersionRequest()
        self.send_cmd(req, "mf_ultralight_read_version_req")

    def read_version_resp(self) -> dict:
        resp = self.receive_cmd("mf_ultralight_read_version_resp")
        field_names = [f.name for f in resp.DESCRIPTOR.fields]
        return dict((field_name, self.printer(getattr(resp, field_name))) for field_name in field_names)
    
    def printer(self, var: any) -> str:
        if isinstance(myvar, bytes):
            return ...
        elif isinstance(myvar, int):
            return ...
        return {'error': resp.error,
                'header': resp.header,
                'vendor_id': resp.vendor_id,
                'prod_type': resp.prod_type,
                'prod_subtype': resp.prod_subtype,
                'prod_ver_major': resp.prod_ver_major,
                'prod_ver_minor': resp.prod_ver_minor,
                'storage_size': resp.storage_size,
                'protocol_type': resp.protocol_type}

    def write_page_req(self, page: int, data: bytes) -> None:
        req = mf_ultralight_pb2.WritePageRequest()
        req.page = page
        req.data = data
        self.send_cmd(req, "mf_ultralight_write_page_req")

    def write_page_resp(self) -> bool:
        resp = self.receive_cmd("mf_ultralight_write_page_resp")
        return {'error': resp.error}

    def read_signature_req(self) -> None:
        req = mf_ultralight_pb2.ReadSignatureRequest()
        self.send_cmd(req, "mf_ultralight_read_signature_req")

    def read_signature_resp(self) -> dict:
        resp = self.receive_cmd("mf_ultralight_read_signature_resp")
        return {'error': resp.error, 'data': self.decode_bytes(resp.data, 32)}

    def read_counter_req(self, counter_num: int) -> None:
        req = mf_ultralight_pb2.ReadCounterRequest()
        req.counter_num = counter_num
        self.send_cmd(req, "mf_ultralight_read_counter_req")

    def read_counter_resp(self) -> dict:
        resp = self.receive_cmd("mf_ultralight_read_counter_resp")
        return {'error': resp.error, 'counter_num': resp.counter_num, 'data': self.decode_bytes(resp.data, 3)}

    def read_tearing_flag_req(self, flag_num: int) -> None:
        req = mf_ultralight_pb2.ReadTearingFlagRequest()
        req.flag_num = flag_num
        self.send_cmd(req, "mf_ultralight_read_tearing_flag_req")

    def read_tearing_flag_resp(self) -> dict:
        resp = self.receive_cmd("mf_ultralight_read_tearing_flag_resp")
        return {'error': resp.error, 'flag_num': resp.flag_num, 'data': self.decode_bytes(resp.data, 1)}

    def emulate_start_req(self, data: bytes) -> None:
        req = mf_ultralight_pb2.EmulateStartRequest()
        req.data = data
        self.send_cmd(req, "mf_ultralight_emulate_start_req")

    def emulate_start_resp(self) -> dict:
        resp = self.receive_cmd("mf_ultralight_emulate_start_resp")
        return {"error": resp.error}

    def emulate_stop_req(self) -> None:
        req = mf_ultralight_pb2.EmulateStopRequest()
        self.send_cmd(req, "mf_ultralight_emulate_stop_req")

    def emulate_stop_resp(self) -> dict:
        resp = self.receive_cmd("mf_ultralight_emulate_stop_resp")
        return {"error": resp.error}
