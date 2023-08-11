import os
import processOverviewTable

# This file aggregates results obtained from the benchmarks, it uses a version of the overview table as its input.

queryFiles=["result-psbrtitle-disc1-3.csv", "result-psbrtitle-disc4-6.csv", "result-psbrtitle-disc7-8.csv", "result-psbrtitle-short1-3.csv", "result-psbrtitle-short4-6.csv", "result-psbrtitle-short7.csv"]

# This function calculates percentage of queries with performance increase/decrease of over 10% and average improvement.
def generateImprovementPercentageTable(queryFiles):
    baselineFolder = "/home/simon/Documents/Unief/Thesis/1-benchmarking/grapher.py/experiment-results/23.6.12/baseline/baseline-zero"
    confignames=["index\\_zero", "index\\_card", "count", "count+i"]
    queryFolders=[
        "/home/simon/Documents/Unief/Thesis/1-benchmarking/grapher.py/experiment-results/23.6.12/index/index-zero",
        "/home/simon/Documents/Unief/Thesis/1-benchmarking/grapher.py/experiment-results/23.6.12/index/index-card",
        "/home/simon/Documents/Unief/Thesis/1-benchmarking/grapher.py/experiment-results/23.6.12/timeout/timeout-noindex-card",
        "/home/simon/Documents/Unief/Thesis/1-benchmarking/grapher.py/experiment-results/23.6.12/timeout/timeout-index-card",
        ]

    baselineResultsPerQuery={}
    for queryFileName in queryFiles:
        lines = open(baselineFolder+'/'+queryFileName, 'r').readlines()
        for line in lines[1:]:
            qTitle = line.split(';')[0].strip("interactive-")
            qExTime = int(line.split(';')[3])
            baselineResultsPerQuery[qTitle] = qExTime

    percentagesPerConfig={}
    for i, folder in enumerate(queryFolders):
        configname=confignames[i]
        amountOfQueries=0
        amountOfQueries10PercentBetter=0
        queries10PercentBetter=[]
        amountOfQueries10PercentWorse=0
        queries10PercentWorse=[]
        for queryFileName in queryFiles:
            lines = open(folder+'/'+queryFileName, 'r').readlines()
            amountOfQueries+=len(lines)-1
            for line in lines[1:]:
                qName = line.split(';')[0].strip("interactive-")
                qExTime = int(line.split(';')[3])
                if (qExTime>baselineResultsPerQuery[qName] + (baselineResultsPerQuery[qName])/10):
                    amountOfQueries10PercentWorse += 1
                    queries10PercentWorse.append(line)
                elif (qExTime<baselineResultsPerQuery[qName] - (baselineResultsPerQuery[qName])/10):
                    amountOfQueries10PercentBetter += 1
                    queries10PercentBetter.append(line)
        print("------------------")
        print("------------------")
        print(configname)
        print("------------------")
        print("------------------")
        print("queries10PercentWorse")
        for i in queries10PercentWorse:
            print(i.strip('\n'))
        print("queries10PercentBetter")
        for i in queries10PercentBetter:
            print(i.strip('\n'))
        percentagesPerConfig[configname] = [amountOfQueries10PercentBetter/amountOfQueries, amountOfQueries10PercentWorse/amountOfQueries]

    outputFileName="percentageTable"
    with open(f"{outputFileName}.tex", 'w') as f:
        f.write("\\documentclass[preview]{standalone} \n")
        f.write("\\usepackage[a4paper]{geometry} \n")
        f.write("\\usepackage{tabularx} \n")
        f.write("\\begin{document} \n")
        f.write("\\begin{table}[!ht] \n")
        f.write("\\caption{Percentage of cases in which the approaches achieve response times that are at least 10\% better (resp. 10 worse) than the baseline} \n")
        f.write("\\centering \n")
        f.write("\\begin{tabular}{lcc} \n")

        columnNames = ["better", "worse"]
        f.write(f'& {" & ".join(columnNames)} \\\\ \\hline \n')
        for configname in confignames:
            f.write(f'{configname} & {" & ".join(map(lambda x: "{:.2f}".format(x*100), percentagesPerConfig[configname][0:2]))} \\\\ \n ')

        f.write("\\end{tabular} \n")
        f.write("\\end{table} \n")
        f.write("\\end{document} \n")

    os.system(f"texliveonfly {outputFileName}.tex")
    os.system(f"rm {outputFileName}.aux")
    os.system(f"rm {outputFileName}.log")
    os.system(f"rm {outputFileName}.synctex.gz")

