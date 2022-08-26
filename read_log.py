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

flipper_log_path = '/ext/nfc/debug.txt'

class colors:
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    ENDC = '\033[0m'


def main():

    proto = FlipperProto()

    print(f"Read flipper log file from {flipper_log_path}")
    try:
        log_file = proto.rpc_read(flipper_log_path).decode("utf-8")
    except FlipperProtoException:
        print("No new logs available")
        return

    lines = log_file.splitlines()
    for i, line in enumerate(lines):
        if line.find('T') == -1:
            print(colors.GREEN + line + colors.ENDC)
        else:
            print(colors.YELLOW + line + colors.ENDC)

    try:
        proto.rpc_delete(flipper_log_path)
    except FlipperProtoException:
        print("Failed to delete logs")


    return


if __name__ == '__main__':
    main()
