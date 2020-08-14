#!/usr/bin/env python3
# -*- coding: utf8 -*-
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
plt.rc('text', usetex=True)
plt.rc('font', size=14)

Vo = 70.4
DP = -19.76/10
data = pd.read_csv('gaps.dat', sep='\s+')
plt.plot(data['preassure'][1:-2]/10+DP, data['Indirect-finger'][1:-2], '--ok', label='Indirect')
plt.plot(data['preassure'][1:-2]/10+DP, data['Direct'][1:-2], '--^k', label='Direct')
plt.legend()
#plt.xlabel(r'$V / V_o$')
plt.xlabel(r'$P (GPa)$')
plt.ylabel('Band Gap (eV)')

plt.savefig('gaps.pdf')



