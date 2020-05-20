# Generated with SMOP  0.41
from libsmop import *
# SiStER_get_strain_rate.m

    
@function
def SiStER_get_strain_rate(vx=None,vy=None,dx=None,dy=None,BC=None,*args,**kwargs):
    varargin = SiStER_get_strain_rate.varargin
    nargin = SiStER_get_strain_rate.nargin

    # [EXX EXY]=SiStER_get_strain_rate(vx,vy,dx,dy,BC)
# computes the deviatoric strain rate: EXX, at normal nodes
# and EXY, at shear nodes, from vx and vy on the eulerian grid
    
    # G.Ito 11/12/15 updated calculations at corner nodes to be
#    consistent with the top and bottom boundary conditions, as those
#    (not the side) conditions control the solutions for vx,vy at the
#    points closest to the corners in SiStER_Stokes_solver.m
    
    Ny,Nx=size(vx,nargout=2)
# SiStER_get_strain_rate.m:11
    EXX=zeros(size(vx))
# SiStER_get_strain_rate.m:13
    EXY=zeros(size(vy))
# SiStER_get_strain_rate.m:14
    # Getting EXX (on normal nodes) is straightforward
    for i in arange(2,Ny).reshape(-1):
        for j in arange(2,Nx).reshape(-1):
            EXX[i,j]=(vx(i - 1,j) - vx(i - 1,j - 1)) / dx(j - 1)
# SiStER_get_strain_rate.m:19
    
    
    # Getting EXY (on shear nodes) requires some thinking when dealing with
# boundaries
    for i in arange(1,Ny).reshape(-1):
        for j in arange(1,Nx).reshape(-1):
            if i >= 2 and i <= Ny - 1 and j >= 2 and j <= Nx - 1:
                EXY[i,j]=dot(0.5,(dot(2,(vx(i,j) - vx(i - 1,j))) / (dy(i - 1) + dy(i)) + dot(2,(vy(i,j) - vy(i,j - 1))) / (dx(j - 1) + dx(j))))
# SiStER_get_strain_rate.m:29
            if i == 1 and j >= 2 and j <= Nx - 1:
                if BC.top(1) == 1:
                    dvxdy=0
# SiStER_get_strain_rate.m:34
                else:
                    if BC.top(1) == 0:
                        dvxdy=dot(2,vx(i,j)) / dy(i)
# SiStER_get_strain_rate.m:36
                EXY[i,j]=dot(0.5,(dvxdy + dot(2,(vy(i,j) - vy(i,j - 1))) / (dx(j - 1) + dx(j))))
# SiStER_get_strain_rate.m:38
            else:
                if i == Ny and j >= 2 and j <= Nx - 1:
                    if BC.bot(1) == 1:
                        dvxdy=0
# SiStER_get_strain_rate.m:42
                    else:
                        if BC.bot(1) == 0:
                            #dvxdy=-2*vx(i-1,j)/dy(i-1);
                            dvxdy=dot(2.0,(BC.bot(4) - vx(i - 1,j))) / dy(i - 1)
# SiStER_get_strain_rate.m:45
                    EXY[i,j]=dot(0.5,(dvxdy + dot(2,(vy(i,j) - vy(i,j - 1))) / (dx(j - 1) + dx(j))))
# SiStER_get_strain_rate.m:47
                else:
                    if j == 1 and i >= 2 and i <= Ny - 1:
                        if BC.left(1) == 1:
                            dvydx=0
# SiStER_get_strain_rate.m:51
                        else:
                            if BC.left(1) == 0:
                                dvydx=dot(2,vy(i,j)) / dx(j)
# SiStER_get_strain_rate.m:53
                        EXY[i,j]=dot(0.5,(dot(2,(vx(i,j) - vx(i - 1,j))) / (dy(i - 1) + dy(i)) + dvydx))
# SiStER_get_strain_rate.m:55
                    else:
                        if j == Nx and i >= 2 and i <= Ny - 1:
                            if BC.right(1) == 1:
                                dvydx=0