# This version leaves out queries we see as outliers (low ex.time in baseline)
representativeQueries=[f"discover-1-{i}" for i in range(0,5)]
representativeQueries+=[f"discover-2-{i}" for i in range(0,5)]
representativeQueries+=[f"discover-5-{i}" for i in range(0,5)]
representativeQueries+=[f"discover-6-{i}" for i in [1,2,4]]
representativeQueries+=[f"discover-7-{i}" for i in range(0,5)]
def generateImprovementPercentageTableFilter(queryFiles):
    baselineFolder = "/home/simon/Documents/Unief/Thesis/1-benchmarking/grapher.py/experiment-results/23.6.12/baseline/baseline-zero"
    confignames=["index\\_zero", "index\\_card", "count", "count+index"]
    improvementPerConfig=[processOverviewTable.averageImprovement(1, 3)[0], processOverviewTable.averageImprovement(1, 4)[0], processOverviewTable.averageImprovement(1, 5)[0], processOverviewTable.averageImprovement(1, 6)[0]]
    queryFolders=[
        "/home/simon/Documents/Unief/Thesis/1-benchmarking/grapher.py/experiment-results/23.6.12/index/index-zero",
        "/home/simon/Documents/Unief/Thesis/1-benchmarking/grapher.py/experiment-results/23.6.12/index/index-card",
        "/home/simon/Documents/Unief/Thesis/1-benchmarking/grapher.py/experiment-results/23.6.12/timeout/timeout-noindex-card",
        "/home/simon/Documents/Unief/Thesis/1-benchmarking/grapher.py/experiment-results/23.6.12/timeout/timeout-index-card",
        ]

    baselineResultsPerQuery={}
    for queryFileName in queryFiles:
        lines = open(baselineFolder+'/'+queryFileName, 'r').readlines()
        for line in lines[1:]:
            qTitle = line.split(';')[0].strip("interactive-")
            qExTime = int(line.split(';')[3])
            baselineResultsPerQuery[qTitle] = qExTime

    percentagesPerConfig={}
    for i, folder in enumerate(queryFolders):
        configname=confignames[i]
        improvementOfConfig=improvementPerConfig[i]
        amountOfQueries=0
        amountOfQueries10PercentBetter=0
        queries10PercentBetter=[]
        amountOfQueries10PercentWorse=0
        queries10PercentWorse=[]
        for queryFileName in queryFiles:
            lines = open(folder+'/'+queryFileName, 'r').readlines()
            amountOfQueries+=len(lines)-1
            for line in lines[1:]:
                qName = line.split(';')[0].strip("interactive-")
                if qName in representativeQueries:
                    qExTime = int(line.split(';')[3])
                    if (qExTime>baselineResultsPerQuery[qName] + (baselineResultsPerQuery[qName])/10):
                        amountOfQueries10PercentWorse += 1
                        queries10PercentWorse.append(line)
                    elif (qExTime<baselineResultsPerQuery[qName] - (baselineResultsPerQuery[qName])/10):
                        amountOfQueries10PercentBetter += 1
                        queries10PercentBetter.append(line)
        print("------------------")
        print("------------------")
        print(configname)
        print("------------------")
        print("------------------")
        print("queries10PercentWorse")
        for i in queries10PercentWorse:
            print(i.strip('\n'))
        print("queries10PercentBetter")
        for i in queries10PercentBetter:
            print(i.strip('\n'))
        print(amountOfQueries10PercentBetter)
        print(amountOfQueries10PercentWorse)
        print(improvementOfConfig)
        percentagesPerConfig[configname] = [amountOfQueries10PercentBetter/amountOfQueries, amountOfQueries10PercentWorse/amountOfQueries, improvementOfConfig/100]
        print(percentagesPerConfig[configname])

    outputFileName="percentageTable"
    with open(f"{outputFileName}.tex", 'w') as f:
        f.write("\\documentclass[preview]{standalone} \n")
        f.write("\\usepackage[a4paper]{geometry} \n")
        f.write("\\usepackage{tabularx} \n")
        f.write("\\begin{document} \n")
        f.write("\\begin{table}[!ht] \n")
        # f.write("\\captionsetup{justification=centering} \n")
        f.write("\\centering \n")
        f.write("\\begin{tabular}{lccc} \n")

        columnNames = ["better", "worse", "average improvement"]
        f.write('& \multicolumn{2}{c}{\% of queries} \\\\')
        f.write('\cline{2-3}')
        f.write(f'& {" & ".join(columnNames)} \\\\ \\hline \n')
        for configname in confignames:
            f.write(f'{configname} & {" & ".join(map(lambda x: "{:.2f}".format(x*100), percentagesPerConfig[configname][0:3]))} \\\\ \n ')

        f.write("\\end{tabular} \n")
        f.write("\\caption{Queries with execution time of at least 10\% better (resp. 10 worse) than the baseline}\n")
        f.write("\\end{table} \n")
        f.write("\\end{document} \n")

    os.system(f"texliveonfly {outputFileName}.tex")
    os.system(f"rm {outputFileName}.aux")
    os.system(f"rm {outputFileName}.log")
    os.system(f"rm {outputFileName}.synctex.gz")

