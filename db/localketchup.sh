#!/bin/bash

cd ~/Documents/babynet/rina-acc/db/
source /opt/anaconda3/etc/profile.d/conda.sh
conda activate dbb
python updatelocal.py
conda deactivate