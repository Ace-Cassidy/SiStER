# Generated with SMOP  0.41
from libsmop import *
# SiStER_get_thermal_properties.m

    
@function
def SiStER_get_thermal_properties(im=None,MAT=None,*args,**kwargs):
    varargin = SiStER_get_thermal_properties.varargin
    nargin = SiStER_get_thermal_properties.nargin

    # [km, cpm]=SiStER_get_thermal_properties(im,MAT)
# obtain thermal conductivity and heat capacity
    
    km=zeros(size(im))
# SiStER_get_thermal_properties.m:5
    cpm=copy(km)
# SiStER_get_thermal_properties.m:6
    types=unique(im)
# SiStER_get_thermal_properties.m:8
    for i in arange(1,length(types)).reshape(-1):
        imInd=im == types(i)
# SiStER_get_thermal_properties.m:10
        km[imInd]=MAT(types(i)).k
# SiStER_get_thermal_properties.m:11
        cpm[imInd]=MAT(types(i)).cp
# SiStER_get_thermal_properties.m:12
    