# This version includes each query that finds the correct results
representativeQueriesAllCorrect =[f"discover-1-{i}" for i in range(0,5)]
representativeQueriesAllCorrect+=[f"discover-2-{i}" for i in range(0,5)]
representativeQueriesAllCorrect+=[f"discover-3-{i}" for i in range(0,5)]
representativeQueriesAllCorrect+=[f"discover-4-{i}" for i in range(0,5)]
representativeQueriesAllCorrect+=[f"discover-5-{i}" for i in range(0,5)]
representativeQueriesAllCorrect+=[f"discover-6-{i}" for i in [1,2,4]]
representativeQueriesAllCorrect+=[f"discover-7-{i}" for i in [1,2,4]]
representativeQueriesAllCorrect+=[f"discover-8-{i}" for i in range(0,5)]
representativeQueriesAllCorrect+=[f"short-4-{i}" for i in range(0,5)]
def generateImprovementPercentageTableAllCorrect(queryFiles):
    baselineFolder = "/home/simon/Documents/Unief/Thesis/1-benchmarking/grapher.py/experiment-results/23.6.12/baseline/baseline-zero"
    confignames=["index\\_zero", "index\\_card", "count", "count+index"]
    improvementPerConfig=[processOverviewTable.averageImprovementAllCorrect(1, 3)[0], processOverviewTable.averageImprovementAllCorrect(1, 4)[0], processOverviewTable.averageImprovementAllCorrect(1, 5)[0], processOverviewTable.averageImprovementAllCorrect(1, 6)[0]]
    queryFolders=[
        "/home/simon/Documents/Unief/Thesis/1-benchmarking/grapher.py/experiment-results/23.6.12/index/index-zero",
        "/home/simon/Documents/Unief/Thesis/1-benchmarking/grapher.py/experiment-results/23.6.12/index/index-card",
        "/home/simon/Documents/Unief/Thesis/1-benchmarking/grapher.py/experiment-results/23.6.12/timeout/timeout-noindex-card",
        "/home/simon/Documents/Unief/Thesis/1-benchmarking/grapher.py/experiment-results/23.6.12/timeout/timeout-index-card",
        ]

    baselineResultsPerQuery={}
    for queryFileName in queryFiles:
        lines = open(baselineFolder+'/'+queryFileName, 'r').readlines()
        for line in lines[1:]:
            qTitle = line.split(';')[0].strip("interactive-")
            qExTime = int(line.split(';')[3])
            baselineResultsPerQuery[qTitle] = qExTime

    percentagesPerConfig={}
    for i, folder in enumerate(queryFolders):
        configname=confignames[i]
        improvementOfConfig=improvementPerConfig[i]
        amountOfQueries=0
        amountOfQueries10PercentBetter=0
        queries10PercentBetter=[]
        amountOfQueries10PercentWorse=0
        queries10PercentWorse=[]
        for queryFileName in queryFiles:
            lines = open(folder+'/'+queryFileName, 'r').readlines()
            amountOfQueries+=len(lines)-1
            for line in lines[1:]:
                qName = line.split(';')[0].strip("interactive-")
                if qName in representativeQueriesAllCorrect:
                    qExTime = int(line.split(';')[3])
                    if (qExTime>baselineResultsPerQuery[qName] + (baselineResultsPerQuery[qName])/10):
                        amountOfQueries10PercentWorse += 1
                        queries10PercentWorse.append(line)
                    elif (qExTime<baselineResultsPerQuery[qName] - (baselineResultsPerQuery[qName])/10):
                        amountOfQueries10PercentBetter += 1
                        queries10PercentBetter.append(line)
        print("------------------")
        print("------------------")
        print(configname)
        print("------------------")
        print("------------------")
        print("queries10PercentWorse: ", amountOfQueries10PercentWorse)
        for i in queries10PercentWorse:
            print(i.strip('\n'))
        # print("queries10PercentBetter")amountOfQueries10PercentBetter
        # for i in queries10PercentBetter:
        #     print(i.strip('\n'))
        # print(improvementOfConfig)
        percentagesPerConfig[configname] = [amountOfQueries10PercentBetter/amountOfQueries, amountOfQueries10PercentWorse/amountOfQueries, improvementOfConfig/100]
        print(percentagesPerConfig[configname])

    outputFileName="percentageTable"
    with open(f"{outputFileName}.tex", 'w') as f:
        f.write("\\documentclass[preview]{standalone} \n")
        f.write("\\usepackage[a4paper]{geometry} \n")
        f.write("\\usepackage{tabularx} \n")
        f.write("\\begin{document} \n")
        f.write("\\begin{table}[!ht] \n")
        # f.write("\\captionsetup{justification=centering} \n")
        f.write("\\centering \n")
        f.write("\\begin{tabular}{lccc} \n")

        columnNames = ["better", "worse", "average improvement"]
        f.write('& \multicolumn{2}{c}{\% of queries} \\\\')
        f.write('\cline{2-3}')
        f.write(f'& {" & ".join(columnNames)} \\\\ \\hline \n')
        for configname in confignames:
            f.write(f'{configname} & {" & ".join(map(lambda x: "{:.2f}".format(x*100), percentagesPerConfig[configname][0:3]))} \\\\ \n ')

        f.write("\\end{tabular} \n")
        f.write("\\caption{Queries with execution time of at least 10\% better (resp. 10 worse) than the baseline}\n")
        f.write("\\end{table} \n")
        f.write("\\end{document} \n")

    os.system(f"texliveonfly {outputFileName}.tex")
    os.system(f"rm {outputFileName}.aux")
    os.system(f"rm {outputFileName}.log")
    os.system(f"rm {outputFileName}.synctex.gz")

