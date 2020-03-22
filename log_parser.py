import os
import re

#path = '/Users/asamra/dev/PythonFundamentals.Labs.RSVPAgentProcessingLogParser/data/rsvp_agent_log.dat'
path = './data/rsvp_agent_log.dat'


'''
pattern = re.compile(r'WARNING')

with open(path, 'r') as f:
	contents = f.read()
	
	matches = pattern.finditer(contents)

	for match in matches:
		print(match)
 
This isn't working. 
 '''


with open(path, 'r') as f:
	#contents = f.read()
	for line in f:
		match = re.search("WARNING", line)
		if match != None:
			print(line)



#test
#print(re.match("c", "abcdef"))
#print(re.search("c", "abcdef"))

