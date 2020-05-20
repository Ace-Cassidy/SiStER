# Generated with SMOP  0.41
from libsmop import *
# SiStER_interp_shear_nodes_to_markers.m

    
@function
def SiStER_interp_shear_nodes_to_markers(varS=None,x=None,y=None,xm=None,ym=None,icn=None,jcn=None,*args,**kwargs):
    varargin = SiStER_interp_shear_nodes_to_markers.varargin
    nargin = SiStER_interp_shear_nodes_to_markers.nargin

    # [varm]=SiStER_interp_shear_nodes_to_markers(varS,x,y,xm,ym,icn,jcn)
# interpolates properties from shear nodes to markers
    
    m,__=size(varS,nargout=2)
# SiStER_interp_shear_nodes_to_markers.m:5
    xnodes=concat([[x(jcn)],[x(jcn + 1)],[x(jcn + 1)],[x(jcn)]])
# SiStER_interp_shear_nodes_to_markers.m:7
    ynodes=concat([[y(icn)],[y(icn)],[y(icn + 1)],[y(icn + 1)]])
# SiStER_interp_shear_nodes_to_markers.m:8
    INDEX=sub2ind(size(varS),icn,jcn)
# SiStER_interp_shear_nodes_to_markers.m:10
    VARnodes=concat([[varS(INDEX)],[varS(INDEX + m)],[varS(INDEX + m + 1)],[varS(INDEX + 1)]])
# SiStER_interp_shear_nodes_to_markers.m:11
    varm=SiStER_interp_grid_to_marker_vector(xnodes,ynodes,VARnodes,xm,ym)
# SiStER_interp_shear_nodes_to_markers.m:13
    return varm
    
if __name__ == '__main__':
    pass
    