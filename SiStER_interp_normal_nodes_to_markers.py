# Generated with SMOP  0.41
from libsmop import *
# SiStER_interp_normal_nodes_to_markers.m

    
@function
def SiStER_interp_normal_nodes_to_markers(varN=None,xc=None,yc=None,xm=None,ym=None,icn=None,jcn=None,*args,**kwargs):
    varargin = SiStER_interp_normal_nodes_to_markers.varargin
    nargin = SiStER_interp_normal_nodes_to_markers.nargin

    # [varm]=SiStER_interp_normal_nodes_to_markers(varN,xc,yc,xm,ym,icn,jcn)
# interpolates properties from normal nodes to markers
# J.-A. Olive, 2011 (First cut)
# B.Z. Klein, 2014 (speedup)
    
    Nx=length(xc) + 1
# SiStER_interp_normal_nodes_to_markers.m:7
    Ny=length(yc) + 1
# SiStER_interp_normal_nodes_to_markers.m:8
    m,__=size(varN,nargout=2)
# SiStER_interp_normal_nodes_to_markers.m:9
    ic=copy(icn)
# SiStER_interp_normal_nodes_to_markers.m:11
    jc=copy(jcn)
# SiStER_interp_normal_nodes_to_markers.m:12
    jc[xm > xc(jc)]=jc(xm > xc(jc)) + 1
# SiStER_interp_normal_nodes_to_markers.m:14
    jc[jc < 2]=2
# SiStER_interp_normal_nodes_to_markers.m:15
    jc[jc > Nx - 1]=Nx - 1
# SiStER_interp_normal_nodes_to_markers.m:16
    ic[ym > yc(ic)]=ic(ym > yc(ic)) + 1
# SiStER_interp_normal_nodes_to_markers.m:18
    ic[ic < 2]=2
# SiStER_interp_normal_nodes_to_markers.m:19
    ic[ic > Ny - 1]=Ny - 1
# SiStER_interp_normal_nodes_to_markers.m:20
    xNnodes=concat([[xc(jc - 1)],[xc(jc)],[xc(jc)],[xc(jc - 1)]])
# SiStER_interp_normal_nodes_to_markers.m:22
    yNnodes=concat([[yc(ic - 1)],[yc(ic - 1)],[yc(ic)],[yc(ic)]])
# SiStER_interp_normal_nodes_to_markers.m:23
    IND=sub2ind(size(varN),ic,jc)
# SiStER_interp_normal_nodes_to_markers.m:25
    VARnodes=concat([[varN(IND)],[varN(IND + m)],[varN(IND + 1 + m)],[varN(IND + 1)]])
# SiStER_interp_normal_nodes_to_markers.m:26
    varm=SiStER_interp_grid_to_marker_vector(xNnodes,yNnodes,VARnodes,xm,ym)
# SiStER_interp_normal_nodes_to_markers.m:28