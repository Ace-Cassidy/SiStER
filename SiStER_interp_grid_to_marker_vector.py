# Generated with SMOP  0.41
from libsmop import *
# SiStER_interp_grid_to_marker_vector.m

    
@function
def SiStER_interp_grid_to_marker_vector(xnodes=None,ynodes=None,paramnodes=None,xm=None,ym=None,*args,**kwargs):
    varargin = SiStER_interp_grid_to_marker_vector.varargin
    nargin = SiStER_interp_grid_to_marker_vector.nargin

    # [param] = SiStER_interp_grid_to_marker_vector(xnodes,ynodes,paramnodes,xm,ym)
# interpolates a grid value to the entire vector of markers,
# used by SiStER_get_marker_velocities
# B.Z. Klein, 2013
    
    dxm=(xm - xnodes(1,arange()))
# SiStER_interp_grid_to_marker_vector.m:7
    dym=(ym - ynodes(1,arange()))
# SiStER_interp_grid_to_marker_vector.m:8
    dx=abs(xnodes(2,arange()) - xnodes(1,arange()))
# SiStER_interp_grid_to_marker_vector.m:9
    dy=abs(ynodes(3,arange()) - ynodes(2,arange()))
# SiStER_interp_grid_to_marker_vector.m:10
    w1=multiply((1 - dxm / dx),(1 - dym / dy))
# SiStER_interp_grid_to_marker_vector.m:12
    w2=multiply((dxm / dx),(1 - dym / dy))
# SiStER_interp_grid_to_marker_vector.m:13
    w4=multiply((dym / dy),(1 - dxm / dx))
# SiStER_interp_grid_to_marker_vector.m:14
    w3=multiply((dxm / dx),(dym / dy))
# SiStER_interp_grid_to_marker_vector.m:15
    wnodes=concat([[w1],[w2],[w3],[w4]])
# SiStER_interp_grid_to_marker_vector.m:16
    param=sum(multiply(paramnodes,wnodes),1)
# SiStER_interp_grid_to_marker_vector.m:18
    return param
    
if __name__ == '__main__':
    pass
    