from ..nfc_rpc_transport import NfcRpcTransport
from ..nfc_protobuf_compiled import main_pb2

class NfcBaseProto():
    def __init__(self, transport: NfcRpcTransport):
        self.transport = transport
    
    def decode_bytes(self, data, length=0):
        return bytes(' '.join('{:02x}'.format(x) for x in data[:length]).encode('utf-8'))

    def send_cmd(self, cmd_data, cmd_name:str):
        cmd = main_pb2.Main()
        cmd.command_status = main_pb2.CommandStatus.Value("OK")
        getattr(cmd, cmd_name).CopyFrom(cmd_data)
        self.transport.send(cmd.SerializeToString())
    
    def receive_cmd(self, cmd_name: str):
        cmd = main_pb2.Main()
        resp = self.transport.receive()
        try:
            cmd.ParseFromString(resp)
        except:
            print("Error parsing response")
            return
        return getattr(cmd, cmd_name)
