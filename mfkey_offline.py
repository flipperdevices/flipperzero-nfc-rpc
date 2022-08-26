#!/usr/bin/env python3

import os
import sys
import pprint
import datetime
import subprocess

from google.protobuf.json_format import MessageToDict
from flipperzero_protobuf.flipper_proto import FlipperProto
from flipperzero_protobuf.cli_helpers import *
from flipperzero_protobuf.flipper_base import FlipperProtoException

flipper_params_file_path = '/ext/nfc/.mfkey32.log'
flipper_user_dict_path = '/ext/nfc/assets/mf_classic_dict_user.nfc'


def mfkey32v2(params):
    mfkey_args = (params[2:])
    args = ["flipper-nfc/mfkey"]
    args.extend(mfkey_args)
    result = subprocess.run(
        args, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, encoding='ascii')

    if result.returncode == 0:
        return result.stdout
    else:
        return None


def main():

    proto = FlipperProto()

    print(f"Read flipper log file from {flipper_params_file_path}")
    try:
        log_file = proto.rpc_read(flipper_params_file_path).decode("utf-8")
    except FlipperProtoException:
        print("No new logs available")
        return

    reader_logs = log_file.splitlines()
    print(f"\nFound {len(reader_logs)} params")

    print(f"\nStarting mfkey32v2 attack")
    keys_found = set()
    for line in reader_logs:
        params = line.split(' ')[1::2]
        print(f"\nProcessing sector {params[0]} key {params[1]}")
        key = mfkey32v2(params)
        if key is not None:
            print(f"Retrived key {key}")
            keys_found.add(key)
        else:
            print("Failed to retrieve key")

    print(f"\nFound {len(keys_found)} unique keys:")
    for key in keys_found:
        print(key)

    print(f"\nLoading user dictionary from {flipper_user_dict_path}")

    try:
        user_dict = proto.rpc_read(flipper_user_dict_path).decode("utf-8")
    except FlipperProtoException:
        print("No user dictionary found")
        user_dict = ''

    user_keys = set(user_dict.splitlines())
    print(f"User dict contains {len(user_keys)} keys:")
    for key in user_keys:
        print(key)

    new_user_keys = user_keys.copy()
    for key in keys_found:
        new_user_keys.add(key)

    keys_added = len(new_user_keys) - len(user_keys)
    if keys_added == 0:
        print("No unique keys found")
    else:
        new_keys = new_user_keys - user_keys
        print(f"\nFound {len(new_keys)} new keys:")
        for key in new_keys:
            print(key)

        print("\nUpdating user dictionary")
        new_user_dict = '\n'.join(key for key in new_user_keys)
        new_user_dict.join('\n')

        try:
            proto.rpc_write(
                flipper_user_dict_path, new_user_dict.encode("utf-8"))
        except FlipperProtoException:
            print("Failed to update user dictionary")
            return

    print("\nDeleting reader log file")

    try:
        proto.rpc_delete(flipper_params_file_path)
    except FlipperProtoException:
        print("Failed to delete reader log file")
        return


if __name__ == '__main__':
    main()
