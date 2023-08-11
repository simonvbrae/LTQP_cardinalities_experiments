# Code with all scripts used within my thesis to
- Run experiments
- Clean & structure data
- Plot results
- Generate tables with results used in my thesis
- Calculate comprehensive results used in my thesis

Code in this repository doesn't form one cohesive workflow as most files were created on the fly when something was needed. As such, it would certainly benefit from refactoring and cleanup. Beware of the fact that folders are hardcoded and, as a result, this code doesn't seamlessly transition to another machine.

# Files included in this thesis
- bench.sh -> To run a benchmark using this file: 
1) Correctly set input and output folders in the script, change comunica path
2) Change any parameters
3) Switch to the configuration branch in comunica
4) Call the script from the comunica repo

- splotQueryResultFiles.bash -> Splits the query results from bench.sh into files with less queries.
- plot.sh -> Uses the [process_sparql_benchmark_results]() project to plot result data. 
- generateDiefficiencyData.bash -> Formats the data for creating diefficiency graphs with psbr.

- extractBestExecutionTimePerTimeout.py -> Functions that different manipulations and calculations on the timeout data. Also contains a function that selects the best execution time and writes its full result and the corresponding execution time to a file.
- generateImprovementPercentageTable.py -> Aggregates results obtained from the benchmarks, it uses a version of the overview table as its input.
- generateOverviewTable -> Generates a table with results obtained for each query and configuration, providing an overview of the results.
- generateTimeoutOptimumTable -> Generates a Latex table which shows what the best timeout value was for each query.
- grapher.py -> Generates different plots used throughout the work.
- processOverviewTable.py -> Contains functions that calculate useful metrics, it was made on the fly as metrics were needed during the process of writing.
