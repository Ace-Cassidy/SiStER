# Generated with SMOP  0.41
from libsmop import *
# SiStER_assemble_L_R.m

    
@function
def SiStER_assemble_L_R(dx=None,dy=None,etas=None,etan=None,rho=None,BC=None,PARAMS=None,srhs_xx=None,srhs_xy=None,*args,**kwargs):
    varargin = SiStER_assemble_L_R.varargin
    nargin = SiStER_assemble_L_R.nargin

    ## Fill LHS and RHS Solution Matrices
    
    p0cell=PARAMS.p0cell
# SiStER_assemble_L_R.m:6
    Nx=length(dx) + 1
# SiStER_assemble_L_R.m:8
    Ny=length(dy) + 1
# SiStER_assemble_L_R.m:9
    gx=PARAMS.gx
# SiStER_assemble_L_R.m:11
    gy=PARAMS.gy
# SiStER_assemble_L_R.m:12
    # Vector of right part initialization
    R=zeros(dot(dot(Nx,Ny),3),1)
# SiStER_assemble_L_R.m:15
    Lii=zeros(dot(dot(dot(10,Nx),Ny),3),1)
# SiStER_assemble_L_R.m:16
    Ljj=zeros(dot(dot(dot(10,Nx),Ny),3),1)
# SiStER_assemble_L_R.m:17
    Lvv=zeros(dot(dot(dot(10,Nx),Ny),3),1)
# SiStER_assemble_L_R.m:18
    nn=1
# SiStER_assemble_L_R.m:19
    ########## SCALING THE FD MATRIX
# Computing Kc and Kb coefficients
    meta=min(min(etas))
# SiStER_assemble_L_R.m:23
    mdx=max(dx)
# SiStER_assemble_L_R.m:24
    mdy=max(dy)
# SiStER_assemble_L_R.m:25
    Kc=dot(2,meta) / (mdx + mdy)
# SiStER_assemble_L_R.m:26
    Kb=dot(4,meta) / (mdx + mdy) ** 2
# SiStER_assemble_L_R.m:27
    # pressure anchor
#IP=2;
#JP=3;
    JP=ceil((Nx - 1) / 2)
# SiStER_assemble_L_R.m:33
    
    IP=2
# SiStER_assemble_L_R.m:34
    # fill in FD matrix and right-hand side
    
    for j in arange(1,Nx).reshape(-1):
        for i in arange(1,Ny).reshape(-1):
            #for j=1:Nx
            in_=dot((j - 1),Ny) + i
# SiStER_assemble_L_R.m:43
            inp=dot(3,in_) - 2
# SiStER_assemble_L_R.m:44
            invx=dot(3,in_) - 1
# SiStER_assemble_L_R.m:45
            invy=dot(3,in_)
# SiStER_assemble_L_R.m:46
            if (i == 1) or (j == 1) or (i == 2 and j == 2) or (i == 2 and j == Nx) or (i == Ny and j == 2) or (i == Ny and j == Nx) or (i == IP and j == JP and BC.top(2) != 3) or (BC.top(2) == 3 and i == 2 and j > 2 and j < Ny):
                # boundary conditions
                if (i == 1) or (j == 1):
                    #                L(inp,inp)=Kb;
                    Lii[nn]=inp
# SiStER_assemble_L_R.m:62
                    Ljj[nn]=inp
# SiStER_assemble_L_R.m:63
                    Lvv[nn]=Kb
# SiStER_assemble_L_R.m:64
                    nn=nn + 1
# SiStER_assemble_L_R.m:65
                    R[inp,1]=0
# SiStER_assemble_L_R.m:67
                if (i == 2 and j == 2) or (i == Ny and j == 2):
                    #                L(inp,inp)=Kb;
                #                L(inp,inp+3*Ny)=-Kb;
                    Lii[nn]=inp
# SiStER_assemble_L_R.m:73
                    Ljj[nn]=inp
# SiStER_assemble_L_R.m:74
                    Lvv[nn]=Kb
# SiStER_assemble_L_R.m:75
                    nn=nn + 1
# SiStER_assemble_L_R.m:76
                    Lii[nn]=inp
# SiStER_assemble_L_R.m:78
                    Ljj[nn]=inp + dot(3,Ny)
# SiStER_assemble_L_R.m:79
                    Lvv[nn]=- Kb
# SiStER_assemble_L_R.m:80
                    nn=nn + 1
# SiStER_assemble_L_R.m:81
                    R[inp,1]=0
