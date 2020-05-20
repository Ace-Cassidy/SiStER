# Generated with SMOP  0.41
from libsmop import *
# SiStER_get_friction.m

    
@function
def SiStER_get_friction(im=None,ep=None,MAT=None,*args,**kwargs):
    varargin = SiStER_get_friction.varargin
    nargin = SiStER_get_friction.nargin

    # [fric]=SiStER_get_friction(im,ep,MAT)
# compute friction on markers based on plastic strain, like cohesion
# J.-A. Olive 4/2017
    
    fric=zeros(size(im))
# SiStER_get_friction.m:7
    types=unique(im)
# SiStER_get_friction.m:9
    for i in arange(1,length(types)).reshape(-1):
        imInd=im == types(i)
# SiStER_get_friction.m:11
        mumax=MAT(types(i)).mu
# SiStER_get_friction.m:12
        if isfield(MAT,'mumin') == 1:
            mumin=MAT(types(i)).mumin
# SiStER_get_friction.m:15
        else:
            mumin=MAT(types(i)).mu
# SiStER_get_friction.m:17
        epscrit=MAT(types(i)).ecrit
# SiStER_get_friction.m:20
        fric[imInd]=max(mumax + multiply((mumin - mumax),ep(imInd)) / epscrit,mumin)
# SiStER_get_friction.m:23
    
    return fric
    ## OLD (slow due to brackets)
# mumax=[MAT(im).mu];
# 
# 
# if isfield(MAT,'mumin')==1  
#     mumin=[MAT(im).mumin];
# else
#     mumin=[MAT(im).mu];
# end
# 
# epscrit=[MAT(im).ecrit];
# 
# # get cohesion
# fric=max(mumax+(mumin-mumax).*ep./epscrit,mumin);
# 
# return