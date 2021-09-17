#import setuptools
from __future__ import print_function
from numpy.distutils.core import setup, Extension


setup(name = "espresso_ase_calculator",
      version = "0.1",
      description = "A calculator to interface ASE and Quantum ESPRESSO with the focus of implementing the calculation of effective charges and Raman Tensor",
      author = "Lorenzo Monacelli",
      packages = ["espresso_ase_calculator"],
      package_dir = {"espresso_ase_calculator": "Modules"},
      license = "GPLv3")


def readme():
    with open("README.md") as f:
        return f.read()
