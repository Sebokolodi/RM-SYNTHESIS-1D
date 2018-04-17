# RM-SYNTHESIS-1D
Description:
This code performs RM synthesis on a data cube with RA, DEC and FREQ axis. 



Inputs:

1. Stokes Q cube
2. Stokes U cube

NB: These cubes must have the same shape. Most importantly, have RA, DEC and FREQUENCY AXIS. 

3. Frequency file. Must be a txt file with no strings.

NB: The FREQUENCY axis of these data cubes must be equal to the length of the frequencies provided. 




Outputs:

1. We compute the product P * exp(-2 i RM wavelength^2) in a matrix form. By doing so, this considers all pixels at once instead of looping through them. Thus, the process is much faster but uses a lot for processing memory.

2. We return Q(RM) and U(RM) cubes.
3. A PNG plot of the RM spread function.
4. A FITS file of the RM corresponding to the peak in Faraday Dispersion Spectra.
3. There is an option to return the derotated Q(RM) and U(RM). These are cubes after removing contributions from RM peak.
4. Another option is to return RM Cleaned components:  Still to incorporate.


How to run:



