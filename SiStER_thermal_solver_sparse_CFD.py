# Generated with SMOP  0.41
from libsmop import *
# SiStER_thermal_solver_sparse_CFD.m

    
@function
def SiStER_thermal_solver_sparse_CFD(x=None,y=None,Told=None,rho=None,cp=None,k=None,dt=None,BCtherm=None,H=None,*args,**kwargs):
    varargin = SiStER_thermal_solver_sparse_CFD.varargin
    nargin = SiStER_thermal_solver_sparse_CFD.nargin

    # [T, rhs, Lii, Ljj, Lvv]=SiStER_thermal_solver_sparse_CFD(x,y,Told,rho,cp,k,dt,BCtherm,H)
# implicit Solver for thermal diffusion
# rho cp dT/dt = div (k grad T) + H
# J.-A. Olive, November 2014
# B.Z. Klein, added sparse matrix filling, End of 2014
# Added internal heat gen - howellsm 2/2017
# Updated to fully conservative (centered finite difference)
# for variable thermal diffusivity
# by S. Howell, now accepts k on shear nodes
    
    Nx=length(x)
# SiStER_thermal_solver_sparse_CFD.m:12
    Ny=length(y)
# SiStER_thermal_solver_sparse_CFD.m:13
    dx=diff(x)
# SiStER_thermal_solver_sparse_CFD.m:14
    dy=diff(y)
# SiStER_thermal_solver_sparse_CFD.m:15
    Li=zeros(dot(Nx,Ny),1)
# SiStER_thermal_solver_sparse_CFD.m:17
    Lj=zeros(dot(Nx,Ny),1)
# SiStER_thermal_solver_sparse_CFD.m:18
    Lv=zeros(dot(Nx,Ny),1)
# SiStER_thermal_solver_sparse_CFD.m:19
    rhs=zeros(dot(Nx,Ny),1)
# SiStER_thermal_solver_sparse_CFD.m:20
    n=1
# SiStER_thermal_solver_sparse_CFD.m:22
    for i in arange(1,Ny).reshape(-1):
        for j in arange(1,Nx).reshape(-1):
            in_=i + dot(Ny,(j - 1))
# SiStER_thermal_solver_sparse_CFD.m:27
            if i == 1:
                if BCtherm.top(1) == 1:
                    Li[n]=in_
# SiStER_thermal_solver_sparse_CFD.m:33
                    Lj[n]=in_
# SiStER_thermal_solver_sparse_CFD.m:34
                    Lv[n]=1
# SiStER_thermal_solver_sparse_CFD.m:35
                    n=n + 1
# SiStER_thermal_solver_sparse_CFD.m:37
                    rhs[in_]=BCtherm.top(2)
# SiStER_thermal_solver_sparse_CFD.m:39
                    #rhs(in)=BCtherm.top(2);
                else:
                    if BCtherm.top(1) == 2:
                        Li[n]=in_
# SiStER_thermal_solver_sparse_CFD.m:46
                        Lj[n]=in_
# SiStER_thermal_solver_sparse_CFD.m:47
                        Lv[n]=- 1
# SiStER_thermal_solver_sparse_CFD.m:48
                        n=n + 1
# SiStER_thermal_solver_sparse_CFD.m:50
                        Li[n]=in_
# SiStER_thermal_solver_sparse_CFD.m:52
                        Lj[n]=in_ + 1
# SiStER_thermal_solver_sparse_CFD.m:53
                        Lv[n]=1
# SiStER_thermal_solver_sparse_CFD.m:54
                        n=n + 1
# SiStER_thermal_solver_sparse_CFD.m:56
                        rhs[in_]=dot(BCtherm.top(2),dy(i))
# SiStER_thermal_solver_sparse_CFD.m:58
                        #             L(in,in)=-1;
#             L(in,in+1)=1;
#             rhs(in)=BCtherm.top(2)*dy(i);
            else:
                if i == Ny:
                    if BCtherm.bot(1) == 1:
                        Li[n]=in_
# SiStER_thermal_solver_sparse_CFD.m:71
                        Lj[n]=in_
# SiStER_thermal_solver_sparse_CFD.m:72
                        Lv[n]=1
# SiStER_thermal_solver_sparse_CFD.m:73
                        n=n + 1
# SiStER_thermal_solver_sparse_CFD.m:75
                        rhs[in_]=BCtherm.bot(2)
# SiStER_thermal_solver_sparse_CFD.m:77
                        #             L(in,in)=1;
#             rhs(in)=BCtherm.bot(2);
                    else:
                        if BCtherm.bot(1) == 2:
                            Li[n]=in_
# SiStER_thermal_solver_sparse_CFD.m:84
                            Lj[n]=in_
# SiStER_thermal_solver_sparse_CFD.m:85
                            Lv[n]=1