# This version includes queries 8.X
representativeQueriesWith8 =[f"discover-1-{i}" for i in range(0,5)]
representativeQueriesWith8+=[f"discover-2-{i}" for i in range(0,5)]
representativeQueriesWith8+=[f"discover-5-{i}" for i in range(0,5)]
representativeQueriesWith8+=[f"discover-6-{i}" for i in [1,2,4]]
representativeQueriesWith8+=[f"discover-7-{i}" for i in range(0,5)]
representativeQueriesWith8+=[f"discover-8-{i}" for i in range(0,5)]
def generateImprovementPercentageTableFilterWith8(queryFiles):
    baselineFolder = "/home/simon/Documents/Unief/Thesis/1-benchmarking/grapher.py/experiment-results/23.6.12/baseline/baseline-zero"
    confignames=["index\\_zero", "index\\_card", "count", "count+index"]
    improvementPerConfig=[processOverviewTable.averageImprovementWith8(1, 3)[0], processOverviewTable.averageImprovementWith8(1, 4)[0], processOverviewTable.averageImprovementWith8(1, 5)[0], processOverviewTable.averageImprovementWith8(1, 6)[0]]
    queryFolders=[
        "/home/simon/Documents/Unief/Thesis/1-benchmarking/grapher.py/experiment-results/23.6.12/index/index-zero",
        "/home/simon/Documents/Unief/Thesis/1-benchmarking/grapher.py/experiment-results/23.6.12/index/index-card",
        "/home/simon/Documents/Unief/Thesis/1-benchmarking/grapher.py/experiment-results/23.6.12/timeout/timeout-noindex-card",
        "/home/simon/Documents/Unief/Thesis/1-benchmarking/grapher.py/experiment-results/23.6.12/timeout/timeout-index-card",
        ]

    baselineResultsPerQuery={}
    for queryFileName in queryFiles:
        lines = open(baselineFolder+'/'+queryFileName, 'r').readlines()
        for line in lines[1:]:
            qTitle = line.split(';')[0].strip("interactive-")
            qExTime = int(line.split(';')[3])
            baselineResultsPerQuery[qTitle] = qExTime

    percentagesPerConfig={}
    for i, folder in enumerate(queryFolders):
        configname=confignames[i]
        improvementOfConfig=improvementPerConfig[i]
        amountOfQueries=0
        amountOfQueries10PercentBetter=0
        queries10PercentBetter=[]
        amountOfQueries10PercentWorse=0
        queries10PercentWorse=[]
        for queryFileName in queryFiles:
            lines = open(folder+'/'+queryFileName, 'r').readlines()
            amountOfQueries+=len(lines)-1
            for line in lines[1:]:
                qName = line.split(';')[0].strip("interactive-")
                if qName in representativeQueriesWith8:
                    qExTime = int(line.split(';')[3])
                    if (qExTime>baselineResultsPerQuery[qName] + (baselineResultsPerQuery[qName])/10):
                        amountOfQueries10PercentWorse += 1
                        queries10PercentWorse.append(line)
                    elif (qExTime<baselineResultsPerQuery[qName] - (baselineResultsPerQuery[qName])/10):
                        amountOfQueries10PercentBetter += 1
                        queries10PercentBetter.append(line)
        print("------------------")
        print("------------------")
        print(configname)
        print("------------------")
        print("------------------")
        print("queries10PercentWorse: ", amountOfQueries10PercentWorse)
        for i in queries10PercentWorse:
            print(i.strip('\n'))
        # print("queries10PercentBetter")amountOfQueries10PercentBetter
        # for i in queries10PercentBetter:
        #     print(i.strip('\n'))
        # print(improvementOfConfig)
        percentagesPerConfig[configname] = [amountOfQueries10PercentBetter/amountOfQueries, amountOfQueries10PercentWorse/amountOfQueries, improvementOfConfig/100]
        print(percentagesPerConfig[configname])

    outputFileName="percentageTable"
    with open(f"{outputFileName}.tex", 'w') as f:
        f.write("\\documentclass[preview]{standalone} \n")
        f.write("\\usepackage[a4paper]{geometry} \n")
        f.write("\\usepackage{tabularx} \n")
        f.write("\\begin{document} \n")
        f.write("\\begin{table}[!ht] \n")
        # f.write("\\captionsetup{justification=centering} \n")
        f.write("\\centering \n")
        f.write("\\begin{tabular}{lccc} \n")

        columnNames = ["better", "worse", "average improvement"]
        f.write('& \multicolumn{2}{c}{\% of queries} \\\\')
        f.write('\cline{2-3}')
        f.write(f'& {" & ".join(columnNames)} \\\\ \\hline \n')
        for configname in confignames:
            f.write(f'{configname} & {" & ".join(map(lambda x: "{:.2f}".format(x*100), percentagesPerConfig[configname][0:3]))} \\\\ \n ')

        f.write("\\end{tabular} \n")
        f.write("\\caption{Queries with execution time of at least 10\% better (resp. 10 worse) than the baseline}\n")
        f.write("\\end{table} \n")
        f.write("\\end{document} \n")

    os.system(f"texliveonfly {outputFileName}.tex")
    os.system(f"rm {outputFileName}.aux")
    os.system(f"rm {outputFileName}.log")
    os.system(f"rm {outputFileName}.synctex.gz")

