#!/bin/bash
echo "dir Vol Pressure Evsk1 Evsk2 Evsk3 Evsk4 Evsk5" > datavol.dat
for dir in ZrO2-new-*
do
  if [ ! -z $vol ]
  then
    echo "unset vol="$vol
    unset vol
    unset E
    unset pre
  fi
  vol=$(tar -xf $dir/TOTEN_3dir/OUT-OSZ-CON.tar.gz OUTCAR -O| grep volume | tail -1 | awk '{print $NF}')
  pre=$(tar -xf $dir/TOTEN_3dir/OUT-OSZ-CON.tar.gz OUTCAR -O | grep pressure -i | awk '{print $4 / 10}')
  for i in 1 2 3 4 5
  do
     E=$E" "$(tar -xf $dir/TOTEN_"$i"dir/OUT-OSZ-CON.tar.gz OSZICAR -O | tail -1 | awk '{print $5}')
  done
  echo "$dir $vol $pre $E  " | tee -a  datavol.dat
done
