#!/bin/bash

for i in $(cat /tmp/wifitemp-01.kismet.csv|head -n 12|awk -F ',' '{print $1}'|sed -r 's/\s+//g'|grep -n -v ESSID)
do
name=$(echo $i|awk -F ';' '{print $3}')
mac=$(echo $i|awk -F ';' '{print $4}')
channel=$(echo $i|awk -F ';' '{print $6}')

echo "Name:" $name  "**" "Mac:" $mac "**" "Channel:" $channel >> wifiaddresslist
echo $name $mac $channel >> /tmp/wifiaddresslist
done
cat wifiaddresslist|nl -s '.'
rm -rf wifiaddresslist
