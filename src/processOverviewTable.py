import itertools
import numpy as np

# The functions in this file calculate useful metrics, it was made on the fly as metrics were needed during the process of writing.

table=[]
lines = open("/home/simon/Documents/Unief/Thesis/1-benchmarking/grapher.py/plots_14_jun/overviewTableButPythonReadable.txt").readlines()
for line in lines:
    lineStripped = line.strip('\n').split('&')
    integer_columns = list(map(lambda l: int(l.strip()), lineStripped[1:]))
    integer_columns.insert(0, lineStripped[0].strip("interactive-"), )
    table.append(integer_columns)

# Queries that aren't edge cases or outliers
representativeQueries=[f"discover-1-{i}" for i in range(0,5)]
representativeQueries+=[f"discover-2-{i}" for i in range(0,5)]
representativeQueries+=[f"discover-5-{i}" for i in range(0,5)]
representativeQueries+=[f"discover-6-{i}" for i in [1,2,4]]
representativeQueries+=[f"discover-7-{i}" for i in range(0,5)]

def countCasesWhereCardBaseIsBetter():
    casesCardBetter=[]
    amountCardBetter=0
    casesCardBetter10P=[]
    amountCardBetter10P=0
    for row in table:
        if row[1] > row[2]:
            amountCardBetter+=1
            casesCardBetter.append([row[0:3], row[1]-row[2]])
        if row[1]-row[2] >= row[1]/10:
            amountCardBetter10P+=1
            casesCardBetter10P.append([row[0:3], row[1]-row[2]])
    print(f'amountCardBetter {amountCardBetter} out of {len(table)}')
    print('Cases where Card is better:')
    for i in casesCardBetter:
        print(list(itertools.chain(i)))
    print(f'amountCardBetter10P {amountCardBetter10P} out of {len(table)}')
    print('Cases where Card is 10% better:')
    for i in casesCardBetter10P:
        print(list(itertools.chain(i)))

def compareIndexCardZero():
    casesCardBetter=[]
    amountCardBetter=0
    casesCardBetter10P=[]
    amountCardBetter10P=0
    casesEqual=[]
    amountEqual=0
    casesZeroBetter=[]
    amountZeroBetter=0
    casesZeroBetter10P=[]
    amountZeroBetter10P=0
    for row in table:
        if row[3] > row[4]:
            amountCardBetter+=1
            casesCardBetter.append([row[0],row[3],row[4],row[3]-row[4]])
        if row[3]-row[4] >= row[3]/10:
            amountCardBetter10P+=1
            casesCardBetter10P.append([row[0],row[3],row[4],row[3]-row[4]])
        if row[3]==row[4]:
            amountEqual+=1
            casesEqual.append([row[0], row[3], row[4]])
        if row[4]>row[3]:
            amountZeroBetter+=1
            casesZeroBetter.append([row[0],row[3],row[4],row[4]-row[3]])
        if row[4]-row[3] >= row[4]/10:
            amountZeroBetter10P+=1
            casesZeroBetter10P.append([row[0],row[3],row[4],row[4]-row[3]])
    print(f'amountCardBetter {amountCardBetter} out of {len(table)}')
    print('Cases where Card is better:')
    for i in casesCardBetter:
        print(list(itertools.chain(i)))
    print(f'amountCardBetter10P {amountCardBetter10P} out of {len(table)}')
    print('Cases where Card is 10% better:')
    for i in casesCardBetter10P:
        print(list(itertools.chain(i)))
    print(f'amountEqual {amountEqual} out of {len(table)}')
    print('Cases where Card is equal:')
    for i in casesEqual:
        print(list(itertools.chain(i)))
    print(f'amountZeroBetter {amountZeroBetter} out of {len(table)}')
    print('Cases where Zero is better:')
    for i in casesZeroBetter:
        print(list(itertools.chain(i)))
    print(f'amountZeroBetter10P {amountZeroBetter10P} out of {len(table)}')
    print('Cases where Zero is 10% better:')
    for i in casesZeroBetter10P:
        print(list(itertools.chain(i)))
