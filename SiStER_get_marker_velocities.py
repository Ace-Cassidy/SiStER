# Generated with SMOP  0.41
from libsmop import *
# SiStER_get_marker_velocities.m

    
@function
def SiStER_get_marker_velocities(quad=None,icn=None,jcn=None,x=None,y=None,xm=None,ym=None,vx=None,vy=None,dx=None,dy=None,*args,**kwargs):
    varargin = SiStER_get_marker_velocities.varargin
    nargin = SiStER_get_marker_velocities.nargin

    
    # [VX,VY] = SiStER_get_marker_velocities(quad,icn,jcn,x,y,xm,ym,vx,vy,dx,dy)
# interpolates velocities at nodes to velocities on markers
    
    # First cut - J.A. Olive, 2011-2012, modified by B.Z. Klein 2013-2014
    
    Nx=length(x)
# SiStER_get_marker_velocities.m:8
    Ny=length(y)
# SiStER_get_marker_velocities.m:9
    m,__=size(vx,nargout=2)
# SiStER_get_marker_velocities.m:10
    #boolean arrays for interpolation
    quad1=quad == 1
# SiStER_get_marker_velocities.m:13
    quad2=quad == 2
# SiStER_get_marker_velocities.m:14
    quad3=quad == 3
# SiStER_get_marker_velocities.m:15
    quad4=quad == 4
# SiStER_get_marker_velocities.m:16
    top=icn == 1
# SiStER_get_marker_velocities.m:18
    bot=icn == Ny - 1
# SiStER_get_marker_velocities.m:19
    left=jcn == 1
# SiStER_get_marker_velocities.m:21
    right=jcn == Nx - 1
# SiStER_get_marker_velocities.m:22
    #linear index vector of icn & jcn for vx, vy
    IND=sub2ind(size(vx),icn,jcn)
# SiStER_get_marker_velocities.m:25
    ######################
## Vx Interpolation ##
######################
    
    Vx_xnodes=concat([[x(jcn)],[x(jcn + 1)],[x(jcn + 1)],[x(jcn)]])
# SiStER_get_marker_velocities.m:31
    ## case 1, icn == 1 (top)
    c1=copy(top)
# SiStER_get_marker_velocities.m:35
    Vx_ynodes[arange(),c1]=concat([[y(icn(c1)) + dy(icn(c1)) / 2],[y(icn(c1)) + dy(icn(c1)) / 2],[y(icn(c1) + 1) + dy(icn(c1) + 1) / 2],[y(icn(c1) + 1) + dy(icn(c1) + 1) / 2]])
# SiStER_get_marker_velocities.m:37
    Vx_nodes[arange(),c1]=concat([[vx(IND(c1))],[vx(IND(c1) + m)],[vx(IND(c1) + 1 + m)],[vx(IND(c1) + 1)]])
# SiStER_get_marker_velocities.m:42
    ## case 2, icn == Ny-1 (bot) && in quad 3 or 4
    c2=copy(bot)
# SiStER_get_marker_velocities.m:48
    
    Vx_ynodes[arange(),c2]=concat([[y(icn(c2) - 1) + dy(icn(c2) - 1) / 2],[y(icn(c2) - 1) + dy(icn(c2) - 1) / 2],[y(icn(c2)) + dy(icn(c2)) / 2],[y(icn(c2)) + dy(icn(c2)) / 2]])
# SiStER_get_marker_velocities.m:50
    Vx_nodes[arange(),c2]=concat([[vx(IND(c2) - 1)],[vx(IND(c2) - 1 + m)],[vx(IND(c2) + m)],[vx(IND(c2))]])
# SiStER_get_marker_velocities.m:55
    ## case 3 icn ~top & ~bot, quad = 1 | 2
    c3=logical_and(logical_and(logical_not(top),logical_not(bot)),(logical_or(quad1,quad2)))
# SiStER_get_marker_velocities.m:61
    Vx_ynodes[arange(),c3]=concat([[y(icn(c3)) - dy(icn(c3) - 1) / 2],[y(icn(c3)) - dy(icn(c3) - 1) / 2],[y(icn(c3)) + dy(icn(c3)) / 2],[y(icn(c3)) + dy(icn(c3)) / 2]])
# SiStER_get_marker_velocities.m:63
    Vx_nodes[arange(),c3]=concat([[vx(IND(c3) - 1)],[vx(IND(c3) - 1 + m)],[vx(IND(c3) + m)],[vx(IND(c3))]])
# SiStER_get_marker_velocities.m:68
    ## case 4 icn ~top & ~bot & quad = 3|4
    c4=logical_and(logical_and(logical_not(top),logical_not(bot)),(logical_or(quad3,quad4)))
