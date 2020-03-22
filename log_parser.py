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
I know I shouldn't leave dead code behind but I need to ask Roberto why the above didn't work.
 '''


with open(path, 'r') as f:
	#contents = f.read()
	for line in f:
		match = re.search("WARNING", line)
		if match != None:
			print(line[0:14] + ' -- ' + line[45:73] + ' -- ' + line[77:] )



#test
#print(re.match("c", "abcdef"))
#print(re.search("c", "abcdef"))

