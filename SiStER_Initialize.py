# Generated with SMOP  0.41
from libsmop import *
# SiStER_Initialize.m

    # SiStER Initialize
    
    PARAMS.Nphase = copy(Nphase)
# SiStER_Initialize.m:3
    
    # construct staggered grids
    X,Y,x,y,xc,yc,dx,dy,Nx,Ny=SiStER_initialize_grid(xsize,ysize,GRID,nargout=10)
# SiStER_Initialize.m:6
    # initialize marker arrays and positions
    xm,ym=SiStER_initialize_marker_positions(xsize,ysize,dx,dy,Mquad,nargout=2)
# SiStER_Initialize.m:9
    # locate markers with respect to grid
    qd,icn,jcn=SiStER_locate_markers_in_grid(xm,ym,x,y,dx,dy,nargout=3)
# SiStER_Initialize.m:12
    # assign marker phases
    im=SiStER_initialize_marker_phases(Nphase,GEOM,xm,ym)
# SiStER_Initialize.m:15
    # initialize marker plastic strain (to zero) and strain rate (to one)
    ep=zeros(size(xm))
# SiStER_Initialize.m:17
    epNH=copy(ep)
# SiStER_Initialize.m:18
    epsIIm=ones(size(xm))
# SiStER_Initialize.m:19
    # initialize marker stresses
    sxxm=zeros(size(xm))
# SiStER_Initialize.m:22
    sxym=copy(sxxm)
# SiStER_Initialize.m:23
    # initialize marker index (a unique number to identify and track each marker)
    idm=arange(1,length(xm))
# SiStER_Initialize.m:26
    # initialize temperature structure on nodes
    T=PARAMS.a0 + dot(PARAMS.a1,Y) + dot(PARAMS.a2,Y ** 2) + dot(PARAMS.a3,Y ** 3)
# SiStER_Initialize.m:29
    T=T + dot(PARAMS.amp,sin(dot(dot(2,pi),X) / PARAMS.lam))
# SiStER_Initialize.m:30
    if PARAMS.ynTreset == 1:
        T[T < PARAMS.T0]=PARAMS.T0
# SiStER_Initialize.m:32
    
    # pass initial nodal T to markers
    Tm=SiStER_interp_shear_nodes_to_markers(T,x,y,xm,ym,icn,jcn)
# SiStER_Initialize.m:35
    Tm0=copy(Tm)
# SiStER_Initialize.m:36
    # initialize nodal strain rate and other useful arrays
    EXX=zeros(size(X))
# SiStER_Initialize.m:39
    EXY=zeros(size(X))
# SiStER_Initialize.m:40
    vx=zeros(size(X))
# SiStER_Initialize.m:41
    vy=zeros(size(X))
# SiStER_Initialize.m:42
    v=copy(vx)
# SiStER_Initialize.m:43
    p=dot(1e+12,ones(size(EXX)))
# SiStER_Initialize.m:44
    
    etan_new=zeros(Ny,Nx)
# SiStER_Initialize.m:45
    #-------------------------------------------------------------------------
# initialize dt_m small to keep things elastic & no plasticity at t=1, G.Ito
#-------------------------------------------------------------------------
    if (exist('dt_m','var') == 0):
        dt_m=100.0
# SiStER_Initialize.m:50
    
    # initialize marker chain to track base of layer 1 (sticky layer)
    Ntopo=PARAMS.Ntopo_markers
# SiStER_Initialize.m:54
    topo_x=linspace(0,xsize,Ntopo)
# SiStER_Initialize.m:55
    topo_y=dot(GEOM(1).bot,ones(size(topo_x)))
# SiStER_Initialize.m:56
    topo_marker_spacing=mean(diff(topo_x))
# SiStER_Initialize.m:57
    