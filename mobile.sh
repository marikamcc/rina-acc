#!/bin/bash

cd ~/Documents/babynet/rina-acc/
source /opt/anaconda3/etc/profile.d/conda.sh
conda activate proj
echo $1 | python pouchpb.py
conda deactivate