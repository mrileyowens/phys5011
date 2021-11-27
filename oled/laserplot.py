import numpy as np
import pandas as pd

import matplotlib.pyplot as plt
plt.rcParams['figure.dpi']=100
plt.rcParams['lines.linewidth']=1.0

home='C:/Users/15136/OneDrive - University of Cincinnati/Documents/Courses/PHYS 5011/oled'
data=home+'/data'
figs=home+'/figs'

dfLaser=pd.read_csv(data+'/laser_oled/AbsoluteIrradiance_17-30-23-294.txt',delimiter='\t',header=0,skiprows=13)

wLaser=dfLaser.iloc[:,0].to_numpy()
fLaser=dfLaser.iloc[:,1].to_numpy()

fLaser=fLaser[wLaser <= 700.0]
wLaser=wLaser[wLaser <= 700.0]

fLaser=fLaser[wLaser >= 450.0]
wLaser=wLaser[wLaser >= 450.0]

plt.close('all')
fig,ax=plt.subplots(1)

ax.plot(wLaser,fLaser,c='black')
plt.xlim(450.0,700.0)
plt.ylim(0.0)
ax.set_ylabel('Absolute Spectral Irradiance ($\mu$W cm$^{-2}$ nm$^{-1}$)')
ax.set_xlabel('Wavelength (nm)')
ax.legend(loc='upper left')

plt.savefig(figs+'/laserplot.png',bbox_inches='tight',overwrite=True)
plt.show()
