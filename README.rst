**Description:**

RM-Synthesis is technique used to transform polarized intensity between wavelength-space (lambda) and faraday-space (RM). See Brentjen & de Bruyn (2005) for more detail. 

This technqiue can become computationally expensive. For example, wide-field views imply a large number of line-of-sights (pixels) to evaluate, and wide spectral-bandwidth, although necessary, imply a large number of channels to average across. Thus, optimizing RM-Synthesis technqiue is important. Particularly for all-sky surveys such as VLASS, whereby all pixels need to be evaluated -- this is unlike the case where specific pixel locations are known and of interest.
In the original implementation, all pixels within lambda^2-plane are evaluated at once, although this is may have been optimum at that time, the large dataset of modern instruments makes it infeasible.

In our RM-Synthesis code, we evaluate each pixel at a time. This approach as is is the less optimum thus, we have incorporated multiprocessing (and we intend to extend this to GPUs) so that multiple pixels can we evaluated at once. This was tested on Cyngus A 2k by 2k images with 2-18 GHz bandwidth (~1000 channels). Without parallel processing, this task takes over > 20 hours to run and with multi-processing using 6 cores this takes exactly 2 hours. When using the original approach, we encounter Memory Error since the combined data size of our Stokes Q and U is 33 GB. 

**Installation:**

pip install RMSYNTHESIS


**Dependencies:**

1. Numpy
2. Multiprocessing
3. Astropy


**Data Requirements:**

1. Stokes Q and U FITS data cubes - shape 312 that is frequency, ra and dec.

2. Frequencies file - only text file is supported. 

NB:The number of frequencies in 2. but be the same as in 1.

**How to run the code:**

1. You can check for all the inputs using:

            rmsynthesis -h
            
2. The require inputs (non-optional inputs are Stokes Q and U, and a frequency file). 


            rmsynthesis -q Q.fits -u U.fits -f freq.txt 
            
3. If you want your outputs to have a certain name, then you can specify the prefix by adding:

            rmsynthesis -q Q.fits -u U.fits -f freq.txt -o myprefix
            
4. You have an option to specify the range of Faraday depth by specifying the maximum, mininum and the sample width. These are in rad/m^2.

            rmsynthesis -q Q.fits -u U.fits -f freq.txt -rn -3000 -rx 3000 -rs 30

5. Another option is to include multiprocessing. This is highly recommended for speeding up the process especially if you going to be dealing with large images. 

            rmsynthesis -q Q.fits -u U.fits -f freq.txt -np 3

NB: 3 is the number of cores to use.


