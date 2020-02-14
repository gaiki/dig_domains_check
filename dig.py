import subprocess
import re
import time

dane = open('lista.txt', 'r').readlines()

for i in range (len(dane)):
	dsource = (dane[i])
	domena = dsource[:-1]
	
	digspeak = subprocess.check_output (['dig', domena, 'a']).decode('utf-8')
	check = re.search(r'ANSWER: 0', str(digspeak))
	if check == None:
		print('jest ' + domena)
	else:
		print('nie ma ' + domena)
	time.sleep(1)