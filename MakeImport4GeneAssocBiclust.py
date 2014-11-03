#!/usr/bin/python

#################################
#  Diatom Import Script for creating gene mappings to biclusters (for Import into Diatom Portal)
#  Author:  Micheleen Harris
#################################

import csv

def main():

	gene2biclust = {}

	lncnt = 1

	with open('cluster.members.genes.txt', 'rb') as f:
		for line in f:

			line.rstrip()

			linespl = line.split(' ')

			members = linespl[1:(len(linespl)-1)] # Remove first element

			for member in members:
				if not member in gene2biclust:
					clusts = []
					clusts.append('bicluster_%04d' % lncnt)
					gene2biclust[member] = clusts
				else:
					clusts = gene2biclust[member]
					clusts.append('bicluster_%04d' % lncnt)
					gene2biclust[member] = clusts

			lncnt+=1

	f.close()

	OUT = open('bicluster_members4genepage.tsv', 'wb')
	OUT.write('%s\t%s\n' % ('gene', 'biclusters'))

	print(len(gene2biclust))

	for member in gene2biclust:

		clusts = gene2biclust[member]

		cluststr = ":".join(clusts)

		OUT.write('%s\t%s\n' % (member, cluststr))

	OUT.close()

if __name__ == '__main__':
	main()