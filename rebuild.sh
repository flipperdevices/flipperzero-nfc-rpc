#!/bin/bash

# Set NFC RPC app folder
NFC_RPC_APP_FOLDER="/home/nikita/localgit/flipperzero-firmware/applications/main/nfc_rpc"

rm -rf nfc_rpc_client/nfc_protobuf_compiled
mkdir nfc_rpc_client/nfc_protobuf_compiled
protoc -I=nfc_rpc_client/nfc_protobuf --python_out=nfc_rpc_client/nfc_protobuf_compiled nfc_rpc_client/nfc_protobuf/*.proto
protol --create-package --in-place --python-out nfc_rpc_client/nfc_protobuf_compiled protoc --proto-path nfc_rpc_client/nfc_protobuf nfc_rpc_client/nfc_protobuf/*.proto

# Copy compiled protobuf files to NFC RPC app folder
rm -rf $NFC_RPC_APP_FOLDER/assets/*
mkdir $NFC_RPC_APP_FOLDER/assets/protobuf
mkdir $NFC_RPC_APP_FOLDER/assets/compiled
cp -r nfc_rpc_client/nfc_protobuf/* $NFC_RPC_APP_FOLDER/assets/protobuf
nanopb/generator/nanopb_generator.py -I ./nfc_rpc_client/nfc_protobuf -D $NFC_RPC_APP_FOLDER/assets/compiled ./nfc_rpc_client/nfc_protobuf/*.proto