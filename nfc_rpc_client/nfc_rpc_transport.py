from flipperzero_protobuf_py.flipperzero_protobuf.flipper_proto import FlipperProto

class NfcRpcTransport():
    def __init__(self) -> None:
        self.proto = FlipperProto()
        self.proto.rpc_app_start("NfcRpc", "RPC")

    def send(self, data) -> None:
        self.proto.rpc_app_data_exchange_send(data)
    
    def receive(self) -> bytes:
        return self.proto.rpc_app_data_exchange_recv()