from pymatgen.io.vasp.outputs import Vasprun, Eigenval
from ifermi.fermi_surface import FermiSurface
from ifermi.plotter import FermiSurfacePlotter
from ifermi.interpolator import Interpolater

vr = Vasprun('vasprun.xml')
bs = vr.get_band_structure()
interpolater=Interpolater(bs)
interpolate_factor=2
interp_bs, kpoint_dim = interpolater.interpolate_bands(interpolate_factor)
fs = FermiSurface.from_band_structure(
        interp_bs, kpoint_dim, mu=4.5, wigner_seitz=True, 
    )
plotter = FermiSurfacePlotter(fs)
plotter.plot(plot_type='mpl', interactive=True)

