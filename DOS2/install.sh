#!/bin/sh

banner() 
{
	printf "\n"
	printf "\e[1;77m           ██████╗    ██████╗   ███████╗    \e[0m\n"
	printf "\e[1;77m           ██╔══██╗  ██╔═══██╗  ██╔════╝    \e[0m\n"
	printf "\e[1;77m           ██║  ██║  ██║   ██║  ███████╗    \e[0m\n"
	printf "\e[1;77m           ██║  ██║  ██║   ██║  ╚════██║    \e[0m\n"
	printf "\e[1;77m           ██████╔╝  ╚██████╔╝  ███████║    \e[0m\n"
	printf "\e[1;77m           ╚═════╝    ╚═════╝   ╚══════╝    v1.0\e[0m\n"
	printf "\n"
	printf "\e[1;93m  .:.:.\e[0m\e[1;77m Denial of service attack tool \e[0m\e[1;93m.:.:.\e[0m\n\n\n"
}

install()
{
	printf "\e${blanc}[${orange}*${blanc}] ${orange}Check updates [1/4] ${blanc}\n\n"
	sudo apt update

	printf "\n\n\e${blanc}[${orange}*${blanc}] ${orange}Installing hping3 [2/4] ${gris}\n\n"
	sudo apt-get install hping3

	printf "\n\n\e${blanc}[${orange}*${blanc}] ${orange}Check python version [3/4] ${blanc}\n\n"
	python3 --version || sudo apt-get install python3

	printf "\n\n\e${blanc}[${orange}*${blanc}] ${orange}Finalization [4/4] ${blanc}\n\n"
	sudo apt-get install python3-gi
	#pwd=$PWD
	#cd /usr/local/bin/
	#sudo mkdir DOS 
	#sudo cp $pwd/dos.sh /usr/local/bin/DOS
	#sudo cp $pwd/var /usr/local/bin/DOS
	#sudo echo "1">/usr/local/bin/DOS/var
}


step1()
{
	printf "\e\n\n${blanc}[${orange}*${blanc}] You can now use dos.py by executing '${orange}sudo ./dos.py ${blanc}' \n\n\n"
}

blanc='\e[1;37m'
gris='\e[0;37m'
orange='\e[0;33m'

banner
install
step1
exit

