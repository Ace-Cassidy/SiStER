# Generated with SMOP  0.41
from libsmop import *
# SiStER_set_timestep.m

    
@function
def SiStER_set_timestep(dx=None,dy=None,vx=None,vy=None,PARAMS=None,*args,**kwargs):
    varargin = SiStER_set_timestep.varargin
    nargin = SiStER_set_timestep.nargin

    # [dt_m]=SiStER_set_timestep(dx,dy,vx,vy,PARAMS)
# sets the advection time step
# J.-A. Olive, November 2014
    
    dt_m=dot(dot(PARAMS.fracCFL,0.5),min(min(dx),min(dy))) / max(max(max(abs(vx))),max(max(abs(vy))))
# SiStER_set_timestep.m:6