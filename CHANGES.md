# 0.1.1


Moved from version 0.1.0 to 0.1.1
Fixed error: "astropy.io.fits.verify.VerifyError:  Verification reported errors: HDU 0:     NAXISj keyword out of range ('NAXIS4' when NAXIS == 2)     NAXISj keyword out of range ('NAXIS5' when NAXIS == 2) Note: PyFITS uses zero-based indexing." by removing the impose of the number of axis i.e by not specifying 'naxis':N.
