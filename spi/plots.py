import numpy as np

import pandas as pd

import matplotlib.pyplot as plt

home='C:/Users/15136/OneDrive - University of Cincinnati/Documents/Courses/PHYS 5011/spi'

data=home+'/data'
figs=home+'/figs'

dfLaser=pd.read_csv(data+'/laser.csv',delimiter=',')

v=dfLaser.iloc[:,0].to_numpy()
m2=dfLaser.iloc[:,1].to_numpy()
m3=dfLaser.iloc[:,2].to_numpy()
m4=dfLaser.iloc[:,3].to_numpy()

fig,ax=plt.subplots(1,1)

ax.plot(v,m2,label='Mode 2')
ax.plot(v,m3,label='Mode 3')
ax.plot(v,m4,label='Mode 4')

ax.set_xlim(0.0,8.0)
ax.set_ylim(0.0)

ax.set_xlabel('Position (mm)')
ax.set_ylabel('Voltage (mV)')

ax.legend(loc='upper right')

fig.savefig(figs+'/lModes.png',dpi=100,bbox_inches='tight')

dfPMT=pd.read_csv(data+'/pmt.csv',delimiter=',')

v=dfPMT.iloc[:,0].to_numpy()
d=dfPMT.iloc[:,1].to_numpy()*1000.0
l=dfPMT.iloc[:,3].to_numpy()*1000.0

fig,ax=plt.subplots(1,1)

ax.axvline(540,ls='dashed',c='black')
ax.semilogy(v,d,label='Closed')
ax.semilogy(v,l,label='Open')

ax.set_xlim(np.min(v),np.max(v))
ax.set_ylim(np.min(d))

ax.set_xlabel('PMT Bias (V)')
ax.set_ylabel('Count Rate (Hz)')

ax.legend(loc='upper left')

fig.savefig(figs+'/pmt.png',dpi=100,bbox_inches='tight')
