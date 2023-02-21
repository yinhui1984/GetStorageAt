#! /usr/bin/env python3

import sys
import binascii
from web3 import Web3, HTTPProvider


def print_title(title):
    print("\033[92m" + title.ljust(12, " ") + "\033[0m", end="")


def print_as_hex(w3, value):
    print_title("AS HEX:")
    print(w3.toHex(value))


def print_as_int(w3, value):
    print_title("AS INT:")
    print(w3.toInt(value))


def print_as_string(w3, value):
    print_title("AS STRING:")
    try:
        print(w3.toText(value))
    except UnicodeDecodeError:
        print("Not a string")


def print_as_bytes(w3, value):
    print_title("AS BYTES:")
    print(w3.toBytes(value))


def print_as_address(w3, value):
    print_title("AS ADDRESS:")
    txt = "0x" + binascii.hexlify(value[12:32]).decode("ascii")
    if w3.isAddress(txt):
        print(w3.toChecksumAddress(txt))
    else:
        print("Not an address")


# noinspection PyBroadException
def main(_provider, _address, _slot):
    print("Using provider: " + str(_provider))

    try:
        w3 = Web3(_provider)

        value = w3.eth.get_storage_at(_address, _slot)
        print_as_hex(w3, value)
        print_as_int(w3, value)
        print_as_bytes(w3, value)
        print_as_string(w3, value)
        print_as_address(w3, value)
    except:
        print("Error: " + str(sys.exc_info()[0].__name__))
        exit(-1)


if __name__ == '__main__':
    if len(sys.argv) == 4:
        main(HTTPProvider(sys.argv[1]), sys.argv[2], sys.argv[3])
    elif len(sys.argv) == 3:
        main(HTTPProvider("http://localhost:8545"), sys.argv[1], sys.argv[2])
    else:
        print("Usage: getStorageAt.py <rpc_url> <address> <slot>")
        print("Usage: getStorageAt.py <address> <slot>")
        exit(-1)
