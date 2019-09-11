
from __future__ import print_function, division
import numpy as np
import scipy as sp
from scipy import stats
import pylab as pl
#pl.inline
pl.style.use("https://raw.githubusercontent.com/fedhere/DSPS/master/fbb.mplstyle")

np.random.randn(123)
fig, ax = pl.subplots()
for a in [0.2, 0.6, 1.0]:
    ax.hist(sp.stats.chi.rvs(df=3, scale=a, size=1000), # could as well be sp.stats.maxwell.rvs(scale=a, size=1000)
          bins=np.arange(0,5,0.1), alpha=0.7,
       label="a = %.1f"%a);
pl.xlabel('Temperature (Kelvin)')
pl.ylabel('Particle Velocity (m/s)')
pl.legend();


mu_1 = np.sqrt(2) * sp.special.gamma(1.2/2)/sp.special.gamma(.2/2)
mu_2 = np.sqrt(2) * sp.special.gamma(1.6/2)/sp.special.gamma(.6/2)
mu_3 = np.sqrt(2) * sp.special.gamma(2/2)/sp.special.gamma(1/2)

mean1 = mu_1 *.2
mean2 = mu_2 *.6
mean3 = mu_3 

print(mean1, mean2, mean3)

