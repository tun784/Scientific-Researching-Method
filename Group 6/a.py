#Code used to produce Figure 1.3
#Classical EIT
from numpy import *
from pylab import *
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
	1j*gamma2*o_s) / (m * ((omega**2 - o_s**2 - 1j*gamma1*o_s)*(omega**2 -
	o_s**2 - 1j*gamma2*o_s) - omega_r[k]**4)))
f = figure(figsize=(6,7))
subplots_adjust(hspace=0.1)
65
# subplot 1 (top)
ax1 = subplot(411)
ax1.plot(detuning,p[0],'b')
ax1.text(-.14,1.8,'a.)')
ylim([0,2])
xlim([-.15,.15])
ylabel(r'$P_2$')

xticklabels = ax1.get_xticklabels()
setp(xticklabels, visible=False)
ax1.xaxis.set_major_locator(MaxNLocator(4))
xlabel('$\delta=\omega_s-\omega$')
ax1.text(-.14,1.8,'a.)')
show()
