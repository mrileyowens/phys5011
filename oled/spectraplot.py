import numpy as np
import pandas as pd

import matplotlib.pyplot as plt
plt.rcParams['figure.dpi']=100
plt.rcParams['lines.linewidth']=1.0

home='C://Users/15136/OneDrive - University of Cincinnati/Documents/Courses/PHYS 5011/oled'
data=home+'/data'
figs=home+'/figs'

dfGled=pd.read_csv(data+'/greenled/spectra/AbsoluteIrradiance_18-12-59-289.txt',delimiter='\t',header=0,skiprows=13)

dfOled150=pd.read_csv(data+'/oled1/AbsoluteIrradiance_15-07-19-341.txt',delimiter='\t',header=0,skiprows=13)
dfOled170=pd.read_csv(data+'/oled1/AbsoluteIrradiance_15-41-49-332.txt',delimiter='\t',header=0,skiprows=13)
dfOled190=pd.read_csv(data+'/oled1/AbsoluteIrradiance_16-07-49-325.txt',delimiter='\t',header=0,skiprows=13)

dfOled250=pd.read_csv(data+'/oled2/AbsoluteIrradiance_16-57-10-525.txt',delimiter='\t',header=0,skiprows=13)
dfOled270=pd.read_csv(data+'/oled2/AbsoluteIrradiance_17-04-10-523.txt',delimiter='\t',header=0,skiprows=13)
dfOled290=pd.read_csv(data+'/oled2/AbsoluteIrradiance_17-13-50-521.txt',delimiter='\t',header=0,skiprows=13)

wGled=dfGled.iloc[:,0].to_numpy()
fGled=dfGled.iloc[:,1].to_numpy()

wOled=dfOled190.iloc[:,0].to_numpy()

fOled150=dfOled150.iloc[:,1].to_numpy()
fOled170=dfOled170.iloc[:,1].to_numpy()
fOled190=dfOled190.iloc[:,1].to_numpy()

fOled250=dfOled250.iloc[:,1].to_numpy()
fOled270=dfOled270.iloc[:,1].to_numpy()
fOled290=dfOled290.iloc[:,1].to_numpy()

fOled150=fOled150[wOled <= 700.0]
fOled170=fOled170[wOled <= 700.0]
fOled190=fOled190[wOled <= 700.0]

fOled250=fOled250[wOled <= 700.0]
fOled270=fOled270[wOled <= 700.0]
fOled290=fOled290[wOled <= 700.0]

wOled=wOled[wOled <= 700.0]

fOled150=fOled150[wOled >= 450.0]
fOled170=fOled170[wOled >= 450.0]
fOled190=fOled190[wOled >= 450.0]

fOled250=fOled250[wOled >= 450.0]
fOled270=fOled270[wOled >= 450.0]
fOled290=fOled290[wOled >= 450.0]

wOled=wOled[wOled >= 450.0]

plt.close('all')
fig,ax=plt.subplots(3,sharex=True)

#xlim1=400.0
#xlim2=600.0

ax[0].plot(wGled,fGled,c='black')
#ax[0].set_ylabel('Irradiance ($\mu$W cm$^{-2}$ nm$^{-1}$)')
ax[0].set_ylim(0.0)

ax[1].plot(wOled,fOled150,c='black',ls='dashdot',label='50 V')
ax[1].plot(wOled,fOled170,c='black',ls='dotted',label='70 V')
ax[1].plot(wOled,fOled190,c='black',label='90 V')
ax[1].legend(loc='upper right')
#ax[1].set_ylabel('Irradiance ($10^{-5}$ $\mu$W cm$^{-2}$ nm$^{-1}$)')
ax[1].set_ylim(0.0)

ax[2].plot(wOled,fOled250,c='black',ls='dashdot',label='50 V')
ax[2].plot(wOled,fOled270,c='black',ls='dotted',label='70 V')
ax[2].plot(wOled,fOled290,c='black',label='90 V')
ax[2].legend(loc='upper right')
#ax[1].set_ylabel('Irradiance ($10^{-5}$ $\mu$W cm$^{-2}$ nm$^{-1}$)')
ax[2].set_ylim(0.0)

plt.xlim(450.0,700.0)
plt.xlabel('Wavelength (nm)')

fig.text(0.00, 0.5, 'Absolute Spectral Irradiance ($\mu$W cm$^{-2}$ nm$^{-1}$)', va='center', rotation='vertical')

plt.savefig(figs+'/spectraplot.png',bbox_inches='tight',overwrite=True)
plt.show()
