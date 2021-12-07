# Author: Riley Owens (GitHub: mrileyowens)

# This file plots interference patterns from
# a laser and a filtered bulb, and photon
# count rates as a function of PMT bias.

import numpy as np

import pandas as pd

import matplotlib.pyplot as plt

from scipy.optimize import curve_fit

# Fraunhofer diffraction function for
# diffraction by the source, detector,
# and double slits
def f(x,I,a,d,s,e,w):

    alpha=a*np.sin(x)/w
    beta=np.pi*d*np.sin(x)/w
    gamma=s*np.sin(x)/w
    delta=e*np.sin(x)/w

    return I*(np.cos(beta))**2*(np.sinc(alpha))**2*(np.sinc(gamma))**2*(np.sinc(delta))

# Establishing directories and file paths
home='C:/Users/15136/OneDrive - University of Cincinnati/Documents/Courses/phys5011/spi'
data=home+'/data'
figs=home+'/figs'

# Opening laser interference pattern data
dfLaser=pd.read_csv(data+'/laser.csv',delimiter=',')

# Extracting columns as NumPy arrays
# and subtracting background voltage
x=dfLaser.iloc[:,0].to_numpy()
m2=dfLaser.iloc[:,1].to_numpy()-7.6
m3=dfLaser.iloc[:,2].to_numpy()-7.6
m4=dfLaser.iloc[:,3].to_numpy()-7.6

# Converting microdial position to
# angular distance
theta=(x-4.0382)/506.5

# Fitting Fraunhofer diffraction model to laser interference pattern
popt,pcov=curve_fit(f,theta,m3,p0=[180,100.0,353.0,132.9,110.5,0.670])#,bounds=bounds)

print(popt,np.sqrt(np.diag(pcov)))

# Computing fractional residual
r=(m3-f(theta,*popt))/f(theta,*popt)

# Figure to show the patterns at the detector for each mode and the
# interference pattern fit
fig,ax=plt.subplots(2,1,gridspec_kw={'height_ratios':[4,1]},sharex=True)

ax[0].plot(theta,f(theta,*popt),label='Fit',c='red',ls='dashed')
ax[0].plot(theta,m2,label='Mode 2')
ax[0].plot(theta,m3,label='Mode 3')
ax[0].plot(theta,m4,label='Mode 4')

ax[0].set_ylim(0.0)

ax[0].set_ylabel('Voltage (mV)')
ax[0].legend(loc='upper right')

ax[1].scatter(theta,r,marker='.',c='orange')
ax[1].axhline(0.0,ls='dashed',c='black')

ax[1].set_xlim(-0.007,0.007)
ax[1].set_ylim(-1.0,2.0)

ax[1].set_xlabel('Angular Position (rad.)')
ax[1].set_ylabel('Residual')

fig.savefig(figs+'/lModes.pdf',bbox_inches='tight')

# Opening PMT count rate data
dfPMT=pd.read_csv(data+'/pmt.csv',delimiter=',')

# Extracting columns as NumPy arrays
v=dfPMT.iloc[:,0].to_numpy()
d=dfPMT.iloc[:,1].to_numpy()*1000.0
l=dfPMT.iloc[:,3].to_numpy()*1000.0

# Figure to show count rate as a
# function of PMT bias
fig,ax=plt.subplots(1,1)

ax.axvline(540,ls='dashed',c='black')
ax.semilogy(v,d,label='closed')
ax.semilogy(v,l,label='open')

ax.set_xlim(np.min(v),np.max(v))

ax.set_xlabel('PMT Bias (V)')
ax.set_ylabel('Count Rate (Hz)')
ax.legend(loc='upper left')

fig.savefig(figs+'/pmt.pdf',bbox_inches='tight')

# Opening bulb interference pattern data
dfspi=pd.read_csv(data+'/spi.csv',delimiter=',')

# Extracting columns as NumPy arrays
x=dfspi.iloc[:,0].to_numpy()
m2=dfspi.iloc[:,2].to_numpy()
m3=dfspi.iloc[:,1].to_numpy()
m4=dfspi.iloc[:,3].to_numpy()
m5=dfspi.iloc[:,4].to_numpy()

# Computing average background count rate
bckgnd=np.mean(m5)

# Converting microdial position to
# angular distance
theta=(x-4.24)/506.5

# Fitting Fraunhofer diffraction model to laser interference pattern
popt,pcov=curve_fit(f,theta,m3,p0=[35.0,100.0,353.0,132.9,110.5,0.546])#,bounds=bounds)

# Computing residual
r=(m3-f(theta,*popt))/f(theta,*popt)

print(popt,np.sqrt(np.diag(pcov)))

# Figure to show the patterns at the detector for each mode and the
# interference pattern fit
fig,ax=plt.subplots(2,2,gridspec_kw={'height_ratios':[4,1]},sharey='row')

ax[0,0].plot(theta,f(theta,*popt),ls='dashed',c='red',label='Fit')
ax[0,0].plot(theta,m3-bckgnd,c='orange',label='Mode 3')

ax[0,0].set_xlim(-0.007,0.007)
ax[0,0].set_ylim(0.0)

ax[0,0].set_ylabel('Count Rate (Hz)')
ax[0,0].legend(loc='upper right')
ax[0,0].set_xticklabels([])

ax[1,0].scatter(theta,r,marker='.',c='orange')
ax[1,0].axhline(0.0,ls='dashed',c='black')

ax[1,0].set_xlim(-0.007,0.007)
ax[1,0].set_ylim(-0.5,3.0)

ax[1,0].set_xlabel('Angular Position (rad.)')
ax[1,0].set_ylabel('Residual')

ax[0,1].plot(theta,m2-bckgnd,c='blue',label='Mode 2')
ax[0,1].plot(theta,m4-bckgnd,c='green',label='Mode 4')

ax[0,1].set_xlim(-0.007,0.007)

ax[0,1].set_xlabel('Angular Position (rad.)')

ax[0,1].legend(loc='upper right')

ax[1,1].axis('off')

fig.savefig(figs+'/spi.pdf',bbox_inches='tight')

dfCnt=pd.read_csv(data+'/count.csv',delimiter=',')

cnt=dfCnt.iloc[:,0].to_numpy()*(1./.04)

fig,ax=plt.subplots(1,1)

ax.hist(cnt,bins=25)

ax.set_xlabel('Count Rate (Hz)')
ax.set_ylabel('Frequency')

fig.savefig(figs+'/count.pdf',bbox_inches='tight')
