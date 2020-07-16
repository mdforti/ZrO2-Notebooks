echo "dir  vol  Indirect  Direct "
for dir in ZrO2-new-* 
do 
  vol=$(tar -xf $dir/BANDSdir/OUT-OSZ-CON.tar.gz OUTCAR -O | grep "volume" | tail -1 | awk '{print $NF}')
  IGAP=$(grep "Indirect band gap" $dir/BANDSdir/sumo-bandstats.log| cut -d" " -f 4 )
  DGAP=$(grep   "Direct band gap" $dir/BANDSdir/sumo-bandstats.log| cut -d" " -f 4)
  echo "$dir $vol $IGAP  $DGAP"
done

