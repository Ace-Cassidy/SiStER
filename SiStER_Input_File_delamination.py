# Generated with SMOP  0.41
from libsmop import *
# SiStER_Input_File_delamination.m

    # SiStER_Input_File
    
    # DURATION OF SIMULATION AND FREQUENCY OF OUTPUT ##########################
    Nt=200
# SiStER_Input_File_delamination.m:5
    
    dt_out=10
# SiStER_Input_File_delamination.m:6
    
    # DOMAIN SIZE AND GRIDDING ################################################
    xsize=500000.0
# SiStER_Input_File_delamination.m:10
    ysize=300000.0
# SiStER_Input_File_delamination.m:11
    # gridding- from 0 to GRID.x(1), grid size is GRID.dx(1)
# from GRID.x(1) to GRID.x(2), grid size is GRID.dx(1) etc...
# same for y
    GRID.dx[1]=5000.0
# SiStER_Input_File_delamination.m:15
    GRID.x[1]=500000.0
# SiStER_Input_File_delamination.m:16
    GRID.dy[1]=5000.0
# SiStER_Input_File_delamination.m:17
    GRID.y[1]=300000.0
# SiStER_Input_File_delamination.m:18
    # LAGRANGIAN MARKERS ######################################################
    Mquad=6
# SiStER_Input_File_delamination.m:22
    
    Mquad_crit=3
# SiStER_Input_File_delamination.m:23
    
    # GEOMETRY ################################################################
    
    Nphase=4
# SiStER_Input_File_delamination.m:27
    
    # phase 1
    GEOM(1).type = copy(1)
# SiStER_Input_File_delamination.m:30
    
    GEOM(1).top = copy(0)
# SiStER_Input_File_delamination.m:31
    GEOM(1).bot = copy(50000.0)
# SiStER_Input_File_delamination.m:32
    # phase 2
    GEOM(2).type = copy(1)
# SiStER_Input_File_delamination.m:35
    
    GEOM(2).top = copy(50000.0)
# SiStER_Input_File_delamination.m:36
    GEOM(2).bot = copy(150000.0)
# SiStER_Input_File_delamination.m:37
    # phase 3
    GEOM(3).type = copy(1)
# SiStER_Input_File_delamination.m:40
    
    GEOM(3).top = copy(150000.0)
# SiStER_Input_File_delamination.m:41
    GEOM(3).bot = copy(300000.0)
# SiStER_Input_File_delamination.m:42
    # phase 4
    GEOM(4).type = copy(3)
# SiStER_Input_File_delamination.m:45
    
    GEOM(4).top = copy(100000.0)
# SiStER_Input_File_delamination.m:46
    GEOM(4).bot = copy(190000.0)
# SiStER_Input_File_delamination.m:47
    GEOM(4).left = copy(200000.0)
# SiStER_Input_File_delamination.m:48
    GEOM(4).right = copy(300000.0)
# SiStER_Input_File_delamination.m:49
    # MATERIAL PROPERTIES #####################################################
    
    # creep laws of the form: pre^(-1/n)*epsII^((1-n)/n)*exp(E/(nRT))
# harmonically averaging diffusion creep, dislocation creep 
# (and plastic creep to simulate brittle failure)
    
    # phase 1
    MAT(1).phase = copy(1)
# SiStER_Input_File_delamination.m:59
    # density parameters
    MAT(1).rho0 = copy(0.01)
# SiStER_Input_File_delamination.m:61
    MAT(1).alpha = copy(0)
# SiStER_Input_File_delamination.m:62
    # elasticity
    MAT(1).G = copy(1e+18)
# SiStER_Input_File_delamination.m:64
    # diffusion creep parameters
    MAT(1).pre_diff = copy(0.5 / 1e+18)
# SiStER_Input_File_delamination.m:66
    MAT(1).Ediff = copy(0)
# SiStER_Input_File_delamination.m:67
    MAT(1).ndiff = copy(1)
# SiStER_Input_File_delamination.m:68
    # dislocation creep parameters
    MAT(1).pre_disc = copy(0.5 / 1e+18)
# SiStER_Input_File_delamination.m:70
    MAT(1).Edisc = copy(0)
# SiStER_Input_File_delamination.m:71
    MAT(1).ndisc = copy(1)
# SiStER_Input_File_delamination.m:72
    # plasticity
    MAT(1).mu = copy(0.6)
# SiStER_Input_File_delamination.m:74
    MAT(1).Cmax = copy(10000000000.0)
# SiStER_Input_File_delamination.m:75
    MAT(1).Cmin = copy(10000000000.0)
# SiStER_Input_File_delamination.m:76
    MAT(1).ecrit = copy(0.1)
# SiStER_Input_File_delamination.m:77
    # phase 2
    MAT(2).phase = copy(2)
