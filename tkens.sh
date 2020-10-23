#!/bin/bash
function getens(){
  if [ ! -z $2 ]
  then
    OUTFILE=$2
  else
    OUTFILE=datavol.dat
  fi

  echo "dir Vol Pressure Evsk1 Evsk2 Evsk3 Evsk4 Evsk5" > $OUTFILE

  for dir in $1
  do
    if [ ! -d $dir/TOTENdir ]
    then
      echo "$dir is not a results directory"
      continue
    fi

    if [ ! -z $vol ]
    then
      echo "unset vol="$vol
      unset vol
      unset E
      unset pre
    fi
    vol=$(tar -xf $dir/TOTENdir/OUT-OSZ-CON.tar.gz OUTCAR -O| grep volume | tail -1 | awk '{print $NF}')
    pre=$(tar -xf $dir/TOTENdir/OUT-OSZ-CON.tar.gz OUTCAR -O | grep pressure -i | tail -1 | awk '{print $4 / 10}')
    for i in 1 2 3 4 5
    do
      if [ ! -d $dir/TOTEN_"$i"dir ]
      then 
	echo $dir"/TOTEN_"$i"dir does not exist"
	E=$E"   0 "
      else
	E=$E" "$(tar -xf $dir/TOTEN_"$i"dir/OUT-OSZ-CON.tar.gz OSZICAR -O | tail -1 | awk '{print $5}')
      fi
    done
    echo "$dir $vol $pre $E  " | tee -a  datavol.dat
  done

}

getens  "ZrO2-*"
