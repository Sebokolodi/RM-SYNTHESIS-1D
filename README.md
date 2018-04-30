RM-Synthesis is technique used to transform polarized intensity between wavelength-space (lambda) and faraday-space (RM). The details can be found in Brentjen & de Bruyn (2005).

This technqiue becomes computationally expensive in wide-field and large spectral coverage data. Particular, if one is to compute a Fourier transform for all pixels -- e.g such is necessary for all-sky surveys. Thus, it is appropriate and relevant that we seek to optimize this technique. In the original implementation, each plane in lambda-space was considered at once, although this is reasonable and much faster, it becomes infeasible for large dataset (Memory problem).

In our RM-Synthesis code, we evaluate each pixel individually but we have implemented multiprocessing (and we intend to extend this to GPUs) so that multiple cores can look at different pixels at once.

1. Installation:







2. Executing

