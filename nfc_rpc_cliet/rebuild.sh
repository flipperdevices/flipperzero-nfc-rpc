#!/bin/bash

rm -rf ./nfc_protobuf_compiled
mkdir ./nfc_protobuf_compiled
protoc -I=./nfc_protobuf --python_out=./nfc_protobuf_compiled ./nfc_protobuf/*.proto
protol --create-package --in-place --python-out ./nfc_protobuf_compiled protoc --proto-path ./nfc_protobuf ./nfc_protobuf/*.proto