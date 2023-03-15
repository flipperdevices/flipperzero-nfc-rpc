from .base_command import BaseCommand
from ..nfc_protocols.nfca import Nfca
from ..nfc_rpc_transport import NfcRpcTransport


class NfcaCommand(BaseCommand):
    class ReadCommand(BaseCommand):
        def __init__(self, nfca: Nfca):
            super().__init__(name='read')
            self.nfca = nfca

        def execute(self, args):
            result = self.nfca.read()
            print("Nfca detected")
            print(f"UID: {result['uid']}")
            print(f"ATQA: {result['atqa']}")
            print(f"SAK: {result['sak']}")

    def __init__(self, transport: NfcRpcTransport):
        super().__init__(name='nfca')
        self.nfca = Nfca(transport)
        self.add_child(self.ReadCommand(self.nfca))
