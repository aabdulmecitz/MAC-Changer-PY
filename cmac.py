import subprocess

subprocess.call(["ifconfig","eth0", "down"])
subprocess.call(["ifconfig", "eth0", "hw", "ether", "1z:23:45:53:hd:vs"])
subprocess.call(["ifconfig","eth0", "down"])
