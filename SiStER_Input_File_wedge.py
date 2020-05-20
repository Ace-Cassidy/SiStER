# Generated with SMOP  0.41
from libsmop import *
# SiStER_Input_File_wedge.m

    # SiStER_Input_File
    
    # DURATION OF SIMULATION AND FREQUENCY OF OUTPUT ##########################
    Nt=100
# SiStER_Input_File_wedge.m:5
    
    dt_out=10
# SiStER_Input_File_wedge.m:6
    
    # DOMAIN SIZE AND GRIDDING ################################################
    xsize=120000.0
# SiStER_Input_File_wedge.m:10
    ysize=20000.0
# SiStER_Input_File_wedge.m:11
    # gridding- from 0 to GRID.x(1), grid size is GRID.dx(1)
# from GRID.x(1) to GRID.x(2), grid size is GRID.dx(1) etc...
# same for y
    GRID.dx[1]=1000 / 2
# SiStER_Input_File_wedge.m:15
    GRID.x[1]=120000.0
# SiStER_Input_File_wedge.m:16
    GRID.dy[1]=1000 / 2
# SiStER_Input_File_wedge.m:17
    GRID.y[1]=20000.0
# SiStER_Input_File_wedge.m:18
    # LAGRANGIAN MARKERS ######################################################
    Mquad=6
# SiStER_Input_File_wedge.m:23
    
    Mquad_crit=3
# SiStER_Input_File_wedge.m:24
    
    # GEOMETRY ################################################################
    
    Nphase=4
# SiStER_Input_File_wedge.m:28
    
    # phase 1
    GEOM(1).type = copy(1)
# SiStER_Input_File_wedge.m:31
    
    GEOM(1).top = copy(0)
# SiStER_Input_File_wedge.m:32
    GEOM(1).bot = copy(7000.0)
# SiStER_Input_File_wedge.m:33
    # phase 2
    GEOM(2).type = copy(1)
# SiStER_Input_File_wedge.m:36
    
    GEOM(2).top = copy(7000.0)
# SiStER_Input_File_wedge.m:37
    GEOM(2).bot = copy(18000.0)
# SiStER_Input_File_wedge.m:38
    # phase 3
    GEOM(3).type = copy(1)
# SiStER_Input_File_wedge.m:41
    
    GEOM(3).top = copy(18000.0)
# SiStER_Input_File_wedge.m:42
    GEOM(3).bot = copy(20000.0)
# SiStER_Input_File_wedge.m:43
    # phase 4
    GEOM(4).type = copy(2)
# SiStER_Input_File_wedge.m:46
    
    GEOM(4).x0 = copy(xsize / 9)
# SiStER_Input_File_wedge.m:47
    GEOM(4).y0 = copy(17000.0)
# SiStER_Input_File_wedge.m:48
    GEOM(4).rad = copy(1000.0)
# SiStER_Input_File_wedge.m:49
    # MATERIAL PROPERTIES #####################################################
    
    # creep laws of the form: pre^(-1/n)*epsII^((1-n)/n)*exp(E/(nRT))
# harmonically averaging diffusion creep, dislocation creep 
# (and plastic creep to simulate brittle failure)
    
    # phase 1
    MAT(1).phase = copy(1)
# SiStER_Input_File_wedge.m:59
    # density parameters
    MAT(1).rho0 = copy(0.01)
# SiStER_Input_File_wedge.m:61
    MAT(1).alpha = copy(0)
# SiStER_Input_File_wedge.m:62
    # elasticity
    MAT(1).G = copy(1e+18)
# SiStER_Input_File_wedge.m:64
    # diffusion creep parameters
    MAT(1).pre_diff = copy(0.5 / 1e+18)
# SiStER_Input_File_wedge.m:66
    MAT(1).Ediff = copy(0)
# SiStER_Input_File_wedge.m:67
    MAT(1).ndiff = copy(1)
# SiStER_Input_File_wedge.m:68
    # dislocation creep parameters
    MAT(1).pre_disc = copy(0.5 / 1e+18)
# SiStER_Input_File_wedge.m:70
    MAT(1).Edisc = copy(0)
# SiStER_Input_File_wedge.m:71
    MAT(1).ndisc = copy(1)
# SiStER_Input_File_wedge.m:72
    # plasticity
    MAT(1).mu = copy(0.6)
# SiStER_Input_File_wedge.m:74
    MAT(1).Cmax = copy(40000000.0)
# SiStER_Input_File_wedge.m:75
    MAT(1).Cmin = copy(10000.0)
# SiStER_Input_File_wedge.m:76
    MAT(1).ecrit = copy(0.1)
# SiStER_Input_File_wedge.m:77
    # phase 2
    MAT(2).phase = copy(2)
# SiStER_Input_File_wedge.m:81
    # density parameters
    MAT(2).rho0 = copy(2700)