# SiStER_get_marker_velocities.m:74
    Vx_ynodes[arange(),c4]=concat([[y(icn(c4)) + dy(icn(c4)) / 2],[y(icn(c4)) + dy(icn(c4)) / 2],[y(icn(c4) + 1) + dy(icn(c4) + 1) / 2],[y(icn(c4) + 1) + dy(icn(c4) + 1) / 2]])
# SiStER_get_marker_velocities.m:76
    Vx_nodes[arange(),c4]=concat([[vx(IND(c4))],[vx(IND(c4) + m)],[vx(IND(c4) + 1 + m)],[vx(IND(c4) + 1)]])
# SiStER_get_marker_velocities.m:81
    VX=SiStER_interp_grid_to_marker_vector(Vx_xnodes,Vx_ynodes,Vx_nodes,xm,ym)
# SiStER_get_marker_velocities.m:88
    #######################
## VY INTERPOLATION  ##
#######################
    
    Vy_ynodes=concat([[y(icn)],[y(icn)],[y(icn + 1)],[y(icn + 1)]])
# SiStER_get_marker_velocities.m:96
    ## case 1 jcn == 1 (left)
    c1=copy(left)
# SiStER_get_marker_velocities.m:99
    Vy_xnodes[arange(),c1]=concat([[x(jcn(c1)) + dx(jcn(c1)) / 2],[x(jcn(c1) + 1) + dx(jcn(c1) + 1) / 2],[x(jcn(c1) + 1) + dx(jcn(c1) + 1) / 2],[x(jcn(c1)) + dx(jcn(c1)) / 2]])
# SiStER_get_marker_velocities.m:101
    Vy_nodes[arange(),c1]=concat([[vy(IND(c1))],[vy(IND(c1) + m)],[vy(IND(c1) + 1 + m)],[vy(IND(c1) + 1)]])
# SiStER_get_marker_velocities.m:106
    ## case 2 jcn == Nx-1 (right) & Quad = 2 | 3
    c2=copy(right)
# SiStER_get_marker_velocities.m:112
    
    Vy_xnodes[arange(),c2]=concat([[x(jcn(c2) - 1) + dx(jcn(c2) - 1) / 2],[x(jcn(c2)) + dx(jcn(c2)) / 2],[x(jcn(c2)) + dx(jcn(c2)) / 2],[x(jcn(c2) - 1) + dx(jcn(c2) - 1) / 2]])
# SiStER_get_marker_velocities.m:114
    Vy_nodes[arange(),c2]=concat([[vy(IND(c2) - m)],[vy(IND(c2))],[vy(IND(c2) + 1)],[vy(IND(c2) + 1 - m)]])
# SiStER_get_marker_velocities.m:119
    
    c3=logical_and(logical_and(logical_not(left),logical_not(right)),(logical_or(quad1,quad4)))
# SiStER_get_marker_velocities.m:125
    Vy_xnodes[arange(),c3]=concat([[x(jcn(c3)) - dx(jcn(c3) - 1) / 2],[x(jcn(c3)) + dx(jcn(c3)) / 2],[x(jcn(c3)) + dx(jcn(c3)) / 2],[x(jcn(c3)) - dx(jcn(c3) - 1) / 2]])
# SiStER_get_marker_velocities.m:127
    Vy_nodes[arange(),c3]=concat([[vy(IND(c3) - m)],[vy(IND(c3))],[vy(IND(c3) + 1)],[vy(IND(c3) + 1 - m)]])
# SiStER_get_marker_velocities.m:132
    ## case 4 ~left & ~right & quad = 2 | 3
    c4=logical_and(logical_and(logical_not(left),logical_not(right)),(logical_or(quad2,quad3)))
# SiStER_get_marker_velocities.m:138
    Vy_xnodes[arange(),c4]=concat([[x(jcn(c4)) + dx(jcn(c4)) / 2],[x(jcn(c4) + 1) + dx(jcn(c4) + 1) / 2],[x(jcn(c4) + 1) + dx(jcn(c4) + 1) / 2],[x(jcn(c4)) + dx(jcn(c4)) / 2]])
# SiStER_get_marker_velocities.m:140
    Vy_nodes[arange(),c4]=concat([[vy(IND(c4))],[vy(IND(c4) + m)],[vy(IND(c4) + m + 1)],[vy(IND(c4) + 1)]])
# SiStER_get_marker_velocities.m:145
    VY=SiStER_interp_grid_to_marker_vector(Vy_xnodes,Vy_ynodes,Vy_nodes,xm,ym)
# SiStER_get_marker_velocities.m:152