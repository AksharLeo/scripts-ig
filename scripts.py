import os

#command is python3 scripts.py

hm = int(input('''
            1 - new install
            2 - install omf
            3 - do both
            4 - exit
            '''))

new_install = '''
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
            sudo apt-get install libcurl4-openssl-dev
            sudo apt-get install pkg-config
            sudo apt install libevent-dev
            sudo apt-get update && sudo apt-get install spotify-client -y
            sudo apt-get install gtk2-engines-murrine gtk2-engines-pixbuf git

            
            git clone https://github.com/vinceliuice/McMojave-cursors.git
            git clone https://github.com/vinceliuice/Qogir-theme.git
            git clone https://github.com/vinceliuice/Tela-circle-icon-theme.git
            cd McMojave-cursors
            ./install.sh
            cd ../Qogir-theme
            ./install.sh
            cd ../Tela-circle-icon-theme
            ./install.sh'''

install_omf = '''
                curl -L https://get.oh-my.fish | fish
                curl -L https://get.oh-my.fish > install
                fish install --path=~/.local/share/omf --config=~/.config/omf -y
                bb1f4025934600ea6feef2ec11660e17e2b6449c5a23c033860aed712ad328c9 install -y
                omf install sashimi'''
            
if   hm == 1:
    os.system(new_install)
elif hm == 2:
    os.system(install_omf)
elif hm == 3:
    os.system(new_install)
    os.system(install_omf)
elif hm == 4:
    exit
else:
    print('please enter a valid input')
exit
