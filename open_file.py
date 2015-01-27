
#1.1.5 opening a file, making a calculation with a changed data type
#   then output to a dif csv (overwritten)
#start 1/26
#finished 1/26

import collections
population_dict=collections.defaultdict(int)

with open('lecz-urban-rural-population-land-area-estimates_continent-90m.csv', 'rU') as inputFile:
	header = next(inputFile) #first row is just headers for the code

	for line in inputFile:
		line = line.rstrip().split(',') #rstrip removes any beginning or srailing spaces
		line[5] = int(line[5])
		if line[1] == 'Total National Population':
			population_dict[line[0]] += line[5]
			

with open('national_population.csv', 'w') as outputFile:
	outputFile.write('continent,2010_population\n')

	for k, v in population_dict.iteritems():
		outputFile.write( k + ',' + str(v) + '\n')
