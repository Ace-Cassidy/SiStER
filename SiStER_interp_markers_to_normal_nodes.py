# Generated with SMOP  0.41
from libsmop import *
# SiStER_interp_markers_to_normal_nodes.m

    
@function
def SiStER_interp_markers_to_normal_nodes(xm=None,ym=None,icn=None,jcn=None,x=None,y=None,varargin=None,*args,**kwargs):
    varargin = SiStER_interp_markers_to_normal_nodes.varargin
    nargin = SiStER_interp_markers_to_normal_nodes.nargin

    # [n2interp] = SiStER_interp_markers_to_normal_nodes(xm,ym,icn,jcn,x,y,varargin)
# interpolates properties (in the order of input) from markers to normal nodes
    
    # First cut - J.A. Olive, March 2011
# Modified by E. Mittelstaedt, April 2011 to allow multiple inputs  
# Modified by B.Z. Klein, Spring 2014 for speedup
    
    Nx=length(x)
# SiStER_interp_markers_to_normal_nodes.m:9
    Ny=length(y)
# SiStER_interp_markers_to_normal_nodes.m:10
    dx=diff(x)
# SiStER_interp_markers_to_normal_nodes.m:11
    dy=diff(y)
# SiStER_interp_markers_to_normal_nodes.m:12
    # check for number of properties to interpolate
    numV=size(varargin,2)
# SiStER_interp_markers_to_normal_nodes.m:15
    n2interp[arange(1,numV)]=struct('data',zeros(Ny,Nx))
# SiStER_interp_markers_to_normal_nodes.m:16
    INDEX=sub2ind(concat([Ny - 1,Nx - 1]),icn,jcn)
# SiStER_interp_markers_to_normal_nodes.m:18
    AcCell=bsxfun(times,dy.T,dx)
# SiStER_interp_markers_to_normal_nodes.m:20
    xN=x(arange(1,Nx - 1)) + dx / 2
# SiStER_interp_markers_to_normal_nodes.m:22
    yN=y(arange(1,Ny - 1)) + dy / 2
# SiStER_interp_markers_to_normal_nodes.m:23
    XN,YN=meshgrid(xN,yN,nargout=2)
# SiStER_interp_markers_to_normal_nodes.m:24
    AMvec=abs(multiply((xm - XN(INDEX)),(ym - YN(INDEX))))
# SiStER_interp_markers_to_normal_nodes.m:26
    WMvec=(AcCell(INDEX) - AMvec) / AcCell(INDEX)
# SiStER_interp_markers_to_normal_nodes.m:27
    w=accumarray(concat([icn.T,jcn.T]),WMvec.T,[],sum)
# SiStER_interp_markers_to_normal_nodes.m:29
    for vn in arange(1,numV).reshape(-1):
        VecData=multiply(varargin[vn],WMvec)
# SiStER_interp_markers_to_normal_nodes.m:32
        n2interp(vn).data[arange(2,Ny),arange(2,Nx)]=accumarray(concat([icn.T,jcn.T]),VecData.T,[],sum) / w
# SiStER_interp_markers_to_normal_nodes.m:33
    
    return n2interp
    
if __name__ == '__main__':
    pass
    