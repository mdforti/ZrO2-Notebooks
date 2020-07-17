# https://github.com/materialsproject/pymatgen/issues/582
vrun = Vasprun('vasprun.xml.gz')
bs = vrun.get_band_structure()
nelect = vrun.parameters['NELECT']
vbm = int(nelect/2 -1)
BoltztrapRunner(bs=bs,nelec=nelect,lpfac=100,run_type='FERMI',band_nb=vbm,cond_band=False).run(path_dir='vbm/')
an=BoltztrapAnalyzer.from_files("vbm/boltztrap/")
plot_fermi_surface(an.fermi_surface_data,bs.structure,cbm=False,energy_levels=[-0.01])
