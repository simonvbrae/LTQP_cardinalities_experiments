#!/bin/bash

# This file groups the benchmark results into a couple groups with less queries each. This allowed us to use the plot.sh code without having overly busy graphs.

output_folder='.'
output_filename='result-psbrtitle'

fileNameExtensions=("disc1-3" "disc4-6" "disc7-8" "short1-3" "short4-6" "short7")
sedCommandsPerFile=('/name\|interactive-discover-1\|interactive-discover-2\|interactive-discover-3/!d' '/name\|interactive-discover-4\|interactive-discover-5\|interactive-discover-6/!d' '/name\|interactive-discover-7\|interactive-discover-8/!d' '/name\|interactive-short-1\|interactive-short-2\|interactive-short-3/!d' '/name\|interactive-short-4\|interactive-short-5\|interactive-short-6/!d' '/name\|interactive-short-7/!d')
for i in 0 1 2 3 4 5; do
    fileNameExtension=${fileNameExtensions[$i]}
    cp 'result-psbrtitle.csv' "./result-psbrtitle-$fileNameExtension.csv"
    sed -i "2,\$s/;/-/" "$output_folder/$output_filename-$fileNameExtension.csv" # append query index to query name
    sed -i "2,\$s/;/;0;/" "$output_folder/$output_filename-$fileNameExtension.csv" # add index 0
    sed -i "2,\$s/;[0-9]*;true/;60000;true/" "$output_folder/$output_filename-$fileNameExtension.csv" # Set timeouted query time to 60000 
    sed -i ${sedCommandsPerFile[$i]} "$output_folder/$output_filename-$fileNameExtension.csv"
done
