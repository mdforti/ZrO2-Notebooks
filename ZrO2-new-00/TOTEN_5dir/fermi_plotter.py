#!/usr/bin/env python3
from pymatgen.io.vasp.outputs import Vasprun, Eigenval
from pymatgen.electronic_structure.boltztrap import BoltztrapRunner, BoltztrapAnalyzer
from pymatgen.electronic_structure.plotter import plot_fermi_surface

vrun = Vasprun('vasprun.xml')
bs = vrun.get_band_structure()
nelect = vrun.parameters['NELECT']
vbm = int(nelect/2 - 1)
BoltztrapRunner(
        bs=bs,
        nelec=nelect,
        lpfac=100,
        run_type='FERMI',
        band_nb=25,
        spin=1,
        cond_band=True
        ).run('./b25/')
an = BoltztrapAnalyzer.from_files("b25/boltztrap/")
plot_fermi_surface(
        an.fermi_surface_data,
        bs.structure,
        cbm=True,
        energy_levels=[0.2])
BoltztrapRunner(bs=bs, nelec=nelec, type='BOLTZ').run(path_dir='full/')
anfull = BoltztrapAnalyzer.from_files("full/")
effmas_vs_t = anfull.get_average_eff_mass()


#from pymatgen.io.vasp.outputs import Vasprun, Eigenval
#from pymatgen.electronic_structure.boltztrap2 import *
#from pymatgen.electronic_structure.boltztrap import BoltztrapRunner, BoltztrapAnalyzer
# from pymatgen.electronic_structure.plotter import plot_fermi_surface
#from monty.serialization import loadfn

#data=VasprunLoader().from_file('vasprun.xml')
#bs = loadfn(
#vrun = Vasprun('vasprun.xml')
#bs = vrun.get_band_structure()
#nelect = vrun.parameters['NELECT']
#vbm = int(nelect/2 - 1)
#BoltztrapRunner(
#        bs=bs,
#        nelec=nelect,
#        lpfac=100,
#        run_type='FERMI',
#        band_nb=vbm,
#        cond_band=False,
#        spin=1
#        ).run(path_dir='vbm/')
#
#an = BoltztrapAnalyzer.from_files("vbm/boltztrap/")
#plot_fermi_surface(
#        an.fermi_surface_data,
#        bs.structure,
#        cbm=False,
#        energy_levels=[-0.01]
#        )
