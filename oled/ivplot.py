import numpy as np
import pandas as pd

import matplotlib.pyplot as plt
plt.rcParams['figure.dpi']=100
plt.rcParams['lines.linewidth']=1.0

home='C:/Users/15136/OneDrive - University of Cincinnati/Documents/Courses/PHYS 5011/oled'
data=home+'/data'
figs=home+'/figs'

dfOled1=pd.read_excel(data+'/oled1/OLED2.6.xlsx')
dfOled2=pd.read_excel(data+'/oled2/OLED4.8.xlsx')
dfLed=pd.read_excel(data+'/greenled/green_iv_data.xlsx')

oled1v=dfOled1.iloc[:,0].to_numpy()
oled1i=dfOled1.iloc[:,1].to_numpy()

oled2v=dfOled2.iloc[:,0].to_numpy()
oled2i=dfOled2.iloc[:,1].to_numpy()

ledv=dfLed.iloc[:,0].to_numpy()
ledi=dfLed.iloc[:,1].to_numpy()

ledi=ledi[ledv<=2.0]
ledv=ledv[ledv<=2.0]

plt.close('all')
fig,ax=plt.subplots(2)

ax[0].plot(ledv,ledi,c='black')
ax[0].set_ylabel('Current (mA)')

ax[1].plot(oled1v,oled1i,label='OLED 1',ls='dotted',c='black')
ax[1].plot(oled2v,oled2i,label='OLED 2',ls='dashdot',c='black')
ax[1].set_xlabel('Voltage (V)')
ax[1].set_ylabel('Current (mA)')
ax[1].legend(loc='upper left')

plt.savefig(figs+'/ivplot.png',bbox_inches='tight',overwrite=True)
plt.show()
