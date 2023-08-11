import csv
import numpy as np
import matplotlib.pyplot as plt

# This file generates plots used throughout the work.

cm = 1/2.54  # centimeters in inches
def get_cmap(n, name='hsv'):
    '''Returns a function that maps each index in 0, 1, ..., n-1 to a distinct 
    RGB color; the keyword argument name must be a standard mpl colormap name.'''
    return plt.cm.get_cmap(name, n)
cmap=get_cmap(100)
# Read card card experiment data
def readExperimentData(inputDir, idk):
  inputFiles = []
  inputBarTitles=[]
  for i in [1,3,5,7,9,10,50,100,1000,2000,4000,6000]:
    inputFiles.append(f'{inputDir}{i}-{idk}-card.csv')
    inputBarTitles.append(str(i))

  dataRaw=[]
  executionTimeData=[]
  for f in inputFiles:
    fileData = []
    with open(f, 'r') as file:
      dataPerConfiguration=[]
      csvreader = csv.reader(file, delimiter=';')
      mustSkip=True
      for row in csvreader:
        if mustSkip:
          mustSkip=False
        else:
          dataPerConfiguration.append(row)
          fileData.append(int(row[3]))
      dataRaw.append(dataPerConfiguration)
    executionTimeData.append(fileData)
  return dataRaw, executionTimeData, inputBarTitles
def readExperimentDataZeroMinOne(inputDir, idk):
  inputFiles = []
  inputBarTitles=[]
  for i in [1,3,5,7,9,10,50,100,1000,2000,4000,6000]:
    inputFiles.append(f'{inputDir}{i}-{idk}-card.csv')
    inputBarTitles.append(str(i))

  dataRaw=[]
  executionTimeData=[]
  for f in inputFiles:
    executionTimesOfFile = []
    with open(f, 'r') as file:
      dataPerConfiguration=[]
      csvreader = csv.reader(file, delimiter=';')
      mustSkip=True
      for row in csvreader:
        if mustSkip:
          mustSkip=False
        else:
          dataPerConfiguration.append(row)
          gotError=row[4]=='true'
          if gotError:
            executionTimesOfFile.append(-1)
          else:
            executionTimesOfFile.append(int(row[3]))
      dataRaw.append(dataPerConfiguration)
    executionTimeData.append(executionTimesOfFile)
  return dataRaw, executionTimeData, inputBarTitles
def readSkipData():
  dataRaw=[]
  executionTimeData=[]
  with open('/home/simon/Documents/Unief/Thesis/1-benchmarking/grapher.py/experiment-results/experiment-skip-zero/skip-zero.csv', 'r') as file:
    csvreader = csv.reader(file, delimiter=';')
    mustSkip=True
    for row in csvreader:
      if mustSkip:
        mustSkip=False
      else:
        dataRaw.append(row)
        executionTimeData.append(int(row[3]))
  return dataRaw, executionTimeData, ['skip']
def readSkipDataZeroMinOne():
  dataRaw=[]
  executionTimeData=[]
  with open('/home/simon/Documents/Unief/Thesis/1-benchmarking/grapher.py/experiment-results/experiment-skip-zero/skip-zero.csv', 'r') as file:
    csvreader = csv.reader(file, delimiter=';')
    mustSkip=True
    for row in csvreader:
      if mustSkip:
        mustSkip=False
      else:
        dataRaw.append(row)
        gotError=row[4]=='true'
        if gotError:
          executionTimeData.append(-1)
        else:
          executionTimeData.append(int(row[3]))

  return dataRaw, executionTimeData, ['skip']

# Calculate average runtime of all queries per configuration
def calc_avg(executionTimes):
  return list(map(lambda d: np.mean(d), executionTimes))

def calc_std(executionTimes):
  return list(map(lambda d: np.std(d), executionTimes))

# Plot the average execution time of configurations
def plotAverage(avg_times, barTitles, filename, legend_label, color):
  plt.clf()
  # Input: [v1, v2, ...]
  x_pos = np.arange(len(avg_times))

  plt.bar(x_pos, avg_times, color = color, label=legend_label)

  plt.title('Average execution time per configuration')
  plt.xlabel('Timeout before phase two (ms)')
  plt.ylabel('Average execution time (ms)')
  plt.xticks(x_pos, barTitles)
  plt.legend()

  figure = plt.gcf()
  figure.set_size_inches(16, 6)
  plt.savefig(filename)

# cardCardDataRaw, cardCardExecutionTimes, cardCardTitles = readExperimentData("experiment-results/experiment-card-card/", "card")
# average_times_card_card=calc_avg(cardCardExecutionTimes)
# plotAverage(average_times_card_card, cardCardTitles, "avg_card_card", "card-card", cmap(0))

