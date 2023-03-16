#!/usr/bin/env python3

import argparse

def hexstr2list(data):
    data_bytes = bytes.fromhex(data)
    print([x for x in data_bytes])
    return [int(x, 16) for x in data_bytes]

parser = argparse.ArgumentParser(prog='test')
parser.add_argument('-d', '--data', type=hexstr2list, required=True)

args = parser.parse_args()
print(args.data)