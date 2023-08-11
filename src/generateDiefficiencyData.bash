#!/bin/bash
# This file puts the data in a format interpreted by the diefficiency graph script.
output_folder='.'
input_filename='result-psbrtitle.csv'
output_filename='result-psbrtitle-qtimes.csv'

sed "2,\$s/;/-/" "$output_folder/$input_filename" > "$output_folder/$output_filename" # append index to name
sed -i "2,\$s/;/;0;/" "$output_folder/$output_filename" # append index to name
