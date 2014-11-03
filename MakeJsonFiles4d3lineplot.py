#!/usr/bin/python

#######################################
#  Python script to make json files for clusters of gene members across all conditions for d3lineplot.html
######################################

import csv
import json
import numpy

def main():

    #  Utilizing RData ratios file (processed and made by ProcessRdata.R) read in ratios for a gene across all conditions

    genes2ratios = {}
    colHeaders = []
    with open('Tps.ratios.TMM.tab', 'rb') as f:
        headers = f.next().strip().replace('\"','').split()
        colHeaders = headers

        for line in f:
            data = line.strip().split()
            gene = data[0].replace('\"','')
            genes2ratios[gene] = data[1:]

    f.close()

    """
    #  Get cluster members
    clust2genes = {}
    with open('cluster_members.tsv', 'rb') as f:
        for line in csv.DictReader(f, dialect='excel-tab'):
            clust2genes[line['cluster']] = line['members'].split(';')

    f.close()
    """

    clust2genes = {}
    with(open('cluster.members.genes.txt', 'rb')) as f:
        for line in f:
            lnspl = line.rstrip().split()
            clust2genes[lnspl[0]] = lnspl[1:]

    f.close()

    #  For ea cluster make a json file with genes (members of a cluster), conditions, and ratios
    #  1.  For a cluster look up members
    #  2.  For a gene in the cluster get ratios
    #  3.  Make json string for ratios of a gene
    #  4.  Make json string for conditions (simply use colHeaders)
    #  5.  Json string for indices of genes (for now 1 - num conditions - easy - maybe can sort later)
    #  6.  So, for ea cluster will have a json file and an html file (must be a better way!)



    for clust in clust2genes:
        print(clust)
        clustnum = int(clust.replace('cluster_',''))
        jsonstr = '{'
        
        members = clust2genes[clust]
        jsonstr+='\n\"labels\": '+json.dumps(members) + ','
        alldata = [] # for ratios data for a gene

        memcnt = 1
        indices = []
        
        for mem in members:
            if mem in genes2ratios:
                data = genes2ratios[mem]
                #datanums = [float(x) if x != 'NA' else numpy.nan for x in data] # convert to float for sorting
                datanums = [float(x) if x != 'NA' else 10e6 for x in data]
                if memcnt == 1: # sort by first member
                    indices = sorted(range(len(datanums)),key=datanums.__getitem__)
                    #indices = [i[0] for i in sorted(range(len(datanums)),key=lambda x:datanums[x])]
                    #indices = sorted(range(len(datanums)),key=lambda x:datanums[x])
                    #indicesdata = sorted(range(len(data)),key=lambda x:data[x])
                    memcnt+=1
                    #datanums = [datanums[i] for i in indices]
                    #alldata.append([str(x) for x in datanums])
                    #continue

                #  Replace back the large number with NN

                datanums = [ datanums[i] for i in indices]
                datanums = ['NA' if x == 10e6 else x for x in datanums]
                #alldata.append(datanums)
                alldata.append([str(x) for x in datanums])


        jsonstr+='\n\"conditions\": '+ json.dumps([ colHeaders[i] for i in indices])+','
        jsonstr+='\n\"times\": ' + json.dumps([x for x in range(len(colHeaders))])+',' # could sort later
        jsonstr+='\n\"curves\": ' + json.dumps(alldata)+'}'

        OUT = open('lineplot_data/bicluster_%04d.json' % clustnum, 'wb')
        OUT.write(jsonstr)
        OUT.close()

if __name__ == '__main__':
    main()


