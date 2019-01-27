#!/usr/bin/python

import sys
import os


def searchFiles(path, file):
	for root, dirs, files in os.walk(path, topdown=False):
		for name in files:
			if file == name:
				print(os.path.join(root,name))



def searchDirs(path, subdirectory):
	for root, dirs, files in os.walk(path, topdown=False):
		for name in dirs:
			if subdirectory == name:
				print(os.path.join(root,name))

if len(sys.argv) > 2:
	if sys.argv[1] == "-f":
		searchFiles(sys.argv[2], sys.argv[3])
	if sys.argv[1] == "-d":
		searchDirs(sys.argv[2], sys.argv[3])
else:
	print("Uso: python " + os.path.basename(__file__) + " [-f|-d] path file/subdirectory")