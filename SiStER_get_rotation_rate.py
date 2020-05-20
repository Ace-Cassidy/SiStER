# Generated with SMOP  0.41
from libsmop import *
# SiStER_get_rotation_rate.m

    
@function
def SiStER_get_rotation_rate(vx=None,vy=None,dx=None,dy=None,BC=None,*args,**kwargs):
    varargin = SiStER_get_rotation_rate.varargin
    nargin = SiStER_get_rotation_rate.nargin

    # [om]=SiStER_get_rotation_rate(vx,vy,dx,dy,BC)
# computes the rotation rate (vorticity) at shear nodes
    
    Ny,Nx=size(vx,nargout=2)
# SiStER_get_rotation_rate.m:6
    om=zeros(size(vy))
# SiStER_get_rotation_rate.m:7
    for i in arange(1,Ny).reshape(-1):
        for j in arange(1,Nx).reshape(-1):
            if i >= 2 and i <= Ny - 1 and j >= 2 and j <= Nx - 1:
                om[i,j]=dot(0.5,(dot(- 2,(vx(i,j) - vx(i - 1,j))) / (dy(i - 1) + dy(i)) + dot(2,(vy(i,j) - vy(i,j - 1))) / (dx(j - 1) + dx(j))))
# SiStER_get_rotation_rate.m:14
            if i == 1 and j >= 2 and j <= Nx - 1:
                if BC.top(1) == 1:
                    dvxdy=0
# SiStER_get_rotation_rate.m:19
                else:
                    if BC.top(1) == 0:
                        dvxdy=dot(2,vx(i,j)) / dy(i)
# SiStER_get_rotation_rate.m:21
                om[i,j]=dot(0.5,(- dvxdy + dot(2,(vy(i,j) - vy(i,j - 1))) / (dx(j - 1) + dx(j))))
# SiStER_get_rotation_rate.m:23
            else:
                if i == Ny and j >= 2 and j <= Nx - 1:
                    if BC.bot(1) == 1:
                        dvxdy=0
# SiStER_get_rotation_rate.m:27
                    else:
                        if BC.bot(1) == 0:
                            dvxdy=dot(- 2,vx(i - 1,j)) / dy(i - 1)
# SiStER_get_rotation_rate.m:29
                    om[i,j]=dot(0.5,(- dvxdy + dot(2,(vy(i,j) - vy(i,j - 1))) / (dx(j - 1) + dx(j))))
# SiStER_get_rotation_rate.m:31
                else:
                    if j == 1 and i >= 2 and i <= Ny - 1:
                        if BC.left(1) == 1:
                            dvydx=0
# SiStER_get_rotation_rate.m:35
                        else:
                            if BC.left(1) == 0:
                                dvydx=dot(2,vy(i,j)) / dx(j)
# SiStER_get_rotation_rate.m:37
                        om[i,j]=dot(0.5,(dot(- 2,(vx(i,j) - vx(i - 1,j))) / (dy(i - 1) + dy(i)) + dvydx))
# SiStER_get_rotation_rate.m:39
                    else:
                        if j == Nx and i >= 2 and i <= Ny - 1:
                            if BC.right(1) == 1:
                                dvydx=0
# SiStER_get_rotation_rate.m:43
                            else:
                                if BC.right(1) == 0:
                                    dvydx=dot(- 2,vy(i,j - 1)) / dx(j - 1)
# SiStER_get_rotation_rate.m:45
                            om[i,j]=dot(0.5,(dot(- 2,(vx(i,j) - vx(i - 1,j))) / (dy(i - 1) + dy(i)) + dvydx))
# SiStER_get_rotation_rate.m:47
            # corners
            if i == 1 and j == 1:
                if BC.top(1) == 1:
                    dvxdy=0
# SiStER_get_rotation_rate.m:55
                else:
                    if BC.top(1) == 0:
                        dvxdy=dot(2,vx(i,j)) / dy(i)
# SiStER_get_rotation_rate.m:57
                if BC.left(1) == 1:
                    dvydx=0
# SiStER_get_rotation_rate.m:60
                else:
                    if BC.left(1) == 0:
                        dvydx=dot(2,vy(i,j)) / dx(j)
# SiStER_get_rotation_rate.m:62
                om[i,j]=(- dvxdy + dvydx) / 2
# SiStER_get_rotation_rate.m:64
            else:
                if i == 1 and j == Ny:
                    if BC.top(1) == 1:
                        dvxdy=0
# SiStER_get_rotation_rate.m:69
                    else:
                        if BC.top(1) == 0:
                            dvxdy=dot(2,vx(i,j)) / dy(i)
# SiStER_get_rotation_rate.m:71
                    if BC.right(1) == 1:
                        dvydx=0
# SiStER_get_rotation_rate.m:74
                    else:
                        if BC.right(1) == 0:
                            dvydx=dot(- 2,vy(i,j - 1)) / dx(j - 1)
# SiStER_get_rotation_rate.m:76
                    om[i,j]=(- dvxdy + dvydx) / 2
# SiStER_get_rotation_rate.m:78
                else:
                    if i == Nx and j == Ny:
                        if BC.right(1) == 1:
                            dvydx=0
# SiStER_get_rotation_rate.m:82
                        else:
                            if BC.right(1) == 0:
                                dvydx=dot(- 2,vy(i,j - 1)) / dx(j - 1)
# SiStER_get_rotation_rate.m:84
                        if BC.bot(1) == 1:
                            dvxdy=0
# SiStER_get_rotation_rate.m:87
                        else:
                            if BC.bot(1) == 0:
                                dvxdy=dot(- 2,vx(i - 1,j)) / dy(i - 1)
# SiStER_get_rotation_rate.m:89
                        om[i,j]=(- dvxdy + dvydx) / 2
# SiStER_get_rotation_rate.m:91
                    else:
                        if i == Nx and j == 1:
                            if BC.bot(1) == 1:
                                dvxdy=0
# SiStER_get_rotation_rate.m:95
                            else:
                                if BC.bot(1) == 0:
                                    dvxdy=dot(- 2,vx(i - 1,j)) / dy(i - 1)
# SiStER_get_rotation_rate.m:97
                            if BC.left(1) == 1:
                                dvydx=0
# SiStER_get_rotation_rate.m:100
                            else:
                                if BC.left(1) == 0:
                                    dvydx=dot(2,vy(i,j)) / dx(j)
# SiStER_get_rotation_rate.m:102
                            om[i,j]=(- dvxdy + dvydx) / 2
# SiStER_get_rotation_rate.m:104
    