# SiStER_Input_File_wedge.m:83
    MAT(2).alpha = copy(0)
# SiStER_Input_File_wedge.m:84
    # elasticity
    MAT(2).G = copy(30000000000.0)
# SiStER_Input_File_wedge.m:86
    # diffusion creep parameters
    MAT(2).pre_diff = copy(0.5 / 1e+40)
# SiStER_Input_File_wedge.m:88
    MAT(2).Ediff = copy(0)
# SiStER_Input_File_wedge.m:89
    MAT(2).ndiff = copy(1)
# SiStER_Input_File_wedge.m:90
    # dislocation creep parameters
    MAT(2).pre_disc = copy(0.001)
# SiStER_Input_File_wedge.m:92
    MAT(2).Edisc = copy(dot(167000,2.25))
# SiStER_Input_File_wedge.m:93
    MAT(2).ndisc = copy(2)
# SiStER_Input_File_wedge.m:94
    # plasticity
    MAT(2).mu = copy(0.6)
# SiStER_Input_File_wedge.m:96
    MAT(2).Cmax = copy(40000000.0)
# SiStER_Input_File_wedge.m:97
    MAT(2).Cmin = copy(10000.0)
# SiStER_Input_File_wedge.m:98
    MAT(2).ecrit = copy(0.1)
# SiStER_Input_File_wedge.m:99
    # phase 3
    MAT(3).phase = copy(3)
# SiStER_Input_File_wedge.m:102
    # density parameters
    MAT(3).rho0 = copy(2700)
# SiStER_Input_File_wedge.m:104
    MAT(3).alpha = copy(0)
# SiStER_Input_File_wedge.m:105
    # elasticity
    MAT(3).G = copy(1e+18)
# SiStER_Input_File_wedge.m:107
    # diffusion creep parameters
    MAT(3).pre_diff = copy(0.5 / 1e+18)
# SiStER_Input_File_wedge.m:109
    MAT(3).Ediff = copy(0)
# SiStER_Input_File_wedge.m:110
    MAT(3).ndiff = copy(1)
# SiStER_Input_File_wedge.m:111
    # dislocation creep parameters
    MAT(3).pre_disc = copy(0.5 / 1e+18)
# SiStER_Input_File_wedge.m:113
    MAT(3).Edisc = copy(0)
# SiStER_Input_File_wedge.m:114
    MAT(3).ndisc = copy(1)
# SiStER_Input_File_wedge.m:115
    # plasticity
    MAT(3).mu = copy(0.6)
# SiStER_Input_File_wedge.m:117
    MAT(3).Cmax = copy(40000000.0)
# SiStER_Input_File_wedge.m:118
    MAT(3).Cmin = copy(10000.0)
# SiStER_Input_File_wedge.m:119
    MAT(3).ecrit = copy(0.1)
# SiStER_Input_File_wedge.m:120
    # phase 4
    MAT(4).phase = copy(4)
# SiStER_Input_File_wedge.m:123
    # density parameters
    MAT(4).rho0 = copy(2700)
# SiStER_Input_File_wedge.m:125
    MAT(4).alpha = copy(0)
# SiStER_Input_File_wedge.m:126
    # elasticity
    MAT(4).G = copy(30000000000.0)
# SiStER_Input_File_wedge.m:128
    # diffusion creep parameters
    MAT(4).pre_diff = copy(0.5 / 1e+40)
# SiStER_Input_File_wedge.m:130
    MAT(4).Ediff = copy(0)
# SiStER_Input_File_wedge.m:131
    MAT(4).ndiff = copy(1)
# SiStER_Input_File_wedge.m:132
    # dislocation creep parameters
    MAT(4).pre_disc = copy(0.001)
# SiStER_Input_File_wedge.m:134
    MAT(4).Edisc = copy(dot(167000,2.25))
# SiStER_Input_File_wedge.m:135
    MAT(4).ndisc = copy(2)
# SiStER_Input_File_wedge.m:136
    # plasticity
    MAT(4).mu = copy(0.6)
# SiStER_Input_File_wedge.m:138
    MAT(4).Cmax = copy(10000.0)
# SiStER_Input_File_wedge.m:139
    MAT(4).Cmin = copy(10000.0)
# SiStER_Input_File_wedge.m:140
    MAT(4).ecrit = copy(0.1)
# SiStER_Input_File_wedge.m:141
    # ADDITIONAL PARAMETERS ###################################################
    PARAMS.YNElast = copy(1)
# SiStER_Input_File_wedge.m:146
    
    PARAMS.YNPlas = copy(1)
# SiStER_Input_File_wedge.m:147
    
    PARAMS.tau_heal = copy(1e+11)
# SiStER_Input_File_wedge.m:148
    
    PARAMS.gx = copy(0)
