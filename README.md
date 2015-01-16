# PyTMC

Simple script for creating transition matrix for network analysis from csv file. 

USAGE:
0. Make sure you have Python 2.* installed.

1. Place script in the directory where your csv file is situated (say, C:\Users\Alexey\Desktop\Folder_with_data).

2. CSV file should be named "data.csv" and values inside the file should be separated with ";" (no quotes).

3. Run the script (for example, using command line: Start -> Run.. -> Type "cmd" -> in the cmd type "cd C:\Users\Alexey\Desktop\Folder_with_data" and then "python pytmc.py"). 

According to default settings, your input file should contain agents (who will be seen in transition matrix as a number in cells) in the first column, years (according to which the fact of transition is calculated) in the second column, and nodes (which are represented by columns and rows in transition matrix) in the third.
Tested only for English language.