# zeroCardDataRaw, zeroCardExecutionTimes, zeroCardTitles = readExperimentData("experiment-results/experiment-zero-card/", "zero")
# average_times_zero_card=list(map(lambda d: np.mean(d), zeroCardExecutionTimes))
# plotAverage(average_times_zero_card, zeroCardTitles, "avg_zero_card", "zero-card", cmap(25))

def plotAverageWithStdDev(executionTimePerQueryPerConfiguration, barTitles, filename, legend_label, color):
  plt.clf()
  x=executionTimePerQueryPerConfiguration
  avg_times=calc_avg(x)
  std_times=calc_std(x)
  x_pos = np.arange(len(avg_times))

  plt.bar(x_pos, avg_times, yerr=std_times, color = color, label=legend_label)

  plt.title('Average execution time per configuration')
  plt.xlabel('Timeout before phase two (ms)')
  plt.ylabel('Average execution time (ms)')
  plt.xticks(x_pos, barTitles)
  plt.legend()

  figure = plt.gcf()
  figure.set_size_inches(16, 6)
  plt.savefig(filename)

# zeroCardDataRaw, zeroCardExecutionTimes, zeroCardTitles = readExperimentData("experiment-results/experiment-zero-card/", "zero")
# plotAverageWithStdDev(zeroCardExecutionTimes, zeroCardTitles, "avg_std_zero_card", "zero-card", cmap(25))
# cardCardDataRaw, cardCardExecutionTimes, cardCardTitles = readExperimentData("experiment-results/experiment-card-card/", "card")
# plotAverageWithStdDev(cardCardExecutionTimes, cardCardTitles, "avg_std_card_card", "card-card", cmap(25))

###
### Plot multiple bar charts
###
def plot_comparison():
  plt.clf()

  avg_times, barTitles, filename, legend_label = average_times_card_card, cardCardTitles, "avg_card_card", "card-card"
  x_pos = np.arange(len(avg_times))
  plt.bar(x_pos-.2, avg_times, width=0.4, color = cmap(0), label=legend_label)

  avg_times, barTitles, filename, legend_label = average_times_zero_card, zeroCardTitles, "avg_zero_card", "zero-card"
  plt.bar(x_pos+.2, avg_times, width=0.4, color = cmap(25), label=legend_label)

  plt.title('Average execution time per configuration')
  plt.xlabel('Timeout before phase two (ms)')
  plt.ylabel('Average execution time (ms)')
  plt.xticks(x_pos, barTitles)
  plt.legend()

  figure = plt.gcf()
  figure.set_size_inches(16, 6)
  plt.savefig("comparison")

def plot_per_query_bar_card_card():
  cardCardDataRaw, cardCardExecutionTimes, cardCardTitles = readExperimentData("experiment-results/experiment-card-card/", "card")
  numpyExecutionTimes = np.array(cardCardExecutionTimes)
  for queryIndex,_ in enumerate(cardCardExecutionTimes[0]):
    resultsOfQuery = numpyExecutionTimes[:,queryIndex]

    plt.clf()

    x_pos = np.arange(len(resultsOfQuery))
    plt.bar(x_pos, resultsOfQuery, color = cmap(4), label=cardCardDataRaw[0][queryIndex][0])

    plt.title('Query execution time in function of timeout value')
    plt.xlabel('Timeout before phase two (ms)')
    plt.ylabel('Execution time (ms)')
    plt.xticks(x_pos, cardCardTitles)
    plt.legend()

    figure = plt.gcf()
    figure.set_size_inches(16, 6)
    plt.savefig(f'query-plots-card-card/{cardCardDataRaw[0][queryIndex][0]}')

def plot_per_query_line_card_card():
  cardCardDataRaw, cardCardExecutionTimes, cardCardTitles = readExperimentData("experiment-results/experiment-card-card/", "card")
  numpyExecutionTimes = np.array(cardCardExecutionTimes)
  cmap=get_cmap(len(zeroCardExecutionTimes[0]))

  for queryIndex,_ in enumerate(cardCardExecutionTimes[0]):
    plt.clf()
    resultsOfQuery = numpyExecutionTimes[:,queryIndex]

    x_pos = np.arange(len(resultsOfQuery))
    plt.plot(x_pos, resultsOfQuery, color = cmap(queryIndex), label=f'{cardCardDataRaw[0][queryIndex][0]}.{cardCardDataRaw[0][queryIndex][1]}')

    plt.title('Query execution time in function of timeout value')
    plt.xlabel('Timeout before phase two (ms)')
    plt.ylabel('Execution time (ms)')
    plt.xticks(x_pos, cardCardTitles)
    plt.legend()

    figure = plt.gcf()
    figure.set_size_inches(16, 6)
    plt.savefig(f'query-plots-card-card/query-plots-lines/{cardCardDataRaw[0][queryIndex][0]}-{cardCardDataRaw[0][queryIndex][1]}')

