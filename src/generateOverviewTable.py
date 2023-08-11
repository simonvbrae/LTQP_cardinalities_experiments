import os

# This file generates a table with results obtained for each query and configuration, providing an overview of the results.

outputFileName="overviewTable"

queryFolders=[
    "/home/simon/Documents/Unief/Thesis/1-benchmarking/grapher.py/experiment-results/23.6.12/baseline/baseline-zero",
    "/home/simon/Documents/Unief/Thesis/1-benchmarking/grapher.py/experiment-results/23.6.12/baseline/baseline-card",
    "/home/simon/Documents/Unief/Thesis/1-benchmarking/grapher.py/experiment-results/23.6.12/index/index-zero",
    "/home/simon/Documents/Unief/Thesis/1-benchmarking/grapher.py/experiment-results/23.6.12/index/index-card",
    "/home/simon/Documents/Unief/Thesis/1-benchmarking/grapher.py/experiment-results/23.6.12/timeout/timeout-noindex-card",
    "/home/simon/Documents/Unief/Thesis/1-benchmarking/grapher.py/experiment-results/23.6.12/timeout/timeout-index-card",
    ]
queryFileNames=["result-psbrtitle-disc1-3.csv", "result-psbrtitle-disc4-6.csv", "result-psbrtitle-disc7-8.csv", "result-psbrtitle-short1-3.csv", "result-psbrtitle-short4-6.csv", "result-psbrtitle-short7.csv"]

resultsPerQuery={}
for folder in queryFolders:
    for queryFileName in queryFileNames:
        lines = open(folder+'/'+queryFileName, 'r').readlines()
        for line in lines[1:]:
            qTitle = line.split(';')[0]
            qExTime = line.split(';')[3]
            if qTitle in resultsPerQuery:
                resultsPerQuery[qTitle].append(qExTime)
            else:
                resultsPerQuery[qTitle] = [qExTime]

for i in resultsPerQuery:
    print(i, resultsPerQuery[i])

confignames=["b-heuristic", "b-card", "i-heuristic", "i-card", "t.o.", "t.o.+i"]
with open(f"{outputFileName}.tex", 'w') as f:
    f.write("\\documentclass[preview]{standalone} \n")
    f.write("\\usepackage[a4paper]{geometry} \n")
    f.write("\\usepackage{tabularx} \n")
    f.write("\\begin{document} \n")
    f.write("\\begin{table}[!ht] %[H]\n")
    f.write("\\caption{Execution time per query of each configuration} \n")
    f.write("\\centering \n")
    f.write("\\begin{tabular}{lcccccc} \n")

    f.write(f'& {" & ".join(confignames)} \\\\ \\hline \n')
    for queryTitle in resultsPerQuery:
        bestExTime = str(min([int(x) for x in resultsPerQuery[queryTitle]]))
        resultsWithBoldMinimum=[f'\\textbf\u007b{x}\u007d' if x == bestExTime else x for x in resultsPerQuery[queryTitle] ]
        if (not all([x=='60000' for x in resultsPerQuery[queryTitle]])): # Dont write line if each config had timeouts
            f.write(f'{queryTitle} & {" & ".join(resultsWithBoldMinimum)} \\\\ \n ')

    f.write("\\end{tabular} \n")
    f.write("\\end{table} \n")
    f.write("\\end{document} \n")

os.system(f"texliveonfly {outputFileName}.tex")
os.system(f"rm {outputFileName}.aux")
os.system(f"rm {outputFileName}.log")
os.system(f"rm {outputFileName}.synctex.gz")