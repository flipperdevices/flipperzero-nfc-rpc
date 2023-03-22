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

    class ReadVersionCommand(BaseCommand):
        def __init__(self, mf_ultralight: MfUltralight):
            super().__init__(name='read_version')
            self.mf_ultralight = mf_ultralight

        def execute(self, args) -> None:
            print(f"Reading Mifare Ultralight Version")
            result = self.mf_ultralight.read_version()
            if result['error'] == 0:
                print(f"Header: {result['header']}")
                print(f"Vendor ID: {result['vendor_id']}")
                print(f"Product type: {result['prod_type']}")
                print(f"Product subtype: {result['prod_subtype']}")
                print(f"Product major version: {result['prod_ver_major']}")
                print(f"Product minor version: {result['prod_ver_minor']}")
                print(f"Storage size: {result['storage_size']}")
                print(f"Protocol type: {result['protocol_type']}")
            else:
                print(
                    f"Read Version failed. Error: {result['error']}")

    class ReadSignatureCommand(BaseCommand):
        def __init__(self, mf_ultralight: MfUltralight):
            super().__init__(name='read_signature')
            self.mf_ultralight = mf_ultralight

        def execute(self, args) -> None:
            result = self.mf_ultralight.read_signature()
            if result['error'] == 0:
                print(f"Signature {result['data']}")
            else:
                print(
                    f"Read signature failed. Error: {result['error']}")

    class ReadCounterCommand(BaseCommand):
        def __init__(self, mf_ultralight: MfUltralight):
            super().__init__(name='read_counter')
            self.add_argument('-c', '--counter', type=int, required=True)
            self.mf_ultralight = mf_ultralight

        def execute(self, args) -> None:
            print(f"Reading {args.counter} counter")
            result = self.mf_ultralight.read_counter(args.counter)
            if result['error'] == 0:
                print(f"Counter value {result['data']}")
            else:
                print(
                    f"Read {args.counter} counter failed. Error: {result['error']}")

    class ReadTeringFlagCommand(BaseCommand):
        def __init__(self, mf_ultralight: MfUltralight):
            super().__init__(name='read_tearing_flag')
            self.add_argument('-f', '--flag', type=int, required=True)
            self.mf_ultralight = mf_ultralight

        def execute(self, args) -> None:
            print(f"Reading {args.flag} tearing flag")
            result = self.mf_ultralight.read_tearing_flag(args.flag)
            if result['error'] == 0:
                print(f"Tering flag value {result['data']}")
            else:
                print(
                    f"Read {args.flag} tearing flag failed. Error: {result['error']}")

    def __init__(self, transport: NfcRpcTransport):
        super().__init__(name='mf_ultralight')
        self.mf_ultralight = MfUltralight(transport)
        self.add_child(self.ReadPageCommand(self.mf_ultralight))
        self.add_child(self.WritePageCommand(self.mf_ultralight))
        self.add_child(self.ReadVersionCommand(self.mf_ultralight))
        self.add_child(self.ReadSignatureCommand(self.mf_ultralight))
        self.add_child(self.ReadCounterCommand(self.mf_ultralight))
        self.add_child(self.ReadTeringFlagCommand(self.mf_ultralight))
