import numpy as np

import pandas as pd

import matplotlib.pyplot as plt

from scipy.optimize import curve_fit

def f(x,I,a,d,w):

    alpha=np.pi*a*np.sin(x)/w
    beta=np.pi*d*np.sin(x)/w

    return I*(np.cos(beta))**2*(np.sin(alpha)/alpha)**2

home='C:/Users/15136/OneDrive - University of Cincinnati/Documents/Courses/phys5011/spi'

data=home+'/data'
figs=home+'/figs'

dfLaser=pd.read_csv(data+'/laser.csv',delimiter=',')

x=dfLaser.iloc[:,0].to_numpy()
m2=dfLaser.iloc[:,1].to_numpy()-7.6
m3=dfLaser.iloc[:,2].to_numpy()-7.6
m4=dfLaser.iloc[:,3].to_numpy()-7.6

theta=(x-4.0382)/506.5

popt,pcov=curve_fit(f,theta,m3,p0=[175,100e-6,253e-6,0.546e-6])

print(popt,pcov)

r=(m3-f(theta,*popt))/m3

fig,ax=plt.subplots(2,1,gridspec_kw={'height_ratios':[3,1]},sharex=True)

ax[0].plot(theta,f(theta,*popt),label='Fit',c='red',ls='dashed')
ax[0].plot(theta,m2,label='Mode 2')
ax[0].plot(theta,m3,label='Mode 3')
ax[0].plot(theta,m4,label='Mode 4')

#ax[0].set_xlim(-0.005,0.005)
ax[0].set_ylim(0.0)

ax[0].set_ylabel('Voltage (mV)')

ax[0].legend(loc='upper right')

ax[1].scatter(theta,r,marker='.',c='black')
ax[1].axhline(0.0,ls='dashed',c='black')

ax[1].set_yscale('log')

#ax[1].set_ylim(-2.0,2.0)

ax[1].set_xlabel('Angular Position (rad.)')
ax[1].set_ylabel('Residual')

fig.savefig(figs+'/lModes.pdf',bbox_inches='tight')

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
