# Generated with SMOP  0.41
from libsmop import *
# SiStER_initialize_marker_positions.m

    
@function
def SiStER_initialize_marker_positions(xsize=None,ysize=None,dx=None,dy=None,Mquad=None,*args,**kwargs):
    varargin = SiStER_initialize_marker_positions.varargin
    nargin = SiStER_initialize_marker_positions.nargin

    # [xm, ym] = SiStER_initialize_marker_positions(xsize,ysize,dx,dy,Mquad)
# assigns markers their inital position (coordinates)
# markers are seeded by cell quadrant, to make sure there is enough of them
# in each quadrant
    
    # smallest quadrant sizes
    mdx=min(dx) / 2
# SiStER_initialize_marker_positions.m:10
    mdy=min(dy) / 2
# SiStER_initialize_marker_positions.m:11
    # creating a regular grid with step = that of the smallest quadrant
    xx=arange(0,xsize,mdx)
# SiStER_initialize_marker_positions.m:14
    yy=arange(0,ysize,mdy)
# SiStER_initialize_marker_positions.m:15
    nxx=length(xx)
# SiStER_initialize_marker_positions.m:17
    nyy=length(yy)
# SiStER_initialize_marker_positions.m:18
    midx=1
# SiStER_initialize_marker_positions.m:21
    for i in arange(1,nyy - 1).reshape(-1):
        for j in arange(1,nxx - 1).reshape(-1):
            xmtemp,ymtemp=SiStER_seed_markers_uniformly(xx(j),yy(i),mdx,mdy,Mquad,nargout=2)
# SiStER_initialize_marker_positions.m:25
            xm[arange(midx,midx + Mquad - 1)]=xmtemp
# SiStER_initialize_marker_positions.m:26
            ym[arange(midx,midx + Mquad - 1)]=ymtemp
# SiStER_initialize_marker_positions.m:27
            midx=midx + Mquad
# SiStER_initialize_marker_positions.m:28
    