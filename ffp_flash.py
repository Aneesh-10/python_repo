#Version 2

import os
import time
import sys
import ipaddress



def dev_stat():
	init_count = 0
	while True:		
		cmd = os.popen(f'ping -c 2 {ip}').read()
		data = str(os.path.split(cmd))
		if "64 bytes" in data:
			print(f"Device status is True")
			time.sleep(5)
			return 1
		else:
			init_count = init_count + 1
			print("Waiting for target...")
			if init_count == 3:
				print("Target is not responding. Hence exiting.")
				exit()

key = "/home/devuser/Desktop/auth_key/id_ed25519_mgu22"
file_path ="/home/devuser/Desktop/script/ffp/"
ip = str("160.48.199.99")

count = int(sys.argv[1])
i = 0

print("###############################################################")
print("#                        FFP FLASHING                         #")
print("###############################################################")

os.system("rm -rf log/")
os.system("mkdir log")
os.system("cd log")

#while i <= count:
for i in range(1, count+1):
	flag = 0
	index = 0
	target = dev_stat()	
	if target == 1:
		os.system(f"ssh -i {key} root@{ip} mkdir /tmp/test")
		os.system(f"scp -i {key} {file_path}bmw_mgu* root@{ip}:/tmp/test/ > log.txt")
		print("Files pushed")
		time.sleep(5)
		os.system(f"ssh -i {key} root@{ip} ffptool /usr/lib/libffp_ioc.so.0 flash /tmp/test/*.tar /tmp/test/*.sig >> log.txt")
		time.sleep(1)
		os.system(f"ssh -i {key} root@{ip} ls -l /tmp/test/")
		print("Target Rebooting...")
		os.system(f"ssh -i {key} root@{ip} nsm_control --r 0 >> log.txt")
		time.sleep(5)
		file1 = open("log.txt", "r")  		
  		# Loop through the file line by line
		for line in file1:  
			index += 1 
      			# checking string is present in line or not
			if "Flash update successful" in line:
        			flag = 1
		if flag == 1:
			print("###############################################################")
			print(f"#                     Flash {i} successful                      #")
			print("###############################################################")
			os.system(f"mv log.txt log/log_{i}.txt")
			i = i+1
			time.sleep(3)
		else:
        		print("###############################################################")
        		print(f"#                    Flash {i} unsuccessful                     #")
        		print("###############################################################")
        		os.system(f"mv log.txt log_error_{i}.txt")
        		i = i+1
        		time.sleep(3)
        	
			
		#os.system(f"ssh root@{ip} ls -l /tmp/test/")
		#time.sleep()
		#os.system(f"ssh root@{ip} ls -l /tmp")
		time.sleep(3)
		os.system(f"ssh -i {key} root@{ip} ls -l /tmp/test/")
			
	else:
		print("Target is not ready")
		sleep(2)

print("###############################################################")
print("#                          FFP DONE                           #")
print("###############################################################")



"""
def validation(val):
	try:		
		IP = ipaddress.ip_address(val)
		ip = str(IP)
		#func()
		return 1
	except ValueError:
		print('address/netmask is invalid: %s' % sys.argv[1])
	except:
		print('Usage : python3 %s variant ipaddress' % sys.argv[0])

def idc():
	i = 1
	if sys.argv[3] == "-n":
		count = int(sys.argv[4])
		while i <= count:
			os.system(f"ssh root@{ip} mkdir /tmp/test")
			os.system("scp bmw_idc* root@{ip}:/tmp/test/")
			print("pushed")
			time.sleep(5)
			os.system(f"ssh root@{ip} ffptool /usr/lib/libffp_ioc.so.0 flash /tmp/test/*.tar /tmp/test/*.sig > log.txt")
			time.sleep(5)
			os.system(f"ssh root@{ip} ls -l /tmp")
			print("reboot")
			os.system(f"ssh root@{ip} nsm_control --r 2")
			time.sleep(5)
			os.system(f"ssh root@{ip} ls -l /tmp")
			time.sleep(5)
			os.system(f"ssh root@{ip} ls -l /tmp")
			time.sleep(5)
			os.system(f"ssh root@{ip} ls -l /tmp")
			time.sleep(5)
			os.system(f"ssh root@{ip} ls -l /tmp")
			print(f"Flashed {i} times")
			i = i+1
	
def mgu():
	print("1")
def rse():	
	print("2")
	
	
if __name__=="__main__":
	ip = sys.argv[2]
	val = validation(ip)	
	if val == 1:
		var = sys.argv[1]
		if var == "-i":
			idc()
		elif var == "-m":
			mgu()
		elif var == "-r":
			rse()
		else:
			print("Invalid variant")
			
"""

	



