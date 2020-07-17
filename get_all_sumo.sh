#!/bin/bash
#===============================================================================
#
#          FILE:  get_all_sumo.sh
# 
#         USAGE:  ./get_all_sumo.sh 
# 
#   DESCRIPTION:  Read Bandstructure info with sumo-bandstat
# 
#       OPTIONS:  ---
#  REQUIREMENTS:  ---
#          BUGS:  ---
#         NOTES:  ---
#        AUTHOR:  Mariano Forti (MF), mfotri@cnea.gov.ar
#       COMPANY:  Comisión Nacional de Energía Atómica
#       VERSION:  1.0
#       CREATED:  28/05/20 16:51:32 -03
#      REVISION:  ---
#===============================================================================
WD=$(pwd)
LOG=$WD/alldata-all.txt
echo "28/05/2020 ==================== " > $LOG
#for i in 00 01 02 03 04 05 06 07 09 10
for i in 11 12 
do
  dir=ZrO2-new-$i
  echo "" >> $LOG
  echo $dir
  banddir=$dir/BANDSdir
  echo $banddir  >> $LOG
  cd $banddir
    7za x vasprun.7z -y
    tar -xf inputs.tar.gz KPOINTS
    sed -i 's/gamma/\Gamma/g' KPOINTS
    tar -xf OUT-OSZ-CON.tar.gz OUTCAR -O | grep "volume of cell" >> $LOG
    vol=$(tar -xf OUT-OSZ-CON.tar.gz OUTCAR -O | grep "volume" | tail -1 | awk '{print $NF}')
    sumo-bandstats -f vasprun.xml
    sumo-bandplot -f vasprun.xml --prefix $dir --project Zr.d,O.p
    sumo-bandplot -f vasprun.xml --prefix 'hole-detail' --project Zr.d,O.p --ymin -1 --ymax 0.5 --band-edges
    rm KPOINTS vasprun.xml
  cd $WD  
  cat $banddir/sumo-bandstats.log >> $LOG
done