# SiStER_Input_File_wedge.m:149
    
    PARAMS.gy = copy(9.8)
# SiStER_Input_File_wedge.m:150
    
    PARAMS.fracCFL = copy(0.5)
# SiStER_Input_File_wedge.m:151
    
    PARAMS.R = copy(8.314)
# SiStER_Input_File_wedge.m:152
    
    PARAMS.etamax = copy(1e+25)
# SiStER_Input_File_wedge.m:153
    
    PARAMS.etamin = copy(1e+18)
# SiStER_Input_File_wedge.m:154
    
    PARAMS.Tsolve = copy(1)
# SiStER_Input_File_wedge.m:155
    
    # initial temperature profile, polynomial with depth 
# T = a0 + a1*y+a2*y^2+a3*y^3+amp*sin(2*pi*X/lam)
# (make sure it matches the BCs)
    PARAMS.a0 = copy(0)
# SiStER_Input_File_wedge.m:159
    PARAMS.a1 = copy(0)
# SiStER_Input_File_wedge.m:160
    PARAMS.a2 = copy(0)
# SiStER_Input_File_wedge.m:161
    PARAMS.a3 = copy(1000 / (30000.0) ** 3)
# SiStER_Input_File_wedge.m:162
    PARAMS.amp = copy(0)
# SiStER_Input_File_wedge.m:163
    
    PARAMS.lam = copy(1)
# SiStER_Input_File_wedge.m:164
    
    PARAMS.ynTreset = copy(1)
# SiStER_Input_File_wedge.m:165
    
    PARAMS.T0 = copy(0)
# SiStER_Input_File_wedge.m:166
    # reference values for the constant diffusivity thermal solver
# (kappa = kref / (rhoref*cpref))
    PARAMS.rhoref = copy(MAT(2).rho0)
# SiStER_Input_File_wedge.m:169
    PARAMS.kref = copy(3)
# SiStER_Input_File_wedge.m:170
    PARAMS.cpref = copy(1000)
# SiStER_Input_File_wedge.m:171
    # TOPOGRAPHY EVOLUTION (interface between rock and sticky air/water layer)
    PARAMS.Ntopo_markers = copy(1000)
# SiStER_Input_File_wedge.m:174
    
    PARAMS.YNSurfaceProcesses = copy(1)
# SiStER_Input_File_wedge.m:175
    
    PARAMS.topo_kappa = copy(1e-08)
# SiStER_Input_File_wedge.m:176
    
    # Picard iterations
    PARAMS.Npicard_min = copy(10)
# SiStER_Input_File_wedge.m:179
    
    PARAMS.Npicard_max = copy(100)
# SiStER_Input_File_wedge.m:180
    
    PARAMS.conv_crit_ResL2 = copy(1e-09)
# SiStER_Input_File_wedge.m:181
    PARAMS.pitswitch = copy(0)
# SiStER_Input_File_wedge.m:182
    
    # BOUNDARY CONDITIONS #####################################################
    
    # pressure
    PARAMS.p0cell = copy(0)
# SiStER_Input_File_wedge.m:188
    
    # flow
    
    # boundary conditions
# entries in BC correspond to
# 1/ rollers? (1=yes, 0=no)
# 2/ type of velocity normal to boundary (0=constant)
# 3/ value of normal velocity
    
    BC.top = copy(concat([1,3,0]))
# SiStER_Input_File_wedge.m:199
    BC.bot = copy(concat([0,0,0,- 0.01 / 365.25 / 24 / 3600]))
# SiStER_Input_File_wedge.m:200
    BC.left = copy(concat([1,0,0]))
# SiStER_Input_File_wedge.m:201
    BC.right = copy(concat([1,0,- 0.01 / 365.25 / 24 / 3600]))
# SiStER_Input_File_wedge.m:202
    BC.bot_profile = copy(multiply(dot(- (0.01 / 365.25 / 24 / 3600),ones(1,481)),(1 - exp(- (concat([arange(1,481)]) - 1) / 10))))
# SiStER_Input_File_wedge.m:203
    PARAMS.BalanceStickyLayer = copy(0)
# SiStER_Input_File_wedge.m:204
    
    # / outflow BCs to balance the inflow / outflow of sticky layer material,
# and rock separately, based on the position of the sticky layer / air
# interface
    
    # thermal
    
    # entries in BCtherm correspond to
# 1/ type? (1=Dirichlet, 2=Neumann)
# 2/ value
    BCtherm.top = copy(concat([1,0]))
# SiStER_Input_File_wedge.m:215
    BCtherm.bot = copy(concat([1,400]))
# SiStER_Input_File_wedge.m:216
    BCtherm.left = copy(concat([2,0]))
# SiStER_Input_File_wedge.m:217
    BCtherm.right = copy(concat([2,0]))
# SiStER_Input_File_wedge.m:218