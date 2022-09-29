#!/usr/bin/env python3


import subprocess
import psutil
import main

def nomonitor():
	while True:
		subprocess.run(["clear"])
		intErface=list(psutil.net_if_stats().keys())
		lenList=len(intErface)
		for serialNum in range(1,(lenList+1)):
			print(str(serialNum)+"."+intErface[serialNum-1])
		print(str(lenList+1)+"."+"Exit")
		print("("+str(lenList+2)+" or 0)"+"."+"Mainmenu")
		try:
			inTerFacE=int(input("Choose the interface you want to disable monitormode: "))
			if inTerFacE <= lenList and inTerFacE != 0:
				inTERFACE=intErface[inTerFacE-1]
				def run_commnd(inTERFACE):
					subprocess.run(["xterm","-e","sudo ip link set "+ inTERFACE +" down;sleep 2s;sudo iw "+ inTERFACE +" set type managed;sudo ip link set "+ inTERFACE +" up;sudo service NetworkManager restart"])
					subprocess.run(["clear"])
				run_commnd(inTERFACE)
			elif inTerFacE == lenList+1 and inTerFacE != 0:
				subprocess.run(["clear"])
				exit()
			else:
				subprocess.run(["clear"])
				main.main()
		except ValueError:
			print("Please Enter a Number from above list")
if __name__=="__main__":
	nomonitor()
