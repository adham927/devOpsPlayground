from datetime import datetime
import re
from collections import defaultdict

fileTransactions = defaultdict(dict)
examFile = open('C:/exam/exam.log' , 'r')
FMT = '%H:%M:%S.%f'
file_lines = examFile.readlines()
transRegex = r'transaction\s\d+'
timeRegex = r'\d+:\d+:\d+.\d+'
for line in file_lines:
    tranR = re.search(transRegex, line)
    ti = re.search(timeRegex, line)
    time_str = ti.group(0)
    time = datetime.strptime(time_str,FMT)

    if tranR is not None:
        ID = tranR.group(1)
        if 'begin' in line:
            fileTransactions[ID]['start'] = time
        if 'end' in line:
            fileTransactions[ID]['end'] = time

        if 'end' in fileTransactions[ID] and 'start' in fileTransactions[ID]:
            delta_time = fileTransactions[ID]['end'] - fileTransactions[ID]['start']
            fileTransactions[ID]['delta'] = delta_time.total_seconds()

total_time = 0
delta_count = 0
for ID, tData in fileTransactions.items():
    if 'delta' in tData:
        total_time += tData['delta']
        delta_count += 1

print((total_time / delta_count)*1000)


    # split_line = line.split()
    # if split_line[5] == 'transaction':
    #     id = split_line[6]
    #     startTime = datetime.strptime(split_line[1], FMT)
    #     for line in file_lines:
    #         split_line = line.split()
    #         if split_line[7] == 'id':
    #             endTime = datetime.strptime(split_line[1], FMT)
    #             min = (datetime.strptime(endTime) - datetime.strptime(startTime)).total_seconds()
    #             break
    #
    #
    #

#     tdelta = (datetime.strptime(spline[2], FMT) - datetime.strptime(spline[1], FMT)).total_seconds()
#     if tdelta < min:
#         min = tdelta
#         id = spline[3]
# print(id)




# count = 0
# for line in file_lines:
#     spline = line.split()
#     for word in spline:
#         if word == 'INFO':
#             count += 1
# print(count)

# infile = open('C:/Users/log.txt', 'r')
# FMT = '%H:%M:%S'
# count = 0
# sum = 0
# file_lines = infile.readlines()
# for line in file_lines:
#     count += 1
#     spline = line.split()
#     tdelta = (datetime.strptime(spline[2], FMT) - datetime.strptime(spline[1], FMT)).total_seconds()
#     print(tdelta)
#     sum = sum + int(tdelta)
# print(sum/count)

# examFile = open('C:/exam/exam.log' , 'r')
# firstLine = examFile.readline()
# print(firstLine)

# examFile = open('C:/exam/exam.log' , 'r')
# count_ERROR = 0
# file_lines = examFile.readlines()
# for line in file_lines:
#     splitLine = line.split( )
#     if splitLine[2] == 'ERROR':
#         count_ERROR += 1
# print(count_ERROR)

# examFile = open('C:/exam/exam.log' , 'r')
# count_transactions = 0
# file_lines = examFile.readlines()
# for line in file_lines:
#     splitLine = line.split('')
# print(splitLine)
    # if splitLine[5] == 'end':
    #     count_transactions += 1
# print(count_transactions)