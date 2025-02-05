import pandas as pd
a=[1,2,3]
my=pd.Series(a,index=['x','y','z'])
print(my["y"])