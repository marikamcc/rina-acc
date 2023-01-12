#!/bin/bash

cd ~/Documents/babynet/rina-acc/
source /opt/anaconda3/etc/profile.d/conda.sh
conda activate dbb
python add-gooey-post.py
conda deactivate