# SiStER_assemble_L_R.m:83
                if (i == 2 and j == Nx) or (i == Ny and j == Nx):
                    #                L(inp,inp)=Kb;
                #                L(inp,inp-3*Ny)=-Kb;
                    Lii[nn]=inp
# SiStER_assemble_L_R.m:89
                    Ljj[nn]=inp
# SiStER_assemble_L_R.m:90
                    Lvv[nn]=Kb
# SiStER_assemble_L_R.m:91
                    nn=nn + 1
# SiStER_assemble_L_R.m:92
                    Lii[nn]=inp
# SiStER_assemble_L_R.m:94
                    Ljj[nn]=inp - dot(3,Ny)
# SiStER_assemble_L_R.m:95
                    Lvv[nn]=- Kb
# SiStER_assemble_L_R.m:96
                    nn=nn + 1
# SiStER_assemble_L_R.m:97
                    R[inp,1]=0
# SiStER_assemble_L_R.m:99
                if (BC.top(2) == 3 and i == 2 and j > 2 and j < Ny):
                    # Pressure gradient between top two rows extrapolates to 0 pressure at very top
#
                    Lii[nn]=inp
# SiStER_assemble_L_R.m:105
                    Ljj[nn]=inp
# SiStER_assemble_L_R.m:106
                    Lvv[nn]=multiply(Kb,(1 + dy(i - 1) / (dy(i) + dy(i - 1))))
# SiStER_assemble_L_R.m:107
                    nn=nn + 1
# SiStER_assemble_L_R.m:108
                    Lii[nn]=inp
# SiStER_assemble_L_R.m:110
                    Ljj[nn]=inp + 3
# SiStER_assemble_L_R.m:111
                    Lvv[nn]=multiply(- Kb,dy(i - 1)) / (dy(i) + dy(i - 1))
# SiStER_assemble_L_R.m:112
                    nn=nn + 1
# SiStER_assemble_L_R.m:113
                    R[inp,1]=0
# SiStER_assemble_L_R.m:115
                if (i == IP and j == JP and BC.top(2) != 3):
                    #                L(inp,inp)=Kb;
                    Lii[nn]=inp
# SiStER_assemble_L_R.m:122
                    Ljj[nn]=inp
# SiStER_assemble_L_R.m:123
                    Lvv[nn]=Kb
# SiStER_assemble_L_R.m:124
                    nn=nn + 1
# SiStER_assemble_L_R.m:125
                    R[inp,1]=dot(Kb,p0cell) / Kc
# SiStER_assemble_L_R.m:127
            else:
                # internal nodes
                # coeffs for vx
            #             L(inp,invx-3)=Kc/dx(j-1);
            #             L(inp,invx-3*Ny-3)=-Kc/dx(j-1);
                Lii[nn]=inp
# SiStER_assemble_L_R.m:141
                Ljj[nn]=invx - 3
# SiStER_assemble_L_R.m:142
                Lvv[nn]=Kc / dx(j - 1)
# SiStER_assemble_L_R.m:143
                nn=nn + 1
# SiStER_assemble_L_R.m:144
                Lii[nn]=inp
# SiStER_assemble_L_R.m:146
                Ljj[nn]=invx - dot(3,Ny) - 3
# SiStER_assemble_L_R.m:147
                Lvv[nn]=- Kc / dx(j - 1)
# SiStER_assemble_L_R.m:148
                nn=nn + 1
# SiStER_assemble_L_R.m:149
                #             L(inp,invy-3*Ny)=Kc/dy(i-1);
            #             L(inp,invy-3*Ny-3)=-Kc/dy(i-1);
                Lii[nn]=inp
# SiStER_assemble_L_R.m:155
                Ljj[nn]=invy - dot(3,Ny)
# SiStER_assemble_L_R.m:156
                Lvv[nn]=Kc / dy(i - 1)
# SiStER_assemble_L_R.m:157
                nn=nn + 1
# SiStER_assemble_L_R.m:158
                Lii[nn]=inp
# SiStER_assemble_L_R.m:160
                Ljj[nn]=invy - dot(3,Ny) - 3
# SiStER_assemble_L_R.m:161
                Lvv[nn]=- Kc / dy(i - 1)
# SiStER_assemble_L_R.m:162
                nn=nn + 1
# SiStER_assemble_L_R.m:163
                R[inp,1]=0
