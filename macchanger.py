import subprocess
import argparse


def arguments():
	parser=argparse.ArgumentParser()
	parser.add_argument('-i','--interface',metavar='',help='provide interface name for following operation')
	parser.add_argument('-m','--mac',metavar='',help='provide new mac address for following operation')
	arg=parser.parse_args()
	
	if not arg.interface :
		parser.error("ERROR!!!!enter interface:: use --help for more info\n")
		
		
	elif not arg.mac:
		parser.error("ERROR!!!!enter interface:: use --help for more info\n")
		
		
	
		

	print("[+] changing mac address to ",arg.mac)
	return arg



def exec(interface,mac):
	subprocess.run(["ifconfig",interface,"down"])
	subprocess.run(["ifconfig",interface,"hw","ether",mac])
	subprocess.run(["ifconfig",interface,"up"])
	print("[+]MAC ADDRESS changed successfully(^_^)!!!")

args=arguments()
exec(args.interface, args.mac)


