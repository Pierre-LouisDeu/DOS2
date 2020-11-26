#!/bin/sh

blanc='\e[1;37m'
orange='\e[0;33m'


stopX()
{
  nb=$nb
  pid=$(cat pid.txt) 
  inc=0
  printf "${orange}Stoping hping3 \n"
  let "nb=nb+nb"
  while ((inc!=nb))
  do
      let "pid=pid+1"
      sudo kill -9 $pid >/dev/null 2> /dev/null & 
      let "inc=inc+1"
  done
}

nb=$1
stopX $nb