def plot_per_query_line_zero_card():
  zeroCardDataRaw, zeroCardExecutionTimes, zeroCardTitles = readExperimentData("experiment-results/experiment-zero-card/", "zero")
  numpyExecutionTimes = np.array(zeroCardExecutionTimes)
  cmap=get_cmap(len(zeroCardExecutionTimes[0]))

  for queryIndex,_ in enumerate(zeroCardExecutionTimes[0]):
    plt.clf()
    resultsOfQuery = numpyExecutionTimes[:,queryIndex]

    x_pos = np.arange(len(resultsOfQuery))
    plt.plot(x_pos, resultsOfQuery, color = cmap(queryIndex), label=f'{zeroCardDataRaw[0][queryIndex][0]}.{zeroCardDataRaw[0][queryIndex][1]}')

    plt.title('Query execution time in function of timeout value')
    plt.xlabel('Timeout before phase two (ms)')
    plt.ylabel('Execution time (ms)')
    plt.xticks(x_pos, zeroCardTitles)
    plt.legend()

    figure = plt.gcf()
    figure.set_size_inches(16, 6)
    plt.savefig(f'{zeroCardDataRaw[0][queryIndex][0]}-{zeroCardDataRaw[0][queryIndex][1]}')

def plot_per_subquery_line_card_card():
  cardCardDataRaw, cardCardExecutionTimes, cardCardTitles = readExperimentData("experiment-results/experiment-card-card/", "card")
  numpyExecutionTimes = np.array(cardCardExecutionTimes)
  cmap=get_cmap(5)

  amountOfSubQueries=5
  
  for start in range(0,len(cardCardExecutionTimes[0]),amountOfSubQueries):
    print(start)
    print(cardCardExecutionTimes[0][start:start+amountOfSubQueries])
    plt.clf()
    for queryIndex,_ in enumerate(cardCardExecutionTimes[0][start:start+amountOfSubQueries]):
      qI=queryIndex+start
      print(cardCardDataRaw[0][qI][0])
      resultsOfQuery = numpyExecutionTimes[:,qI]

      x_pos = np.arange(len(resultsOfQuery))
      plt.plot(x_pos, resultsOfQuery, color = cmap(queryIndex), label=f'{cardCardDataRaw[0][qI][0]}.{cardCardDataRaw[0][queryIndex][1]}')

      plt.title('Query execution time in function of timeout value')
      plt.xlabel('Timeout before phase two (ms)')
      plt.ylabel('Execution time (ms)')
      plt.xticks(x_pos, cardCardTitles)
      plt.legend()

      figure = plt.gcf()
      figure.set_size_inches(16, 6)
      plt.savefig(f'{cardCardDataRaw[0][qI][0]}-summary')

def plot_per_subquery_line_zero_card():
  dataRaw, executionTimes, tickLabels = readExperimentData("experiment-results/experiment-zero-card/", "zero")
  numpyExecutionTimes = np.array(executionTimes)
  cmap=get_cmap(5)

  amountOfSubQueries=5
  
  for start in range(0,len(executionTimes[0]),amountOfSubQueries):
    plt.clf()
    for queryIndex,_ in enumerate(executionTimes[0][start:start+amountOfSubQueries]):
      qI=queryIndex+start
      print(dataRaw[0][qI][0])
      resultsOfQuery = numpyExecutionTimes[:,qI]

      x_pos = np.arange(len(resultsOfQuery))
      plt.plot(x_pos, resultsOfQuery, color = cmap(queryIndex), label=f'{dataRaw[0][qI][0]}.{dataRaw[0][queryIndex][1]}')

      plt.title('Query execution time in function of timeout value')
      plt.xlabel('Timeout before phase two (ms)')
      plt.ylabel('Execution time (ms)')
      plt.xticks(x_pos, tickLabels)
      plt.legend()

      figure = plt.gcf()
      figure.set_size_inches(16, 6)
      plt.savefig(f'{dataRaw[0][qI][0]}-summary')

