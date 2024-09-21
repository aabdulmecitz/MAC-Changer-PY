import subprocess
import optparse

parse_obj = optparse.OptionParser()
parse_obj.add_option("-i", "--interface",dest='interface',help='interface for changing')
parse_obj.add_option("-m","--mac", dest='mac',help='mac to change')
(inputs, args) = parse_obj.parse_args()

interface = inputs.interface
mac = inputs.mac

print("function started")

subprocess.call(["ifconfig", interface , "down"])
subprocess.call(["ifconfig", interface , "hw", "ether", mac])
subprocess.call(["ifconfig", interface , "up"])
