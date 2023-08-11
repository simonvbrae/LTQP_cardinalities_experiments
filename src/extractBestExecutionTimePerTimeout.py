import csv
import os
import math
import re

def countResultsPerQuery(file):
  resultsFile=file
  resultAmountPerQuery={}
  lines=open(resultsFile).readlines()
  for line in lines[1:]:
    x=line.strip('\n').split(';')
    resultAmountPerQuery[f'{x[0]}-{x[1]}'] = (len(re.findall(r"[0-9]+ ", x[-1]) + re.findall(r"[0-9]+$", x[-1])), x[4])
  return resultAmountPerQuery

resultsPerQueryBaseline=countResultsPerQuery("/home/simon/Documents/Unief/Thesis/1-benchmarking/grapher.py/experiment-results/23.6.12/baseline/baseline-card/baseline-card.csv")
def compareResultToBaseline(d1, d2):
  worseThanBaseline=[]
  for key in d1.keys():
    if d2[key][1]=="false" and d2[key][0] < d1[key][0]:
      worseThanBaseline.append((key, d1[key], d2[key]))
  return worseThanBaseline

count_index=countResultsPerQuery("/home/simon/Documents/Unief/Thesis/1-benchmarking/grapher.py/experiment-results/23.6.12/timeout/timeout-index-card/result-psbrtitle.csv")
x=compareResultToBaseline(resultsPerQueryBaseline, count_index)
print("[print(x) for x in x]")
[print(x) for x in x]

count=countResultsPerQuery("/home/simon/Documents/Unief/Thesis/1-benchmarking/grapher.py/experiment-results/23.6.12/timeout/timeout-noindex-card/result-psbrtitle.csv")
x=compareResultToBaseline(resultsPerQueryBaseline, count)
print("[print(x) for x in x]")
[print(x) for x in x]

# This function changes the timestamp of a query with timeout into 60000 for more uniform data which simplifies further processing and interpreting plots.
def readTimeoutFilesInDirectory(dirWithTimeoutFiles):
  files=os.listdir(dirWithTimeoutFiles)
  CsvFiles=filter(lambda fileName: fileName.endswith(".csv"), files)
  CsvFilesAndPaths=map(lambda fileName: dirWithTimeoutFiles+'/'+fileName, CsvFiles)

  data=[]
  for CsvFileAndPath in CsvFilesAndPaths:
    with open(CsvFileAndPath, 'r') as file:
      dataPerConfiguration=[]
      csvreader = csv.reader(file, delimiter=';')
      skipFirstRow=True
      for row in csvreader:
        if skipFirstRow:
          skipFirstRow=False
        else:
          if row[4] == "true":
            dataPerConfiguration.append(row[0:3] + ['60000'] + row[4:])
          else:
            dataPerConfiguration.append(row)
      data.append((CsvFileAndPath, dataPerConfiguration))
  return data

# This function finds the timeout value providing the best result.
def findBestTimeoutPerQueryInListOfTimeoutFiles(dataPerTimeoutFile):
  bestResultPerQueryIndex=[]
  for queryIndexInResultSet in range(len(dataPerTimeoutFile[0][1])):
    lowestExTime=math.inf
    filenameWithLowestExTime=None
    resultWithLowestExTime=None
    for (resultOfTimeoutFileName, resultSetOfTimeout) in dataPerTimeoutFile:
      currentQueryResult=resultSetOfTimeout[queryIndexInResultSet]
      if int(currentQueryResult[3]) < lowestExTime:
        lowestExTime=int(currentQueryResult[3])
        filenameWithLowestExTime=resultOfTimeoutFileName
        resultWithLowestExTime=currentQueryResult
    bestResultPerQueryIndex.append((filenameWithLowestExTime, resultWithLowestExTime))
  return bestResultPerQueryIndex

# This function writes the best execution time and its timeout value.
def writeMappingAndBestResult(bestResultPerQueryIndex):
  with open('result-psbrtitle-mapping.txt', 'w') as mappingOutputFile:
    for i in bestResultPerQueryIndex:
      mappingOutputFile.write(f'{i[0][i[0].rindex("/")+1:i[0].rindex("-")]} - {i[1]}\n')

  with open('result-psbrtitle.csv', 'w') as mappingOutputFile:
    mappingOutputFile.write("name;id;results;time;error;timestamps\n")
    for i in bestResultPerQueryIndex:
      mappingOutputFile.write(f'{";".join(i[1])}\n')


dataPerTimeoutFile=readTimeoutFilesInDirectory('.')
bestResultPerQueryIndex = findBestTimeoutPerQueryInListOfTimeoutFiles(dataPerTimeoutFile)
writeMappingAndBestResult(bestResultPerQueryIndex)