# SiStER_get_strain_rate.m:59
                            else:
                                if BC.right(1) == 0:
                                    dvydx=dot(- 2,vy(i,j - 1)) / dx(j - 1)
# SiStER_get_strain_rate.m:61
                            EXY[i,j]=dot(0.5,(dot(2,(vx(i,j) - vx(i - 1,j))) / (dy(i - 1) + dy(i)) + dvydx))
# SiStER_get_strain_rate.m:63
            # corners
            if i == 1 and j == 1:
                if BC.top(1) == 1:
                    dvxdy=0
# SiStER_get_strain_rate.m:71
                else:
                    if BC.top(1) == 0:
                        dvxdy=dot(2,vx(i,j)) / dy(i)
# SiStER_get_strain_rate.m:73
                if BC.top(2) == 0:
                    dvydx=0
# SiStER_get_strain_rate.m:77
                else:
                    if BC.top(2) == 3:
                        dvydx=dot(2,(vy(i,j + 1) - vy(i,j))) / (dx(j) + dx(j + 1))
# SiStER_get_strain_rate.m:79
                    else:
                        disp(concat(['Stopped in get_strain_rate:  EXY for corner elements not coded for BC.top(2)=',num2str(BC.top(2))]))
                        halt
                EXY[i,j]=(dvxdy + dvydx) / 2
# SiStER_get_strain_rate.m:85
            else:
                if i == 1 and j == Nx:
                    if BC.top(1) == 1:
                        dvxdy=0
# SiStER_get_strain_rate.m:90
                    else:
                        if BC.top(1) == 0:
                            dvxdy=dot(2,vx(i,j)) / dy(i)
# SiStER_get_strain_rate.m:92
                    if BC.top(2) == 0:
                        dvydx=0
# SiStER_get_strain_rate.m:95
                    else:
                        if BC.top(2) == 3:
                            dvydx=dot(2,(vy(i,j - 1) - vy(i,j - 2))) / (dx(j - 1) + dx(j - 2))
# SiStER_get_strain_rate.m:97
                    EXY[i,j]=(dvxdy + dvydx) / 2
# SiStER_get_strain_rate.m:99
                else:
                    if i == Ny and j == Nx:
                        if BC.bot(1) == 1:
                            dvxdy=0
# SiStER_get_strain_rate.m:103
                        else:
                            if BC.bot(1) == 0:
                                dvxdy=dot(- 2,vx(i - 1,j)) / dy(i - 1)
# SiStER_get_strain_rate.m:105
                        if BC.bot(2) == 0:
                            dvydx=0
# SiStER_get_strain_rate.m:108
                        else:
                            if BC.bot(2) == 3:
                                dvydx=dot(2,(vy(i,j - 1) - vy(i,j - 2))) / (dx(j - 1) + dx(j - 2))
# SiStER_get_strain_rate.m:110
                            else:
                                disp(concat(['Stopped in get_strain_rate:  EXY for corner elements not coded for BC.bot(2)=',num2str(BC.bot(2))]))
                                halt
                        EXY[i,j]=(dvxdy + dvydx) / 2
# SiStER_get_strain_rate.m:116
                    else:
                        if i == Ny and j == 1:
                            if BC.bot(1) == 1:
                                dvxdy=0
# SiStER_get_strain_rate.m:120
                            else:
                                if BC.bot(1) == 0:
                                    dvxdy=dot(- 2,vx(i - 1,j)) / dy(i - 1)
# SiStER_get_strain_rate.m:122
                            if BC.bot(2) == 0:
                                dvydx=0
# SiStER_get_strain_rate.m:125
                            else:
                                if BC.bot(2) == 3:
                                    dvydx=dot(2,(vy(i,j + 1) - vy(i,j))) / (dx(j + 1) + dx(j))
# SiStER_get_strain_rate.m:127
                            EXY[i,j]=(dvxdy + dvydx) / 2
# SiStER_get_strain_rate.m:129
    