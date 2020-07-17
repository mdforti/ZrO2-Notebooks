#!/bin/bash
#===============================================================================
#
#          FILE:  get_remote_data.sh
# 
#         USAGE:  ./get_remote_data.sh 
# 
#   DESCRIPTION:  GG
# 
#       OPTIONS:  ---
#  REQUIREMENTS:  ---
#          BUGS:  ---
#         NOTES:  ---
#        AUTHOR:  Mariano Forti (MF), mfotri@cnea.gov.ar
#       COMPANY:  Comisión Nacional de Energía Atómica
#       VERSION:  1.0
#       CREATED:  17/06/20 12:51:06 -03
#      REVISION:  ---
#===============================================================================
current=$(pwd)
for dirs in ZrO2-new-{11,12}
do
  cd $dirs
  remotedir=${dirs/0/}
  echo $remotedir
  rsync -utpr --progress neurus:/home/mforti/stage/Bulk-ZrO2/$remotedir/BANDSdir .
  cd $current
done
