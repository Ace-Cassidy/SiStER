# Generated with SMOP  0.41
from libsmop import *
# SiStER_Input_File_run_check.m

    # SiStER_Input_File
    
    # DURATION OF SIMULATION AND FREQUENCY OF OUTPUT ##########################
    Nt=5
# SiStER_Input_File_run_check.m:5
    
    dt_out=5
# SiStER_Input_File_run_check.m:6
    
    # DOMAIN SIZE AND GRIDDING ################################################
    xsize=100000.0
# SiStER_Input_File_run_check.m:10
    ysize=100000.0
# SiStER_Input_File_run_check.m:11
    # gridding- from 0 to GRID.x(1), grid size is GRID.dx(1)
# from GRID.x(1) to GRID.x(2), grid size is GRID.dx(1) etc...
# same for y
    GRID.dx[1]=5000.0
# SiStER_Input_File_run_check.m:15
    GRID.x[1]=100000.0
# SiStER_Input_File_run_check.m:16
    GRID.dy[1]=5000.0
# SiStER_Input_File_run_check.m:17
    GRID.y[1]=100000.0
# SiStER_Input_File_run_check.m:18
    # LAGRANGIAN MARKERS ######################################################
    Mquad=6
# SiStER_Input_File_run_check.m:22
    
    Mquad_crit=3
# SiStER_Input_File_run_check.m:23
    
    # GEOMETRY ################################################################
    
    Nphase=2
# SiStER_Input_File_run_check.m:27
    
    # phase 1
    GEOM(1).type = copy(1)
# SiStER_Input_File_run_check.m:30
    
    GEOM(1).top = copy(0)
# SiStER_Input_File_run_check.m:31
    GEOM(1).bot = copy(100000.0)
# SiStER_Input_File_run_check.m:32
    # phase 2
    GEOM(2).type = copy(2)
# SiStER_Input_File_run_check.m:36
    
    GEOM(2).x0 = copy(xsize / 2)
# SiStER_Input_File_run_check.m:37
    GEOM(2).y0 = copy(ysize / 2)
# SiStER_Input_File_run_check.m:38
    GEOM(2).rad = copy(10000.0)
# SiStER_Input_File_run_check.m:39
    # MATERIAL PROPERTIES #####################################################
    
    # creep laws of the form: pre^(-1/n)*epsII^((1-n)/n)*exp(E/(nRT))
# harmonically averaging diffusion creep, dislocation creep 
# (and plastic creep to simulate brittle failure)
    
    # phase 1
    MAT(1).phase = copy(1)
# SiStER_Input_File_run_check.m:49
    # density parameters
    MAT(1).rho0 = copy(3000)
# SiStER_Input_File_run_check.m:51
    MAT(1).alpha = copy(0)
# SiStER_Input_File_run_check.m:52
    # elasticity
    MAT(1).G = copy(1e+18)
# SiStER_Input_File_run_check.m:54
    # diffusion creep parameters
    MAT(1).pre_diff = copy(0.5 / 1e+20)
# SiStER_Input_File_run_check.m:56
    MAT(1).Ediff = copy(0)
# SiStER_Input_File_run_check.m:57
    MAT(1).ndiff = copy(1)
# SiStER_Input_File_run_check.m:58
    # dislocation creep parameters
    MAT(1).pre_disc = copy(0.5 / 1e+20)
# SiStER_Input_File_run_check.m:60
    MAT(1).Edisc = copy(0)
# SiStER_Input_File_run_check.m:61
    MAT(1).ndisc = copy(1)
# SiStER_Input_File_run_check.m:62
    # plasticity
    MAT(1).mu = copy(0.6)
# SiStER_Input_File_run_check.m:64
    MAT(1).Cmax = copy(10000000000.0)
# SiStER_Input_File_run_check.m:65
    MAT(1).Cmin = copy(10000000000.0)
# SiStER_Input_File_run_check.m:66
    MAT(1).ecrit = copy(0.1)
# SiStER_Input_File_run_check.m:67
    # phase 2
    MAT(2).phase = copy(2)
# SiStER_Input_File_run_check.m:71
    # density parameters
    MAT(2).rho0 = copy(2700)
# SiStER_Input_File_run_check.m:73
    MAT(2).alpha = copy(0)
# SiStER_Input_File_run_check.m:74
    # elasticity
    MAT(2).G = copy(1e+18)
# SiStER_Input_File_run_check.m:76
    # diffusion creep parameters
    MAT(2).pre_diff = copy(0.5 / 1e+18)
# SiStER_Input_File_run_check.m:78
    MAT(2).Ediff = copy(0)
# SiStER_Input_File_run_check.m:79
    MAT(2).ndiff = copy(1)
# SiStER_Input_File_run_check.m:80
    # dislocation creep parameters
    MAT(2).pre_disc = copy(0.5 / 1e+18)
# SiStER_Input_File_run_check.m:82
    MAT(2).Edisc = copy(0)
# SiStER_Input_File_run_check.m:83
    MAT(2).ndisc = copy(1)
# SiStER_Input_File_run_check.m:84
    # plasticity
    MAT(2).mu = copy(0.6)
# SiStER_Input_File_run_check.m:86
    MAT(2).Cmax = copy(10000000000.0)
