# Ojbective
Create a GUI program from the ground up that can be used to analyze log files. There are existing solutions readily available for this purpose; however, as project for the purpoose challenging myself and creating a solution to address every need I have decided to create my own solution.

## Current Objective
1) ~~Open File~~
2) ~~Take A Single Line~~
3) Take The Next Word(s) Between The Given Parameters

## TODOS:
1) Because there is no (hasNext) function in Python like in Java, there must be a way to
check how many lines there are.
    1) Fixed! Import File, Open File, `saidFile.readlines()`, length of the array is the length of the file. 

Example:

`file = "C:\\Users\\USER\\Desktop\\example.txt"`  
`f = open(file, "r")`  
`f_list = f.readlines()`  
`print(len(f_list))`

* Selecting OBJECTS can be done in a cyclical manner. Parameters can be given for every column and the program
can just cycle through the parameters until the end of the file.