def averageImprovement(baseIndex, newIndex):
    improvements = []
    for row in table:
        if row[0].strip() in representativeQueries:
            improvement = (row[baseIndex] - row[newIndex]) / row[baseIndex] * 100
            improvements.append([row[0], row[baseIndex], row[newIndex], improvement])
    averageImprovement=np.array([x[-1] for x in improvements])
    averageImprovement=np.average(averageImprovement)
    return averageImprovement, improvements
def averageImprovementAll(baseIndex, newIndex):
    improvements = []
    for row in table:
        improvement = (row[baseIndex] - row[newIndex]) / row[baseIndex] * 100
        improvements.append([row[0], row[baseIndex], row[newIndex], improvement])
    averageImprovement=np.array([x[-1] for x in improvements])
    averageImprovement=np.average(averageImprovement)
    return averageImprovement, improvements

representativeQueriesSmall=representativeQueries.copy()
representativeQueriesSmall+=[f"discover-3-{i}" for i in range(0,5)]
representativeQueriesSmall+=[f"discover-4-{i}" for i in range(0,5)]
representativeQueriesSmall+=[f"short-4-{i}" for i in range(0,5)]
def averageImprovementSmall(baseIndex, newIndex):
    improvements = []
    for row in table:
        if row[0].strip() in representativeQueriesSmall:
            improvement = (row[baseIndex] - row[newIndex]) / row[baseIndex] * 100
            improvements.append([row[0], row[baseIndex], row[newIndex], improvement])
    averageImprovement=np.array([x[-1] for x in improvements])
    averageImprovement=np.average(averageImprovement)
    return averageImprovement, improvements

representativeQueriesBaseTimeout=representativeQueries.copy()
representativeQueriesBaseTimeout+=[f"short-3-{i}" for i in range(0,5)]
representativeQueriesBaseTimeout+=[f"short-7-{i}" for i in range(0,5)]
def averageImprovementBaseTimeout(baseIndex, newIndex):
    improvements = []
    for row in table:
        if row[0].strip() in representativeQueriesBaseTimeout:
            improvement = (row[baseIndex] - row[newIndex]) / row[baseIndex] * 100
            improvements.append([row[0], row[baseIndex], row[newIndex], improvement])
    averageImprovement=np.array([x[-1] for x in improvements])
    averageImprovement=np.average(averageImprovement)
    return averageImprovement, improvements

representativeQueriesWith8=representativeQueries.copy()
representativeQueriesWith8+=[f"discover-8-{i}" for i in range(0,5)]
def averageImprovementWith8(baseIndex, newIndex):
    improvements = []
    for row in table:
        if row[0].strip() in representativeQueriesWith8:
            improvement = (row[baseIndex] - row[newIndex]) / row[baseIndex] * 100
            improvements.append([row[0], row[baseIndex], row[newIndex], improvement])
    averageImprovement=np.array([x[-1] for x in improvements])
    averageImprovement=np.average(averageImprovement)
    return averageImprovement, improvements

representativeQueriesAllCorrect=representativeQueries.copy()
representativeQueriesAllCorrect =[f"discover-1-{i}" for i in range(0,5)]
representativeQueriesAllCorrect+=[f"discover-2-{i}" for i in range(0,5)]
representativeQueriesAllCorrect+=[f"discover-3-{i}" for i in range(0,5)]
representativeQueriesAllCorrect+=[f"discover-4-{i}" for i in range(0,5)]
representativeQueriesAllCorrect+=[f"discover-5-{i}" for i in range(0,5)]
representativeQueriesAllCorrect+=[f"discover-6-{i}" for i in [1,2,4]]
representativeQueriesAllCorrect+=[f"discover-7-{i}" for i in [1,2,4]]
representativeQueriesAllCorrect+=[f"discover-8-{i}" for i in range(0,5)]
representativeQueriesAllCorrect+=[f"short-4-{i}" for i in range(0,5)]
def averageImprovementAllCorrect(baseIndex, newIndex):
    improvements = []
    for row in table:
        if row[0].strip() in representativeQueriesAllCorrect:
            improvement = (row[baseIndex] - row[newIndex]) / row[baseIndex] * 100
            improvements.append([row[0], row[baseIndex], row[newIndex], improvement])
    averageImprovement=np.array([x[-1] for x in improvements])
    averageImprovement=np.average(averageImprovement)
    return averageImprovement, improvements