# SiStER_assemble_L_R.m:167
            ####### X-STOKES ###########################################
            if ((j == 1) and (i <= Ny - 1)) or ((j == Nx) and (i <= Ny - 1)) or (i == 1 and j <= Nx - 1 and j >= 2) or (i == Ny - 1 and j <= Nx - 1 and j >= 2) or (i == Ny):
                if ((j == 1) and (i <= Ny - 1)):
                    #              L(invx,invx)=Kb;
                    Lii[nn]=invx
# SiStER_assemble_L_R.m:184
                    Ljj[nn]=invx
# SiStER_assemble_L_R.m:185
                    Lvv[nn]=Kb
# SiStER_assemble_L_R.m:186
                    nn=nn + 1
# SiStER_assemble_L_R.m:187
                    R[invx,1]=dot(Kb,BC.left(3))
# SiStER_assemble_L_R.m:189
                if ((j == Nx) and (i <= Ny - 1)):
                    #              L(invx,invx)=Kb;
                    Lii[nn]=invx
# SiStER_assemble_L_R.m:195
                    Ljj[nn]=invx
# SiStER_assemble_L_R.m:196
                    Lvv[nn]=Kb
# SiStER_assemble_L_R.m:197
                    nn=nn + 1
# SiStER_assemble_L_R.m:198
                    R[invx,1]=dot(Kb,BC.right(3))
# SiStER_assemble_L_R.m:200
                if i == 1 and j <= Nx - 1 and j >= 2:
                    if BC.top(1) == 1:
                        #                  L(invx,invx+3)=Kc/(0.5*(dy(i)+dy(i+1)));
                    #                  L(invx,invx)=-Kc/(0.5*(dy(i)+dy(i+1)));
                        Lii[nn]=invx
# SiStER_assemble_L_R.m:209
                        Ljj[nn]=invx + 3
# SiStER_assemble_L_R.m:210
                        Lvv[nn]=Kc / (dot(0.5,(dy(i) + dy(i + 1))))
# SiStER_assemble_L_R.m:211
                        nn=nn + 1
# SiStER_assemble_L_R.m:212
                        Lii[nn]=invx
# SiStER_assemble_L_R.m:214
                        Ljj[nn]=invx
# SiStER_assemble_L_R.m:215
                        Lvv[nn]=- Kc / (dot(0.5,(dy(i) + dy(i + 1))))
# SiStER_assemble_L_R.m:216
                        nn=nn + 1
# SiStER_assemble_L_R.m:217
                        R[invx,1]=0
# SiStER_assemble_L_R.m:219
                    else:
                        if BC.top(1) == 0:
                            #                  L(invx,invx+3)=Kc/(dy(i)+dy(i+1));
                    #                  L(invx,invx)=-Kc*(1/dy(i)+1/(dy(i)+dy(i+1)));
                    # Multiply whole eq. by 2 so coefficients are closer to
                    # the others
                            Lii[nn]=invx
# SiStER_assemble_L_R.m:226
                            Ljj[nn]=invx + 3
# SiStER_assemble_L_R.m:227
                            Lvv[nn]=dot(- 2,Kc) / (dy(i) + dy(i + 1))
# SiStER_assemble_L_R.m:228
                            nn=nn + 1
# SiStER_assemble_L_R.m:229
                            Lii[nn]=invx
# SiStER_assemble_L_R.m:231
                            Ljj[nn]=invx
# SiStER_assemble_L_R.m:232
                            Lvv[nn]=dot(dot(2,Kc),(1 / dy(i) + 1 / (dy(i) + dy(i + 1))))
# SiStER_assemble_L_R.m:233
                            nn=nn + 1
# SiStER_assemble_L_R.m:234
                            R[invx,1]=dot(dot(dot(2,Kc),(1 / dy(i))),BC.top_profile(j))
# SiStER_assemble_L_R.m:236
                if i == Ny - 1 and j <= Nx - 1 and j >= 2:
                    if BC.bot(1) == 0:
                        #                  L(invx,invx)=Kc*(1/dy(i)+1/(dy(i-1)+dy(i)));
                    #                  L(invx,invx-3)=-Kc/(dy(i-1)+dy(i));
                        Lii[nn]=invx
# SiStER_assemble_L_R.m:246
                        Ljj[nn]=invx
# SiStER_assemble_L_R.m:247
                        Lvv[nn]=dot(dot(2,Kc),(1 / dy(i) + 1 / (dy(i - 1) + dy(i))))
# SiStER_assemble_L_R.m:248
                        nn=nn + 1
