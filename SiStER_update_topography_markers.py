# Generated with SMOP  0.41
from libsmop import *
# SiStER_update_topography_markers.m

    # SiStER_update_topography_markers
    
    # advect the marker chain that keeps track of topography 
# in the current flow field
    topo_x,topo_y=SiStER_advect_markers(x,y,topo_x,topo_y,dx,dy,dt_m,vx,vy,nargout=2)
# SiStER_update_topography_markers.m:5
    # locate the interface between sticky layer and left / right edge
    if isempty(find(topo_x < 0,1)) == 1:
        topoL=topo_y(1)
# SiStER_update_topography_markers.m:9
    else:
        topoL=interp1(topo_x,topo_y,0)
# SiStER_update_topography_markers.m:11
    
    if isempty(find(topo_x > xsize,1)) == 1:
        topoR=topo_y(end())
# SiStER_update_topography_markers.m:15
    else:
        topoR=interp1(topo_x,topo_y,xsize)
# SiStER_update_topography_markers.m:17
    
    # eliminate topography markers that left domain, keep the first one out on both sides
    Iin=find(topo_x < logical_and(xsize,topo_x) > 0)
# SiStER_update_topography_markers.m:21
    topo_x=topo_x(Iin)
# SiStER_update_topography_markers.m:22
    topo_y=topo_y(Iin)
# SiStER_update_topography_markers.m:23
    topo_x=concat([0,topo_x,xsize])
# SiStER_update_topography_markers.m:24
    topo_y=concat([topoL,topo_y,topoR])
# SiStER_update_topography_markers.m:25
    if PARAMS.YNSurfaceProcesses == 1:
        # ERODE TOPOGRAPHY
        topo_y=SiStER_topography_diffusion_solver(topo_x,topo_y,dt_m,PARAMS.topo_kappa)
# SiStER_update_topography_markers.m:29
        topomarkers=interp1(topo_x,topo_y,xm)
# SiStER_update_topography_markers.m:31
        im[im == logical_and(1,ym) >= topomarkers]=2
# SiStER_update_topography_markers.m:32
        im[im >= logical_and(2,ym) < topomarkers]=1
# SiStER_update_topography_markers.m:33
    
    # if there has been too much stretching, regrid the surface topography
    if max(diff(topo_x)) > dot(5,topo_marker_spacing) or issorted(topo_x) == 0:
        # surface regridding happens if somewhere 2 topo markers have been
    # stretched apart by more than 5 times the inital mean marker spacing
    # or if topo_x is no longer sorted due to compression.
        topo_xREGRID=linspace(0,xsize,Ntopo)
# SiStER_update_topography_markers.m:41
        topo_yREGRID=interp1(topo_x,topo_y,topo_xREGRID(arange(2,end() - 1)))
# SiStER_update_topography_markers.m:42
        topo_yREGRID=concat([topoL,topo_yREGRID,topoR])
# SiStER_update_topography_markers.m:43
        topo_x=copy(topo_xREGRID)
# SiStER_update_topography_markers.m:44
        topo_y=copy(topo_yREGRID)
# SiStER_update_topography_markers.m:45
        disp('**REGRIDDING TOPOGRAPHY MARKERS**')
    