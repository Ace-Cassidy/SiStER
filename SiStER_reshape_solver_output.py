# Generated with SMOP  0.41
from libsmop import *
# SiStER_reshape_solver_output.m

    
@function
def SiStER_reshape_solver_output(S=None,Kc=None,Nx=None,Ny=None,*args,**kwargs):
    varargin = SiStER_reshape_solver_output.varargin
    nargin = SiStER_reshape_solver_output.nargin

    # [p, vx, vy]=SiStER_reshape_solver_output(S,Kc,Nx,Ny)
# reshapes the output of the Stokes solver into pressure and velocity
# arrays
# B.Z. Klein, rewritten from J.-A. Olive, Spring 2013
    
    INDp=arange(1,length(S),3)
# SiStER_reshape_solver_output.m:8
    INDvx=INDp + 1
# SiStER_reshape_solver_output.m:9
    INDvy=INDp + 2
# SiStER_reshape_solver_output.m:10
    p=dot(reshape(S(INDp),Ny,Nx),Kc)
# SiStER_reshape_solver_output.m:12
    vx=reshape(S(INDvx),Ny,Nx)
# SiStER_reshape_solver_output.m:13
    vy=reshape(S(INDvy),Ny,Nx)
# SiStER_reshape_solver_output.m:14