# Generated with SMOP  0.41
from libsmop import *
# SiStER_seed_markers_uniformly.m

    
@function
def SiStER_seed_markers_uniformly(x=None,y=None,dx=None,dy=None,N=None,*args,**kwargs):
    varargin = SiStER_seed_markers_uniformly.varargin
    nargin = SiStER_seed_markers_uniformly.nargin

    # [xm, ym]=SiStER_seed_markers_uniformly(x,y,dx,dy,N)
# seeds N markers in the cell or quadrant whose upper-left node 
# has coordinates (x,y) and width, height (dx,dy)
    
    # create a subgrid
    
    fact=0.4
# SiStER_seed_markers_uniformly.m:9
    
    nx=ceil(sqrt(dot(N,dx) / dy))
# SiStER_seed_markers_uniformly.m:11
    ny=ceil(N / nx)
# SiStER_seed_markers_uniformly.m:12
    actual_N=dot(nx,ny)
# SiStER_seed_markers_uniformly.m:13
    ddx=linspace(x,x + dx,nx + 1)
# SiStER_seed_markers_uniformly.m:15
    ddy=linspace(y,y + dy,ny + 1)
# SiStER_seed_markers_uniformly.m:16
    DX,DY=meshgrid(ddx,ddy,nargout=2)
# SiStER_seed_markers_uniformly.m:17
    xm=zeros(1,actual_N)
# SiStER_seed_markers_uniformly.m:19
    ym=copy(xm)
# SiStER_seed_markers_uniformly.m:20
    k=0
# SiStER_seed_markers_uniformly.m:22
    for i in arange(1,ny).reshape(-1):
        for j in arange(1,nx).reshape(-1):
            k=k + 1
# SiStER_seed_markers_uniformly.m:26
            xsub=DX(i,j)
# SiStER_seed_markers_uniformly.m:27
            ysub=DY(i,j)
# SiStER_seed_markers_uniformly.m:28
            dxsub=dx / nx
# SiStER_seed_markers_uniformly.m:29
            dysub=dy / ny
# SiStER_seed_markers_uniformly.m:30
            xm[k]=xsub + dot((dxsub / 2),(1 + dot(dot(fact,2),(rand - 0.5))))
# SiStER_seed_markers_uniformly.m:33
            ym[k]=ysub + dot((dysub / 2),(1 + dot(dot(fact,2),(rand - 0.5))))
# SiStER_seed_markers_uniformly.m:34
    
    if actual_N > N:
        idx=randperm(actual_N)
# SiStER_seed_markers_uniformly.m:42
        idx=idx(arange(1,N))
# SiStER_seed_markers_uniformly.m:43
        xm=xm(idx)
# SiStER_seed_markers_uniformly.m:44
        ym=ym(idx)
# SiStER_seed_markers_uniformly.m:45
    