def plot_per_query_line_comparison():
  dataRawZero, executionTimesZero, tickLabels = readExperimentData("experiment-results/experiment-zero-card/", "zero")
  dataRawCard, executionTimesCard, _ = readExperimentData("experiment-results/experiment-card-card/", "card")
  numpyExecutionTimesZero = np.array(executionTimesZero)
  numpyExecutionTimesCard = np.array(executionTimesCard)
  cmap=get_cmap(20)

  for queryIndex,_ in enumerate(numpyExecutionTimesZero[0]):
    plt.clf()
    resultsOfQueryZero = numpyExecutionTimesZero[:,queryIndex]
    resultsOfQueryCard = numpyExecutionTimesCard[:,queryIndex]

    x_pos = np.arange(len(resultsOfQueryZero))
    plt.plot(x_pos, resultsOfQueryZero, color = cmap(0), label=f'zero: {dataRawZero[0][queryIndex][0]}.{dataRawZero[0][queryIndex][1]}')
    plt.plot(x_pos, resultsOfQueryCard, color = cmap(10), label=f'card: {dataRawZero[0][queryIndex][0]}.{dataRawZero[0][queryIndex][1]}')

    plt.title('Query execution time in function of timeout value')
    plt.xlabel('Timeout before phase two (ms)')
    plt.ylabel('Execution time (ms)')
    plt.xticks(x_pos, tickLabels)
    plt.legend()

    figure = plt.gcf()
    figure.set_size_inches(16, 6)
    plt.savefig(f'{zeroCardDataRaw[0][queryIndex][0]}-{zeroCardDataRaw[0][queryIndex][1]}')

def plot_per_query_line_comparison_add_skip():
  _, executionTimesSkip, _ = readSkipData()
  dataRawZero, executionTimesZero, tickLabels = readExperimentData("experiment-results/experiment-zero-card/", "zero")
  # tickLabels.insert(0, "no\nrestart")
  _, executionTimesCard, _ = readExperimentData("experiment-results/experiment-card-card/", "card")
  numpyExecutionTimesZero = np.array(executionTimesZero)
  numpyExecutionTimesCard = np.array(executionTimesCard)
  cmap=get_cmap(21)

  for queryIndex,_ in enumerate(numpyExecutionTimesZero[0]):
    plt.clf()
    resultsOfQueryZero = numpyExecutionTimesZero[:,queryIndex]
    resultsOfQueryCard = numpyExecutionTimesCard[:,queryIndex]
    resultsOfQuerySkipZero = [executionTimesSkip[queryIndex]] * len(resultsOfQueryZero)

    x_pos = np.arange(len(resultsOfQueryZero))
    plt.plot(x_pos, resultsOfQueryZero, color = cmap(0), label=f'zero: {dataRawZero[0][queryIndex][0]}.{dataRawZero[0][queryIndex][1]}')
    plt.plot(x_pos, resultsOfQueryCard, color = cmap(10), label=f'card: {dataRawZero[0][queryIndex][0]}.{dataRawZero[0][queryIndex][1]}')
    plt.plot(x_pos, resultsOfQuerySkipZero, color = cmap(16), label=f'skip: {dataRawZero[0][queryIndex][0]}.{dataRawZero[0][queryIndex][1]}')

    plt.title('Query execution time in function of timeout value')
    plt.xlabel('Timeout before phase two (ms)')
    plt.ylabel('Execution time (ms)')
    plt.xticks(x_pos, tickLabels)
    plt.legend()

    figure = plt.gcf()
    figure.set_size_inches(16, 6)
    plt.savefig(f'{zeroCardDataRaw[0][queryIndex][0]}-{zeroCardDataRaw[0][queryIndex][1]}')

def plot_per_query_line_comparison_correct_add_skip():
  _, executionTimesSkip, _ = readSkipDataZeroMinOne()
  dataRawZero, executionTimesZero, tickLabels = readExperimentDataZeroMinOne("experiment-results/experiment-zero-card/", "zero")
  _, executionTimesCard, _ = readExperimentDataZeroMinOne("experiment-results/experiment-card-card-correct/", "card")
  numpyExecutionTimesZero = np.array(executionTimesZero)
  numpyExecutionTimesCard = np.array(executionTimesCard)
  cmap=get_cmap(21)

  for queryIndex,_ in enumerate(numpyExecutionTimesZero[0]):
    plt.clf()
    resultsOfQueryZero = numpyExecutionTimesZero[:,queryIndex]
    resultsOfQueryCard = numpyExecutionTimesCard[:,queryIndex]
    resultsOfQuerySkipZero = [executionTimesSkip[queryIndex]] * len(resultsOfQueryZero)

    x_pos = np.arange(len(resultsOfQueryZero))
    plt.plot(x_pos, resultsOfQueryZero, color = cmap(0), label=f'zero: {dataRawZero[0][queryIndex][0]}.{dataRawZero[0][queryIndex][1]}')
    plt.plot(x_pos, resultsOfQueryCard, color = cmap(10), label=f'card: {dataRawZero[0][queryIndex][0]}.{dataRawZero[0][queryIndex][1]}')
    plt.plot(x_pos, resultsOfQuerySkipZero, color = cmap(16), label=f'skip: {dataRawZero[0][queryIndex][0]}.{dataRawZero[0][queryIndex][1]}')

    plt.title('Query execution time in function of timeout value')
    plt.xlabel('Timeout before phase two (ms)')
    plt.ylabel('Execution time (ms)')
    plt.xticks(x_pos, tickLabels)
    plt.legend()

    figure = plt.gcf()
    figure.set_size_inches(16, 6)
    plt.savefig(f'{zeroCardDataRaw[0][queryIndex][0]}-{zeroCardDataRaw[0][queryIndex][1]}')

