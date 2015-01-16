# -*- coding: utf-8 -*-
"""
PyTransitionMatrix script 1.0
16.01.2015

Simple script for creating transition matrix from csv file.

Up-to-date version is available on github.org/Kilexus/PyTransitionMatrix
Or you can email me: a.v.knorre@gmail.com

USAGE:
0. Make sure you have Python 2.* installed.
1. Place script in the directory where your csv file is situated.
2. CSV file should be named "data.csv" and values inside the file should be separated with ";" (no quotes).
3. Run the script. 

According to default settings, your input file should contain agents (who will be seen in transition matrix as a number in cells)
in the first column, years (according to which the fact of transition is calculated) in the second column, and nodes (which are
represented by columns and rows in transition matrix) in the third.
Tested only for English data.

"""

import csv
from operator import itemgetter

#Defining columns in input file to extract data
nodes=2
years=1
agents=0

delimiter=';' #Change if you want use another delimiter in input and output csv files
input_file="./data.csv"
save_to="./transitions_matrix.csv"
log_file="./transitions_log.txt"


#Reading input data
with open(input_file, 'r') as csv_con:
    reader = csv.reader(csv_con, delimiter=delimiter)
    data = list(reader)

#Sorting data    
data = sorted(data, key=itemgetter(years), reverse=False)
data = sorted(data, key=itemgetter(agents), reverse=False)


#Creating headers list, which will be column and row titles
header_list=["#FROM/TO"]
for i in data:
    if str(i[nodes])=="":
        i[nodes]="unknown journal"        
    if i[nodes] not in header_list:
        header_list.append(i[nodes])
header_list.sort()

#Creating matrix filled with zeroes
matrix = [0] * len(header_list)
for i in range(len(header_list)):
    matrix[i] = [0] * len(header_list)    


#Counting transitions
prev_row = [0,0,0,0,0]
log=""
for row in data:
    if row[agents]==prev_row[agents]: #Here you can specify other conditions to register transition
        old=str(prev_row[nodes])
        new=str(row[nodes])
        log=log + row[agents]+" goes from "+ prev_row[nodes] +" in "+prev_row[years]+" to "+ row[nodes] +" in "+ row[years] +"\n"
        matrix[header_list.index(old)][header_list.index(new)]+=1
    prev_row=row

#Filling our matrix with names of nodes
c=0
for i in header_list:
    matrix[0][c] = str(i)
    matrix[c][0] = str(i)
    c+=1    
 
 
#Saving matrix and log file
with open(save_to, "wb") as f:
    writer = csv.writer(f, delimiter=delimiter)
    writer.writerows(matrix) 
  
with open(log_file, 'w') as writer:
    writer.write(log)
    
print "Successfully finished."
