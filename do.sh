#!/bin/bash

# Define an associative array of old names to new names
declare -A rename_map=(
    ["2602_eval_val_inter_5_naive_0"]="Naive"
    ["2602_eval_val_inter_5_w_cur_lpips_rot_0"]="Lpips"
    ["2602_eval_val_inter_5_w_cur_rot_0"]="Rot"
)

# Recursively find and rename directories
find . -type d | while read -r dir; do
    base=$(basename "$dir")
    parent=$(dirname "$dir")
    if [[ ${rename_map[$base]+_} ]]; then
        new_name="${rename_map[$base]}"
        mv "$dir" "$parent/$new_name"
    fi
done