# Generated with SMOP  0.41
from libsmop import *
# SiStER_interp_velocities_to_shear_nodes.m

    #=========================================================================
# Computes velocities at cell corners (shear nodes) from vx and vy 
# on staggered grid 
# (it can be useful to have vx and vy at the same location)
# G.Ito 7/15
#=========================================================================
    
    ## ------------------------------------------------------------------------
# Vx is defined on the x values of cell edges so only need to interpolate
# to y values of cell tops and bottoms
# -------------------------------------------------------------------------
    vxc=zeros(Ny,Nx)
# SiStER_interp_velocities_to_shear_nodes.m:13
    # internal nodes
    vxc[arange(2,Ny - 1),arange()]=multiply(vx(arange(1,Ny - 2),arange()),(dot(((1 - dy(arange(1,Ny - 2)) / (dy(arange(1,Ny - 2)) + dy(arange(2,Ny - 1))))).T,ones(1,Nx)))) + multiply(vx(arange(2,Ny - 1),arange()),(dot(((1 - dy(arange(2,Ny - 1)) / (dy(arange(1,Ny - 2)) + dy(arange(2,Ny - 1))))).T,ones(1,Nx))))
# SiStER_interp_velocities_to_shear_nodes.m:15
    # Top
    if (BC.top(1) == 1):
        vxc[1,arange()]=vx(2,arange())
# SiStER_interp_velocities_to_shear_nodes.m:19
    else:
        if (BC.top(1) == 0):
            vxc[1,arange()]=0
# SiStER_interp_velocities_to_shear_nodes.m:21
        else:
            disp('Problems in interp_velocities_to_shear_nodes: ')
            disp('BC.top(1) ~= 0 or 1')
            halt
    
    # Bottom
    if (BC.bot(1) == 1):
        vxc[Ny,arange()]=vx(Ny - 1,arange())
# SiStER_interp_velocities_to_shear_nodes.m:29
    else:
        if (BC.bot(1) == 0):
            if (length(BC.bot) == 4):
                vxc[Ny,arange()]=BC.bot(4)
# SiStER_interp_velocities_to_shear_nodes.m:33
            else:
                vxc[Ny,arange()]=0
# SiStER_interp_velocities_to_shear_nodes.m:35
        else:
            disp('Problems in interp_velocities_to_shear_nodes: ')
            disp('BC.bot(1) ~= 0 or 1')
            halt
    
    ## ------------------------------------------------------------------------
# Vy is defined on y values of cell tops and bottoms so only need to 
# interpolate to x-values of cell edges
# -------------------------------------------------------------------------
    vyc=zeros(Ny,Nx)
# SiStER_interp_velocities_to_shear_nodes.m:49
    # internal values
    vyc[arange(),arange(2,Nx - 1)]=multiply(vy(arange(),arange(1,Nx - 2)),(dot(ones(Ny,1),(1 - dx(arange(1,Nx - 2)) / (dx(arange(1,Nx - 2)) + dx(arange(2,Nx - 1))))))) + multiply(vy(arange(),arange(2,Nx - 1)),(dot(ones(Ny,1),(1 - dx(arange(2,Nx - 1)) / (dx(arange(1,Nx - 2)) + dx(arange(2,Nx - 1)))))))
# SiStER_interp_velocities_to_shear_nodes.m:51
    #Left
    if (BC.left(1) == 1):
        vyc[arange(),1]=vy(arange(),2)
# SiStER_interp_velocities_to_shear_nodes.m:55
    else:
        if (BC.left(1) == 0):
            vyc[arange(),1]=0
# SiStER_interp_velocities_to_shear_nodes.m:57
        else:
            disp('Problems in interp_velocities_to_shear_nodes: ')
            disp('BC.left(1) ~= 0 or 1')
            halt
    
    #Right
    if (BC.right(1) == 1):
        vyc[arange(),Nx]=vy(arange(),Nx - 1)
# SiStER_interp_velocities_to_shear_nodes.m:66
    else:
        if (BC.right(1) == 0):
            vyc[arange(),Nx]=0.0
# SiStER_interp_velocities_to_shear_nodes.m:69
        else:
            disp('Problems in interp_velocities_to_shear_nodes: ')
            disp('BC.right(1) ~= 0 or 1')
            halt
    
    