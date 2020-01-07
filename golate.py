import pandas as pd
import goslate
languages=[]
file=pd.read_csv('filename.csv')
df=pd.DataFrame(file)
text='hello world'
gs = goslate.Goslate()
translatedText = gs.translate(text,'fr')
print(translatedText)
