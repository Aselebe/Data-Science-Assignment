# -*- coding: utf-8 -*-
"""
Created on Tue Oct 18 11:57:02 2022

@author: dell
"""
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

x = np.linspace(-2.0 * np.pi, 2.0 * np.pi, 1000)
sample1 = np.random.normal(-1.0, 1.0, 10000)
sample2 = np.random.normal(1.0, 0.5, 10000)
sample3 = np.random.normal(0.0, 1.5, 10000)
sample4 = np.random.normal(-0.2, 2.0, 10000)
# join in an iterable list
data = [sample1, sample2, sample3, sample4]
plt.figure()
# adjust space between plots
plt.subplots_adjust(hspace=0.4, wspace=0.4)
# loop over list of samples
for i in range(4):
    plt.subplot(2, 2, i+1) # subplot count starts at 1
    plt.xlim(-4.0, 4.0)
    plt.ylim(0.0, 750.0)
    plt.hist(data[i], bins=50)
    plt.xlabel("Sample "+str(i+1))
    plt.ylabel("N")
    plt.show()
