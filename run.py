import sys
import os
import decode
import encode


def run():
    if str(sys.argv[1]).endswith(".py"):
        encode.encode(str(sys.argv[1]))
    elif str(sys.argv[1]).endswith(".pycn"):
        decode.decode(str(sys.argv[1]))


if __name__ == '__main__' and len(sys.argv) == 2:
    run()
    os.system("pause")
