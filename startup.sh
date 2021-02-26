#!/bin/bash
if (( $EUID != 0 )); then
    sudo /home/aksharleo/startup.sh
    exit
fi
apt update
apt -y upgrade
apt-get -y dist-upgrade
apt clean
apt -y autoremove
apt purge -y $(dpkg -l | awk '/^rc/ { print $2 }')
sudo -u aksharleo flatpak update -y
sudo systemd-resolve --flush-caches
