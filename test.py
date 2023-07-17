#!/usr/bin/env python3

import asyncio
from bleak import BleakClient
from bleak import BleakGATTCharacteristic
from flipperzero_protobuf_py.flipperzero_protobuf.flipperzero_protobuf_compiled import flipper_pb2
from flipperzero_protobuf_py.flipperzero_protobuf.flipperzero_protobuf_compiled import system_pb2
from google.protobuf.internal.encoder import _VarintBytes

tx_char_uuid = "19ed82ae-ed21-4c9d-4145-228e62fe0000"
tx_handler = 0
rx_char_uuid = "19ed82ae-ed21-4c9d-4145-228e61fe0000"
rx_handler = 0
flow_ctrl_uuid = "19ed82ae-ed21-4c9d-4145-228e63fe0000"
flow_ctrl_handler = 0

def callback(sender: BleakGATTCharacteristic, data: bytearray):
    print(f"{sender}: {data}")


def ping(data: bytes) -> bytearray:
    cmd = flipper_pb2.Main()
    cmd.command_id = 0
    cmd.command_status = flipper_pb2.CommandStatus.Value("OK")
    cmd_data = system_pb2.PingRequest()
    cmd_data.data = data
    getattr(cmd, 'system_ping_request').CopyFrom(cmd_data)
    return bytearray(
        _VarintBytes(cmd.ByteSize())
        + cmd.SerializeToString()
    )


async def main():
    async with BleakClient("80:E1:26:AF:C3:F4") as client:
        await client.start_notify(rx_char_uuid, callback)

        # for service in client.services:
        #     print(service.characteristics)
        # Read a characteristic, etc.
        await client.write_gatt_char(tx_char_uuid, ping(bytes([1, 2, 3, 4, 5, 6, 7, 8])))

    # Device will disconnect when block exits.
    ...

# Using asyncio.run() is important to ensure that device disconnects on
# KeyboardInterrupt or other unhandled exception.
if __name__ == '__main__':
    asyncio.run(main())
