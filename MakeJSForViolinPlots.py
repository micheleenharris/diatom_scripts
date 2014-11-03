#!/usr/bin/python

####################################
#  Script to make data javascript for d3violinplots
#  Author:  Micheleen Harris
###################################

import glob
import os
import codecs
import numpy

def main():

	clustfiles = glob.glob("*.diffs")

	clust2genes = {}

	
	for clustf in clustfiles:
		clust = os.path.basename(clustf).split('.')[1]
		geneHeaders = []
		
		f = open(clustf, 'r')

		lines = f.readlines()
		conds = [line.split()[0] for line in lines[1:]]
		dataMatrix = [line.split()[1:] for line in lines[1:]]
		headers = lines[0].strip().replace('\"','').split()

		f.close()

		OUT = open('violin_data/cluster_%04d.js' % int(clust), 'wb')
		allratios = []

		for i in range(0,len(dataMatrix)):
			ratios = dataMatrix[i] #  Row corresponds to ratios for a gene
			ratios = [value for value in ratios if not 'NaN' in value]
			ostr = "\n["+",".join(ratios)+"]"
			allratios.append(ostr)

		bigostr = "["+",".join(allratios)+"]"

		OUT.write("var results = " + bigostr)
		OUT.write("\n\nvar conditions = " + "[%s]" % ",".join(conds))

		OUT.close()

if __name__ == '__main__':
	main()










