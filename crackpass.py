#!/usr/bin/env python3

import subprocess
import main

def crackpass():
	while True:
		subprocess.run(["clear"])
		print("1.Crackhash")
		print("2.Exit")
		print("(3 or 0)"+"."+"Mainmenu")
		try:
			option_choosed=int(input("Choose the Attack: "))
			if option_choosed==1:
				hashfile=input("Enter the full path to cap file with Extension(start from / ): ")
				wordlist=input("Entet the full path to wordlist file(start from / ) : ")
				def run_commnd(hashfile,wordlist):
					subprocess.run(["xterm","-e","sudo aircrack-ng -w "+wordlist+" "+hashfile+" ;sleep 20s"])
					subprocess.run(["clear"])
				run_commnd(hashfile,wordlist)
			elif option_choosed==2:
				subprocess.run(["clear"])
				exit()
			else:
				subprocess.run(["clear"])
				main.main()
		except ValueError:
			print("Please Enter a Number from above list")
if __name__=="__main__":
	crackpass()


