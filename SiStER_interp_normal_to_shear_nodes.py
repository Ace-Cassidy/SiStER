# Generated with SMOP  0.41
from libsmop import *
# SiStER_interp_normal_to_shear_nodes.m

    #=========================================================================
    
@function
def SiStER_interp_normal_to_shear_nodes(varN=None,dx=None,dy=None,*args,**kwargs):
    varargin = SiStER_interp_normal_to_shear_nodes.varargin
    nargin = SiStER_interp_normal_to_shear_nodes.nargin

    # Interpolates values on normal nodes (varN) to shear nodes
# Potential shortcoming:  interpolation to side shear nodes are only
# based on the closest normal nodes and thus values will be horizontally
# uniform with 1/2 cell of the left/right sides and vertically uniform
# with 1/2 cell of the top and bottoms
    
    # G.Ito 8/2016
#=========================================================================
    varS=zeros(size(varN))
# SiStER_interp_normal_to_shear_nodes.m:11
    Ny,Nx=size(varS,nargout=2)
# SiStER_interp_normal_to_shear_nodes.m:12
    i1=arange(2,Ny - 1)
# SiStER_interp_normal_to_shear_nodes.m:13
    j1=arange(2,Nx - 1)
# SiStER_interp_normal_to_shear_nodes.m:13
    i2=arange(3,Ny)
# SiStER_interp_normal_to_shear_nodes.m:14
    j2=arange(3,Nx)
# SiStER_interp_normal_to_shear_nodes.m:14
    dydx=copy(varS)
# SiStER_interp_normal_to_shear_nodes.m:15
    dydx[arange(2,end()),arange(2,end())]=dot(dy.T,dx)
# SiStER_interp_normal_to_shear_nodes.m:16
    #--------------------------------------------------------------------------
# interior nodes
#--------------------------------------------------------------------------
    varS[i1,j1]=(multiply(varN(i1,j1),dydx(i2,j2)) / 4 + multiply(varN(i1,j2),dydx(i2,j1)) / 4 + multiply(varN(i2,j1),dydx(i1,j2)) / 4 + multiply(varN(i2,j2),dydx(i1,j1)) / 4) / ((dydx(i1,j1) + dydx(i1,j2) + dydx(i2,j1) + dydx(i2,j2)) / 4)
# SiStER_interp_normal_to_shear_nodes.m:21
    #--------------------------------------------------------------------------
# top and bottom, excluding corners
#--------------------------------------------------------------------------
    varS[1,j1]=(multiply(varN(2,j1),dydx(2,j2)) / 4 + multiply(varN(2,j2),dydx(2,j1)) / 4) / (dydx(2,j2) / 4 + dydx(2,j1) / 4)
# SiStER_interp_normal_to_shear_nodes.m:28
    varS[Ny,j1]=(multiply(varN(Ny,j1),dydx(Ny,j2)) / 4 + multiply(varN(Ny,j2),dydx(Ny,j1)) / 4) / (dydx(Ny,j2) / 4 + dydx(Ny,j1) / 4)
# SiStER_interp_normal_to_shear_nodes.m:31
    #--------------------------------------------------------------------------
# left and right, excluding corners
#--------------------------------------------------------------------------
    varS[i1,1]=(multiply(varN(i1,2),dydx(i2,2)) / 4 + multiply(varN(i2,2),dydx(i1,2)) / 4) / (dydx(i1,2) / 4 + dydx(i2,2) / 4)
# SiStER_interp_normal_to_shear_nodes.m:37
    varS[i1,Nx]=(multiply(varN(i1,Nx),dydx(i2,Nx)) / 4 + multiply(varN(i2,Nx),dydx(i1,Nx)) / 4) / (dydx(i2,Nx) / 4 + dydx(i1,Nx) / 4)
# SiStER_interp_normal_to_shear_nodes.m:40
    #--------------------------------------------------------------------------
# corners
#--------------------------------------------------------------------------
    varS[1,1]=varN(2,2)
# SiStER_interp_normal_to_shear_nodes.m:46
    varS[1,Nx]=varN(2,Nx)
# SiStER_interp_normal_to_shear_nodes.m:46
    varS[Ny,1]=varN(Ny,2)
# SiStER_interp_normal_to_shear_nodes.m:47
    varS[Ny,Nx]=varN(Ny,Nx)
# SiStER_interp_normal_to_shear_nodes.m:47
    return varS