from pymatgen.io.vasp.outputs import Vasprun

from pymatgen.electronic_structure.plotter import BSPlotter, DosPlotter, BSDOSPlotter, BoltztrapPlotter

from pymatgen.electronic_structure.core import Spin, Orbital, OrbitalType

from pymatgen.electronic_structure.dos import Dos

from pymatgen.electronic_structure.boltztrap import BoltztrapRunner, BoltztrapAnalyzer

v_dos = Vasprun("vasprun.xml")
bs = v_dos.get_band_structure()
nelect = v_dos.parameters['NELECT']
vbm = int(nelect/2 -1)
BoltztrapRunner(
        bs=bs,
        nelec=nelect,
        lpfac=100,
        run_type='FERMI',
        band_nb=24,
        cond_band=False,
        spin=1
        ).run(path_dir='./b24/')
an=BoltztrapAnalyzer.from_files("b24/boltztrap/")
BoltztrapPlotter.plot_fermi_surface(an.fermi_surface_data,bs.structure,cbm=False,energy_levels=[-0.01])
