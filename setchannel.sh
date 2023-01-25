#!/bin/bash
sed -n $1'p'< /tmp/wifiaddresslist|cut -d ' ' -f 3
sudo rm -rf /tmp/wifiaddresslist
sudo rm -rf /tmp/wifitemp*
