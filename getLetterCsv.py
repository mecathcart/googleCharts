#!/usr/bin/python

# Script to create a CSV of frequencies.
#
# For example, get all the frequencies for words staring with 's' into s.csv:
#	python getLetterCsv.py ^s wikipedia_wordfreq.txt ngram_wordfreq.txt s.csv
#
# Author: 	Theresa Deering
# Date:		03-MAY-2012 : Initial version

import string, sys, os, random

# Gather the command line arguments
my_regex = sys.argv[1]
input_filename_1 = sys.argv[2]
input_filename_2 = sys.argv[3]
output_filename = sys.argv[4]

# Create a temp file of just the lines that match the regex in in_file_1
temp_filename_1 = ".temp" + str(random.random())
os.system("grep '" + my_regex + "' " + input_filename_1 + " > " + temp_filename_1)

# Same thing for in_file_2
temp_filename_2 = ".temp" + str(random.random())
os.system("grep '" + my_regex + "' " + input_filename_2 + " > " + temp_filename_2)

# Initalize an empty hashmap of words
word_map = {}

# Loop over all the lines in the first temp file and add them to a hashmap
f = open(temp_filename_1)
for line in f.readlines():
	# split the line up into (word, frequency) pairs
	[word, frequency] = line.split('\t')

	# Add the frequency to the hashmap and (for now) say it's never in in_fiLe_2
	word_map[word.strip()] = {'file1':frequency.strip(), 'file2':0}
f.close()

# Loop over all the lines in the second temp file and add them to the hashmap
f = open(temp_filename_2)
for line in f.readlines():
	# Split the line up into (word, frequency) pairs
	[word, frequency] = line.split('\t')

	# If this is a new word, say that it never occurred in in_file_1
	if (not word_map.has_key(word)):
		word_map[word.strip()] = {'file1':0}

	# Add the frequency to the hashmap
	word_map[word.strip()]['file2'] = frequency.strip()
f.close()

# Put all the words/frequencies into the output file
f = open(output_filename, 'w')
for key in word_map.iterkeys():
	f.write(key + "," + str(word_map[key]['file1']) + "," + str(word_map[key]['file2']) + "\n")

# Remove the temp files
os.system("rm " + temp_filename_1)
os.system("rm " + temp_filename_2)

