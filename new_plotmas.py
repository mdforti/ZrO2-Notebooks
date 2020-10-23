import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import pdb

plt.rc('text', usetex=True)

MASAS = pd.read_csv('masses.dat', sep='\s+')

MASAS['dosm_h']=(MASAS['mh']**2*MASAS['hlong']*MASAS['htrans']**2)**(1/3)
MASAS['dosm_e']=(MASAS['me']**2*MASAS['elong']*MASAS['etrans']**2)**(1/3)

fig, ax = plt.subplots()

reverse_coefs = np.polyfit(MASAS['vol'], MASAS['p'], deg=3)
forward_coefs = np.polyfit(MASAS['p'], MASAS['vol'], deg=3)


def convertion(p, x):
    y = p[0]*x**3+p[1]*x**2+p[2]*x + p[3]
    return y

def forward(x):
    return convertion(forward_coefs, x)


def reverse(x):
    return convertion(reverse_coefs, x)


fig, ax = plt.subplots(constrained_layout=True)

ax.plot(MASAS['vol'], MASAS['dosm_h'], 'o--k', label='holes')

ax.set_xlabel('$V/V_0$', fontsize=14)
#ax.set_title(r'$m^{*}/m_e = \sqrt[3]{m_l m_t g}$', fontsize=14) 
ax.set_ylabel('$m_{holes}/m_e$', fontsize=14)

ax2 = ax.twinx()

l2 = ax2.plot(MASAS['vol'], MASAS['dosm_e'], 'd--b', label='m_{electrons}')[0]
ax2.set_ylabel('$m_{electrons}/m_{e}$', color=l2.get_color(), fontsize=14)
#ax.annotate(
#         '',
#         xy=(0.5,0.8), 
#         xycoords='figure fraction', 
#         xytext=(50, 0), 
#         textcoords='offset points',
#         arrowprops=dict(facecolor='blue', shrink=0.5, color='blue', width=0.5))
ax.arrow(0.98, 10, -0.01, 0, width=0.05, fc='k', head_length=0.005, color='k')
ax2.arrow(1.01, 0.98, 0.01, 0, width=0.0005, head_length=0.005, fc='b', color='b')

ax_up = ax.secondary_xaxis ('top', functions = (reverse, forward))
ax_up.set_xlabel(r'Pressure(GPa)')

fig.savefig('new_dosmas.pdf')


#MDF-COMMENT atencion, del archivo borre estas lines 

# 1.12	-20.06	7.18	2.21	4	2.49	0.64	1
# 1.15	-21.97	6.92	2.286	4	2.59	0.64	1
