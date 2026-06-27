#!/bin/bash

gpuid=$1

dataroot='/user/Data/TCGA/BLCA/PLIP_features/pt_files'


# Loop through different folds
for k in 0 1 2 3 4; do
	split_dir="/survival/TCGA_BLCA_overall_survival_k=${k}"
	split_names="train"
	bash "./scripts/prototype/clustering.sh" $gpuid $split_dir $split_names "$dataroot}"
done