def plot_line_compare_no_extract_correct():
  _, executionTimesSkip, _ = readSkipDataZeroMinOne()
  dataRawZero, executionTimesNoExtract, tickLabels = readExperimentDataZeroMinOne("experiment-results/experiment-card-card-no-extract/", "card")
  _, executionTimesCard, _ = readExperimentDataZeroMinOne("experiment-results/experiment-card-card-correct/", "card")
  numpyExecutionTimesNoExtract = np.array(executionTimesNoExtract)
  numpyExecutionTimesCard = np.array(executionTimesCard)
  cmap=get_cmap(21)

  for queryIndex,_ in enumerate(numpyExecutionTimesNoExtract[0]):
    plt.clf()
    resultsOfQueryNoExtract = numpyExecutionTimesNoExtract[:,queryIndex]
    resultsOfQueryCard = numpyExecutionTimesCard[:,queryIndex]
    resultsOfQuerySkipZero = [executionTimesSkip[queryIndex]] * len(resultsOfQueryNoExtract)
    
    print(f'{dataRawZero[0][queryIndex][0]}.{dataRawZero[0][queryIndex][1]}')
    print(resultsOfQueryNoExtract)

    x_pos = np.arange(len(resultsOfQueryNoExtract))
    plt.plot(x_pos, resultsOfQueryNoExtract, color = cmap(0), label=f'card: counted: {dataRawZero[0][queryIndex][0]}.{dataRawZero[0][queryIndex][1]}')
    plt.plot(x_pos, resultsOfQueryCard, color = cmap(10), label=f'card: metadata {dataRawZero[0][queryIndex][0]}.{dataRawZero[0][queryIndex][1]}')
    plt.plot(x_pos, resultsOfQuerySkipZero, color = cmap(16), label=f'skip: {dataRawZero[0][queryIndex][0]}.{dataRawZero[0][queryIndex][1]}')

    plt.title('Query execution time in function of timeout value')
    plt.xlabel('Timeout before phase two (ms)')
    plt.ylabel('Execution time (ms)')
    plt.xticks(x_pos, tickLabels)
    plt.legend()

    figure = plt.gcf()
    figure.set_size_inches(16, 6)
    plt.savefig(f'{zeroCardDataRaw[0][queryIndex][0]}-{zeroCardDataRaw[0][queryIndex][1]}')


def plot_comparison():
  plt.clf()

  avg_times, barTitles, filename, legend_label = average_times_card_card, cardCardTitles, "avg_card_card", "card-card"
  x_pos = np.arange(len(avg_times))
  plt.bar(x_pos-.2, avg_times, width=0.4, color = cmap(0), label=legend_label)

  avg_times, barTitles, filename, legend_label = average_times_zero_card, zeroCardTitles, "avg_zero_card", "zero-card"
  plt.bar(x_pos+.2, avg_times, width=0.4, color = cmap(25), label=legend_label)

  plt.title('Average execution time per configuration')
  plt.xlabel('Timeout before phase two (ms)')
  plt.ylabel('Average execution time (ms)')
  plt.xticks(x_pos, barTitles)
  plt.legend()

  figure = plt.gcf()
  figure.set_size_inches(16, 6)
  plt.savefig("comparison")

def readTimeoutData(inputDir):
  inputFiles = []
  inputBarTitles=[]
  for i in [1,3,5,7,9,10,100,1000,2000,4000,6000]:
    inputFiles.append(f'{inputDir}{i}-timeout.csv')
    inputBarTitles.append(str(i))

  dataRaw=[]
  executionTimeData=[]
  for f in inputFiles:
    exTimes = []
    with open(f, 'r') as file:
      dataPerConfiguration=[]
      csvreader = csv.reader(file, delimiter=';')
      mustSkip=True
      for row in csvreader:
        if mustSkip:
          mustSkip=False
        else:
          dataPerConfiguration.append(row)
          exTimes.append(int(row[3]))
      dataRaw.append(dataPerConfiguration)
    executionTimeData.append(exTimes)
  return dataRaw, executionTimeData, inputBarTitles