# This version includes small queries
representativeQueriesSmall =[f"discover-1-{i}" for i in range(0,5)]
representativeQueriesSmall+=[f"discover-2-{i}" for i in range(0,5)]
representativeQueriesSmall+=[f"discover-5-{i}" for i in range(0,5)]
representativeQueriesSmall+=[f"discover-6-{i}" for i in [1,2,4]]
representativeQueriesSmall+=[f"discover-7-{i}" for i in range(0,5)]
representativeQueriesSmall+=[f"discover-3-{i}" for i in range(0,5)]
representativeQueriesSmall+=[f"discover-4-{i}" for i in range(0,5)]
representativeQueriesSmall+=[f"short-4-{i}" for i in range(0,5)]
def generateImprovementPercentageTableFilterSmall(queryFiles):
    baselineFolder = "/home/simon/Documents/Unief/Thesis/1-benchmarking/grapher.py/experiment-results/23.6.12/baseline/baseline-zero"
    confignames=["index\\_zero", "index\\_card", "count", "count+index"]
    improvementPerConfig=[processOverviewTable.averageImprovementSmall(1, 3)[0], processOverviewTable.averageImprovementSmall(1, 4)[0], processOverviewTable.averageImprovementSmall(1, 5)[0], processOverviewTable.averageImprovementSmall(1, 6)[0]]
    queryFolders=[
        "/home/simon/Documents/Unief/Thesis/1-benchmarking/grapher.py/experiment-results/23.6.12/index/index-zero",
        "/home/simon/Documents/Unief/Thesis/1-benchmarking/grapher.py/experiment-results/23.6.12/index/index-card",
        "/home/simon/Documents/Unief/Thesis/1-benchmarking/grapher.py/experiment-results/23.6.12/timeout/timeout-noindex-card",
        "/home/simon/Documents/Unief/Thesis/1-benchmarking/grapher.py/experiment-results/23.6.12/timeout/timeout-index-card",
        ]

    baselineResultsPerQuery={}
    for queryFileName in queryFiles:
        lines = open(baselineFolder+'/'+queryFileName, 'r').readlines()
        for line in lines[1:]:
            qTitle = line.split(';')[0].strip("interactive-")
            qExTime = int(line.split(';')[3])
            baselineResultsPerQuery[qTitle] = qExTime

    percentagesPerConfig={}
    for i, folder in enumerate(queryFolders):
        configname=confignames[i]
        improvementOfConfig=improvementPerConfig[i]
        amountOfQueries=0
        amountOfQueries10PercentBetter=0
        queries10PercentBetter=[]
        amountOfQueries10PercentWorse=0
        queries10PercentWorse=[]
        for queryFileName in queryFiles:
            lines = open(folder+'/'+queryFileName, 'r').readlines()
            amountOfQueries+=len(lines)-1
            for line in lines[1:]:
                qName = line.split(';')[0].strip("interactive-")
                if qName in representativeQueriesWith8:
                    qExTime = int(line.split(';')[3])
                    if (qExTime>baselineResultsPerQuery[qName] + (baselineResultsPerQuery[qName])/10):
                        amountOfQueries10PercentWorse += 1
                        queries10PercentWorse.append(line)
                    elif (qExTime<baselineResultsPerQuery[qName] - (baselineResultsPerQuery[qName])/10):
                        amountOfQueries10PercentBetter += 1
                        queries10PercentBetter.append(line)
        print("------------------")
        print("------------------")
        print(configname)
        print("------------------")
        print("------------------")
        print("queries10PercentWorse: ", amountOfQueries10PercentWorse)
        for i in queries10PercentWorse:
            print(i.strip('\n'))
        # print("queries10PercentBetter")amountOfQueries10PercentBetter
        # for i in queries10PercentBetter:
        #     print(i.strip('\n'))
        # print(improvementOfConfig)
        percentagesPerConfig[configname] = [amountOfQueries10PercentBetter/amountOfQueries, amountOfQueries10PercentWorse/amountOfQueries, improvementOfConfig/100]
        print(percentagesPerConfig[configname])

    outputFileName="percentageTable"
    with open(f"{outputFileName}.tex", 'w') as f:
        f.write("\\documentclass[preview]{standalone} \n")
        f.write("\\usepackage[a4paper]{geometry} \n")
        f.write("\\usepackage{tabularx} \n")
        f.write("\\begin{document} \n")
        f.write("\\begin{table}[!ht] \n")
        # f.write("\\captionsetup{justification=centering} \n")
        f.write("\\centering \n")
        f.write("\\begin{tabular}{lccc} \n")

        columnNames = ["better", "worse", "average improvement"]
        f.write('& \multicolumn{2}{c}{\% of queries} \\\\')
        f.write('\cline{2-3}')
        f.write(f'& {" & ".join(columnNames)} \\\\ \\hline \n')
        for configname in confignames:
            f.write(f'{configname} & {" & ".join(map(lambda x: "{:.2f}".format(x*100), percentagesPerConfig[configname][0:3]))} \\\\ \n ')

        f.write("\\end{tabular} \n")
        f.write("\\caption{Queries with execution time of at least 10\% better (resp. 10 worse) than the baseline}\n")
        f.write("\\end{table} \n")
        f.write("\\end{document} \n")

    os.system(f"texliveonfly {outputFileName}.tex")
    os.system(f"rm {outputFileName}.aux")
    os.system(f"rm {outputFileName}.log")
    os.system(f"rm {outputFileName}.synctex.gz")
