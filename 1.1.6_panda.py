#1.1.16 Pandas
#
#
#Pandas is short for Panel Data
#Do not import like this "from pandas import *"
#
import pandas as pd 

with open('lecz-urban-rural-population-land-area-estimates-v2-csv/lecz-urban-rural-population-land-area-estimates_codebook.csv','rU') as inputFile:
    inputReader = csv.reader(inputFile)
    for line in inputReader:
        print len(line)