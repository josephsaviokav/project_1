import pandas as pd 
import matplotlib.pyplot as plt
k=pd.read_csv("data.csv")
k['Calories'].plot(kind='hist')
plt.show()