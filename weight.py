# -*- coding: utf-8 -*-
"""
Created on Mon Mar 18 11:23:40 2019

@author: VWA08VG
"""

"""

I want to use python script to creat a curve which can record the daily 
weight.

"""

import matplotlib
import matplotlib.pyplot as plt
import numpy as np

# set size of new figure window
plt.figure(figsize = (20,14.14))
# create new axes 
ax = plt.gca()
ax.set_visible(True)
# let right and top spine dispear 
ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)

my_y_ticks = np.arange(49, 53.25, 0.25)
my_x_ticks = np.arange(0, 14, 1)
plt.xticks(my_x_ticks)
plt.yticks(my_y_ticks)
ax.set_ylim(49, 53)

plt.xlabel("Date", size = 16)
plt.ylabel("Weight", size = 16)
plt.grid()