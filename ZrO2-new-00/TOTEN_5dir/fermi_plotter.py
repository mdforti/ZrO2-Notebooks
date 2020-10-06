from pymatgen.io.vasp.outputs import Vasprun, Eigenval
from ifermi.fermi_surface import FermiSurface
from ifermi.plotter import FermiSurfacePlotter
from ifermi.interpolator import Interpolater

vr = Vasprun('vasprun.xml')
bs = vr.get_band_structure()
interpolater=Interpolater(bs)
interpolate_factor=3
interp_bs, kpoint_dim = interpolater.interpolate_bands(interpolate_factor)
fs = FermiSurface.from_band_structure(
        interp_bs, kpoint_dim, mu=-0.2, wigner_seitz=True, 
    )
plotter = FermiSurfacePlotter(fs)
plotter.plot(interactive=True, plot_type='mpl')

