# Generated with SMOP  0.41
from libsmop import *
# SiStER_Input_File_continental_rift.m

    # SiStER_Input_File
    
    # DURATION OF SIMULATION AND FREQUENCY OF OUTPUT ##########################
    Nt=100
# SiStER_Input_File_continental_rift.m:5
    
    dt_out=10
# SiStER_Input_File_continental_rift.m:6
    
    # DOMAIN SIZE AND GRIDDING ################################################
    xsize=90000.0
# SiStER_Input_File_continental_rift.m:10
    ysize=30000.0
# SiStER_Input_File_continental_rift.m:11
    # gridding- from 0 to GRID.x(1), grid size is GRID.dx(1)
# from GRID.x(1) to GRID.x(2), grid size is GRID.dx(1) etc...
# same for y
    GRID.dx[1]=2000
# SiStER_Input_File_continental_rift.m:15
    GRID.x[1]=30000.0
# SiStER_Input_File_continental_rift.m:16
    GRID.dx[2]=400
# SiStER_Input_File_continental_rift.m:17
    GRID.x[2]=60000.0
# SiStER_Input_File_continental_rift.m:18
    GRID.dx[3]=2000
# SiStER_Input_File_continental_rift.m:19
    GRID.dy[1]=2000
# SiStER_Input_File_continental_rift.m:20
    GRID.y[1]=9000.0
# SiStER_Input_File_continental_rift.m:21
    GRID.dy[2]=400
# SiStER_Input_File_continental_rift.m:22
    GRID.y[2]=22000.0
# SiStER_Input_File_continental_rift.m:23
    GRID.dy[3]=2000
# SiStER_Input_File_continental_rift.m:24
    # LAGRANGIAN MARKERS ######################################################
    Mquad=8
# SiStER_Input_File_continental_rift.m:28
    
    Mquad_crit=4
# SiStER_Input_File_continental_rift.m:29
    
    # GEOMETRY ################################################################
    
    Nphase=3
# SiStER_Input_File_continental_rift.m:33
    
    # phase 1
    GEOM(1).type = copy(1)
# SiStER_Input_File_continental_rift.m:36
    
    GEOM(1).top = copy(0)
# SiStER_Input_File_continental_rift.m:37
    GEOM(1).bot = copy(10000.0)
# SiStER_Input_File_continental_rift.m:38
    # phase 2
    GEOM(2).type = copy(1)
# SiStER_Input_File_continental_rift.m:41
    
    GEOM(2).top = copy(10000.0)
# SiStER_Input_File_continental_rift.m:42
    GEOM(2).bot = copy(30000.0)
# SiStER_Input_File_continental_rift.m:43
    # phase 3
    GEOM(3).type = copy(2)
# SiStER_Input_File_continental_rift.m:46
    
    GEOM(3).x0 = copy(xsize / 2)
# SiStER_Input_File_continental_rift.m:47
    GEOM(3).y0 = copy(20000.0)
# SiStER_Input_File_continental_rift.m:48
    GEOM(3).rad = copy(1000.0)
# SiStER_Input_File_continental_rift.m:49
    # MATERIAL PROPERTIES #####################################################
    
    # creep laws of the form: pre^(-1/n)*epsII^((1-n)/n)*exp(E/(nRT))
# harmonically averaging diffusion creep, dislocation creep 
# (and plastic creep to simulate brittle failure)
    
    # phase 1
    MAT(1).phase = copy(1)
# SiStER_Input_File_continental_rift.m:59
    # density parameters
    MAT(1).rho0 = copy(0.01)
# SiStER_Input_File_continental_rift.m:61
    MAT(1).alpha = copy(0)
# SiStER_Input_File_continental_rift.m:62
    # thermal parameters
    MAT(1).k = copy(3)
# SiStER_Input_File_continental_rift.m:64
    MAT(1).cp = copy(1000)
# SiStER_Input_File_continental_rift.m:65
    # elasticity
    MAT(1).G = copy(1e+18)
# SiStER_Input_File_continental_rift.m:67
    # diffusion creep parameters
    MAT(1).pre_diff = copy(0.5 / 1e+18)
# SiStER_Input_File_continental_rift.m:69
    MAT(1).Ediff = copy(0)
# SiStER_Input_File_continental_rift.m:70
    MAT(1).ndiff = copy(1)
# SiStER_Input_File_continental_rift.m:71
    # dislocation creep parameters
    MAT(1).pre_disc = copy(0.5 / 1e+18)
# SiStER_Input_File_continental_rift.m:73
    MAT(1).Edisc = copy(0)
# SiStER_Input_File_continental_rift.m:74
    MAT(1).ndisc = copy(1)
# SiStER_Input_File_continental_rift.m:75
    # plasticity
    MAT(1).mu = copy(0.6)