# SiStER_assemble_L_R.m:249
                        Lii[nn]=invx
# SiStER_assemble_L_R.m:251
                        Ljj[nn]=invx - 3
# SiStER_assemble_L_R.m:252
                        Lvv[nn]=dot(- 2,Kc) / (dy(i - 1) + dy(i))
# SiStER_assemble_L_R.m:253
                        nn=nn + 1
# SiStER_assemble_L_R.m:254
                        R[invx,1]=dot(dot(dot(2,Kc),(1 / dy(i))),BC.bot_profile(j))
# SiStER_assemble_L_R.m:256
                    else:
                        if BC.bot(1) == 1:
                            #                  L(invx,invx)=Kc/(0.5*(dy(i-1)+dy(i)));
                    #                  L(invx,invx-3)=-Kc/(0.5*(dy(i-1)+dy(i)));
                            Lii[nn]=invx
# SiStER_assemble_L_R.m:262
                            Ljj[nn]=invx
# SiStER_assemble_L_R.m:263
                            Lvv[nn]=Kc / (dot(0.5,(dy(i - 1) + dy(i))))
# SiStER_assemble_L_R.m:264
                            nn=nn + 1
# SiStER_assemble_L_R.m:265
                            Lii[nn]=invx
# SiStER_assemble_L_R.m:267
                            Ljj[nn]=invx - 3
# SiStER_assemble_L_R.m:268
                            Lvv[nn]=- Kc / (dot(0.5,(dy(i - 1) + dy(i))))
# SiStER_assemble_L_R.m:269
                            nn=nn + 1
# SiStER_assemble_L_R.m:270
                            R[invx,1]=0
# SiStER_assemble_L_R.m:272
                if i == Ny:
                    #              L(invx,invx)=Kb;
                    Lii[nn]=invx
# SiStER_assemble_L_R.m:282
                    Ljj[nn]=invx
# SiStER_assemble_L_R.m:283
                    Lvv[nn]=Kb
# SiStER_assemble_L_R.m:284
                    nn=nn + 1
# SiStER_assemble_L_R.m:285
                    R[invx,1]=0
# SiStER_assemble_L_R.m:287
            else:
                # X-STOKES: internal nodes
                # X-STOKES: coeffs for vx
                #         L(invx,invx-3*Ny)=4*etan(i+1,j)/(dx(j-1)*(dx(j-1)+dx(j))); #
                Lii[nn]=invx
# SiStER_assemble_L_R.m:300
                Ljj[nn]=invx - dot(3,Ny)
# SiStER_assemble_L_R.m:301
                Lvv[nn]=dot(4,etan(i + 1,j)) / (dot(dx(j - 1),(dx(j - 1) + dx(j))))
# SiStER_assemble_L_R.m:302
                nn=nn + 1
# SiStER_assemble_L_R.m:303
                Lii[nn]=invx
# SiStER_assemble_L_R.m:307
                Ljj[nn]=invx
# SiStER_assemble_L_R.m:308
                Lvv[nn]=dot((- 4 / (dx(j - 1) + dx(j))),(etan(i + 1,j + 1) / dx(j) + etan(i + 1,j) / dx(j - 1))) - dot((2 / dy(i)),(etas(i + 1,j) / (dy(i) + dy(i + 1)) + etas(i,j) / (dy(i - 1) + dy(i))))
# SiStER_assemble_L_R.m:309
                nn=nn + 1
# SiStER_assemble_L_R.m:310
                Lii[nn]=invx
# SiStER_assemble_L_R.m:314
                Ljj[nn]=invx + dot(3,Ny)
# SiStER_assemble_L_R.m:315
                Lvv[nn]=dot(4,etan(i + 1,j + 1)) / (dot(dx(j),(dx(j - 1) + dx(j))))
# SiStER_assemble_L_R.m:316
                nn=nn + 1
# SiStER_assemble_L_R.m:317
                Lii[nn]=invx
# SiStER_assemble_L_R.m:321
                Ljj[nn]=invx - 3
# SiStER_assemble_L_R.m:322
                Lvv[nn]=dot(2,etas(i,j)) / (dot(dy(i),(dy(i - 1) + dy(i))))
# SiStER_assemble_L_R.m:323
                nn=nn + 1
# SiStER_assemble_L_R.m:324
                Lii[nn]=invx
# SiStER_assemble_L_R.m:328
                Ljj[nn]=invx + 3
