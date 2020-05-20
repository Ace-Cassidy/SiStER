# Generated with SMOP  0.41
from libsmop import *
# SiStER_MAIN.m

    # SiStER_MAIN.m
    
    # Simple Stokes solver with Exotic Rheologies
    
    # Main routine doing initialization, time loop and outputs
    
    
    # J.-A. Olive, B.Z. Klein, E. Mittelstaedt, M. Behn, G. Ito, S. Howell
# jaolive <at> ldeo.columbia.edu
# March 2011 - April 2017
    
    close_('all')
    # INITIALIZATION
    
    # Input File: loads parameter values, model geometry, boundary conditions
    if exist('running_from_SiStER_RUN','var') == 0:
        clear
        InpFil=input_('Input file ? ','s')
# SiStER_MAIN.m:19
    
    run(InpFil)
    # construct grid and initialize marker / node arrays
    SiStER_Initialize
    # BEGIN TIME LOOP #########################################################
    time=0
# SiStER_MAIN.m:27
    for t in arange(1,Nt).reshape(-1):
        disp(concat(['STARTING ITERATION: ',num2str(t),' out of ',num2str(Nt)]))
        # update time
        time=time + dt_m
# SiStER_MAIN.m:34
        SiStER_material_props_on_nodes
        ### SOLVE STOKES WITH NON-LINEAR RHEOLOGY HERE
        SiStER_flow_solve
        # GET STRAIN RATE FROM CURRENT SOLUTION
        epsIIm=SiStER_interp_shear_nodes_to_markers(epsII_s,x,y,xm,ym,icn,jcn)
# SiStER_MAIN.m:43
        SiStER_update_marker_stresses
        if (PARAMS.YNPlas == 1):
            SiStER_update_ep
        # OUTPUT VARIABLES OF INTEREST (prior to rotation & advection)
        if (mod(t,dt_out) == 0 and dt_out > 0) or t == 1 or t == Nt:
            disp('SAVING SELECTED VARIABLES TO OUTPUT FILE')
            filename=num2str(t)
# SiStER_MAIN.m:56
            etam=SiStER_interp_shear_nodes_to_markers(etas,x,y,xm,ym,icn,jcn)
# SiStER_MAIN.m:57
            save(filename,'X','Y','vx','vy','p','time','xm','ym','etam','rhom','BC','etan','Tm','im','idm','epsIIm','sxxm','sxym','ep','epNH','icn','jcn','qd','topo_x','topo_y')
        # SET ADVECTION TIME STEP BASED ON CURRENT FLOW SOLUTION
        dt_m=SiStER_set_timestep(dx,dy,vx,vy,PARAMS)
# SiStER_MAIN.m:62
        if (PARAMS.YNElast == 1):
            SiStER_rotate_stresses
        # EVOLVE TEMPERATURE FIELD THROUGH DIFFUSION
        if PARAMS.Tsolve == 1:
            SiStER_thermal_update
        # MARKER ADVECTION, REMOVAL, AND ADDITION #############################
        SiStER_move_remove_and_reseed_markers
        # remove markers if necessary
    # add markers if necessary
        SiStER_update_topography_markers
        # here we do the same for the marker chain that keeps track of topography
    #######################################################################
        disp('---------------')
        disp(concat(['END OF ITERATION: ',num2str(t),' out of ',num2str(Nt),' - SIMULATION TIME: ',num2str(time / 365.25 / 24 / 3600 / 1000),' kyrs.']))
        disp('--------------------------------')
        disp('--------------------------------')
    
    disp('FIN')
    