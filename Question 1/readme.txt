the python file process.py contains the python script for the data processing task, it takes in dataset1.csv and 
dataset2.csv and outputs processed.csv with the columns first_name, last_name, price and above_100

the python file can be scheduled using corn by the following steps: 

1. crontab -e 
(to edit the crontab file)

2. append the following line to the end of the file 
0 13 * * * cd Desktop && python3 process.py 
(where cd Desktop is the location of the files and output) 

3. python3 might not be recognised, so we can find the path of python3 interpreter using the command
where is python3
