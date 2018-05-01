RM-Synthesis is technique used to transform polarized intensity between wavelength-space (lambda) and faraday-space (RM). See Brentjen & de Bruyn (2005) for more detail. 

This technqiue can become computationally expensive. Thus, great care is required. For example, wide-field views imply a large number of line-of-sights (pixels) to evaluate, and wide spectral-bandwidth (> 1000s of channels) increases the computation required. Particular, if one is to compute a Fourier transform for all pixels -- e.g such is necessary for all-sky surveys. Thus, it is appropriate and relevant that we seek to optimize this technique. In the original implementation, each plane in lambda-space was considered at once, although this is reasonable and much faster, it becomes infeasible for large dataset (Memory problem).

In our RM-Synthesis code, we evaluate each pixel individually but we have implemented multiprocessing (and we intend to extend this to GPUs) so that multiple cores can look at different pixels at once.

1. Installation:







2. Executing

