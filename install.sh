#!/bin/bash

printf "\n [+] Updating System... \n\n"
sudo apt-get update

printf "\n [+] Installing python3...\n\n"
sudo apt-get install -y python3 python3-pip

printf "\n [+] Installing python3 requeriments... \n\n"
pip3 install -r requeriments.txt

printf "\n [+] Installing aircrack-ng, This may take a while... \n\n"
#wget https://download.aircrack-ng.org/aircrack-ng-1.6.tar.gz
#gunzip -d aircrack-ng-1.6.tar.gz
#tar -xvf aircrack-ng-1.6.tar
#sudo apt-get install build-essential autoconf automake libtool pkg-config libnl-3-dev libnl-genl-3-dev libssl-dev ethtool shtool rfkill zlib1g-dev libpcap-dev libsqlite3-dev libpcre3-dev libhwloc-dev libcmocka-dev hostapd wpasupplicant tcpdump screen iw usbutils
sudo apt-get install -y aircrack-ng

chmod +x Deauthy

printf "\n [+] Settings are DONE ! \n\n"
printf "'sudo bash ./Deauthy' or 'sudo python3 Deauthy' to run the script"