def getQueryTitles(rawQueryDataNestedList):
  return list(np.unique(list(map(lambda row: row[0], rawQueryDataNestedList))))

def plot_per_query_line_comparison():
  params = {'legend.fontsize': '15',
          'axes.labelsize': '20',
          'axes.titlesize':'20',
          'xtick.labelsize':'20',
          'ytick.labelsize':'20'}
  pylab.rcParams.update(params)

  dataRawPerTimeout, executionTimesNoIndex, tickLabels = readTimeoutData("experiment-results/23.6.12/timeout/valueverloop-timeout-noindex-card/")
  queryTitles = getQueryTitles(dataRawPerTimeout[0])
  cmap=get_cmap(20)

  for qTitle in queryTitles:
    subqueriesPerTimeout = [[subQueryResult for subQueryResult in dataRawOfTimeout if subQueryResult[0]==qTitle] for dataRawOfTimeout in dataRawPerTimeout]

    plt.clf()
    for subQueryIndex,_ in enumerate(subqueriesPerTimeout[0]):
      subQueryResults = [timeoutResults[subQueryIndex][3] for timeoutResults in subqueriesPerTimeout]
      subQueryResults=list(map(int, subQueryResults))
      mini=min(subQueryResults)
      mini_index=[subQueryResults.index(mini)]

      x_pos = np.arange(len(subQueryResults))
      plt.plot(x_pos, subQueryResults, color = cmap(subQueryIndex*3), label=f'{qTitle}-{subQueryIndex}', linestyle=(subQueryIndex, (5,5)), linewidth=2)
      plt.plot([mini_index], [mini], "o", color = cmap(subQueryIndex*3), markersize=13)
      plt.tight_layout()

      # plt.title('Query execution time in function of timeout value')
      plt.xlabel('Time before join restart (ms)')
      plt.ylabel('Query execution time (ms)')
      plt.xticks(x_pos, tickLabels)
      plt.legend()

      figure = plt.gcf()
      figure.set_size_inches(16, 6)
    plt.savefig(f'/home/simon/Documents/Unief/Thesis/1-benchmarking/grapher.py/plots_14_jun/timeouts-noindex/{qTitle}')

