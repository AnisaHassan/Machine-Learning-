# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
from mpl_toolkits.mplot3d import Axes3D
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt # plotting
import numpy as np # linear algebra
import os # accessing directory structure
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import matplotlib.image as imp


images = []
for dirname, _, filenames in os.walk('C:/Users/Anisa/OneDrive/Desktop/MachineLearningEksempel/B'):
    for filename in filenames:
        print(os.path.join(dirname, filename))
        im = imp.imread(os.path.join(dirname, filename))
        images.append(im)
        #plt.imshow(im)
        
        
plt.imshow(images[22])
        
    