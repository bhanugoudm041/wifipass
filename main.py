#!/usr/bin/env python3
import monitor
import nomonitor
import viewnetworks
import handshake
import crackpass
import subprocess
import interface

def main():
	subprocess.run(["clear"])
	print("""
	 __    __ _  __ _   ___
	/ / /\ \ (_)/ _(_) / _ \__ _ ___ ___
	\ \/  \/ / | |_| |/ /_)/ _` / __/ __|
 	 \  /\  /| |  _| / ___/ (_| \__ \__ "\"
  	  \/  \/ |_|_| |_\/    \__,_|___/___/
	        Developed by BhanuGoud
            Use it for educational purpose
     We are not responsible if you misuse this Tool
	""")
	print("We are not responsible if you miss use this tool")
	print("Run this tool with sudo privileges(Ex:sudo wifipass)")
	terms_choosed = str(input("I use it for Educational Purpose (y/Y/yes/YES)"))
	if terms_choosed=="y" or terms_choosed=="Y" or terms_choosed=="yes" or terms_choosed=="YES":
		while True:
			print("Welcome to the Wifi pentesting framework")
			print("1.Enable monitor mode")
			print("2.Disable monitor mode")
			print("3.View Networks")
			print("4.Capture Handshake")
			print("5.Crack Handshak")
			print("6.Want to add/remove mon to your interface(ex:wlan0mon or wlan0)")
			print("7.Exit")
			try:
				option_choosed = int(input("Choose the attack number: "))
				if option_choosed==1 or option_choosed==2 or option_choosed==3 or option_choosed==4 or option_choosed==5 or option_choosed==6 or option_choosed==7:
					if option_choosed==1:
						monitor.monitor()
					elif option_choosed==2:
						nomonitor.nomonitor()
					elif option_choosed==3:
						viewnetworks.viewnetworks()
					elif option_choosed==4:
						handshake.handshake()
					elif option_choosed==5:
						crackpass.crackpass()
					elif option_choosed==6:
						interface.interface()
					else:
						exit()
					continue
				else:
					print("please choose a option b/w 1-7")
					continue
			except ValueError:
				print("please choose a option b/w 1-7")
				continue
	else:
		print("Bye...!If want to use the program please accept terms & conditions") 
if __name__=="__main__":
	main()
