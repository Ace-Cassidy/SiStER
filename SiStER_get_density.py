# Generated with SMOP  0.41
from libsmop import *
# SiStER_get_density.m

    
@function
def SiStER_get_density(im=None,Tm=None,MAT=None,*args,**kwargs):
    varargin = SiStER_get_density.varargin
    nargin = SiStER_get_density.nargin

    # [rho]=SiStER_get_density(im,Tm,MAT)
# obtain density from temperature and material identity
# 
# edited by B. Klein, 9/20/2016 to remove struct indexing concatenating
    
    T0=0
# SiStER_get_density.m:7
    rhom=zeros(size(im))
# SiStER_get_density.m:8
    types=unique(im)
# SiStER_get_density.m:10
    for i in arange(1,length(types)).reshape(-1):
        logical=im == types(i)
# SiStER_get_density.m:12
        rho0=MAT(types(i)).rho0
# SiStER_get_density.m:13
        alpha=MAT(types(i)).alpha
# SiStER_get_density.m:14
        rhom[logical]=multiply(rho0,(1 - multiply(alpha,(Tm(logical) - T0))))
# SiStER_get_density.m:15
    
    # OLD WAY (slow)
#T0=0;
#rhom = [MAT(im).rho0].*(1-[MAT(im).alpha].*(Tm-T0));
    