RM-Synthesis is technique used to transform polarized intensity between wavelength-space (lambda) and faraday-space (RM). See Brentjen & de Bruyn (2005) for more detail. 

This technqiue can become computationally expensive. Thus, great care is required. For example, wide-field views imply a large number of line-of-sights (pixels) to evaluate, and wide spectral-bandwidth, although necessary, imply a large number of channels to average across. Thus, optimizing RM-Synthesis technqiue is important. Particularly, for all-sky surveys where a Fourier transformation needs to be performed for a large number of pixels.
In the original implementation, all pixels within lambda^2-plane are evaluated at once. Although this is mcuh, it becomes infeasible for large dataset (Memory problem).

In our RM-Synthesis code, we evaluate each pixel individually but we have implemented multiprocessing (and we intend to extend this to GPUs) so that multiple cores can look at different pixels at once.

1. Installation:







2. Executing