def plot_improvement_Count():
  params = {'legend.fontsize': '15',
         'axes.labelsize': '20',
         'axes.titlesize':'20',
         'xtick.labelsize':'20',
         'ytick.labelsize':'20'}
  pylab.rcParams.update(params)

  plt.clf()
  baseCountImprovement=[['interactive-discover-1-0 ', 11072, 12704, -14.739884393063585], ['interactive-discover-1-1 ', 531, 792, -49.152542372881356], ['interactive-discover-1-2 ', 271, 411, -51.66051660516605], ['interactive-discover-1-3 ', 9366, 9478, -1.195814648729447], ['interactive-discover-1-4 ', 10268, 8671, 15.553174912349046], ['interactive-discover-2-0 ', 13630, 14420, -5.796038151137197], ['interactive-discover-2-1 ', 764, 877, -14.790575916230367], ['interactive-discover-2-2 ', 392, 414, -5.612244897959184], ['interactive-discover-2-3 ', 14467, 12515, 13.492776664132164], ['interactive-discover-2-4 ', 13660, 12397, 9.24597364568082], ['interactive-discover-5-0 ', 3915, 3723, 4.904214559386974], ['interactive-discover-5-1 ', 216, 166, 23.14814814814815], ['interactive-discover-5-2 ', 116, 105, 9.482758620689655], ['interactive-discover-5-3 ', 3396, 3240, 4.593639575971731], ['interactive-discover-5-4 ', 3424, 3359, 1.8983644859813082], ['interactive-discover-6-1 ', 423, 410, 3.0732860520094563], ['interactive-discover-6-2 ', 260, 248, 4.615384615384616], ['interactive-discover-6-4 ', 11980, 11440, 4.507512520868113], ['interactive-discover-7-1 ', 445, 450, -1.1235955056179776], ['interactive-discover-7-2 ', 293, 276, 5.802047781569966], ['interactive-discover-7-4 ', 18596, 9561, 48.585717358571735], ['interactive-discover-8-2 ', 12945, 15377, -18.787176516029355], ['interactive-short-5-0 ', 352, 232, 34.090909090909086], ['interactive-short-5-1 ', 326, 2, 99.38650306748467], ['interactive-short-5-2 ', 676, 207, 69.37869822485207], ['interactive-short-5-3 ', 279, 4, 98.56630824372759], ['interactive-short-5-4 ', 308, 302, 1.948051948051948]]
  indexCountImprovement=[['interactive-discover-1-0 ', 2670, 4217, -57.940074906367045], ['interactive-discover-1-1 ', 484, 520, -7.43801652892562], ['interactive-discover-1-2 ', 241, 280, -16.182572614107883], ['interactive-discover-1-3 ', 10843, 12217, -12.67176980540441], ['interactive-discover-1-4 ', 3366, 4518, -34.22459893048128], ['interactive-discover-2-0 ', 3198, 4107, -28.424015009380867], ['interactive-discover-2-1 ', 483, 697, -44.3064182194617], ['interactive-discover-2-2 ', 322, 394, -22.36024844720497], ['interactive-discover-2-3 ', 13997, 9891, 29.33485746945774], ['interactive-discover-2-4 ', 4297, 5181, -20.572492436583666], ['interactive-discover-5-0 ', 3781, 3992, -5.58053425019836], ['interactive-discover-5-1 ', 150, 213, -42.0], ['interactive-discover-5-2 ', 102, 113, -10.784313725490197], ['interactive-discover-5-3 ', 3160, 3239, -2.5], ['interactive-discover-5-4 ', 3334, 3401, -2.009598080383923], ['interactive-discover-6-1 ', 143, 132, 7.6923076923076925], ['interactive-discover-6-2 ', 111, 106, 4.504504504504505], ['interactive-discover-6-4 ', 8448, 8144, 3.5984848484848486], ['interactive-discover-7-1 ', 190, 156, 17.894736842105264], ['interactive-discover-7-2 ', 150, 110, 26.666666666666668], ['interactive-discover-7-4 ', 15044, 6640, 55.862802446157936], ['interactive-discover-8-2 ', 15371, 14653, 4.671133953548891], ['interactive-short-5-0 ', 434, 385, 11.29032258064516], ['interactive-short-5-1 ', 405, 5, 98.76543209876543], ['interactive-short-5-2 ', 782, 428, 45.26854219948849], ['interactive-short-5-3 ', 313, 11, 96.48562300319489], ['interactive-short-5-4 ', 372, 433, -16.397849462365592]]

  step=5
  for i in range(0, len(baseCountImprovement), step):
    baseCountImprovementSmol = baseCountImprovement[i:i+step]
    indexCountImprovementSmol = indexCountImprovement[i:i+step]

    queries = tuple([x[0].strip() for x in baseCountImprovementSmol])
    improvements = {
      "baseline+count": tuple([i[-1] for i in baseCountImprovementSmol]),
      "index+count": tuple([i[-1] for i in indexCountImprovementSmol])
    }

    x2 = np.arange(len(queries))  # the label locations
    width = 0.25  # the width of the bars
    multiplier = 0

    fig, ax = plt.subplots()
    print(str(queries).replace(",", "").replace("interactive-", "").replace("'", "")) # This prints data I used to put things in an online bar graph maker
    for attribute, measurement in improvements.items():
        print(str(measurement).strip('(').strip(')')) # This prints data I used to put things in an online bar graph maker
        offset = width * multiplier
        rects = ax.bar(x2 + offset, measurement, width, label=attribute)
        ax.bar_label(rects, padding=3)
        multiplier += 1

    # Add some text for labels, title and custom x-axis tick labels, etc.
    fig.subplots_adjust(bottom=.4)
    ax.set_ylabel('Length (mm)')
    ax.set_title('Penguin attributes by species')
    ax.set_xticks(x2 + width, queries, rotation=45)
    ax.legend(loc='upper left', ncols=3)
    ax.set_ylim(-160, 160)

    plt.savefig(f'hi-{i}')

