from .base_command import BaseCommand
from ..nfc_protocols.nfca import Nfca
from ..nfc_rpc_transport import NfcRpcTransport
import signal


class NfcaCommand(BaseCommand):
    class ReadCommand(BaseCommand):
        def __init__(self, nfca: Nfca):
            super().__init__(name='read')
            self.nfca = nfca

        def execute(self, args):
            result = self.nfca.read()
            if result['error'] == 0:
                print("Nfca detected")
                print(f"UID: {result['uid']}")
                print(f"ATQA: {result['atqa']}")
                print(f"SAK: {result['sak']}")
            else:
                print(f"Error: {result['error']}")

    class EmulateCommand(BaseCommand):
        def __init__(self, nfca: Nfca):
            super().__init__(name='emulate')
            self.nfca = nfca
            self.emulation_in_progress = False
            self.add_argument(
                '-u', '--uid', type=self.format_hex_string, required=True)
            self.add_argument(
                '-a', '--atqa', type=self.format_hex_string, required=True)
            self.add_argument(
                '-s', '--sak', type=self.format_hex_string, required=True)

        def execute(self, args):
            print(
                f"Emulating NFC-A with UID: {args.uid} ATQA: {args.atqa} SAK: {args.sak}")
            result = self.nfca.emulate_start(args.uid, args.atqa, args.sak)
            if result['error'] == 0:
                self.emulation_in_progress = True
                print("Press Ctrl+C to abort")
                signal.sigwait({signal.SIGINT})
                result = self.nfca.emulate_stop()
                if result['error'] == 0:
                    print("")
                    print("Emulation stopped")
                else:
                    print(f"Emulation stop failed. Error: {result['error']}")

            else:
                print(f"Failed to start emulation. Error: {result['error']}")

    def __init__(self, transport: NfcRpcTransport):
        super().__init__(name='nfca')
        self.nfca = Nfca(transport)
        self.add_child(self.ReadCommand(self.nfca))
        self.add_child(self.EmulateCommand(self.nfca))
