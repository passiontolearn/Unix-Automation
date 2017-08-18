#!/usr/bin/python
import os
import sys
import time
from datetime import timedelta

def timeFindFile(file_path):
	#print "timeFindFile({0}) called..\n".format(file_path)
	while not os.path.exists(file_path):
		time.sleep(0.01)

if __name__ == "__main__":
	if len(sys.argv) != 2 :
		print "Usage: python " + sys.argv[0] + " <FILE_TO_FIND>"
		print("\nNote: this program simply times how long it took to find the file...\n"
			+ "and will continue until it succeeds! :)")
		sys.exit (1)
	
	fileName = sys.argv[1]
	startTime = time.time();
	timeFindFile(fileName)

	totalTime = time.time() - startTime
	totalTime = str( timedelta(seconds=totalTime) )		# Thanks to http://stackoverflow.com/a/27793118
	print "Took {0} seconds to run ".format(totalTime)
