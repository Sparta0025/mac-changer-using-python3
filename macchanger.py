import subprocess
import argparse

parser=argparse.ArgumentParser()
parser.add_argument('-i','--interface',metavar='',help='provide interface name for following operation')
parser.add_argument('-m','--mac',metavar='',help='provide new mac address for following operation')
args=parser.parse_args()
h=args.interface
print("[+] changing mac address to ",args.mac)
subprocess.run(["ifconfig",args.interface,"down"])
subprocess.run(["ifconfig",args.interface,"hw","ether",args.mac])
subprocess.run(["ifconfig",args.interface,"up"])
print("[+]MAC ADDRESS changed successfully(^_^)!!!")