# SiStER_assemble_L_R.m:329
                Lvv[nn]=dot(2,etas(i + 1,j)) / (dot(dy(i),(dy(i) + dy(i + 1))))
# SiStER_assemble_L_R.m:330
                nn=nn + 1
# SiStER_assemble_L_R.m:331
                #         L(invx,invy+3)=2*etas(i+1,j)/(dy(i)*(dx(j-1)+dx(j))); #
                Lii[nn]=invx
# SiStER_assemble_L_R.m:337
                Ljj[nn]=invy + 3
# SiStER_assemble_L_R.m:338
                Lvv[nn]=dot(2,etas(i + 1,j)) / (dot(dy(i),(dx(j - 1) + dx(j))))
# SiStER_assemble_L_R.m:339
                nn=nn + 1
# SiStER_assemble_L_R.m:340
                Lii[nn]=invx
# SiStER_assemble_L_R.m:344
                Ljj[nn]=invy + 3 - dot(3,Ny)
# SiStER_assemble_L_R.m:345
                Lvv[nn]=dot(- 2,etas(i + 1,j)) / (dot(dy(i),(dx(j - 1) + dx(j))))
# SiStER_assemble_L_R.m:346
                nn=nn + 1
# SiStER_assemble_L_R.m:347
                Lii[nn]=invx
# SiStER_assemble_L_R.m:351
                Ljj[nn]=invy
# SiStER_assemble_L_R.m:352
                Lvv[nn]=dot(- 2,etas(i,j)) / (dot(dy(i),(dx(j - 1) + dx(j))))
# SiStER_assemble_L_R.m:353
                nn=nn + 1
# SiStER_assemble_L_R.m:354
                Lii[nn]=invx
# SiStER_assemble_L_R.m:358
                Ljj[nn]=invy - dot(3,Ny)
# SiStER_assemble_L_R.m:359
                Lvv[nn]=dot(2,etas(i,j)) / (dot(dy(i),(dx(j - 1) + dx(j))))
# SiStER_assemble_L_R.m:360
                nn=nn + 1
# SiStER_assemble_L_R.m:361
                #         L(invx,inp+3*Ny+3)=-2*Kc/(dx(j-1)+dx(j)); #
                Lii[nn]=invx
# SiStER_assemble_L_R.m:367
                Ljj[nn]=inp + dot(3,Ny) + 3
# SiStER_assemble_L_R.m:368
                Lvv[nn]=dot(- 2,Kc) / (dx(j - 1) + dx(j))
# SiStER_assemble_L_R.m:369
                nn=nn + 1
# SiStER_assemble_L_R.m:370
                Lii[nn]=invx
# SiStER_assemble_L_R.m:374
                Ljj[nn]=inp + 3
# SiStER_assemble_L_R.m:375
                Lvv[nn]=dot(2,Kc) / (dx(j - 1) + dx(j))
# SiStER_assemble_L_R.m:376
                nn=nn + 1
# SiStER_assemble_L_R.m:377
                R[invx,1]=dot(- gx,(rho(i,j) + rho(i + 1,j))) / 2 - dot(2.0,(srhs_xx(i + 1,j + 1) - srhs_xx(i + 1,j))) / (dx(j) + dx(j - 1)) - (srhs_xy(i + 1,j) - srhs_xy(i,j)) / dy(i)
# SiStER_assemble_L_R.m:380
            ####### Y-STOKES ###########################################
            if (j == 1 and i <= Ny - 1 and i >= 2) or (j == Nx - 1 and i <= Ny - 1 and i >= 2) or (j == Nx) or (i == 1 and j <= Nx - 1) or (i == Ny and j <= Nx - 1):
                if j == 1 and i >= 2 and i <= Ny - 1:
                    if BC.left(1) == 1:
                        #              L(invy,invy)=-2*Kc/(dx(j)+dx(j+1));
                    #              L(invy,invy+3*Ny)=2*Kc/(dx(j)+dx(j+1));
                        Lii[nn]=invy
# SiStER_assemble_L_R.m:399
                        Ljj[nn]=invy
# SiStER_assemble_L_R.m:400
                        Lvv[nn]=dot(- 2,Kc) / (dx(j) + dx(j + 1))
# SiStER_assemble_L_R.m:401
                        nn=nn + 1
# SiStER_assemble_L_R.m:402
                        Lii[nn]=invy
# SiStER_assemble_L_R.m:404
                        Ljj[nn]=invy + dot(3,Ny)
# SiStER_assemble_L_R.m:405
                        Lvv[nn]=dot(2,Kc) / (dx(j) + dx(j + 1))
