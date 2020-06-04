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
LOG=$WD/alldata.txt
echo "28/05/2020 ==================== " > $LOG
for dir in ZrO2-new-??
do
  echo "" >> $LOG
  echo $dir
  banddir=$dir/BANDSdir
  echo $banddir  >> $LOG
  cd $banddir
    7za x vasprun.7z -y
    tar -xf inputs.tar.gz KPOINTS
    set -xv
    sed -i 's/gamma/\\Gamma/g' KPOINTS
    unset -xv
    vol=$(tar -xf OUT-OSZ-CON.tar.gz OUTCAR -O | grep "volume" | tail -1 | awk '{print $NF}')
    sumo-bandplot -f vasprun.xml --prefix hole-"$vol" --project Zr.d,O.p --ymin -1 --ymax 0.5 --band-edges
    rm KPOINTS vasprun.xml
  cd $WD  
  cat $banddir/sumo-bandstats.log >> $LOG
done
