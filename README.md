# flipperzero-nfc-rpc
Examples for control NFC over RPC

# Structure
`flipper-fw` submodule points to supported flipper firmware

`flipper-nfc` submodule points to binary tool used in this repo

`flipperzero_protobuf_py` submodule points to python RPC implementation for flipper

# Utilities
`mfkey_offline.py` downloads mfkey logs from flipper, calculate keys, updates User Dictionary, removes logs

`read_log.py` downloads and show logs from flipper, saved with Debug option