def plot_improvement_Index():
  plt.clf()
  baseIndexImprovement=[['interactive-discover-1-0 ', 11072, 2670, 75.88511560693641], ['interactive-discover-1-1 ', 531, 484, 8.851224105461393], ['interactive-discover-1-2 ', 271, 241, 11.07011070110701], ['interactive-discover-1-3 ', 9366, 10843, -15.76980568011958], ['interactive-discover-1-4 ', 10268, 3366, 67.21854304635761], ['interactive-discover-2-0 ', 13630, 3198, 76.53705062362435], ['interactive-discover-2-1 ', 764, 483, 36.78010471204188], ['interactive-discover-2-2 ', 392, 322, 17.857142857142858], ['interactive-discover-2-3 ', 14467, 13997, 3.248773069744937], ['interactive-discover-2-4 ', 13660, 4297, 68.54319180087847], ['interactive-discover-5-0 ', 3915, 3781, 3.422733077905492], ['interactive-discover-5-1 ', 216, 150, 30.555555555555557], ['interactive-discover-5-2 ', 116, 102, 12.068965517241379], ['interactive-discover-5-3 ', 3396, 3160, 6.9493521790341575], ['interactive-discover-5-4 ', 3424, 3334, 2.628504672897196], ['interactive-discover-6-1 ', 423, 143, 66.19385342789597], ['interactive-discover-6-2 ', 260, 111, 57.30769230769231], ['interactive-discover-6-4 ', 11980, 8448, 29.48247078464107], ['interactive-discover-7-1 ', 445, 190, 57.30337078651685], ['interactive-discover-7-2 ', 293, 150, 48.80546075085324], ['interactive-discover-7-4 ', 18596, 15044, 19.10088191008819], ['interactive-discover-8-2 ', 12945, 15371, -18.740826573966782], ['interactive-short-5-0 ', 352, 434, -23.295454545454543], ['interactive-short-5-1 ', 326, 405, -24.233128834355828], ['interactive-short-5-2 ', 676, 782, -15.680473372781064], ['interactive-short-5-3 ', 279, 313, -12.186379928315413], ['interactive-short-5-4 ', 308, 372, -20.77922077922078]]
  countIndexImprovement=[['interactive-discover-1-0 ', 12704, 4217, 66.80573047858942], ['interactive-discover-1-1 ', 792, 520, 34.34343434343434], ['interactive-discover-1-2 ', 411, 280, 31.873479318734795], ['interactive-discover-1-3 ', 9478, 12217, -28.898501793627347], ['interactive-discover-1-4 ', 8671, 4518, 47.895283127666936], ['interactive-discover-2-0 ', 14420, 4107, 71.51872399445215], ['interactive-discover-2-1 ', 877, 697, 20.524515393386544], ['interactive-discover-2-2 ', 414, 394, 4.830917874396135], ['interactive-discover-2-3 ', 12515, 9891, 20.9668397922493], ['interactive-discover-2-4 ', 12397, 5181, 58.20763087843833], ['interactive-discover-5-0 ', 3723, 3992, -7.225355895782972], ['interactive-discover-5-1 ', 166, 213, -28.313253012048197], ['interactive-discover-5-2 ', 105, 113, -7.6190476190476195], ['interactive-discover-5-3 ', 3240, 3239, 0.030864197530864196], ['interactive-discover-5-4 ', 3359, 3401, -1.2503721345638583], ['interactive-discover-6-1 ', 410, 132, 67.8048780487805], ['interactive-discover-6-2 ', 248, 106, 57.25806451612904], ['interactive-discover-6-4 ', 11440, 8144, 28.81118881118881], ['interactive-discover-7-1 ', 450, 156, 65.33333333333333], ['interactive-discover-7-2 ', 276, 110, 60.14492753623188], ['interactive-discover-7-4 ', 9561, 6640, 30.55119757347558], ['interactive-discover-8-2 ', 15377, 14653, 4.708330623658711], ['interactive-short-5-0 ', 232, 385, -65.94827586206897], ['interactive-short-5-1 ', 2, 5, -150.0], ['interactive-short-5-2 ', 207, 428, -106.7632850241546], ['interactive-short-5-3 ', 4, 11, -175.0], ['interactive-short-5-4 ', 302, 433, -43.377483443708606]]

  step=10
  for i in range(0, len(baseIndexImprovement), step):
    baseCountImprovementSmol = baseIndexImprovement[i:i+step]
    indexCountImprovementSmol = countIndexImprovement[i:i+step]

    queries = tuple([x[0].strip() for x in baseCountImprovementSmol])
    improvements = {
      "baseline+count": tuple([i[-1] for i in baseCountImprovementSmol]),
      "index+count": tuple([i[-1] for i in indexCountImprovementSmol])
    }

    x2 = np.arange(len(queries))  # the label locations
    width = 0.25  # the width of the bars
    multiplier = 0

    fig, ax = plt.subplots()
    print(str(queries).replace(",", "").replace("interactive-", "").replace("'", "").strip("(").strip(")")) # This prints data I used to put things in an online bar graph maker
    for attribute, measurement in improvements.items():
        print(str(measurement).strip('(').strip(')')) # This prints data I used to put things in an online bar graph maker
        offset = width * multiplier
        rects = ax.bar(x2 + offset, measurement, width, label=attribute)
        ax.bar_label(rects, padding=3)
        multiplier += 1

    # Add some text for labels, title and custom x-axis tick labels, etc.
    fig.subplots_adjust(bottom=.4)
    ax.set_ylabel('Length (mm)')
    ax.set_title('Penguin attributes by species')
    ax.set_xticks(x2 + width, queries, rotation=45)
    ax.legend(loc='upper left', ncols=3)
    ax.set_ylim(-160, 160)

    plt.savefig(f'hi-{i}')

plot_improvement_Index()