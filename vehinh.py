from qutip import *
from pylab import *
from numpy import *
#Code used to produce Fig. 4.7
nsteps=100
zsteps=nsteps
e1=basis(3,0)
g1=basis(3,1)
g2=basis(3,2)
#dipole transitions
sigma_g1e1=tensor(g1*e1.dag())
sigma_g2e1=tensor(g2*e1.dag())
sigma_g1g1=tensor(g1*g1.dag())
sigma_e1e1=tensor(e1*e1.dag())
sigma_g2g2=tensor(g2*g2.dag())
#Rabi frequencies (right, left polarized)
ratio=.5
omega2=3 #probe beam
omega1=omega2*ratio #pump/coupling beam
ratio=.5
omega2=3 #probe beam
omegamax=3
ratiomax=3
uB=-5
reset=uB
uB_max=5
r=(uB_max-uB)*(nsteps)**(-1)
d=(omegamax-omega2)*(zsteps)**(-1)
rr=(ratiomax-ratio)*(zsteps)**(-1)
#clebsch gordan coefficients
e1g1=1
e1g2=sqrt(1.0/3.0)
#spontaneous emisssion

gamma_e1g1=e1g1**2
gamma_e1g2=e1g2**2
#collapse operators
c1=sqrt(gamma_e1g1)*sigma_g1e1
c2=sqrt(gamma_e1g2)*sigma_g2e1
collapse=[c1,c2]
x=linspace(uB,uB_max,nsteps+1)
y=linspace(ratio,ratiomax,nsteps+1)
list1=[]
zlist1=zeros(shape=(nsteps+1,nsteps+1))
for j in range (zsteps+1):
    for i in range (nsteps+1):
        #interaction hamiltonian
        H_i=e1g1*omega2*(sigma_g1e1.dag()+sigma_g1e1)+e1g2*omega1*(sigma_g2e1.dag()+sigma_g2e1)
        H_b=(uB)*(-sigma_g1g1+0*sigma_e1e1+sigma_g2g2)
        H=H_i+H_b
        #liouvillian
        L=liouvillian(H,collapse)
        rhoss=steady(L)
        pe1=rhoss[0,0]
        list1.append(pe1)
        uB=uB+r
    zlist1[j]=list1
    list1=[]
    uB=reset
ratio=ratio+rr
omega1=omega2*ratio
x,y=meshgrid(x,y)
fig= plt.figure()
ax = fig.add_subplot(111, projection ='3d')
surf=ax.plot_surface(x, y, zlist1, rstride=1, cstride=1,
cmap=cm.jet, linewidth=0, antialiased=False)
ax.set_ylabel(r'$\Omega_{p}/\Omega_{c}$', fontsize=27)
ax.set_zlabel(r'$P_e$', fontsize=27)

ax.set_xlabel('$\mu{B}$', fontsize=27)
show()