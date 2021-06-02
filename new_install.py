import os


os.system('''
			pip install apt-smart -y
			apt-smart -a
			sudo apt update
			sudo apt install apt-transport-https curl gnupg -y
			curl -s https://brave-browser-apt-release.s3.brave.com/brave-core.asc | sudo apt-key --keyring /etc/apt/trusted.gpg.d/brave-browser-release.gpg add -
			echo "deb [arch=amd64] https://brave-browser-apt-release.s3.brave.com/ stable main" | sudo tee /etc/apt/sources.list.d/brave-browser-release.list
			curl -sS https://download.spotify.com/debian/pubkey_0D811D58.gpg | sudo apt-key add -
			echo "deb http://repository.spotify.com stable non-free" | sudo tee /etc/apt/sources.list.d/spotify.list
			sudo apt update
			sudo apt install fish brave-browser piper shotwell flameshot alacritty gnome-tweaks gnome-shell-extensions discord gparted mpv \
			libcurl4-openssl-dev pkg-config libevent-dev spotify-client gtk2-engines-murrine gtk2-engines-pixbuf qbittorrent adb fastboot -y
			curl https://raw.githubusercontent.com/AksharLeo/scripts-ig/main/alacritty.yml | cat >> alacritty.yml && mv alacritty.yml .config/alacritty/alacritty.yml
			curl https://raw.githubusercontent.com/AksharLeo/scripts-ig/main/startup.sh | cat >> startup.sh && chmod +x startup.sh
		''')

os.system('''
			git clone https://github.com/vinceliuice/McMojave-cursors.git
			git clone https://github.com/vinceliuice/Qogir-theme.git
			git clone https://github.com/vinceliuice/Tela-circle-icon-theme.git
		''')

os.chdir('McMojave-cursors')
os.system('./install.sh')

os.chdir('../Qogir-theme')
os.system('./install.sh')

os.chdir('../Tela-circle-icon-theme')
os.system('./install.sh')

os.chdir('../')

os.system('curl -L https://get.oh-my.fish | fish && omf install sashimi')