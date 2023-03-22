from .base_command import BaseCommand
from ..nfc_protocols.mf_ultralight import MfUltralight
from ..nfc_rpc_transport import NfcRpcTransport


class MfUltralightCommand(BaseCommand):
    class ReadPageCommand(BaseCommand):
        def __init__(self, mf_ultralight: MfUltralight):
            super().__init__(name='read_page')
            self.add_argument('-p', '--page', type=int, required=True)
            self.mf_ultralight = mf_ultralight

        def execute(self, args) -> None:
            result = self.mf_ultralight.read_page(args.page)
            if result['error'] == 0:
                print(f"Page {result['page']}")
                print(f"{result['data']}")
            else:
                print(
                    f"Page {args.page} read failed. Error: {result['error']}")

    class WritePageCommand(BaseCommand):
        def __init__(self, mf_ultralight: MfUltralight):
            super().__init__(name='write_page')
            self.add_argument('-p', '--page', type=int, required=True)
            self.add_argument(
                '-d', '--data', type=self.format_hex_string, required=True)
            self.mf_ultralight = mf_ultralight

        def execute(self, args) -> None:
            print(f"Writing MfUltralight page {args.page} data {args.data}")
            result = self.mf_ultralight.write_page(args.page, args.data)
            if result['error'] == 0:
                print(f"Page {args.page} write success")
            else:
                print(
                    f"Page {args.page} write failed. Error: {result['error']}")

    def __init__(self, transport: NfcRpcTransport):
        super().__init__(name='mf_ultralight')
        self.mf_ultralight = MfUltralight(transport)
        self.add_child(self.ReadPageCommand(self.mf_ultralight))
        self.add_child(self.WritePageCommand(self.mf_ultralight))