# SiStER_assemble_L_R.m:406
                        nn=nn + 1
# SiStER_assemble_L_R.m:407
                        R[invy,1]=0
# SiStER_assemble_L_R.m:409
                    else:
                        if BC.left(1) == 0:
                            #              L(invy,invy)=-2*Kc*(1/(dx(j)+dx(j+1))+1/dx(j));
                    #              L(invy,invy+3*Ny)=2*Kc/(dx(j+1)+dx(j));
                            Lii[nn]=invy
# SiStER_assemble_L_R.m:415
                            Ljj[nn]=invy
# SiStER_assemble_L_R.m:416
                            Lvv[nn]=dot(dot(- 2,Kc),(1 / (dx(j) + dx(j + 1)) + 1 / dx(j)))
# SiStER_assemble_L_R.m:417
                            nn=nn + 1
# SiStER_assemble_L_R.m:418
                            Lii[nn]=invy
# SiStER_assemble_L_R.m:420
                            Ljj[nn]=invy + dot(3,Ny)
# SiStER_assemble_L_R.m:421
                            Lvv[nn]=dot(2,Kc) / (dx(j + 1) + dx(j))
# SiStER_assemble_L_R.m:422
                            nn=nn + 1
# SiStER_assemble_L_R.m:423
                            R[invy,1]=0
# SiStER_assemble_L_R.m:425
                if j == Nx - 1 and i <= Ny - 1 and i >= 2:
                    if BC.right(1) == 1:
                        #              L(invy,invy)=Kc/(0.5*(dx(j)+dx(j-1)));
                    #              L(invy,invy-3*Ny)=-Kc/(0.5*(dx(j)+dx(j-1)));
                        Lii[nn]=invy
# SiStER_assemble_L_R.m:434
                        Ljj[nn]=invy
# SiStER_assemble_L_R.m:435
                        Lvv[nn]=Kc / (dot(0.5,(dx(j) + dx(j - 1))))
# SiStER_assemble_L_R.m:436
                        nn=nn + 1
# SiStER_assemble_L_R.m:437
                        Lii[nn]=invy
# SiStER_assemble_L_R.m:439
                        Ljj[nn]=invy - dot(3,Ny)
# SiStER_assemble_L_R.m:440
                        Lvv[nn]=- Kc / (dot(0.5,(dx(j) + dx(j - 1))))
# SiStER_assemble_L_R.m:441
                        nn=nn + 1
# SiStER_assemble_L_R.m:442
                        R[invy,1]=0
# SiStER_assemble_L_R.m:444
                    else:
                        if BC.right(1) == 0:
                            #              L(invy,invy)=Kc*(1/(dx(j)+dx(j-1))+1/dx(j));
                    #              L(invy,invy-3*Ny)=-Kc/(dx(j)+dx(j-1));
                            Lii[nn]=invy
# SiStER_assemble_L_R.m:450
                            Ljj[nn]=invy
# SiStER_assemble_L_R.m:451
                            Lvv[nn]=dot(Kc,(1 / (dx(j) + dx(j - 1)) + 1 / dx(j)))
# SiStER_assemble_L_R.m:452
                            nn=nn + 1
# SiStER_assemble_L_R.m:453
                            Lii[nn]=invy
# SiStER_assemble_L_R.m:455
                            Ljj[nn]=invy - dot(3,Ny)
# SiStER_assemble_L_R.m:456
                            Lvv[nn]=- Kc / (dx(j) + dx(j - 1))
# SiStER_assemble_L_R.m:457
                            nn=nn + 1
# SiStER_assemble_L_R.m:458
                            R[invy,1]=0
# SiStER_assemble_L_R.m:460
                if j == Nx:
                    #              L(invy,invy)=Kb;
                    Lii[nn]=invy
# SiStER_assemble_L_R.m:468
                    Ljj[nn]=invy
# SiStER_assemble_L_R.m:469
                    Lvv[nn]=Kb
# SiStER_assemble_L_R.m:470
                    nn=nn + 1
# SiStER_assemble_L_R.m:471
                    R[invy,1]=0
# SiStER_assemble_L_R.m:473
                if i == 1 and j <= Nx - 1:
                    if BC.top(2) == 0:
                        #              L(invy,invy)=Kb;
                        Lii[nn]=invy
# SiStER_assemble_L_R.m:481
                        Ljj[nn]=invy