# SiStER_thermal_solver_sparse_CFD.m:86
                            n=n + 1
# SiStER_thermal_solver_sparse_CFD.m:88
                            Li[n]=in_
# SiStER_thermal_solver_sparse_CFD.m:90
                            Lj[n]=in_ - 1
# SiStER_thermal_solver_sparse_CFD.m:91
                            Lv[n]=- 1
# SiStER_thermal_solver_sparse_CFD.m:92
                            n=n + 1
# SiStER_thermal_solver_sparse_CFD.m:94
                            rhs[in_]=dot(BCtherm.bot(2),dy(i - 1))
# SiStER_thermal_solver_sparse_CFD.m:96
                            #             L(in,in)=1;
#             L(in,in-1)=-1;
#             rhs(in)=BCtherm.bot(2)*dy(i-1);
                else:
                    if j == 1:
                        if BCtherm.left(1) == 2:
                            Li[n]=in_
# SiStER_thermal_solver_sparse_CFD.m:109
                            Lj[n]=in_
# SiStER_thermal_solver_sparse_CFD.m:110
                            Lv[n]=- 1
# SiStER_thermal_solver_sparse_CFD.m:111
                            n=n + 1
# SiStER_thermal_solver_sparse_CFD.m:113
                            Li[n]=in_
# SiStER_thermal_solver_sparse_CFD.m:115
                            Lj[n]=in_ + Ny
# SiStER_thermal_solver_sparse_CFD.m:116
                            Lv[n]=1
# SiStER_thermal_solver_sparse_CFD.m:117
                            n=n + 1
# SiStER_thermal_solver_sparse_CFD.m:119
                            rhs[in_]=dot(BCtherm.left(2),dx(j))
# SiStER_thermal_solver_sparse_CFD.m:121
                            #             L(in,in)=-1;
#             L(in,in+Ny)=1;
#             rhs(in)=BCtherm.left(2)*dx(j);
                        else:
                            if BCtherm.left(1) == 1:
                                Li[n]=in_
# SiStER_thermal_solver_sparse_CFD.m:129
                                Lj[n]=in_
# SiStER_thermal_solver_sparse_CFD.m:130
                                Lv[n]=1
# SiStER_thermal_solver_sparse_CFD.m:131
                                n=n + 1
# SiStER_thermal_solver_sparse_CFD.m:133
                                rhs[in_]=BCtherm.left(2)
# SiStER_thermal_solver_sparse_CFD.m:135
                                #             L(in,in)=1;
#             rhs(in)=BCtherm.left(2);
                    else:
                        if j == Nx:
                            if BCtherm.right(1) == 2:
                                Li[n]=in_
# SiStER_thermal_solver_sparse_CFD.m:148
                                Lj[n]=in_
# SiStER_thermal_solver_sparse_CFD.m:149
                                Lv[n]=1
# SiStER_thermal_solver_sparse_CFD.m:150
                                n=n + 1
# SiStER_thermal_solver_sparse_CFD.m:152
                                Li[n]=in_
# SiStER_thermal_solver_sparse_CFD.m:154
                                Lj[n]=in_ - Ny
# SiStER_thermal_solver_sparse_CFD.m:155
                                Lv[n]=- 1
# SiStER_thermal_solver_sparse_CFD.m:156
                                n=n + 1
# SiStER_thermal_solver_sparse_CFD.m:158
                                rhs[in_]=dot(BCtherm.right(2),dx(j - 1))
# SiStER_thermal_solver_sparse_CFD.m:160
                                #             L(in,in)=1;
#             L(in,in-Ny)=-1;
#             rhs(in)=BCtherm.right(2)*dx(j-1);
                            else:
                                if BCtherm.right(1) == 1:
                                    Li[n]=in_
# SiStER_thermal_solver_sparse_CFD.m:168
                                    Lj[n]=in_
# SiStER_thermal_solver_sparse_CFD.m:169
                                    Lv[n]=1
# SiStER_thermal_solver_sparse_CFD.m:170
                                    n=n + 1
# SiStER_thermal_solver_sparse_CFD.m:172
                                    rhs[in_]=BCtherm.right(2)
# SiStER_thermal_solver_sparse_CFD.m:174
                                    #             L(in,in)=1;
#             rhs(in)=BCtherm.right(2);
                        else:
                            #         #   internal nodes
                            ddx=dx(j - 1) + dx(j)
# SiStER_thermal_solver_sparse_CFD.m:188
                            ddy=dy(i - 1) + dy(i)
# SiStER_thermal_solver_sparse_CFD.m:189
                            kA=(dot(dot(2,k(i,j - 1)),k(i,j))) / (k(i,j - 1) + k(i,j))
