# Generated with SMOP  0.41
from libsmop import *
# SiStER_get_elastic_moduli.m

    
@function
def SiStER_get_elastic_moduli(im=None,MAT=None,*args,**kwargs):
    varargin = SiStER_get_elastic_moduli.varargin
    nargin = SiStER_get_elastic_moduli.nargin

    # [ys]=SiStER_get_elastic_moduli(im,MAT)
# obtain shear modulus from material properties
# B. Klein 9/16
    
    Gm=zeros(size(im))
# SiStER_get_elastic_moduli.m:6
    types=unique(im)
# SiStER_get_elastic_moduli.m:8
    for i in arange(1,length(types)).reshape(-1):
        imInd=im == types(i)
# SiStER_get_elastic_moduli.m:10
        Gm[imInd]=MAT(types(i)).G
# SiStER_get_elastic_moduli.m:11
    
    # faster than:
# Gm=[MAT(im).G];
    