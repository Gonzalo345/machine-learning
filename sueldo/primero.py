import pandas as pd
import numpy as np
df=pd.read_csv('datos.csv')
df['Compra']=df['Compra'].str.replace(',','.').astype(float)
df['Venta']=df['Venta'].str.replace(',','.').astype(float)
df.rename(columns={'Sueldo ': 'Sueldo'}, inplace=True)
df['Sueldo']=df['Sueldo']
dolar=df.iloc[:,0:3]
dolar['Fecha']=pd.to_datetime(dolar['Fecha'], dayfirst=True)
dolar=dolar.set_index('Fecha')
dolar['DiaD']=dolar.index.day
dolar['Med']=((dolar['Compra']+dolar['Venta'])/2)
dolar['Med']=dolar['Med'].round(0)
dolar=dolar.groupby(dolar.index.to_period('M')).first()
sueldo=df.iloc[:,3:5]
sueldo.columns=['Fecha','Sueldo']
sueldo=sueldo.set_index('Fecha').dropna()
sueldo.index=pd.to_datetime(sueldo.index, dayfirst=True)
sueldo['DiaS']=sueldo.index.day
sueldo.index=sueldo.index.to_period('M')
df2=pd.concat([dolar,sueldo], axis=1)
df2=df2.groupby(df2.index).first().dropna()
df2['Real']=(df2['Sueldo']/df2['Med']).round(1)
df2['Sueldo']=df2['Sueldo'].astype(int)
df2['DiaS']=df2['DiaS'].astype(int)
df2['Hoy']=(df2['Real']*1250).round(1).astype(int)
df2['Sueldo']=(df2['Sueldo']).astype(int)
df2.to_csv('datos2.csv')
