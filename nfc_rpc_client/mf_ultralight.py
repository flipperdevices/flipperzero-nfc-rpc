from .base_command import BaseCommand
from .nfc_rpc_transport import NfcRpcTransport
from .nfc_protobuf_glue.mf_ultralight_proto import MfUltralightProto


class MfUltralight(BaseCommand):
    def __init__(self, transport: NfcRpcTransport):
        super().__init__(name='mfu')
        self.transport = transport
        mfu_commands = {
            "info": self.info,
            "dump": self.dump,
            "read": self.read,
            "write": self.write,
            "version": self.read_version,
        }
        self.commands.update(mfu_commands)
        self.commands_args = {
            'read': {'--page'},
            'write': {'--page', '--data'},
        }

    def get_arguments(self, command_name):
        args = {}
        try:
            args.update(self.commands_args[command_name])
        except:
            pass
        return args

    def info(self):
        print("MfUltralight info")

    def dump(self, page):
        print(f"MfUltralight dump page {page}")

    def read(self, page):
        print(f"MfUltralight read page {page}")
        mf_ultralight_proto = MfUltralightProto(self.transport)
        mf_ultralight_proto.read_page_req(int(page))
        resp = mf_ultralight_proto.read_page_resp()
        print(f"{resp['data'].decode('utf-8')}")

    def write(self, page, data):
        print(f"MfUltralight write {data} to page {page}")

    def read_version(self):
        print("MfUltralignt read version")
        mf_ultralight_proto = MfUltralightProto(self.transport)
        mf_ultralight_proto.read_version_req()
        resp = mf_ultralight_proto.read_version_resp()
        print(resp)