# SiStER_Input_File_delamination.m:81
    # density parameters
    MAT(2).rho0 = copy(3400)
# SiStER_Input_File_delamination.m:83
    MAT(2).alpha = copy(0)
# SiStER_Input_File_delamination.m:84
    # elasticity
    MAT(2).G = copy(1e+18)
# SiStER_Input_File_delamination.m:86
    # diffusion creep parameters
    MAT(2).pre_diff = copy(0.5 / 1e+20)
# SiStER_Input_File_delamination.m:88
    MAT(2).Ediff = copy(0)
# SiStER_Input_File_delamination.m:89
    MAT(2).ndiff = copy(1)
# SiStER_Input_File_delamination.m:90
    # dislocation creep parameters
    MAT(2).pre_disc = copy(0.5 / 1e+20)
# SiStER_Input_File_delamination.m:92
    MAT(2).Edisc = copy(0)
# SiStER_Input_File_delamination.m:93
    MAT(2).ndisc = copy(1)
# SiStER_Input_File_delamination.m:94
    # plasticity
    MAT(2).mu = copy(0.6)
# SiStER_Input_File_delamination.m:96
    MAT(2).Cmax = copy(10000000000.0)
# SiStER_Input_File_delamination.m:97
    MAT(2).Cmin = copy(10000000000.0)
# SiStER_Input_File_delamination.m:98
    MAT(2).ecrit = copy(0.1)
# SiStER_Input_File_delamination.m:99
    # phase 3
    MAT(3).phase = copy(3)
# SiStER_Input_File_delamination.m:102
    # density parameters
    MAT(3).rho0 = copy(3200)
# SiStER_Input_File_delamination.m:104
    MAT(3).alpha = copy(0)
# SiStER_Input_File_delamination.m:105
    # elasticity
    MAT(3).G = copy(1e+18)
# SiStER_Input_File_delamination.m:107
    # diffusion creep parameters
    MAT(3).pre_diff = copy(0.5 / 1e+19)
# SiStER_Input_File_delamination.m:109
    MAT(3).Ediff = copy(0)
# SiStER_Input_File_delamination.m:110
    MAT(3).ndiff = copy(1)
# SiStER_Input_File_delamination.m:111
    # dislocation creep parameters
    MAT(3).pre_disc = copy(0.5 / 1e+19)
# SiStER_Input_File_delamination.m:113
    MAT(3).Edisc = copy(0)
# SiStER_Input_File_delamination.m:114
    MAT(3).ndisc = copy(1)
# SiStER_Input_File_delamination.m:115
    # plasticity
    MAT(3).mu = copy(0.6)
# SiStER_Input_File_delamination.m:117
    MAT(3).Cmax = copy(10000000000.0)
# SiStER_Input_File_delamination.m:118
    MAT(3).Cmin = copy(10000000000.0)
# SiStER_Input_File_delamination.m:119
    MAT(3).ecrit = copy(0.1)
# SiStER_Input_File_delamination.m:120
    # phase 4
    MAT(4).phase = copy(4)
# SiStER_Input_File_delamination.m:123
    # density parameters
    MAT(4).rho0 = copy(3400)
# SiStER_Input_File_delamination.m:125
    MAT(4).alpha = copy(0)
# SiStER_Input_File_delamination.m:126
    # elasticity
    MAT(4).G = copy(1e+18)
# SiStER_Input_File_delamination.m:128
    # diffusion creep parameters
    MAT(4).pre_diff = copy(0.5 / 1e+20)
# SiStER_Input_File_delamination.m:130
    MAT(4).Ediff = copy(0)
# SiStER_Input_File_delamination.m:131
    MAT(4).ndiff = copy(1)
# SiStER_Input_File_delamination.m:132
    # dislocation creep parameters
    MAT(4).pre_disc = copy(0.5 / 1e+20)
# SiStER_Input_File_delamination.m:134
    MAT(4).Edisc = copy(0)
# SiStER_Input_File_delamination.m:135
    MAT(4).ndisc = copy(1)
# SiStER_Input_File_delamination.m:136
    # plasticity
    MAT(4).mu = copy(0.6)
# SiStER_Input_File_delamination.m:138
    MAT(4).Cmax = copy(10000000000.0)
# SiStER_Input_File_delamination.m:139
    MAT(4).Cmin = copy(10000000000.0)
# SiStER_Input_File_delamination.m:140
    MAT(4).ecrit = copy(0.1)
# SiStER_Input_File_delamination.m:141
    # ADDITIONAL PARAMETERS ###################################################
    PARAMS.YNElast = copy(0)
# SiStER_Input_File_delamination.m:145
    
    PARAMS.YNPlas = copy(0)
