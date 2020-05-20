# Generated with SMOP  0.41
from libsmop import *
# SiStER_topography_diffusion_solver.m

    
@function
def SiStER_topography_diffusion_solver(xc=None,topo_old=None,dt=None,K=None,*args,**kwargs):
    varargin = SiStER_topography_diffusion_solver.varargin
    nargin = SiStER_topography_diffusion_solver.nargin

    # [topo_new]=SiStER_topography_diffusion_solver(xc,topo_old,dt,K)
# very basic explicit diffusion solver to evolve topography
    
    topo_new=copy(topo_old)
# SiStER_topography_diffusion_solver.m:5
    dt_surf=dot(0.5,min(diff(xc)) ** 2) / K
# SiStER_topography_diffusion_solver.m:7
    # can't take diff of xc close to edge- if reseeding takes place might be
# too small
    
    if dt_surf < dt:
        # DO SEVERAL TEMPERATURE SOLVES UNTIL dt is reached
        nsolve=ceil(dt / dt_surf)
# SiStER_topography_diffusion_solver.m:13
        dt_solve=dt / nsolve
# SiStER_topography_diffusion_solver.m:14
        topo_solve=copy(topo_old)
# SiStER_topography_diffusion_solver.m:15
        for ksolve in arange(1,nsolve - 1).reshape(-1):
            topo_solve[arange(2,end() - 1)]=topo_solve(arange(2,end() - 1)) + multiply(dot(dot(dt_solve,K),(1.0 / (dot(0.5,(xc(arange(3,end())) + xc(arange(2,end() - 1)))) - dot(0.5,(xc(arange(2,end() - 1)) + xc(arange(1,end() - 2))))))),((topo_solve(arange(3,end())) - topo_solve(arange(2,end() - 1))) / (xc(arange(3,end())) - xc(arange(2,end() - 1))) - (topo_solve(arange(2,end() - 1)) - topo_solve(arange(1,end() - 2))) / (xc(arange(2,end() - 1)) - xc(arange(1,end() - 2)))))
# SiStER_topography_diffusion_solver.m:19
        disp(concat(['completed ',num2str(nsolve),' iterations to diffuse topography']))
        topo_new=copy(topo_solve)
# SiStER_topography_diffusion_solver.m:26
    else:
        topo_new[arange(2,end() - 1)]=topo_old(arange(2,end() - 1)) + multiply(dot(dot(dt,K),(1.0 / (dot(0.5,(xc(arange(3,end())) + xc(arange(2,end() - 1)))) - dot(0.5,(xc(arange(2,end() - 1)) + xc(arange(1,end() - 2))))))),((topo_old(arange(3,end())) - topo_old(arange(2,end() - 1))) / (xc(arange(3,end())) - xc(arange(2,end() - 1))) - (topo_old(arange(2,end() - 1)) - topo_old(arange(1,end() - 2))) / (xc(arange(2,end() - 1)) - xc(arange(1,end() - 2)))))
# SiStER_topography_diffusion_solver.m:29
    
    topo_new[1]=topo_new(2)
# SiStER_topography_diffusion_solver.m:34
    topo_new[end()]=topo_new(end() - 1)
# SiStER_topography_diffusion_solver.m:35