# SiStER_thermal_solver_sparse_CFD.m:192
                            kB=(dot(dot(2,k(i,j)),k(i,j + 1))) / (k(i,j) + k(i,j + 1))
# SiStER_thermal_solver_sparse_CFD.m:193
                            kC=(dot(dot(2,k(i - 1,j)),k(i,j))) / (k(i - 1,j) + k(i,j))
# SiStER_thermal_solver_sparse_CFD.m:194
                            kD=(dot(dot(2,k(i,j)),k(i + 1,j))) / (k(i,j) + k(i + 1,j))
# SiStER_thermal_solver_sparse_CFD.m:195
                            Li[n]=in_
# SiStER_thermal_solver_sparse_CFD.m:197
                            Lj[n]=in_
# SiStER_thermal_solver_sparse_CFD.m:198
                            Lv[n]=dot(rho(i,j),cp(i,j)) + dot(dot(2,dt),kB) / (dot(dx(j),ddx)) + dot(dot(2,dt),kA) / (dot(dx(j - 1),ddx)) + dot(dot(2,dt),kD) / (dot(ddy,dy(i))) + dot(dot(2,dt),kC) / (dot(ddy,dy(i - 1)))
# SiStER_thermal_solver_sparse_CFD.m:199
                            n=n + 1
# SiStER_thermal_solver_sparse_CFD.m:202
                            #             Lv(n) = rho(i,j)*cp(i,j)+2*dt*kB/(dx(j)*ddx) + 2*dt*kA/(dx(j-1)*ddx) + ...
#                 2*dt*kD/(ddy*dy(i)) + 2*dt*kC/(ddy*dy(i-1));
                            Li[n]=in_
# SiStER_thermal_solver_sparse_CFD.m:207
                            Lj[n]=in_ + Ny
# SiStER_thermal_solver_sparse_CFD.m:208
                            Lv[n]=dot(dot(- 2,dt),kB) / (dot(dx(j),ddx))
# SiStER_thermal_solver_sparse_CFD.m:209
                            n=n + 1
# SiStER_thermal_solver_sparse_CFD.m:211
                            #             L(in,in+Ny)=-2*dt*k(i,j)/(dx(j)*ddx);
#
                            Li[n]=in_
# SiStER_thermal_solver_sparse_CFD.m:215
                            Lj[n]=in_ - Ny
# SiStER_thermal_solver_sparse_CFD.m:216
                            Lv[n]=dot(dot(- 2,dt),kA) / (dot(dx(j - 1),ddx))
# SiStER_thermal_solver_sparse_CFD.m:217
                            n=n + 1
# SiStER_thermal_solver_sparse_CFD.m:219
                            # 
# #             L(in,in-Ny)=-2*dt*k(i,j-1)/(dx(j-1)*ddx);
#
                            Li[n]=in_
# SiStER_thermal_solver_sparse_CFD.m:223
                            Lj[n]=in_ + 1
# SiStER_thermal_solver_sparse_CFD.m:224
                            Lv[n]=dot(dot(- 2,dt),kD) / (dot(dy(i),ddy))
# SiStER_thermal_solver_sparse_CFD.m:225
                            n=n + 1
# SiStER_thermal_solver_sparse_CFD.m:227
                            # 
# #             L(in,in+1)=-2*dt*k(i,j)/(dy(i)*ddy);
#
                            Li[n]=in_
# SiStER_thermal_solver_sparse_CFD.m:231
                            Lj[n]=in_ - 1
# SiStER_thermal_solver_sparse_CFD.m:232
                            Lv[n]=dot(dot(- 2,dt),kC) / (dot(dy(i - 1),ddy))
# SiStER_thermal_solver_sparse_CFD.m:233
                            n=n + 1
# SiStER_thermal_solver_sparse_CFD.m:235
                            #             L(in,in-1)=-2*dt*k(i-1,j)/(dy(i-1)*ddy);
                            rhs[in_]=dot(dot(rho(i,j),cp(i,j)),Told(i,j)) + dot(H(i,j),dt)
# SiStER_thermal_solver_sparse_CFD.m:239
    
    nn=n - 1
# SiStER_thermal_solver_sparse_CFD.m:246
    Lii=Li(arange(1,nn))
# SiStER_thermal_solver_sparse_CFD.m:248
    Ljj=Lj(arange(1,nn))
# SiStER_thermal_solver_sparse_CFD.m:249
    Lvv=Lv(arange(1,nn))
# SiStER_thermal_solver_sparse_CFD.m:250
    L=sparse(Lii,Ljj,Lvv)
# SiStER_thermal_solver_sparse_CFD.m:252
    tvec=numpy.linalg.solve(L,rhs)
# SiStER_thermal_solver_sparse_CFD.m:254
    T=reshape(tvec,Ny,Nx)
# SiStER_thermal_solver_sparse_CFD.m:256