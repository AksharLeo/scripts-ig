sudo chmod 777 /media
sudo chmod 777 /home

sudo apt install apt-transport-https curl gnupg

curl -s https://brave-browser-apt-release.s3.brave.com/brave-core.asc | sudo apt-key --keyring /etc/apt/trusted.gpg.d/brave-browser-release.gpg add -

echo "deb [arch=amd64] https://brave-browser-apt-release.s3.brave.com/ stable main" | sudo tee /etc/apt/sources.list.d/brave-browser-release.list

curl -sS https://download.spotify.com/debian/pubkey_0D811D58.gpg | sudo apt-key add - 
echo "deb http://repository.spotify.com stable non-free" | sudo tee /etc/apt/sources.list.d/spotify.list

sudo apt update

sudo apt install fish piper shotwell flameshot alacritty gnome-tweaks gnome-shell-extensions discord gparted mpv -y
sudo apt install brave-browser -y
sudo apt-get update && sudo apt-get install spotify-client -y
sudo apt-get install gtk2-engines-murrine gtk2-engines-pixbuf git
git clone https://github.com/vinceliuice/McMojave-cursors.git
git clone https://github.com/vinceliuice/Qogir-theme.git
git clone https://github.com/vinceliuice/Tela-circle-icon-theme.git
