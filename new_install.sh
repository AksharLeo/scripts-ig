#!/bin/bash
if (( $EUID != 0 )); then
    sudo $HOME/new_install.sh
    exit
fi

sudo apt install apt-transport-https curl gnupg -y
curl -s https://brave-browser-apt-release.s3.brave.com/brave-core.asc | sudo apt-key --keyring /etc/apt/trusted.gpg.d/brave-browser-release.gpg add -
echo "deb [arch=amd64] https://brave-browser-apt-release.s3.brave.com/ stable main" | sudo tee /etc/apt/sources.list.d/brave-browser-release.list
curl -sS https://download.spotify.com/debian/pubkey_0D811D58.gpg | sudo apt-key add - 
echo "deb http://repository.spotify.com stable non-free" | sudo tee /etc/apt/sources.list.d/spotify.list
sudo add-apt-repository ppa:lutris-team/lutris
sudo apt update
sudo apt install fish brave-browser piper shotwell flameshot alacritty gnome-tweaks gnome-shell-extensions discord gparted mpv \
libcurl4-openssl-dev pkg-config libevent-dev spotify-client gtk2-engines-murrine gtk2-engines-pixbuf lutris qbittorrent uget -y

git clone https://github.com/vinceliuice/McMojave-cursors.git
git clone https://github.com/vinceliuice/Qogir-theme.git
git clone https://github.com/vinceliuice/Tela-circle-icon-theme.git

McMojave-cursors/./install.sh
Qogir-theme/./install.sh
Tela-circle-icon-theme/./install.sh

curl -L https://get.oh-my.fish | fish
omf install sashimi
