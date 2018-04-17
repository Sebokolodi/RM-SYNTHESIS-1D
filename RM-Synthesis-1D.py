from numpy import newaxis, arange, zeros, exp, loadtxt, argmax, array
import astropy.io.fits as pyfits
import time
import pylab
import os
import sys


def read_data(image, freq=True):
                                                                              
    """ Read and return image data: ra, dec and freq only"""
    with pyfits.open(image) as hdu:
        imagedata = hdu[0].data
        header = hdu[0].header
    imslice = zeros(imagedata.ndim, dtype=int).tolist()
    imslice[-1] = slice(None)
    imslice[-2] = slice(None)
    if freq:
        imslice[-3] = slice(None)
    return imagedata[imslice], header


def check_shape(qfits, ufits, frequencies):
    """
    Checks the shape of the cubes and frequency file
    """
    qhdr =  pyfits.getheader(qfits)
    uhdr =  pyfits.getheader(ufits)
    
    errors = []
    axis = ['naxis1', 'naxis2', 'naxis3']
    if [qhdr['naxis'] < 3 or uhdr['naxis'] < 3:
        errors.append('The dimensions of Q = %d and U = %d, not >=3.' %(qhdr['naxis'], uhdr['naxis']))
    if qhdr['naxis'] != uhdr['naxis']:
        if qhdr['naxis'] >= 3 and uhdr['naxis'] >=3:
             for ax in axis:
                 if qhdr[ax] != uhdr[ax]
                      errors.append('%s for Q is != %d of U.' %(qhdr[ax], uhdr[ax]))
    if qhdr[axis[2]] != len(frequencies) or uhdr[axis[2]] != len(frequencies):
        errors.append('Frequencies axis of the cubes differs from the length of the frequency file provided.')    
            
    return errors


def create_mask():
    """
    This creates a mask. This mask is used upon the 
    user's request. It is recommended when creating
    RM maps -- since one doesn't want to find peaks
    for noisy areas. If clean components are requested
    a mask or threshold is used -- the mask in this
    case will be created. 
    """
    return maskfits



def faraday_phase(phi_sample, wavelengths):       
    
    """return phase term of the Faraday spectrum """
    # ra, dec, wavelengths, faraday depth
    expo = zeros([1, 1, len(wavelengths), len(phi_sample)], dtype=complex)            
    for i, phi in enumerate(phi_sample):                  
        expo[:, :, :, i] = exp(-2 * 1j * phi * (wavelengths -wavelengths.mean()))
                              
    return expo 



def add_phi_to_fits_header(fits_header, phi_array):
    """
    Returns a deep copy of *fits_header*. The returned copy has
    Faraday depth as the third axis, with reference values and
    increments as derived from *phi_array*. It is assumed that
    *phi_array* contains values on a regular comb.

    Knicked from Brentjens RM Synthesis Script
    """
    if len(phi_array) < 2:
        raise ShapeError('RM cube should have two or more frames to be a cube')
    fhdr = fits_header.copy()
    fhdr.update('NAXIS3', len(phi_array))
    fhdr.update('CRPIX3', 1.0)
    fhdr.update('CRVAL3', phi_array[0])
    fhdr.update('CDELT3', phi_array[1]-phi_array[0])
    fhdr.update('CTYPE3', 'FARDEPTH')
    fhdr.update('CUNIT3', 'RAD/M^2')
    return fhdr



def main(freq, qfits, ufits, phi_max=None, phi_min=None,
         dphi=None, rmsf_plot=False, prefix=None):

    ##TODO: check if there is enough space to carry this out.
    
    
    try:
        frequencies = loadtxt(freq)
    except ValueError:
        sys.exit("There seems to be a problem with you frequency file. "
                 "This file should be a text file with no strings. ")
    
    errors = check_shape(qfits, ufits, frequencies)
    if len(errors) > 0:
        print(errors)
        sys.exit()

    wavelengths =  (299792458.0/frequencies)**2 
    qdata, qhdr = read_data(qfits)
    udata, uhdr = read_data(ufits)
       
    # if the user does not provide Faraday depth interval
    # we attempt to compute this internally. 
    if phi_max is None or phi_min is None or dphi is None: 
        phi_max = (1.9/abs(numpy.diff(wavelengths)).max()) * 3.0
        dphi = (3.8/abs(wavelengths[0] - wavelengths[-1]))/3.0
        phi_min = -phi_max

        
    phi_sample =  arange(phi_min, phi_max, dphi)

    P = qdata +  1j * udata
    P_new  = P[newaxis, ...]
    phase  = faraday_phase(phi_sample, wavelengths)

    Faraday_Dispersion = (P_new * phase.T ).sum(1)/len(wavelengths)
    Faraday_amp = numpy.absolute(Faraday_Dispersion)
    
    peaks = argmax(Faraday_amp, axis=0)
    RM_peak = phi_sample[peaks]
    if rmsf:
        RMSF = phase.T.sum(1)[:, 0, 0]/len(wavelengths)
        pylab.plot(phi_sample, absolute(RMSF), '--')
        pylab.savefig(prefix + '-RM.PNG')
   
    qhdr_fara = add_phi_to_fits_header(qhdr, phi_sample)
    uhdr_fara = add_phi_to_fits_header(uhdr, phi_sample)
    if raw:
        QFAR_DEPTH = Faraday_Dispersion.real
        UFAR_DEPTH = Faraday_Dispersion.imag

        pyfits.writeto(prefix + '-QFAR.FITS', QFAR_DEPTH, 
                       qhdr, clobber=True)
        pyfits.writeto(prefix + '-UFAR.FITS', UFAR_DEPTH, 
                       uhdr, clobber=True)
    if clean:
         print('Hello')

    if derotate:
         print('Derotating')
    
    
    




