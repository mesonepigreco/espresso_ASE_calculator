# espresso_ASE_calculator
A calculator to interface ASE and Quantum ESPRESSO 
with the focus of implementing 
the calculation of effective charges and Raman Tensor

This calculator hinerith the default ASE calculator 
for Quantum Espresso, therefore the setup is the same.
The only difference is in the command to run the simulation.
Since it computes also effective charges and Raman tensor,
it requires also the ph.x executable to be run.

The default command is

pw.x -i PREFIX.pwi > PREFIX.pwo && ph.x -i PREFIX.phi > PREFIX.pho

If you want to modify either the path to the executable or the number of processors,
just change the command variable to approperly run it with mpirun
