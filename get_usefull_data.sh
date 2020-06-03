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
echo "system   mass value | band no spin from to" 
for dir in ZrO2-? ZrO2-??
do
  sumolog=$dir/BANDSdir/sumo-bandstats.log
  sed -n "/effective masses/,/^$/s/^\(.*\)|.*\((.*\).*->.*\((.*)\)/$dir \1\2\3/p" $sumolog # | cut -s -d\| -f1,3  \1\2
done