# SiStER_Input_File_run_check.m:87
    MAT(2).Cmin = copy(10000000000.0)
# SiStER_Input_File_run_check.m:88
    MAT(2).ecrit = copy(0.1)
# SiStER_Input_File_run_check.m:89
    # ADDITIONAL PARAMETERS ###################################################
    PARAMS.YNElast = copy(0)
# SiStER_Input_File_run_check.m:93
    
    PARAMS.YNPlas = copy(0)
# SiStER_Input_File_run_check.m:94
    
    PARAMS.epsII_from_stress = copy(1)
# SiStER_Input_File_run_check.m:95
    
    PARAMS.tau_heal = copy(1e+12)
# SiStER_Input_File_run_check.m:96
    
    PARAMS.gx = copy(0)
# SiStER_Input_File_run_check.m:97
    
    PARAMS.gy = copy(9.8)
# SiStER_Input_File_run_check.m:98
    
    PARAMS.fracCFL = copy(0.5)
# SiStER_Input_File_run_check.m:99
    
    PARAMS.R = copy(8.314)
# SiStER_Input_File_run_check.m:100
    
    PARAMS.etamax = copy(1e+25)
# SiStER_Input_File_run_check.m:101
    
    PARAMS.etamin = copy(1e+18)
# SiStER_Input_File_run_check.m:102
    
    PARAMS.Tsolve = copy(0)
# SiStER_Input_File_run_check.m:103
    
    # initial temperature profile, polynomial with depth 
# T = a0 + a1*y+a2*y^2+a3*y^3+amp*sin(2*pi*X/lam)
# (make sure it matches the BCs)
    PARAMS.a0 = copy(0)
# SiStER_Input_File_run_check.m:107
    PARAMS.a1 = copy(0)
# SiStER_Input_File_run_check.m:108
    PARAMS.a2 = copy(0)
# SiStER_Input_File_run_check.m:109
    PARAMS.a3 = copy(1000 / (30000.0) ** 3)
# SiStER_Input_File_run_check.m:110
    PARAMS.amp = copy(0)
# SiStER_Input_File_run_check.m:111
    
    PARAMS.lam = copy(1)
# SiStER_Input_File_run_check.m:112
    
    PARAMS.ynTreset = copy(1)
# SiStER_Input_File_run_check.m:113
    
    PARAMS.T0 = copy(0)
# SiStER_Input_File_run_check.m:114
    # reference values for the constant diffusivity thermal solver
# (kappa = kref / (rhoref*cpref))
    PARAMS.rhoref = copy(MAT(2).rho0)
# SiStER_Input_File_run_check.m:117
    PARAMS.kref = copy(3)
# SiStER_Input_File_run_check.m:118
    PARAMS.cpref = copy(1000)
# SiStER_Input_File_run_check.m:119
    # TOPOGRAPHY EVOLUTION (interface between rock and sticky air/water layer)
    PARAMS.Ntopo_markers = copy(1000)
# SiStER_Input_File_run_check.m:122
    
    PARAMS.YNSurfaceProcesses = copy(0)
# SiStER_Input_File_run_check.m:123
    
    PARAMS.topo_kappa = copy(1e-09)
# SiStER_Input_File_run_check.m:124
    
    # Solver iterations
    PARAMS.Npicard_min = copy(3)
# SiStER_Input_File_run_check.m:129
    
    PARAMS.Npicard_max = copy(50)
# SiStER_Input_File_run_check.m:130
    
    PARAMS.conv_crit_ResL2 = copy(0.001)
# SiStER_Input_File_run_check.m:131
    PARAMS.pitswitch = copy(30)
# SiStER_Input_File_run_check.m:132
    
    # BOUNDARY CONDITIONS #####################################################
    
    # pressure
    PARAMS.p0cell = copy(0)
# SiStER_Input_File_run_check.m:139
    
    # flow
    
    # boundary conditions
# entries in BC correspond to
# 1/ rollers? (1=yes, 0=no)
# 2/ type of velocity normal to boundary (0=constant)
# 3/ value of normal velocity
    
    BC.top = copy(concat([1,0,0.0]))
# SiStER_Input_File_run_check.m:150
    BC.bot = copy(concat([1,0,0.0]))
# SiStER_Input_File_run_check.m:151
    BC.left = copy(concat([1,0,0.0]))
# SiStER_Input_File_run_check.m:152
    BC.right = copy(concat([1,0,0.0]))
# SiStER_Input_File_run_check.m:153
    PARAMS.BalanceStickyLayer = copy(0)
# SiStER_Input_File_run_check.m:154
    
    # / outflow BCs to balance the inflow / outflow of sticky layer material,
# and rock separately, based on the position of the sticky layer / air
# interface
    
    # thermal
    
    # entries in BCtherm correspond to
# 1/ type? (1=Dirichlet, 0=Neumann)
# 2/ value
    BCtherm.top = copy(concat([1,0]))
# SiStER_Input_File_run_check.m:165
    BCtherm.bot = copy(concat([1,1000]))
# SiStER_Input_File_run_check.m:166
    BCtherm.left = copy(concat([2,0]))
# SiStER_Input_File_run_check.m:167
    BCtherm.right = copy(concat([2,0]))
# SiStER_Input_File_run_check.m:168