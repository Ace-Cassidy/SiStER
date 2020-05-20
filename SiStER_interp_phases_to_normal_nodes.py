# Generated with SMOP  0.41
from libsmop import *
# SiStER_interp_phases_to_normal_nodes.m

    
@function
def SiStER_interp_phases_to_normal_nodes(xm=None,ym=None,icn=None,jcn=None,x=None,y=None,phases=None,maxPhases=None,*args,**kwargs):
    varargin = SiStER_interp_phases_to_normal_nodes.varargin
    nargin = SiStER_interp_phases_to_normal_nodes.nargin

    # [phaseWeights] = SiStER_interp_phases_to_normal_nodes(xm,ym,icn,jcn,x,y,phases, maxPhases)
# B.Z. Klein, July 2017, an interp function specific to phase (for normal nodes), to enable 
# exact mixing of several phases
    
    Nx=length(x)
# SiStER_interp_phases_to_normal_nodes.m:6
    Ny=length(y)
# SiStER_interp_phases_to_normal_nodes.m:7
    dx=diff(x)
# SiStER_interp_phases_to_normal_nodes.m:8
    dy=diff(y)
# SiStER_interp_phases_to_normal_nodes.m:9
    INDEX=sub2ind(concat([Ny - 1,Nx - 1]),icn,jcn)
# SiStER_interp_phases_to_normal_nodes.m:12
    AcCell=bsxfun(times,dy.T,dx)
# SiStER_interp_phases_to_normal_nodes.m:14
    xN=x(arange(1,Nx - 1)) + dx / 2
# SiStER_interp_phases_to_normal_nodes.m:16
    yN=y(arange(1,Ny - 1)) + dy / 2
# SiStER_interp_phases_to_normal_nodes.m:17
    XN,YN=meshgrid(xN,yN,nargout=2)
# SiStER_interp_phases_to_normal_nodes.m:18
    AMvec=abs(multiply((xm - XN(INDEX)),(ym - YN(INDEX))))
# SiStER_interp_phases_to_normal_nodes.m:20
    WMvec=(AcCell(INDEX) - AMvec) / AcCell(INDEX)
# SiStER_interp_phases_to_normal_nodes.m:21
    phaseWeights=zeros(Ny,Nx,maxPhases)
# SiStER_interp_phases_to_normal_nodes.m:23
    for n in arange(1,maxPhases).reshape(-1):
        phaseMask=phases == n
# SiStER_interp_phases_to_normal_nodes.m:27
        phaseWeights[arange(2,Ny),arange(2,Nx),n]=accumarray(concat([icn(phaseMask).T,jcn(phaseMask).T]),WMvec(phaseMask).T,size(AcCell),sum)
# SiStER_interp_phases_to_normal_nodes.m:28
    
    
    sumWeights=repmat(sum(phaseWeights,3),concat([1,1,maxPhases]))
# SiStER_interp_phases_to_normal_nodes.m:32
    phaseWeights=phaseWeights / sumWeights
# SiStER_interp_phases_to_normal_nodes.m:33
    return phaseWeights
    
if __name__ == '__main__':
    pass
    