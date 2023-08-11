#!/bin/sh
# This script was used to run benchmarks using the solidbench library.

sparql_benchmark_runner=/home/simon/Documents/Unief/Thesis/sparql-benchmark-runner.js/bin/sparql-benchmark-runner
output_folder="/home/simon/Documents/Unief/Thesis/1-benchmarking/grapher.py" # No trailing slash

query_dir_all=/home/simon/Documents/Unief/Thesis/SolidBenchData/my-queries/all-queries/
query_dir_temp=/home/simon/Documents/Unief/Thesis/SolidBenchData/my-queries/temp/
query_dir_divided=/home/simon/Documents/Unief/Thesis/SolidBenchData/my-queries/divided-queries/
query_dir_few=/home/simon/Documents/Unief/Thesis/SolidBenchData/my-queries/few-queries/

### Important
query_dir=$query_dir_temp
replication=3
timeout=60

###
### Testing all configurations
###
for i in 1
do
    echo "BENCHMARKING TIMEOUT $i"
    output_filename="$i-timeout.csv"
    # Editing comunica configuration
    cd /home/simon/Documents/Unief/Thesis/comunica-feature-link-traversal
    sed -i "s/timeout\": .*$/timeout\": $i,/" /home/simon/Documents/Unief/Thesis/comunica-feature-link-traversal/engines/config-query-sparql-link-traversal/config/rdf-join/actors-inner.json && yarn install --ignore-engines

    ###
    ### Starting server and endpoint
    ###
    echo "STARTING SERVER"
    cd /home/simon/Documents/Unief/Thesis/SolidBenchData
    solidbench serve &
    pid_server=$!
    sleep 10
    echo "STARTED SERVER - PID: $pid_server"

    echo "STARTING ENDPOINT"
    cd /home/simon/Documents/Unief/Thesis/comunica-feature-link-traversal
    node --max_old_space_size=8192 engines/query-sparql-link-traversal-solid/bin/http.js --idp void -p 3001 -c context.json -w 8 --lenient -i --timeout $timeout &
    pid_endpoint=$!
    sleep 10
    echo "STARTED ENDPOINT - PID: $pid_endpoint"

    ###
    ### Running and copying
    ###
    echo "RUNNING BENCHMARK"
    node $sparql_benchmark_runner -t -e http://localhost:3001/sparql -q $query_dir --output output.csv --replication $replication --warmup 0

    echo "COPYING OUTPUT TO $output_folder/$output_filename"
    cp output.csv "$output_folder/$output_filename"
    mv output.txt "$output_folder/$output_filename-output.txt"

    sed "s/;[^;]*;true/;${timeout}000;true/" "$output_folder/$output_filename" > "$output_folder/result-psbrtitle.csv"
    sed -i "s/;0;false/;1;false/" "$output_folder/result-psbrtitle.csv" # Change execution time from 0 to 1 to facilitate the plotting code

    ###
    ### Killing server and endpoint
    ###
    echo "KILLING SERVER - PID: $pid_server"
    kill -9 $pid_server
    echo "KILLING ENDPOINT - PID: $pid_endpoint"
    kill -9 $pid_endpoint
done