# SiStER_Input_File_continental_rift.m:77
    MAT(1).mumin = copy(0.3)
# SiStER_Input_File_continental_rift.m:78
    MAT(1).Cmax = copy(40000000.0)
# SiStER_Input_File_continental_rift.m:79
    MAT(1).Cmin = copy(10000.0)
# SiStER_Input_File_continental_rift.m:80
    MAT(1).ecrit = copy(0.1)
# SiStER_Input_File_continental_rift.m:81
    # phase 2
    MAT(2).phase = copy(2)
# SiStER_Input_File_continental_rift.m:85
    # density parameters
    MAT(2).rho0 = copy(2700)
# SiStER_Input_File_continental_rift.m:87
    MAT(2).alpha = copy(0)
# SiStER_Input_File_continental_rift.m:88
    # thermal parameters
    MAT(2).k = copy(3)
# SiStER_Input_File_continental_rift.m:90
    MAT(2).cp = copy(1000)
# SiStER_Input_File_continental_rift.m:91
    # elasticity
    MAT(2).G = copy(30000000000.0)
# SiStER_Input_File_continental_rift.m:93
    # diffusion creep parameters
    MAT(2).pre_diff = copy(0.5 / 1e+40)
# SiStER_Input_File_continental_rift.m:95
    MAT(2).Ediff = copy(0)
# SiStER_Input_File_continental_rift.m:96
    MAT(2).ndiff = copy(1)
# SiStER_Input_File_continental_rift.m:97
    # dislocation creep parameters
    MAT(2).pre_disc = copy(0.001)
# SiStER_Input_File_continental_rift.m:99
    MAT(2).Edisc = copy(dot(167000,2.25))
# SiStER_Input_File_continental_rift.m:100
    MAT(2).ndisc = copy(2)
# SiStER_Input_File_continental_rift.m:101
    # plasticity
    MAT(2).mu = copy(0.6)
# SiStER_Input_File_continental_rift.m:103
    MAT(2).mumin = copy(0.3)
# SiStER_Input_File_continental_rift.m:104
    MAT(2).Cmax = copy(40000000.0)
# SiStER_Input_File_continental_rift.m:105
    MAT(2).Cmin = copy(10000.0)
# SiStER_Input_File_continental_rift.m:106
    MAT(2).ecrit = copy(0.1)
# SiStER_Input_File_continental_rift.m:107
    # phase 3
    MAT(3).phase = copy(3)
# SiStER_Input_File_continental_rift.m:111
    # density parameters
    MAT(3).rho0 = copy(2700)
# SiStER_Input_File_continental_rift.m:113
    MAT(3).alpha = copy(0)
# SiStER_Input_File_continental_rift.m:114
    # thermal parameters
    MAT(3).k = copy(5)
# SiStER_Input_File_continental_rift.m:116
    MAT(3).cp = copy(1000)
# SiStER_Input_File_continental_rift.m:117
    # elasticity
    MAT(3).G = copy(30000000000.0)
# SiStER_Input_File_continental_rift.m:119
    # diffusion creep parameters
    MAT(3).pre_diff = copy(0.5 / 1e+40)
# SiStER_Input_File_continental_rift.m:121
    MAT(3).Ediff = copy(0)
# SiStER_Input_File_continental_rift.m:122
    MAT(3).ndiff = copy(1)
# SiStER_Input_File_continental_rift.m:123
    # dislocation creep parameters
    MAT(3).pre_disc = copy(0.001)
# SiStER_Input_File_continental_rift.m:125
    MAT(3).Edisc = copy(dot(167000,2.25))
# SiStER_Input_File_continental_rift.m:126
    MAT(3).ndisc = copy(2)
# SiStER_Input_File_continental_rift.m:127
    # plasticity
    MAT(3).mu = copy(0.6)
# SiStER_Input_File_continental_rift.m:129
    MAT(3).mumin = copy(0.3)
# SiStER_Input_File_continental_rift.m:130
    MAT(3).Cmax = copy(10000.0)
# SiStER_Input_File_continental_rift.m:131
    MAT(3).Cmin = copy(10000.0)
# SiStER_Input_File_continental_rift.m:132
    MAT(3).ecrit = copy(0.1)
# SiStER_Input_File_continental_rift.m:133
    # ADDITIONAL PARAMETERS ###################################################
    PARAMS.YNElast = copy(1)
# SiStER_Input_File_continental_rift.m:137
    
    PARAMS.YNPlas = copy(1)
# SiStER_Input_File_continental_rift.m:138
    
    PARAMS.tau_heal = copy(1e+12)
# SiStER_Input_File_continental_rift.m:139
    
    PARAMS.gx = copy(0)
