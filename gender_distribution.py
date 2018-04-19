#Thanks to FiveThiryEight data

import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
import numpy as np
gender = pd.read_csv("gender_distribution.csv",sep=',')

#print(gender.head())

#Show general trend of female in STEM ratio to men to median income levels.
data = np.column_stack((gender['ShareWomen'], gender['Median']))
x, y = data.T
plt.scatter(x,y)
plt.show()
'''
gender['ShareWomen'].plot.area()
plt.legend(loc='upper right')
plt.show()'''