representativeQueriesAllCorrectNotSmall=representativeQueries.copy()
representativeQueriesAllCorrectNotSmall+=["discover-8-0"]
representativeQueriesAllCorrectNotSmall+=["discover-8-1"]
representativeQueriesAllCorrectNotSmall+=["discover-8-2"]
representativeQueriesAllCorrectNotSmall+=["discover-8-3"]
representativeQueriesAllCorrectNotSmall+=["discover-8-4"]
def averageImprovementAllCorrectNotSmall(baseIndex, newIndex):
    improvements = []
    for row in table:
        if row[0].strip() in representativeQueriesAllCorrectNotSmall:
            improvement = (row[baseIndex] - row[newIndex]) / row[baseIndex] * 100
            improvements.append([row[0], row[baseIndex], row[newIndex], improvement])
    averageImprovement=np.array([x[-1] for x in improvements])
    averageImprovement=np.average(averageImprovement)
    return averageImprovement, improvements

allCorrectQueriesNot8 =[f"discover-1-{i}" for i in range(0,5)]
allCorrectQueriesNot8+=[f"discover-2-{i}" for i in range(0,5)]
allCorrectQueriesNot8+=[f"discover-3-{i}" for i in [0,1,3,4]]
allCorrectQueriesNot8+=[f"discover-4-{i}" for i in [0,1,3,4]]
allCorrectQueriesNot8+=[f"discover-5-{i}" for i in range(0,5)]
allCorrectQueriesNot8+=[f"discover-6-{i}" for i in [1,2,4]]
allCorrectQueriesNot8+=[f"discover-7-{i}" for i in range(0,5)]
# allCorrectQueriesNot8+=[f"discover-8-{i}" for i in range(0,5)]
allCorrectQueriesNot8+=[f"short-4-{i}" for i in range(0,5)]
def averageImprovementAllCorrectNot8(baseIndex, newIndex):
    improvements = []
    for row in table:
        if row[0].strip() in allCorrectQueriesNot8:
            improvement = (row[baseIndex] - row[newIndex]) / row[baseIndex] * 100
            improvements.append([row[0], row[baseIndex], row[newIndex], improvement])
    averageImprovement=np.array([x[-1] for x in improvements])
    averageImprovement=np.average(averageImprovement)
    return averageImprovement, improvements

def compare_BaseZero_IndexZero():
    print(f'averageImprovement: {averageImprovement(1, 3)[0]}')
    print(f'averageImprovementAll: {averageImprovementAll(1, 3)[0]}')
def compare_BaseZero_BaseCard():
    print(f'averageImprovement: {averageImprovement(1, 2)[0]}')
    print(f'averageImprovementAll: {averageImprovementAll(1, 2)[0]}')
def compare_BaseZero_IndexCard():
    print(f'averageImprovement: {averageImprovement(1, 4)[0]}')
    print(f'averageImprovementAllCorrect: {averageImprovementAllCorrect(1, 4)[0]}')
    print(f'averageImprovementAllCorrectNotSmall: {averageImprovementAllCorrectNotSmall(1, 4)[0]}')
def compare_BaseZero_Count():
    print(f'averageImprovement: {averageImprovement(1, 5)[0]}')
    print(f'averageImprovementAllCorrect: {averageImprovementAllCorrect(1, 5)[0]}')
    print(f'averageImprovementAllCorrectNotSmall: {averageImprovementAllCorrectNotSmall(1, 5)[0]}')
def compare_BaseCard_Count():
    print(f'averageImprovement: {averageImprovement(2, 5)[0]}')
    print(f'averageImprovementAll: {averageImprovementAll(2, 5)[0]}')