# SiStER_assemble_L_R.m:482
                        Lvv[nn]=Kb
# SiStER_assemble_L_R.m:483
                        nn=nn + 1
# SiStER_assemble_L_R.m:484
                        R[invy,1]=dot(Kb,BC.top(3))
# SiStER_assemble_L_R.m:486
                    else:
                        if BC.top(2) == 3:
                            #               open top dvy/dy=0, G.Ito
                            Lii[nn]=invy
# SiStER_assemble_L_R.m:490
                            Ljj[nn]=invy
# SiStER_assemble_L_R.m:491
                            Lvv[nn]=Kb
# SiStER_assemble_L_R.m:492
                            nn=nn + 1
# SiStER_assemble_L_R.m:493
                            Lii[nn]=invy
# SiStER_assemble_L_R.m:495
                            Ljj[nn]=invy + 3
# SiStER_assemble_L_R.m:496
                            Lvv[nn]=- Kb
# SiStER_assemble_L_R.m:497
                            nn=nn + 1
# SiStER_assemble_L_R.m:498
                            R[invy,1]=0
# SiStER_assemble_L_R.m:500
                if i == Ny and j <= Nx - 1:
                    if BC.bot(2) == 0:
                        #              L(invy,invy)=Kb;
                        Lii[nn]=invy
# SiStER_assemble_L_R.m:510
                        Ljj[nn]=invy
# SiStER_assemble_L_R.m:511
                        Lvv[nn]=Kb
# SiStER_assemble_L_R.m:512
                        nn=nn + 1
# SiStER_assemble_L_R.m:513
                        R[invy,1]=dot(Kb,BC.bot(3))
# SiStER_assemble_L_R.m:515
                    else:
                        if BC.bot(2) == 2:
                            dL=300000.0
# SiStER_assemble_L_R.m:519
                            Lii[nn]=invy
# SiStER_assemble_L_R.m:521
                            Ljj[nn]=invy
# SiStER_assemble_L_R.m:522
                            Lvv[nn]=dot(Kc,(1 / dL + 1 / dy(i - 1)))
# SiStER_assemble_L_R.m:523
                            nn=nn + 1
# SiStER_assemble_L_R.m:524
                            Lii[nn]=invy
# SiStER_assemble_L_R.m:526
                            Ljj[nn]=invy - 3
# SiStER_assemble_L_R.m:527
                            Lvv[nn]=dot(Kc,(- 1 / dy(i - 1)))
# SiStER_assemble_L_R.m:528
                            nn=nn + 1
# SiStER_assemble_L_R.m:529
                            R[invy,1]=0
# SiStER_assemble_L_R.m:531
            else:
                # internal nodes
                # coeffs for vy
            #         L(invy,invy-3*Ny)=2*etas(i,j)/(dx(j)*(dx(j-1)+dx(j))); #
                Lii[nn]=invy
# SiStER_assemble_L_R.m:546
                Ljj[nn]=invy - dot(3,Ny)
# SiStER_assemble_L_R.m:547
                Lvv[nn]=dot(2,etas(i,j)) / (dot(dx(j),(dx(j - 1) + dx(j))))
# SiStER_assemble_L_R.m:548
                nn=nn + 1
# SiStER_assemble_L_R.m:549
                Lii[nn]=invy
# SiStER_assemble_L_R.m:553
                Ljj[nn]=invy
# SiStER_assemble_L_R.m:554
                Lvv[nn]=dot((- 4 / (dy(i - 1) + dy(i))),(etan(i + 1,j + 1) / dy(i) + etan(i,j + 1) / dy(i - 1))) - dot((2 / dx(j)),(etas(i,j + 1) / (dx(j) + dx(j + 1)) + etas(i,j) / (dx(j - 1) + dx(j))))
# SiStER_assemble_L_R.m:555
                nn=nn + 1
# SiStER_assemble_L_R.m:556
                Lii[nn]=invy
# SiStER_assemble_L_R.m:560
                Ljj[nn]=invy + dot(3,Ny)
# SiStER_assemble_L_R.m:561
                Lvv[nn]=dot(2,etas(i,j + 1)) / (dot(dx(j),(dx(j) + dx(j + 1))))
# SiStER_assemble_L_R.m:562
                nn=nn + 1
# SiStER_assemble_L_R.m:563
                Lii[nn]=invy
# SiStER_assemble_L_R.m:567
                Ljj[nn]=invy - 3
