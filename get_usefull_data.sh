#!/bin/bash
#===============================================================================
#
#          FILE:  get_usefull_data.sh
# 
#         USAGE:  ./get_usefull_data.sh 
# 
#   DESCRIPTION:  limiar las salidas de sumo para graaficar
# 
#       OPTIONS:  ---
#  REQUIREMENTS:  ---
#          BUGS:  ---
#         NOTES:  ---
#        AUTHOR:  Mariano Forti (MF), mfotri@cnea.gov.ar
#       COMPANY:  Comisión Nacional de Energía Atómica
#       VERSION:  1.0
#       CREATED:  29/05/20 08:25:31 -03
#      REVISION:  ---
#===============================================================================
# 60.12  m_h: -0.588  band 23 (up)  [0.50, 0.50, 0.50] (A)  [0.00, 0.50, 0.50] (R)
echo "Vol#mass#value#bandno#spin#from#fname#to#toname"
for dir in ZrO2-new-??
do
  sumolog=$dir/BANDSdir/sumo-bandstats.log
  vol=$(tar -xf $dir/BANDSdir/OUT-OSZ-CON.tar.gz OUTCAR -O | grep volume| tail -1 | awk '{print $NF}' )
#   sed -n "/effective masses/,/^$/s/^\(.*\)|.*\([.*].*\).*->.*\([.*].*(.*)\)/$dir,\1,\2,\3/p" $sumolog # | cut -s -d\| -f1,3  \1\2
# 1mass  2val  band  4no  5spin         f                    t
  #m_h: -0.588 | band 23 (up) | [0.50, 0.50, 0.50] (A) -> [0.00, 0.50, 0.50] (R)
  sed -n "/effective masses/,/^$/s/^  \(m_.\): \(.*\) | \(band\) \(.*\) \((.*)\) | \(\[.*\]\)\(.*\) -> \(\[.*\]\) \(.*\)/$vol#\1#\2#\4#\5#\6#\7#\8#\9/p" $sumolog # | cut -s -d\| -f1,3  \1\2
done