"""
#Version 1

import os
import time
import sys
import ipaddress


def dev_stat():
	while True:		
		cmd = os.popen(f'ping -c 2 {ip}').read()
		data = str(os.path.split(cmd))
		if "64 bytes" in data:
			print(f"Device status is True")
			return 1
		else:
			print("Waiting for target...")

ip = str("160.48.199.99")

count = int(sys.argv[1])
i = 0
print("###############################################################")
print("#                        FFP FLASHING                         #")
print("###############################################################")

os.system("rm -rf log/")
os.system("mkdir log")
os.system("cd log")

#while i <= count:
for i in range(1, count+1):
	flag = 0
	index = 0
	target = dev_stat()	
	if target == 1:
		os.system(f"ssh root@{ip} mkdir /tmp/test")
		os.system(f"scp bmw_mgu* root@{ip}:/tmp/test/ > log.txt")
		print("Files pushed")
		time.sleep(5)
		os.system(f"ssh root@{ip} ffptool /usr/lib/libffp_ioc.so.0 flash /tmp/test/*.tar /tmp/test/*.sig >> log.txt")
		time.sleep(5)
		os.system(f"ssh root@{ip} ls -l /tmp/test/")
		print("Target Rebooting...")
		os.system(f"ssh root@{ip} nsm_control --r 0 >> log.txt")
		time.sleep(10)
		file1 = open("log.txt", "r")  		
  		# Loop through the file line by line
		for line in file1:  
			index += 1 
      			# checking string is present in line or not
			if "Flash update successful" in line:
        			flag = 1
		if flag == 1:
			print("###############################################################")
			print(f"#                     Flash {i} successful                      #")
			print("###############################################################")
			os.system(f"mv log.txt log/log_{i}.txt")
			i = i+1
			time.sleep(6)
		else:
        		print("###############################################################")
        		print(f"#                    Flash {i} unsuccessful                     #")
        		print("###############################################################")
        		os.system(f"mv log.txt log_error_{i}.txt")
        		i = i+1
        		time.sleep(6)
        	
			
		#os.system(f"ssh root@{ip} ls -l /tmp/test/")
		#time.sleep()
		#os.system(f"ssh root@{ip} ls -l /tmp")
		time.sleep(12)
		os.system(f"ssh root@{ip} ls -l /tmp/test/")
			
	else:
		print("Target is not ready")
		sleep(6)

print("###############################################################")
print("#                          FFP DONE                           #")
print("###############################################################")


"""
"""
def validation(val):
	try:		
		IP = ipaddress.ip_address(val)
		ip = str(IP)
		#func()
		return 1
	except ValueError:
		print('address/netmask is invalid: %s' % sys.argv[1])
	except:
		print('Usage : python3 %s variant ipaddress' % sys.argv[0])

def idc():
	i = 1
	if sys.argv[3] == "-n":
		count = int(sys.argv[4])
		while i <= count:
			os.system(f"ssh root@{ip} mkdir /tmp/test")
			os.system("scp bmw_idc* root@{ip}:/tmp/test/")
			print("pushed")
			time.sleep(5)
			os.system(f"ssh root@{ip} ffptool /usr/lib/libffp_ioc.so.0 flash /tmp/test/*.tar /tmp/test/*.sig > log.txt")
			time.sleep(5)
			os.system(f"ssh root@{ip} ls -l /tmp")
			print("reboot")
			os.system(f"ssh root@{ip} nsm_control --r 2")
			time.sleep(5)
			os.system(f"ssh root@{ip} ls -l /tmp")
			time.sleep(5)
			os.system(f"ssh root@{ip} ls -l /tmp")
			time.sleep(5)
			os.system(f"ssh root@{ip} ls -l /tmp")
			time.sleep(5)
			os.system(f"ssh root@{ip} ls -l /tmp")
			print(f"Flashed {i} times")
			i = i+1
	
def mgu():
	print("1")
def rse():	
	print("2")
	
	
if __name__=="__main__":
	ip = sys.argv[2]
	val = validation(ip)	
	if val == 1:
		var = sys.argv[1]
		if var == "-i":
			idc()
		elif var == "-m":
			mgu()
		elif var == "-r":
			rse()
		else:
			print("Invalid variant")
			
"""

	

