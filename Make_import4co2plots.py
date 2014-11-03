#!/usr/bin/python

####################
#  Diatom Portal Script to create urls to col2plots for clusters from Pearson - Ward method
####################

def main():

	#co2_files = glob.glob(os.path.join("co2plot_*"))

	OUT = open('bicluster.ward.co2plot.tsv', 'wb')
	OUT.write('%s\t%s\t%s\t%s\t%s\t%s\n' % ('cluster', 'url_co2plot_all', 'url_co2plot_stdst', 'url_co2plot_trans', 'url_conds', 'url_dendro'))

	for i in range(1,580):

		clusnname = 'cluster_%04d' % i

		url_co2plot_all = 'data-files/hc.Pearson.Ward.nonimputed.colsdnorm/co2plots/co2plot_%d_all.png' % i
		url_co2plot_stdst = 'data-files/hc.Pearson.Ward.nonimputed.colsdnorm/co2plots/co2plot_%d_stdst.png' % i
		url_co2plot_trans = 'data-files/hc.Pearson.Ward.nonimputed.colsdnorm/co2plots/co2plot_%d_trans.png' % i

		url_conds = 'data-files/hc.Pearson.Ward.nonimputed.colsdnorm/condplots/condplot_%d.png' % i
		url_dendro = 'data-files/hc.Pearson.Ward.nonimputed.colsdnorm/dendro/dendro.%d.png' % i

		OUT.write('%s\t%s\t%s\t%s\t%s\t%s\n' % (clusnname, url_co2plot_all, url_co2plot_stdst, url_co2plot_trans, url_conds, url_dendro))

	OUT.close()

if __name__ == '__main__':
	main()



