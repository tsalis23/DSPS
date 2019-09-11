#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 10 18:16:38 2019

@author: bensalis
''''''


from __future__ import print_function
__author__= 'fbb'
import pylab as pl
# this package sets up pretty plots
from scipy.optimize import curve_fit, minimize
import seaborn
import numpy as np
seaborn.set_style("darkgrid")

mymean = 100
df = mymean
'''
#distributions = ['pois', 'gaus', 'chisq', 'cauchy', 'lnorm', 'binomial']
distributions = ['chisq']



np.random.seed(456)
md = {}
# md is an empty disctionary; 
# if you are not familiar with python dictionaries see https://www.pythonforbeginners.com/dictionary/how-to-use-dictionaries-in-python
md['chisq'] = np.random.chisquare(mymean, size=100)
# md now is a dictionary with one object: an array by the key 'chisq'
pl.hist(md['chisq'], bins = 30)
pl.ylabel('N')
pl.xlabel('x');
print ("Chisq mean: %.2f, standard deviation: %.2f"%(md['chisq'].mean(), md['chisq'].std()))

mysize = (2000 / (np.array(range(1, 100)))).astype(int)
#mysize = 1000 / (np.array(range(1, 100) + [10]))
#mysize = (np.random.rand(100) * 1000).astype(int)
print ("shape of the 'size' list that contains the size of each distribution", mysize.shape)
pl.plot(mysize, '.')
pl.xlabel("index")
pl.ylabel("size of the array")

md['chisq'] = {} 

#and do it in a for loop. not pythonic, but easily readable

for n in mysize:
    md['chisq'][n] = np.random.chisquare(df, size = n)
    
# save the means for plotting later    

md['chisq']['means'] = {}
axchisq_mu_n = pl.figure(figsize=(10,6)).add_subplot(111)

for nn in md['chisq']:
    if not type(nn) == str:
        md['chisq']['means'][nn] = md['chisq'][nn].mean()
        #and plot it
        axchisq_mu_n.plot(nn, md['chisq']['means'][nn], 'o')
        axchisq_mu_n.set_xlabel('sample size', fontsize=18)
        axchisq_mu_n.set_ylabel('sample mean', fontsize=18)
        axchisq_mu_n.set_title('Chi squared', fontsize=18)
        axchisq_mu_n.plot([min(mysize), max(mysize)], [df, df], 'k')
axchisq_mu_n.text(axchisq_mu_n.get_xlim()[1] * .6, 100, "expected mean", 
                  va="bottom", fontsize=20)


allmeans = list(md['chisq']['means'].values())

pl.figure(figsize=(10, 10))
pl.hist(allmeans,bins=30)
pl.xlabel('sample mean', fontsize = 18)
pl.ylabel('N', fontsize = 18)




distributions = ['pois']

np.random.seed(456)
md = {}
# md is an empty disctionary; 
# if you are not familiar with python dictionaries see https://www.pythonforbeginners.com/dictionary/how-to-use-dictionaries-in-python
md['pois'] = np.random.poisson(1, size=100)
# md now is a dictionary with one object: an array by the key 'chisq'
pl.hist(md['pois'], bins = 30)
pl.ylabel('N')
pl.xlabel('x');
print ("Pois mean: %.2f, standard deviation: %.2f"%(md['pois'].mean(), md['pois'].std()))

mysize = (2000 / (np.array(range(1, 100)))).astype(int)
# mysize = 1000 / (np.array(range(1, 100) + [10]))
# mysize = (np.random.rand(100) * 1000).astype(int)
print ("shape of the 'size' list that contains the size of each distribution", mysize.shape)
pl.plot(mysize, '.')
pl.xlabel("index")
pl.ylabel("size of the array")

md['pois'] = {} 

#and do it in a for loop. not pythonic, but easily readable

for n in mysize:
    md['pois'][n] = np.random.poisson(df, size = n)
    
# save the means for plotting later    

md['pois']['means'] = {}
apois_mu_n = pl.figure(figsize=(10,6)).add_subplot(111)

for nn in md['pois']:
    if not type(nn) == str:
        md['pois']['means'][nn] = md['pois'][nn].mean()
        #and plot it
        apois_mu_n.plot(nn, md['pois']['means'][nn], 'o')
        apois_mu_n.set_xlabel('sample size', fontsize=18)
        apois_mu_n.set_ylabel('sample mean', fontsize=18)
        apois_mu_n.set_title('pois', fontsize=18)
        apois_mu_n.plot([min(mysize), max(mysize)], [df, df], 'k')
apois_mu_n.text(apois_mu_n.get_xlim()[1] * .6, 100, "expected mean", 
                  va="bottom", fontsize=20)

distributions = ['gaus']

np.random.seed(456)
md = {}
# md is an empty disctionary; 
# if you are not familiar with python dictionaries see https://www.pythonforbeginners.com/dictionary/how-to-use-dictionaries-in-python
md['gaus'] = np.random.normal(mymean, size=100)
# md now is a dictionary with one object: an array by the key 'chisq'
pl.hist(md['gaus'], bins = 30)
pl.ylabel('N')
pl.xlabel('x');
print ("Gaus mean: %.2f, standard deviation: %.2f"%(md['gaus'].mean(), md['gaus'].std()))

mysize = (2000 / (np.array(range(1, 100)))).astype(int)
#mysize = 1000 / (np.array(range(1, 100) + [10]))
#mysize = (np.random.rand(100) * 1000).astype(int)
print ("shape of the 'size' list that contains the size of each distribution", mysize.shape)
pl.plot(mysize, '.')
pl.xlabel("index")
pl.ylabel("size of the array")

md['gaus'] = {} 

#and do it in a for loop. not pythonic, but easily readable

for n in mysize:
    md['gaus'][n] = np.random.normal(mymean, size = n)
    
# save the means for plotting later    

md['gaus']['means'] = {}
apois_mu_n = pl.figure(figsize=(10,6)).add_subplot(111)

for nn in md['gaus']:
    if not type(nn) == str:
        md['gaus']['means'][nn] = md['gaus'][nn].mean()
        #and plot it
        apois_mu_n.plot(nn, md['gaus']['means'][nn], 'o')
        apois_mu_n.set_xlabel('sample size', fontsize=18)
        apois_mu_n.set_ylabel('sample mean', fontsize=18)
        apois_mu_n.set_title('gaus', fontsize=18)
        apois_mu_n.plot([min(mysize), max(mysize)], [df, df], 'k')
apois_mu_n.text(apois_mu_n.get_xlim()[1] * .6, 100, "expected mean", 
                  va="bottom", fontsize=20)

allmeans = list(md['gaus']['means'].values())

pl.figure(figsize=(10, 10))
pl.hist(allmeans,bins=30)
pl.xlabel('sample mean', fontsize = 18)
pl.ylabel('N', fontsize = 18)

distributions = ['uniform']

np.random.seed(456)
md = {}
# md is an empty disctionary; 
# if you are not familiar with python dictionaries see https://www.pythonforbeginners.com/dictionary/how-to-use-dictionaries-in-python
md['uniform'] = np.random.uniform(low=0.0, high=456, size=None)
# md now is a dictionary with one object: an array by the key 'chisq'
pl.hist(md['uniform'], bins = 30)
pl.ylabel('N')
pl.xlabel('x');
print ("Uniform mean: %.2f, standard deviation: %.2f"%(md['uniform'].mean(), md['uniform'].std()))

mysize = (2000 / (np.array(range(1, 100)))).astype(int)
#mysize = 1000 / (np.array(range(1, 100) + [10]))
#mysize = (np.random.rand(100) * 1000).astype(int)
print ("shape of the 'size' list that contains the size of each distribution", mysize.shape)
pl.plot(mysize, '.')
pl.xlabel("index")
pl.ylabel("size of the array")

md['uniform'] = {} 

#and do it in a for loop. not pythonic, but easily readable

for n in mysize:
    md['uniform'][n] = np.random.uniform(mymean, size = n)
    
# save the means for plotting later    

md['uniform']['means'] = {}
apois_mu_n = pl.figure(figsize=(10,6)).add_subplot(111)

for nn in md['uniform']:
    if not type(nn) == str:
        md['uniform']['means'][nn] = md['uniform'][nn].mean()
        #and plot it
        apois_mu_n.plot(nn, md['uniform']['means'][nn], 'o')
        apois_mu_n.set_xlabel('sample size', fontsize=18)
        apois_mu_n.set_ylabel('sample mean', fontsize=18)
        apois_mu_n.set_title('uniform', fontsize=18)
        apois_mu_n.plot([min(mysize), max(mysize)], [df, df], 'k')
apois_mu_n.text(apois_mu_n.get_xlim()[1] * .6, 100, "expected mean", 
                  va="bottom", fontsize=20)

allmeans = list(md['uniform']['means'].values())

pl.figure(figsize=(10, 10))
pl.hist(allmeans,bins=30)
pl.xlabel('sample mean', fontsize = 18)
pl.ylabel('N', fontsize = 18)

