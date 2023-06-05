#Code used to produce Figure 1.3
#Classical EIT
from numpy import *
#from pylab import py
from matplotlib import *
import matplotlib.pyplot as plt
k1 = 2.0
k2 = 1
gamma1 = 4.0e-2
gamma2 = 1.0e-7
F = 0.1
m = 1
omega_r = [0, 0.1, 0.2, 0.3]
omega = 1.05613
steps = 1000
detuning = linspace(-0.15, 0.15, steps)
p = [zeros(steps) for i in range(4)]
for i in range(steps):
    o_s = omega + detuning[i]
    for k in range(4): p[k][i] = (-2*pi*1j*F**2*o_s*(omega**2 - o_s**2 -
    1j*gamma2*o_s) / (m * ((omega**2 - o_s**2 - 1j*gamma1*o_s)*(omega**2 - o_s**2 - 1j*gamma2*o_s) - omega_r[k]**4)))

f = plt.figure(figsize=(6,7))
plt.subplots_adjust(hspace=0.1)
# subplot 1 (top)
ax1 = plt.subplot(411)
#ax1.plot(detuning,p[0],’b’)
ax1.plot(detuning,p[0],'b')
ax1.text(-.14,1.8,'a.)')
plt.ylim([0,2])
plt.xlim([-.15,.15])
plt.ylabel(r'$P_2$')
# subplot 2
ax2=plt.subplot(412,sharex=ax1) #share x-axis of subplot 1
ax2.plot(detuning,p[1],'b')
#ax2.plt.plot(detuning,p[1],'b')
plt.ylim([0,2])
plt.xlim([-.15,.15])
plt.ylabel(r'$P_2$')
# subplot 3
ax3=plt.subplot(413,sharex=ax1) #share x-axis of subplot 1
ax3.plot(detuning,p[2],'b')
plt.ylim([0,2])
plt.xlim([-.15,.15])
plt.ylabel(r'$P_2$')
# subplot 4
ax4=plt.subplot(414,sharex=ax1) #share x-axis of subplot 1
ax4.plot(detuning,p[3],'b')
plt.ylim([0,2])
plt.xlim([-.15,.15])
plt.ylabel(r'$P_2$')
xticklabels = ax1.get_xticklabels()+ax2.get_xticklabels()+ax3.get_xticklabels()
plt.setp(xticklabels, visible=False)
ax1.xaxis.set_major_locator(plt.MaxNLocator(4))
plt.xlabel('$\delta=\omega_s-\omega$')
ax1.text(-.14,1.8,'a.)')
ax2.text(-.14,1.8,'b.)')
ax3.text(-.14,1.8,'c.)')
ax4.text(-.14,1.8,'d.)')
plt.show()