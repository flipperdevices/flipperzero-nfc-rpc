from .base_command import BaseCommand
from .nfca_command import NfcaCommand
from .mf_ultralight_command import MfUltralightCommand
from ..nfc_rpc_transport import NfcRpcTransport


class RootCommand(BaseCommand):
    class QuitCommand(BaseCommand):
        def __init__(self):
            super().__init__(name='q')

        def execute(self, args):
            return False

    def __init__(self, transport: NfcRpcTransport):
        super().__init__(name='root')
        self.add_child(self.QuitCommand())
        self.add_child(NfcaCommand(transport))
        self.add_child(MfUltralightCommand(transport))
