# Generated with SMOP  0.41
from libsmop import *
# SiStER_initialize_marker_phases.m

    
@function
def SiStER_initialize_marker_phases(Nphase=None,GEOM=None,xm=None,ym=None,*args,**kwargs):
    varargin = SiStER_initialize_marker_phases.varargin
    nargin = SiStER_initialize_marker_phases.nargin

    # [im] = SiStER_initialize_marker_phases(Nphase,GEOM,xm,ym)
# this is where the identity of each marker (e.g., air, crust, mantle...)
# gets assigned following the geometry specified in the input file 
# (flat layers, circle or rectangle)
# an alternative geometry can be added here.
    
    # assign material identity on markers
    im=zeros(size(xm))
# SiStER_initialize_marker_phases.m:9
    for kk in arange(1,Nphase).reshape(-1):
        if GEOM(kk).type == 1:
            im[ym >= logical_and(GEOM(kk).top,ym) < GEOM(kk).bot]=kk
# SiStER_initialize_marker_phases.m:16
        else:
            if GEOM(kk).type == 2:
                rm=sqrt((xm - GEOM(kk).x0) ** 2 + (ym - GEOM(kk).y0) ** 2)
# SiStER_initialize_marker_phases.m:20
                im[rm <= GEOM(kk).rad]=kk
# SiStER_initialize_marker_phases.m:21
            else:
                if GEOM(kk).type == 3:
                    im[ym >= logical_and(GEOM(kk).top,ym) < logical_and(GEOM(kk).bot,xm) >= logical_and(GEOM(kk).left,xm) < GEOM(kk).right]=kk
# SiStER_initialize_marker_phases.m:25
    
    