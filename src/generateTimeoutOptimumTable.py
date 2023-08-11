import os

# This file generates a Latex table which shows what the best timeout value was for each query.

outputFileName="idealTimeoutsTable"

files=[
    "/home/simon/Documents/Unief/Thesis/1-benchmarking/grapher.py/experiment-results/23.6.12/timeout/timeout-noindex-card/result-psbrtitle-mapping.txt",
    "/home/simon/Documents/Unief/Thesis/1-benchmarking/grapher.py/experiment-results/23.6.12/timeout/timeout-index-card/result-psbrtitle-mapping.txt"
    ]
import ast
linesPerFile=[]
for file in files:
    with open(file) as f:
        lines=f.readlines()
        lines=list(map(lambda x: ("-".join(ast.literal_eval(x[x.index("["):])[0:2]), x[:x.index(" ")]), lines))
        linesPerFile.append(lines)

optimumPerQuery=[(query, opt1, linesPerFile[1][i][1]) for i,(query, opt1) in enumerate(linesPerFile[0])]

confignames=["count", "count+index"]
with open(f"{outputFileName}.tex", 'w') as f:
    f.write("\\documentclass[preview]{standalone} \n")
    f.write("\\usepackage[a4paper]{geometry} \n")
    f.write("\\usepackage{tabularx} \n")
    f.write("\\begin{document} \n")
    f.write("\\begin{table}[!ht] %[H]\n")
    f.write("\\caption{Timout value yielding the lowest execution time per query and configuration} \n")
    f.write("\\centering \n")
    f.write("\\begin{tabular}{lcccccc} \n")

    f.write(f'& {" & ".join(confignames)} \\\\ \\hline \n')
    for (queryTitle, opt1, opt2) in optimumPerQuery:
        f.write(f'{queryTitle.strip("interactive-")} & {opt1} & {opt2} \\\\ \n ')

    f.write("\\end{tabular} \n")
    f.write("\\end{table} \n")
    f.write("\\end{document} \n")

os.system(f"texliveonfly {outputFileName}.tex")
os.system(f"rm {outputFileName}.aux")
os.system(f"rm {outputFileName}.log")
os.system(f"rm {outputFileName}.synctex.gz")