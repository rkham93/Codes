import pandas as pd
import goslate
languages=[]
file=pd.read_csv('filename.csv')
df=pd.DataFrame(file)
gs = goslate.Goslate()
text='hello world'
for line in range(len(pd)):
  
  translatedText = gs.translate(text,'fr')
  print(translatedText)
