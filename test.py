import pandas as pd
from pandas import Series, DataFrame

with  open('lastscore.txt', 'r') as f:
   data= f.read().splitlines() 
with  open('time.txt', 'r', encoding='UTF-8') as f:
   data2= f.read().splitlines() 
kosuu= len(data)
data3 = pd.DataFrame({'SCORE':["0","0","0","0","0","0","0","0","0","0",],'TIME':["0","0","0","0","0","0","0","0","0","0",]},columns=['SCORE','TIME'])
for i in range(kosuu):
  i=int(i)
  row = pd.DataFrame([[data[i],data2[i]]], columns=data3.columns)
  data3 = data3.append(row, ignore_index=True)
  data3[-2:]
data_frame3 = DataFrame(data3)
data3['SCORE']=pd.to_numeric(data3['SCORE'])
data4=data3.sort_values(['SCORE'],ascending=False)

print(data4)

