import matplotlib
matplotlib.use('Agg')

import pandas as pd
import random
import matplotlib.pyplot as plt
import seaborn as sns

import numpy as np 




# def permutation(statistic, error):


def mad(arr):
    """ Median Absolute Deviation: a "Robust" version of standard deviation.
        Indices variabililty of the sample.
        https://en.wikipedia.org/wiki/Median_absolute_deviation 
        http://stackoverflow.com/questions/8930370/where-can-i-find-mad-mean-absolute-deviation-in-scipy
    """
    arr = np.ma.array(arr).compressed() # should be faster to not use masked arrays.
    med = np.median(arr)
    return np.median(np.abs(arr - med))


if __name__ == "__main__":
	df = pd.read_csv('./vehicles.csv')
	print df.columns
	sns_plot = sns.lmplot(df.columns[0], df.columns[1], data=df, fit_reg=False)

	sns_plot.axes[0,0].set_ylim(0,)
	sns_plot.axes[0,0].set_xlim(0,)

	sns_plot.savefig("scaterplot.png",bbox_inches='tight')
	sns_plot.savefig("scaterplot.pdf",bbox_inches='tight')

	data1 = df.values.T[0][:79]
	data2 = df.values.T[1][:79]
	
	print ("Current Mean: %f")%(np.mean(data1))
	print ("Current Median: %f")%(np.median(data1))
	print ("Current Var: %f")%(np.var(data1))
	print ("Current std: %f")%(np.std(data1))
	print ("Current MAD: %f")%(mad(data1))

	print ("New Mean: %f")%(np.mean(data2))
	print ("New Median: %f")%(np.median(data2))
	print ("New Var: %f")%(np.var(data2))
	print ("New std: %f")%(np.std(data2))
	print ("New MAD: %f")%(mad(data2))

	plt.clf()
	sns_plot2 = sns.distplot(data1, bins=20, kde=False, rug=True).get_figure()

	axes = plt.gca()
	axes.set_xlabel('Millons of pounds in sales') 
	axes.set_ylabel('Sales count')

	sns_plot2.savefig("histogram.png",bbox_inches='tight')
	sns_plot2.savefig("histogram.pdf",bbox_inches='tight')

	plt.clf()
	sns_plot2 = sns.distplot(data2, bins=20, kde=False, rug=True).get_figure()
	
	axes = plt.gca()
	axes.set_xlabel('Millons of pounds in sales') 
	axes.set_ylabel('Sales count')

	sns_plot2.savefig("histogram1.png",bbox_inches='tight')
	sns_plot2.savefig("histogram.pdf",bbox_inches='tight')