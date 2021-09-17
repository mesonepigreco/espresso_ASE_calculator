import numpy as np

import ase
import ase.units
from ase.calculators.espresso import Espresso

import cellconstructor as CC 
import cellconstructor.Structure



class EspressoCalc(Espresso):

    def __init__(self, tr2_ph = 1e-18, *args, **kwargs):
        Espresso.__init__(self, *args, **kwargs)

        # Setup what properties the calculator can load
        self.implemented_properties = ["energy", "forces", "stress", "eff_charges", "raman_tensor"]

        if not "command" in kwargs:
            self.command = "pw.x -i PREFIX.pwi > PREFIX.pwo && ph.x -i PREFIX.phi > PREFIX.pho" 
        
    def write_input(self, atoms, *args, **kwargs):
        Espresso.write_input(self, atoms, *args, **kwargs)

        # Check if the calculation is an insulator
        if "occupations" in self.input_dft:
            assert self.input_dft["occupations"] == "fixed"

        if "system" in self.input_dft:
            if "occupations" in self.input_dft["system"]:
                assert self.input_dft["system"]["occupations"] == "fixed"

        # Prepare the input file
        INPUT = """
&inputph
        trans = .false.
        ldisp = .false
        zue = .true.
        lraman = .true.
&end
"""

        with open("{}.phi".format(self.label), "w") as fp:
            fp.write(INPUT)
        



    def read_results(self, *args, **kwargs):
        Espresso.read_results(self, *args, **kwargs)

        # Get the structure
        struct = CC.Structure.Structure()
        struct.generate_from_ase_atoms(self.atoms)

        # Create a fake dynamical matrix
        dyn = CC.Phonons.Phonons(struct)
        dyn.ReadInfoFromESPRESSO("{}.pho".format(self.label))

        self.results["eff_charges"] = dyn.effective_charges
        self.results["raman_tensor"] = dyn.raman_tensor
