# Generated with SMOP  0.41
from libsmop import *
# SiStER_advect_markers.m

    
@function
def SiStER_advect_markers(x=None,y=None,xm=None,ym=None,dx=None,dy=None,tstep=None,vx=None,vy=None,*args,**kwargs):
    varargin = SiStER_advect_markers.varargin
    nargin = SiStER_advect_markers.nargin

    # [xm_new,ym_new,vx_eff,vy_eff] = SiStER_advect_markers(x,y,xm,ym,dx,dy,tstep,vx,vy)
    
    # Uses a Fourth-Order Runge-Kutta method to advect markers 
# in the current velocity field, over the advection time step tstep = dt_m
    
    # First cut J.-A. Olive, 2011-2012 - modified by B.Z. Klein 2013-2014
    
    # point A (particle pts)
    XA=copy(xm)
# SiStER_advect_markers.m:11
    YA=copy(ym)
# SiStER_advect_markers.m:12
    qd,icn,jcn=SiStER_locate_markers_in_grid(XA,YA,x,y,dx,dy,nargout=3)
# SiStER_advect_markers.m:13
    VxA,VyA=SiStER_get_marker_velocities(qd,icn,jcn,x,y,xm,ym,vx,vy,dx,dy,nargout=2)
# SiStER_advect_markers.m:14
    # point B
    XB=XA + dot(dot(0.5,tstep),VxA)
# SiStER_advect_markers.m:17
    YB=YA + dot(dot(0.5,tstep),VyA)
# SiStER_advect_markers.m:18
    qd,icn,jcn=SiStER_locate_markers_in_grid(XB,YB,x,y,dx,dy,nargout=3)
# SiStER_advect_markers.m:19
    VxB,VyB=SiStER_get_marker_velocities(qd,icn,jcn,x,y,xm,ym,vx,vy,dx,dy,nargout=2)
# SiStER_advect_markers.m:20
    # point C
    XC=XA + dot(dot(0.5,tstep),VxB)
# SiStER_advect_markers.m:23
    YC=YA + dot(dot(0.5,tstep),VyB)
# SiStER_advect_markers.m:24
    qd,icn,jcn=SiStER_locate_markers_in_grid(XC,YC,x,y,dx,dy,nargout=3)
# SiStER_advect_markers.m:25
    VxC,VyC=SiStER_get_marker_velocities(qd,icn,jcn,x,y,xm,ym,vx,vy,dx,dy,nargout=2)
# SiStER_advect_markers.m:26
    # point D
    XD=XA + dot(tstep,VxC)
# SiStER_advect_markers.m:29
    YD=YA + dot(tstep,VyC)
# SiStER_advect_markers.m:30
    qd,icn,jcn=SiStER_locate_markers_in_grid(XD,YD,x,y,dx,dy,nargout=3)
# SiStER_advect_markers.m:31
    VxD,VyD=SiStER_get_marker_velocities(qd,icn,jcn,x,y,xm,ym,vx,vy,dx,dy,nargout=2)
# SiStER_advect_markers.m:32
    # effective velocity
    vx_eff=dot((1 / 6),(VxA + dot(2,VxB) + dot(2,VxC) + VxD))
# SiStER_advect_markers.m:36
    vy_eff=dot((1 / 6),(VyA + dot(2,VyB) + dot(2,VyC) + VyD))
# SiStER_advect_markers.m:37
    ## Calculate new coordinates
    
    PP[arange(),1]=XA + dot(tstep,vx_eff)
# SiStER_advect_markers.m:42
    PP[arange(),2]=YA + dot(tstep,vy_eff)
# SiStER_advect_markers.m:43
    xm_new=PP(arange(),1).T
# SiStER_advect_markers.m:45
    ym_new=PP(arange(),2).T
# SiStER_advect_markers.m:46