def compare_BaseZero_CountIndex():
    print(f'averageImprovement: {averageImprovement(1, 6)[0]}')
    print(f'averageImprovementAllCorrect: {averageImprovementAllCorrect(1, 6)[0]}')
    print(f'averageImprovementAllCorrectNotSmall: {averageImprovementAllCorrectNotSmall(1, 6)[0]}')
def compare_IndexZero_CountIndex():
    print(f'averageImprovement: {averageImprovement(3, 6)[0]}')
    print(f'averageImprovementAll: {averageImprovementAll(3, 6)[0]}')
def compare_IndexCard_CountIndex():
    print(f'averageImprovement: {averageImprovement(4, 6)[0]}')
    print(f'averageImprovementAll: {averageImprovementAll(4, 6)[0]}')
def compare_Count_CountIndex():
    print(f'averageImprovement: {averageImprovement(5, 6)[0]}')
    print(f'averageImprovementAll: {averageImprovementAll(5, 6)[0]}')

compare_BaseZero_IndexCard()
compare_BaseZero_Count()
compare_BaseZero_CountIndex()

print("----------------------------------------")
x=averageImprovement(1, 5)
print(sum([i[-1] for i in x[1]]))
[print(i) for i in x[1] if i[-1] > 0]
[print(i) for i in x[1] if i[-1] < 0]
print("----------------------------------------")
x=averageImprovement(4, 6)
print(sum([i[-1] for i in x[1]]))
[print(i) for i in x[1] if i[-1] > 0]
print()
[print(i) for i in x[1] if i[-1] < 0]

def countFirstPlaceFinishes():
    firstPlaceFinishes=[0,0,0,0,0,0]
    for row in table:
        firstPlaceAmount=min(row[1:])
        firstPlaceFinishes[row.index(firstPlaceAmount)-1]+=1
    print(firstPlaceFinishes)

def countFirstPlaceFinishesFilter():
    firstPlaceFinishes=[0,0,0,0,0,0]
    for row in table:
        if row[0].strip() in representativeQueries:
            print(row)
            firstPlaceAmount=min(row[1:])
            firstPlaceFinishes[row.index(firstPlaceAmount)-1]+=1
    print(f'firstPlaceFinishes: {firstPlaceFinishes}')
countFirstPlaceFinishesFilter()

def getTimeouts():
    timeoutTable=[]
    lines = open("/home/simon/Documents/Unief/Thesis/1-benchmarking/grapher.py/plots_14_jun/idealTimeoutsTablePython.txt").readlines()
    for line in lines:
        lineStripped = line.strip('\n').split('&')
        if lineStripped[0] in [i[0] for i in table]:
            integer_columns = list(map(lambda l: int(l.strip()), lineStripped[1:]))
            integer_columns.insert(0, lineStripped[0], )
            timeoutTable.append(integer_columns)

    amountBigger=[]
    amountSmaller=[]
    for ind,el in enumerate(timeoutTable):
        if el[1] > table[ind][5]:
            amountBigger.append([el[0], table[ind][0], el[1], table[ind][5]])
        if el[1] < table[ind][5]:
            amountSmaller.append([el[0], table[ind][0], el[1], table[ind][5]])
    print("amountSmaller count:", len(amountSmaller))
    [print(i) for i in amountSmaller]
    print("amountBigger count:", len(amountBigger))
    [print(i) for i in amountBigger]
    amountBigger=[]
    amountSmaller=[]
    for ind,el in enumerate(timeoutTable):
        if el[2] > table[ind][6]:
            amountBigger.append([el[0], table[ind][0], el[2], table[ind][6]])
        if el[2] < table[ind][6]:
            amountSmaller.append([el[0], table[ind][0], el[2], table[ind][6]])
    print("amountSmaller count+index:", len(amountSmaller))
    [print(i) for i in amountSmaller]
    print("amountBigger count+index:", len(amountBigger))
    [print(i) for i in amountBigger]

compare_BaseZero_IndexCard()
compare_BaseZero_Count()
compare_BaseZero_CountIndex()
x=averageImprovementAll(1, 2)
[print(i) for i in x[1] if i[-1] > 0]