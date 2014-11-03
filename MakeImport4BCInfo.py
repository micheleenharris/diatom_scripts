#!/usr/bin/python

###################################
#  Diatom Portal Import Function for importing cluster score and residual from bicluster.summary.con.tsv
#  Author: Micheleen Harris
###################################

import csv

def main():

	#co2_files = glob.glob(os.path.join("co2plot_*"))

	bc2info = {}

	with open('bicluster.summary.con.tsv', 'rb') as f:
		for line in csv.DictReader(f, dialect='excel-tab'):
			bc = line['bicluster']
			score = line['score']
			resid = line['resid']
			a = [score,resid]
			bc2info = a

	f.close()

	OUT = open('bicluster.score.resid.tsv', 'wb')
	OUT.write('%s\t%s\n' % ('bicluster', 'sco'))

	for i in range(1,401):

		clusnname = 'cluster_%04d' % i
		members = clusnum2mems[i]

		OUT.write('%s\t%s\n' % (clusnname, members))

	OUT.close()

if __name__ == '__main__':
	main()