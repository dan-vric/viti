from subprocess import call
import argparse
import socket

parser = argparse.ArgumentParser(formatter_class=argparse.ArgumentDefaultsHelpFormatter)
parser.add_argument(--n, type=str, required=True, help='provide a single integer to make this device unique')

args = parser.parse_args()

N = args.n
IP = "192.168.81.24" + str(N)

socket.sethostname('viti'+str(N))

call(["ifconfig", "wlan0", IP, "netmask", "255.255.254.0", "broadcast", "192.168.81.255"])