# SiStER_Input_File_delamination.m:146
    
    PARAMS.epsII_from_stress = copy(1)
# SiStER_Input_File_delamination.m:147
    
    PARAMS.tau_heal = copy(1e+12)
# SiStER_Input_File_delamination.m:148
    
    PARAMS.gx = copy(0)
# SiStER_Input_File_delamination.m:149
    
    PARAMS.gy = copy(9.8)
# SiStER_Input_File_delamination.m:150
    
    PARAMS.fracCFL = copy(0.5)
# SiStER_Input_File_delamination.m:151
    
    PARAMS.R = copy(8.314)
# SiStER_Input_File_delamination.m:152
    
    PARAMS.etamax = copy(1e+25)
# SiStER_Input_File_delamination.m:153
    
    PARAMS.etamin = copy(1e+18)
# SiStER_Input_File_delamination.m:154
    
    PARAMS.Tsolve = copy(0)
# SiStER_Input_File_delamination.m:155
    
    # initial temperature profile, polynomial with depth 
# T = a0 + a1*y+a2*y^2+a3*y^3+amp*sin(2*pi*X/lam)
# (make sure it matches the BCs)
    PARAMS.a0 = copy(0)
# SiStER_Input_File_delamination.m:159
    PARAMS.a1 = copy(0)
# SiStER_Input_File_delamination.m:160
    PARAMS.a2 = copy(0)
# SiStER_Input_File_delamination.m:161
    PARAMS.a3 = copy(1000 / (30000.0) ** 3)
# SiStER_Input_File_delamination.m:162
    PARAMS.amp = copy(0)
# SiStER_Input_File_delamination.m:163
    
    PARAMS.lam = copy(1)
# SiStER_Input_File_delamination.m:164
    
    PARAMS.ynTreset = copy(1)
# SiStER_Input_File_delamination.m:165
    
    PARAMS.T0 = copy(0)
# SiStER_Input_File_delamination.m:166
    # reference values for the constant diffusivity thermal solver
# (kappa = kref / (rhoref*cpref))
    PARAMS.rhoref = copy(MAT(2).rho0)
# SiStER_Input_File_delamination.m:169
    PARAMS.kref = copy(3)
# SiStER_Input_File_delamination.m:170
    PARAMS.cpref = copy(1000)
# SiStER_Input_File_delamination.m:171
    # TOPOGRAPHY EVOLUTION (interface between rock and sticky air/water layer)
    PARAMS.Ntopo_markers = copy(1000)
# SiStER_Input_File_delamination.m:174
    
    PARAMS.YNSurfaceProcesses = copy(0)
# SiStER_Input_File_delamination.m:175
    
    PARAMS.topo_kappa = copy(1e-09)
# SiStER_Input_File_delamination.m:176
    
    # Solver iterations
    PARAMS.Npicard_min = copy(3)
# SiStER_Input_File_delamination.m:181
    
    PARAMS.Npicard_max = copy(50)
# SiStER_Input_File_delamination.m:182
    
    PARAMS.conv_crit_ResL2 = copy(0.001)
# SiStER_Input_File_delamination.m:183
    PARAMS.pitswitch = copy(30)
# SiStER_Input_File_delamination.m:184
    
    # BOUNDARY CONDITIONS #####################################################
    
    # pressure
    PARAMS.p0cell = copy(0)
# SiStER_Input_File_delamination.m:191
    
    # flow
    
    # boundary conditions
# entries in BC correspond to
# 1/ rollers? (1=yes, 0=no)
# 2/ type of velocity normal to boundary (0=constant)
# 3/ value of normal velocity
    
    BC.top = copy(concat([1,0,0.0]))
# SiStER_Input_File_delamination.m:202
    BC.bot = copy(concat([1,0,0.0]))
# SiStER_Input_File_delamination.m:203
    BC.left = copy(concat([1,0,0.0]))
# SiStER_Input_File_delamination.m:204
    BC.right = copy(concat([1,0,0.0]))
# SiStER_Input_File_delamination.m:205
    PARAMS.BalanceStickyLayer = copy(0)
# SiStER_Input_File_delamination.m:206
    
    # / outflow BCs to balance the inflow / outflow of sticky layer material,
# and rock separately, based on the position of the sticky layer / air
# interface
    
    # thermal
    
    # entries in BCtherm correspond to
# 1/ type? (1=Dirichlet, 0=Neumann)
# 2/ value
    BCtherm.top = copy(concat([1,0]))
# SiStER_Input_File_delamination.m:217
    BCtherm.bot = copy(concat([1,1000]))
# SiStER_Input_File_delamination.m:218
    BCtherm.left = copy(concat([2,0]))
# SiStER_Input_File_delamination.m:219
    BCtherm.right = copy(concat([2,0]))
# SiStER_Input_File_delamination.m:220