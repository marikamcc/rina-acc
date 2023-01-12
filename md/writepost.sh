#!/bin/bash

cd ~/Documents/babynet/rina-acc/md/
source /opt/anaconda3/etc/profile.d/conda.sh
conda activate proj
#python peanutbuttervibes.py
result=`python pbv2.py`
conda deactivate

cd ~/Documents/babynet/rina/
#echo $result
git add posts/$result
git commit -m "GUI post (automated)"
git push