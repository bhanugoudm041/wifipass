#!/bin/bash
sed -n $1'p'< /tmp/wifiaddresslist|cut -d ' ' -f 2
