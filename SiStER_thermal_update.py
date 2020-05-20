# Generated with SMOP  0.41
from libsmop import *
# SiStER_thermal_update.m

    # SiStER THERMAL SOLVE
    
    # get previous temperature on nodes
    n2interp=SiStER_interp_markers_to_shear_nodes(xm,ym,icn,jcn,qd,x,y,Tm)
# SiStER_thermal_update.m:4
    Told[arange(),arange()]=n2interp(1).data
# SiStER_thermal_update.m:5
    # enforce Dirichlet boundary conditions to avoid mismatch between markers
# and nodes
    if BCtherm.top(1) == 1:
        Told[1,arange()]=BCtherm.top(2)
# SiStER_thermal_update.m:11
    
    if BCtherm.bot(1) == 1:
        Told[Ny,arange()]=BCtherm.bot(2)
# SiStER_thermal_update.m:14
    
    if BCtherm.left(1) == 1:
        Told[arange(),1]=BCtherm.left(2)
# SiStER_thermal_update.m:17
    
    if BCtherm.right(1) == 1:
        Told[arange(),Nx]=BCtherm.right(2)
# SiStER_thermal_update.m:20
    
    # GET VARIABLE DIFFUSIVITY AND CP
    if isfield(MAT,'cp') == 0 or isfield(MAT,'k') == 0:
        cpfield=dot(PARAMS.cpref,ones(size(T)))
# SiStER_thermal_update.m:27
        kfield=dot(PARAMS.kref,ones(size(T)))
# SiStER_thermal_update.m:28
        rhofield=dot(PARAMS.rhoref,ones(size(T)))
# SiStER_thermal_update.m:29
    else:
        km,cpm=SiStER_get_thermal_properties(im,MAT,nargout=2)
# SiStER_thermal_update.m:31
        rhom=SiStER_get_density(im,Tm,MAT)
# SiStER_thermal_update.m:32
        n2interp=SiStER_interp_markers_to_shear_nodes(xm,ym,icn,jcn,qd,x,y,km,cpm,rhom)
# SiStER_thermal_update.m:33
        kfield=n2interp(1).data
# SiStER_thermal_update.m:34
        cpfield=n2interp(2).data
# SiStER_thermal_update.m:35
        rhofield=n2interp(3).data
# SiStER_thermal_update.m:36
    
    # THERMAL SOLVE
    T=SiStER_thermal_solver_sparse_CFD(x,y,Told,rhofield,cpfield,kfield,dt_m,BCtherm,zeros(size(T)))
# SiStER_thermal_update.m:40
    # temperature change
    dT=T - Told
# SiStER_thermal_update.m:45
    # enforce Dirichlet boundary conditions to avoid mismatch between markers
# and nodes
    if BCtherm.top(1) == 1:
        dT[1,arange()]=0
# SiStER_thermal_update.m:49
    
    if BCtherm.bot(1) == 1:
        dT[Ny,arange()]=0
# SiStER_thermal_update.m:52
    
    if BCtherm.left(1) == 1:
        dT[arange(),1]=0
# SiStER_thermal_update.m:55
    
    if BCtherm.right(1) == 1:
        dT[arange(),Nx]=0
# SiStER_thermal_update.m:58
    
    Tm=SiStER_interp_shear_nodes_to_markers(T,x,y,xm,ym,icn,jcn)
# SiStER_thermal_update.m:61
    if PARAMS.ynTreset == 1:
        Tm[im == 1]=PARAMS.T0
# SiStER_thermal_update.m:64
    