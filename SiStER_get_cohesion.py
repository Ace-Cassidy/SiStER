# Generated with SMOP  0.41
from libsmop import *
# SiStER_get_cohesion.m

    
@function
def SiStER_get_cohesion(im=None,ep=None,MAT=None,*args,**kwargs):
    varargin = SiStER_get_cohesion.varargin
    nargin = SiStER_get_cohesion.nargin

    # [cohes]=SiStER_get_cohesion(im,ep,MAT)
# compute cohesion on markers based on ep
#G.Ito 8/2016
# sped up by B. Klein 9/2016
    
    cohes=zeros(size(im))
# SiStER_get_cohesion.m:7
    types=unique(im)
# SiStER_get_cohesion.m:9
    for i in arange(1,length(types)).reshape(-1):
        imInd=im == types(i)
# SiStER_get_cohesion.m:11
        Cmax=MAT(types(i)).Cmax
# SiStER_get_cohesion.m:12
        Cmin=MAT(types(i)).Cmin
# SiStER_get_cohesion.m:13
        epscrit=MAT(types(i)).ecrit
# SiStER_get_cohesion.m:14
        cohes[imInd]=max(Cmax + multiply((Cmin - Cmax),ep(imInd)) / epscrit,Cmin)
# SiStER_get_cohesion.m:17
    
    return cohes
    ## OLD VERSION the bracket approach is really slow
# 
# Cmax=[MAT(im).Cmax];
# Cmin=[MAT(im).Cmin];
# epscrit=[MAT(im).ecrit];
# 
# # get cohesion
# cohes=max(Cmax+(Cmin-Cmax).*ep./epscrit,Cmin);
# 
# return
    