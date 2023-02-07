# Flipper Zero CLI RPC client using protobuf

# Usage:
# Connect the Flipper Zero with the corresponding firmware via USB
# Run `python3 flipperzero_nfc_rpc_client.py`
# 
# Rebuilding the protobuf files:
# Run `protoc nfc.proto --python_out=.` in the directory of this script
# Run `protoc --nanopb_out=../compiled/ nfc.proto` in the firmware applications/plugins/nfc_rpc_actor/.

import sys
import time

import nfc_pb2
from flipperzero_protobuf_py.flipperzero_protobuf.flipper_proto import FlipperProto
from flipperzero_protobuf_py.flipperzero_protobuf.cli_helpers import *
from flipperzero_protobuf_py.flipperzero_protobuf.flipper_base import FlipperProtoException

commands = {
  "anticoll": {
    "args": ["type"],
    "help": "[a, b, bprime, f, v] - perform anticollision with specified type",
    "func": "anticoll",
  },
  "help": {
    "args": [],
    "help": "print this help",
    "func": "print_help",
  },
  "exit": {
    "args": [],
    "help": "exit the script",
    "func": "exit",
  },
  "quit": {
    "args": [],
    "help": "exit the script",
    "func": "exit",
  },
}

nfc_types = {
  "a": {
    "type": nfc_pb2.anticollisionType.NFCA,
    "name": "NFC-A",
    "response": nfc_pb2.NfcAAnticollisionResponse,
  },
  "b": {
    "type": nfc_pb2.anticollisionType.NFCB,
    "name": "NFC-B",
    "response": None,
  },
  "bprime": {
    "type": nfc_pb2.anticollisionType.NFCBPrime,
    "name": "NFC-B'",
    "response": None,
  },
  "f": {
    "type": nfc_pb2.anticollisionType.NFCF,
    "name": "NFC-F",
    "response": None,
  },
  "v": {
    "type": nfc_pb2.anticollisionType.NFCV,
    "name": "NFC-V",
    "response": None,
  },
}

def print_help():
  print("Available commands:")
  for cmd in commands:
    if len(commands[cmd]["args"]) > 0:
      print(f"{cmd} {commands[cmd]['args']}: {commands[cmd]['help']}")
    else:
      print(f"{cmd}: {commands[cmd]['help']}")


def bytes_to_hex(bytes, length=0):
  if length == 0:
    length = len(bytes)
  return ':'.join('{:02x}'.format(x) for x in bytes[:length])


def anticoll(proto, type):
  req = nfc_pb2.NfcAnticollisionRequest()
  try:
    req.type = nfc_types[type]["type"]
  except KeyError:
    print(f"Unknown type: {type}")
    return
  proto.rpc_app_data_exchange_send(req.SerializeToString())
  resp = proto.rpc_app_data_exchange_recv()
  # Decode responce from protobuf
  nfc_resp = nfc_types[type]["response"]()
  nfc_resp.ParseFromString(resp)
  # Format raw bytes to hex string
  uid = bytes_to_hex(nfc_resp.uid, nfc_resp.uid_len)
  print(f"UID: {uid}")
  sak = bytes_to_hex(nfc_resp.sak)
  print(f"SAK: {sak}")
  atqa = bytes_to_hex(nfc_resp.atqa)
  print(f"ATQA: {atqa}")


def main():
  proto = FlipperProto()
  proto.rpc_app_start("/ext/apps/Tools/NfcRpcActor.fap", "RPC")
  print_help()
  while True:
    cmd = input("Enter command: ").split(" ")
    if cmd[0] in commands:
      if cmd[0] == "exit" or cmd[0] == "quit":
        proto.rpc_app_exit()
        sys.exit(0)
      args = cmd[1:]
      if len(args) == len(commands[cmd[0]]["args"]):
        func = getattr(sys.modules[__name__], commands[cmd[0]]["func"])
        try:
          func(proto, *args)
        except FlipperProtoException as e:
          print(f"Error: {e}")
      else:
        print(f"Wrong number of arguments for {cmd[0]}")
    else:
      print("Unknown command")


if __name__ == "__main__":
  main()
