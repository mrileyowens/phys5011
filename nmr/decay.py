# Author: Riley Owens (GitHub: mrileyowens)

import numpy as np
import pandas as pd

import scipy.optimize
from lmfit import Model

import matplotlib.pyplot as plt
plt.rcParams['figure.dpi']=100
plt.rcParams['lines.linewidth']=1.0

def exponential(x,m,t):
    return m*np.exp((-1.0*x)/t)

home='C:/Users/15136/OneDrive - University of Cincinnati/Documents/Courses/PHYS 5011/nmr'
data=home+'/data'
figs=home+'/figs'

dfWarm=pd.read_csv(data+'/moil15-313mhzt2b.csv',delimiter=',')
dfWarmPeak=pd.read_csv(data+'/warmpeak.csv',delimiter=',')
dfCold=pd.read_csv(data+'/moilt2cold0.csv',delimiter=',')
dfColdPeak=pd.read_csv(data+'/moilt2cold0peak.csv',delimiter=',')

warmT=dfWarm.iloc[:,0].to_numpy()
warmV=dfWarm.iloc[:,1].to_numpy()

warmPeakT=dfWarmPeak.iloc[:,0].to_numpy()
warmPeakV=dfWarmPeak.iloc[:,1].to_numpy()

coldT=dfCold.iloc[:,0].to_numpy()
coldV1=dfCold.iloc[:,1].to_numpy()
coldV2=dfCold.iloc[:,2].to_numpy()

coldPeakT=dfColdPeak.iloc[:,0].to_numpy()
coldPeakV1=dfColdPeak.iloc[:,1].to_numpy()

params, cv=scipy.optimize.curve_fit(exponential,coldPeakT,coldPeakV1,p0=[0.13,0.01])
param2,cv2=scipy.optimize.curve_fit(exponential,warmPeakT,warmPeakV,p0=[0.225,0.01])
m,t=params
m2,t2=param2
stdevs=np.sqrt(np.diag(cv))
stdevs2=np.sqrt(np.diag(cv2))
print(params,cv,stdevs)
print(param2,cv2,stdevs2)
res=(coldPeakV1-exponential(coldPeakT,*params))/exponential(coldPeakT,*params)
res2=(warmPeakV-exponential(warmPeakT,*param2))/exponential(warmPeakT,*param2)

plt.close('all')
fig,ax=plt.subplots(2,2,gridspec_kw={'height_ratios':[3,1]},sharex='col')

ax[0,0].plot(coldT*1000.0,coldV1*1000.0,c='black',lw=0.1,ds='steps-mid')
ax[0,0].scatter(coldPeakT*1000.0,coldPeakV1*1000.0,c='black',s=10.0,marker='D')
ax[0,0].plot(coldT*1000.0,exponential(coldT*1000.0,m,t*1000.0)*1000.0,ls='--',c='red')
ax[0,0].set_ylim(0.0,130.0)
ax[0,0].tick_params(bottom=False)
ax[0,0].set_title('Cold Mineral Oil')
ax[0,0].set_ylabel('Voltage (mV)')

ax[1,0].scatter(coldPeakT*1000.0,res,c='black',s=3.0)
ax[1,0].axhline(0.0,ls='--',c='black')
ax[1,0].set_xlim(0.0,31.0)
ax[1,0].set_xlabel('Time (ms)')
ax[1,0].set_ylabel('Residual')

ax[0,1].plot(warmT*1000.0,warmV*1000.0,lw=0.1,ds='steps-mid',c='black')
ax[0,1].scatter(warmPeakT*1000.0,warmPeakV*1000.0,c='black',s=10.0,marker='D')
ax[0,1].plot(warmT*1000.0,exponential(warmT*1000.0,m2,t2*1000.0)*1000.0,ls='--',c='red')
ax[0,1].set_ylim(0.0,225.0)
ax[0,1].tick_params(labelleft=False,labelright=True,bottom=False,left=False,right=True)
ax[0,1].set_title('Warm Mineral Oil')

ax[1,1].get_shared_y_axes().join(ax[1,0], ax[1,1])
ax[1,1].scatter(warmPeakT*1000.0,res2,c='black',s=3.0)
ax[1,1].axhline(0.0,ls='--',c='black')
ax[1,1].set_xlim(0.0,12.0)
ax[1,1].tick_params(labelleft=False,labelright=True,left=False,right=True)
ax[1,1].set_xlabel('Time (ms)')


plt.savefig(figs+'/decay.pdf',bbox_inches='tight',overwrite=True)

plt.show()