# SiStER_assemble_L_R.m:568
                Lvv[nn]=dot(4,etan(i,j + 1)) / (dot(dy(i - 1),(dy(i - 1) + dy(i))))
# SiStER_assemble_L_R.m:569
                nn=nn + 1
# SiStER_assemble_L_R.m:570
                Lii[nn]=invy
# SiStER_assemble_L_R.m:574
                Ljj[nn]=invy + 3
# SiStER_assemble_L_R.m:575
                Lvv[nn]=dot(4,etan(i + 1,j + 1)) / (dot(dy(i),(dy(i - 1) + dy(i))))
# SiStER_assemble_L_R.m:576
                nn=nn + 1
# SiStER_assemble_L_R.m:577
                #         L(invy,invx+3*Ny)=2*etas(i,j+1)/(dx(j)*(dy(i-1)+dy(i)));  #
                Lii[nn]=invy
# SiStER_assemble_L_R.m:583
                Ljj[nn]=invx + dot(3,Ny)
# SiStER_assemble_L_R.m:584
                Lvv[nn]=dot(2,etas(i,j + 1)) / (dot(dx(j),(dy(i - 1) + dy(i))))
# SiStER_assemble_L_R.m:585
                nn=nn + 1
# SiStER_assemble_L_R.m:586
                Lii[nn]=invy
# SiStER_assemble_L_R.m:590
                Ljj[nn]=invx + dot(3,Ny) - 3
# SiStER_assemble_L_R.m:591
                Lvv[nn]=dot(- 2,etas(i,j + 1)) / (dot(dx(j),(dy(i - 1) + dy(i))))
# SiStER_assemble_L_R.m:592
                nn=nn + 1
# SiStER_assemble_L_R.m:593
                Lii[nn]=invy
# SiStER_assemble_L_R.m:598
                Ljj[nn]=invx
# SiStER_assemble_L_R.m:599
                Lvv[nn]=dot(- 2,etas(i,j)) / (dot(dx(j),(dy(i - 1) + dy(i))))
# SiStER_assemble_L_R.m:600
                nn=nn + 1
# SiStER_assemble_L_R.m:601
                Lii[nn]=invy
# SiStER_assemble_L_R.m:605
                Ljj[nn]=invx - 3
# SiStER_assemble_L_R.m:606
                Lvv[nn]=dot(2,etas(i,j)) / (dot(dx(j),(dy(i - 1) + dy(i))))
# SiStER_assemble_L_R.m:607
                nn=nn + 1
# SiStER_assemble_L_R.m:608
                #         L(invy,inp+3*Ny+3)=-2*Kc/(dy(i-1)+dy(i)); #
                Lii[nn]=invy
# SiStER_assemble_L_R.m:613
                Ljj[nn]=inp + dot(3,Ny) + 3
# SiStER_assemble_L_R.m:614
                Lvv[nn]=dot(- 2,Kc) / (dy(i - 1) + dy(i))
# SiStER_assemble_L_R.m:615
                nn=nn + 1
# SiStER_assemble_L_R.m:616
                Lii[nn]=invy
# SiStER_assemble_L_R.m:620
                Ljj[nn]=inp + dot(3,Ny)
# SiStER_assemble_L_R.m:621
                Lvv[nn]=dot(2,Kc) / (dy(i - 1) + dy(i))
# SiStER_assemble_L_R.m:622
                nn=nn + 1
# SiStER_assemble_L_R.m:623
                R[invy,1]=dot(- gy,(rho(i,j) + rho(i,j + 1))) / 2 + dot(2.0,(srhs_xx(i + 1,j + 1) - srhs_xx(i,j + 1))) / (dy(i) + dy(i - 1)) - (srhs_xy(i,j + 1) - srhs_xy(i,j)) / dx(j)
# SiStER_assemble_L_R.m:626
    
    nn=nn - 1
# SiStER_assemble_L_R.m:637
    ### Build Sparse Matrix
    
    Li=Lii(arange(1,nn))
# SiStER_assemble_L_R.m:640
    Lj=Ljj(arange(1,nn))
# SiStER_assemble_L_R.m:641
    Lv=Lvv(arange(1,nn))
# SiStER_assemble_L_R.m:642
    L=sparse(Li,Lj,Lv)
# SiStER_assemble_L_R.m:645
    # SOLVE LINEAR SYSTEM now down in SiStER_flow_solve G.Ito
# Matlab direct solver
# tic
# S=L\R;
# toc
#
    
    return L,R,Kc,Kb
    
if __name__ == '__main__':
    pass
    