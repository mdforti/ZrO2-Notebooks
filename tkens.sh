#!/bin/bash
echo "dir Vol Evsk1 Evsk2 Evsk3 Evsk4 Evsk5" > datavol.dat
for dir in ZrO2-new-*
do
  if [ ! -z $vol ]
  then
    echo "unset vol="$vol
    unset vol
    unset E
  fi
  vol=$(tar -xf $dir/TOTEN_3dir/OUT-OSZ-CON.tar.gz OUTCAR -O| grep volume | tail -1 | awk '{print $NF}')
  for i in 1 2 3 4 5
  do
     E=$E" "$(tar -xf $dir/TOTEN_"$i"dir/OUT-OSZ-CON.tar.gz OSZICAR -O | tail -1 | awk '{print $5}')
  done
  echo "$dir $vol$E" | tee -a  datavol.dat
done
