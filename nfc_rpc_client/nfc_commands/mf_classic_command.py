from .base_command import BaseCommand
from ..nfc_protocols.mf_classic import MfClassic
from ..nfc_rpc_transport import NfcRpcTransport
import signal


class MfClassicCommand(BaseCommand):
    class AuthCommand(BaseCommand):
        def __init__(self, mf_classic: MfClassic):
            super().__init__(name='auth')
            self.add_argument('-b', '--block', type=int, required=True)
            self.add_argument(
                '-k', '--key', type=self.format_hex_string, required=True)
            self.add_argument('-t', '--key_type', type=str, required=True)
            self.mf_classic = mf_classic

        def execute(self, args) -> None:
            key_type = args.key_type.lower()
            if key_type == 'a' or key_type == 'b':
                result = self.mf_classic.auth(
                    args.block, args.key, args.key_type)
                if result['error'] == 0:
                    print(result)
                else:
                    print(
                        f"Error: {result['error']}")
            else:
                self.help()

    class ReadBlockCommand(BaseCommand):
        def __init__(self, mf_classic: MfClassic):
            super().__init__(name='read_block')
            self.add_argument('-b', '--block', type=int, required=True)
            self.add_argument(
                '-k', '--key', type=self.format_hex_string, required=True)
            self.add_argument('-t', '--key_type', type=str, required=True)
            self.mf_classic = mf_classic

        def execute(self, args) -> None:
            key_type = args.key_type.lower()
            if key_type == 'a' or key_type == 'b':
                result = self.mf_classic.read_block(
                    args.block, args.key, args.key_type)
                if result['error'] == 0:
                    print(result)
                else:
                    print(
                        f"Error: {result['error']}")
            else:
                self.help()

    def __init__(self, transport: NfcRpcTransport):
        super().__init__(name='mf_classic')
        self.mf_classic = MfClassic(transport)
        self.add_child(self.AuthCommand(self.mf_classic))
        self.add_child(self.ReadBlockCommand(self.mf_classic))
