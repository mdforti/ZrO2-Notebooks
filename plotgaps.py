#!/usr/bin/env python3
# -*- coding: utf8 -*-
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
plt.rc('text', usetex=True)
plt.rc('font', size=14)

data = pd.read_csv('gaps.dat', sep='\s+')
plt.plot(data['vol'], data['Indirect'], '-ok' , label='Indirect Gap')
plt.plot(data['vol'], data['Direct'], '-^k', label='Direct Gap')
plt.legend()
plt.xlabel('cell volume '+r'($\AA$)')
plt.ylabel('Band Gap (eV)')

plt.savefig('gaps.pdf')
