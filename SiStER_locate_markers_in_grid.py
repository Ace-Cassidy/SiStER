# Generated with SMOP  0.41
from libsmop import *
# SiStER_locate_markers_in_grid.m

    
@function
def SiStER_locate_markers_in_grid(xm=None,ym=None,x=None,y=None,dx=None,dy=None,*args,**kwargs):
    varargin = SiStER_locate_markers_in_grid.varargin
    nargin = SiStER_locate_markers_in_grid.nargin

    # [quad,icn,jcn] = SiStER_locate_markers_in_grid(xm,ym,x,y,dx,dy)
# Tells a marker which cell (and which quadrant of that cell) it belongs to.
    # icn,jcn are the indexes of the upper-left shear node of the cell
    # that a given marker is currently in
    # quad is the quadrant of the cell that contains the marker
    # (quad = 1 means bottom-right, then numbered clockwise)
    # sped up by B. Klein in Fall 2016 by using interp1 function
    
    ## Determine Location of Markers and Quadrant of Element
    M=length(xm)
# SiStER_locate_markers_in_grid.m:12
    icn=zeros(1,M)
# SiStER_locate_markers_in_grid.m:13
    jcn=copy(icn)
# SiStER_locate_markers_in_grid.m:14
    quad=copy(icn)
# SiStER_locate_markers_in_grid.m:15
    
    indX=arange(1,length(x))
# SiStER_locate_markers_in_grid.m:17
    indY=arange(1,length(y))
# SiStER_locate_markers_in_grid.m:18
    Ix=interp1(x,indX,xm,'nearest','extrap')
# SiStER_locate_markers_in_grid.m:20
    Iy=interp1(y,indY,ym,'nearest','extrap')
# SiStER_locate_markers_in_grid.m:21
    # [~, Ix] = min(abs(bsxfun(@minus, xm, x')));
# [~, Iy] = min(abs(bsxfun(@minus, ym, y')));
    
    jcn[xm > x(Ix)]=Ix(xm > x(Ix))
# SiStER_locate_markers_in_grid.m:26
    jcn[xm <= x(Ix)]=Ix(xm <= x(Ix)) - 1
# SiStER_locate_markers_in_grid.m:27
    icn[ym > y(Iy)]=Iy(ym > y(Iy))
# SiStER_locate_markers_in_grid.m:29
    icn[ym <= y(Iy)]=Iy(ym <= y(Iy)) - 1
# SiStER_locate_markers_in_grid.m:30
    jcn[jcn == 0]=1
# SiStER_locate_markers_in_grid.m:32
    jcn[jcn > length(dx)]=length(dx)
# SiStER_locate_markers_in_grid.m:33
    icn[icn == 0]=1
# SiStER_locate_markers_in_grid.m:35
    icn[icn > length(dy)]=length(dy)
# SiStER_locate_markers_in_grid.m:36
    disx=abs((xm - x(jcn)) / dx(jcn))
# SiStER_locate_markers_in_grid.m:38
    disy=abs((ym - y(icn)) / dy(icn))
# SiStER_locate_markers_in_grid.m:39
    xRIGHT=disx > 0.5
# SiStER_locate_markers_in_grid.m:42
    yUP=disy > 0.5
# SiStER_locate_markers_in_grid.m:43
    quad[logical_and(xRIGHT,yUP)]=3
# SiStER_locate_markers_in_grid.m:45
    quad[logical_and(xRIGHT,logical_not(yUP))]=2
# SiStER_locate_markers_in_grid.m:46
    quad[logical_and(logical_not(xRIGHT),yUP)]=4
# SiStER_locate_markers_in_grid.m:47
    quad[logical_and(logical_not(xRIGHT),logical_not(yUP))]=1
# SiStER_locate_markers_in_grid.m:48