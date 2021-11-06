import pandas as pd
import matplotlib.pyplot as plt
import sys

a = pd.read_csv('Data.csv')

a['Presentees'].plot(kind='hist')
plt.show()