# SiStER_Input_File_continental_rift.m:140
    
    PARAMS.gy = copy(9.8)
# SiStER_Input_File_continental_rift.m:141
    
    PARAMS.fracCFL = copy(0.5)
# SiStER_Input_File_continental_rift.m:142
    
    PARAMS.R = copy(8.314)
# SiStER_Input_File_continental_rift.m:143
    
    PARAMS.etamax = copy(1e+25)
# SiStER_Input_File_continental_rift.m:144
    
    PARAMS.etamin = copy(1e+18)
# SiStER_Input_File_continental_rift.m:145
    
    PARAMS.Tsolve = copy(1)
# SiStER_Input_File_continental_rift.m:146
    
    # initial temperature profile, polynomial with depth 
# T = a0 + a1*y+a2*y^2+a3*y^3+amp*sin(2*pi*X/lam)
# (make sure it matches the BCs)
    PARAMS.a0 = copy(0)
# SiStER_Input_File_continental_rift.m:150
    PARAMS.a1 = copy(0)
# SiStER_Input_File_continental_rift.m:151
    PARAMS.a2 = copy(0)
# SiStER_Input_File_continental_rift.m:152
    PARAMS.a3 = copy(1000 / (30000.0) ** 3)
# SiStER_Input_File_continental_rift.m:153
    PARAMS.amp = copy(0)
# SiStER_Input_File_continental_rift.m:154
    
    PARAMS.lam = copy(1)
# SiStER_Input_File_continental_rift.m:155
    
    PARAMS.ynTreset = copy(1)
# SiStER_Input_File_continental_rift.m:156
    
    PARAMS.T0 = copy(0)
# SiStER_Input_File_continental_rift.m:157
    # reference values for the constant diffusivity thermal solver
# (kappa = kref / (rhoref*cpref))
    PARAMS.rhoref = copy(MAT(2).rho0)
# SiStER_Input_File_continental_rift.m:160
    PARAMS.kref = copy(3)
# SiStER_Input_File_continental_rift.m:161
    PARAMS.cpref = copy(1000)
# SiStER_Input_File_continental_rift.m:162
    # TOPOGRAPHY EVOLUTION (interface between rock and sticky air/water layer)
    PARAMS.Ntopo_markers = copy(1000)
# SiStER_Input_File_continental_rift.m:165
    
    PARAMS.YNSurfaceProcesses = copy(1)
# SiStER_Input_File_continental_rift.m:166
    
    PARAMS.topo_kappa = copy(1e-08)
# SiStER_Input_File_continental_rift.m:167
    
    # Solver iterations
    PARAMS.Npicard_min = copy(10)
# SiStER_Input_File_continental_rift.m:171
    
    PARAMS.Npicard_max = copy(100)
# SiStER_Input_File_continental_rift.m:172
    
    PARAMS.conv_crit_ResL2 = copy(1e-09)
# SiStER_Input_File_continental_rift.m:173
    PARAMS.pitswitch = copy(0)
# SiStER_Input_File_continental_rift.m:174
    
    # BOUNDARY CONDITIONS #####################################################
    
    # pressure
    PARAMS.p0cell = copy(0)
# SiStER_Input_File_continental_rift.m:180
    
    # flow
    
    # boundary conditions
# entries in BC correspond to
# 1/ rollers? (1=yes, 0=no)
# 2/ type of velocity normal to boundary (0=constant)
# 3/ value of normal velocity
    
    BC.top = copy(concat([1,0,1.0563e-10]))
# SiStER_Input_File_continental_rift.m:191
    BC.bot = copy(concat([1,0,- 1.0563e-10]))
# SiStER_Input_File_continental_rift.m:192
    BC.left = copy(concat([1,0,- 3.1688e-10]))
# SiStER_Input_File_continental_rift.m:193
    BC.right = copy(concat([1,0,3.1688e-10]))
# SiStER_Input_File_continental_rift.m:194
    PARAMS.BalanceStickyLayer = copy(1)
# SiStER_Input_File_continental_rift.m:195
    
    # / outflow BCs to balance the inflow / outflow of sticky layer material,
# and rock separately, based on the position of the sticky layer / air
# interface
    
    # thermal
    
    # entries in BCtherm correspond to
# 1/ type? (1=Dirichlet, 2=Neumann)
# 2/ value
    BCtherm.top = copy(concat([1,0]))
# SiStER_Input_File_continental_rift.m:206
    BCtherm.bot = copy(concat([1,1000]))
# SiStER_Input_File_continental_rift.m:207
    BCtherm.left = copy(concat([2,0]))
# SiStER_Input_File_continental_rift.m:208
    BCtherm.right = copy(concat([2,0]))
# SiStER_Input_File_continental_rift.m:209