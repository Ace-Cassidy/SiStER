# Generated with SMOP  0.41
from libsmop import *
# SiStER_flow_solve.m

    #==========================================================================
# SiStER_flow_solve
# Performs inner solve of linear LS=R system as well as outer, iterative
# solution for non-linear dependence of L (viscosity) on S (vx,vy,P)
# Used to be named "run_Picard_iterations" but name changed by G.Ito 6/21/16
#==========================================================================
    
    if PARAMS.BalanceStickyLayer == 1:
        # BALANCE FLUXES ### JAO July 16, 2015
# RE-ADJUST BCs SO FLUX OF ROCK AND STICKY AIR MATERIAL ARE CONSERVED
# locate height of sticky layer - rock contact on the sides
        bL=interp1(topo_x,topo_y,0)
# SiStER_flow_solve.m:13
        bR=interp1(topo_x,topo_y,xsize)
# SiStER_flow_solve.m:14
        utop=dot(BC.right(3),(bL + bR)) / xsize
# SiStER_flow_solve.m:15
        ubot=dot(BC.right(3),(dot(2,ysize) - bL - bR)) / xsize
# SiStER_flow_solve.m:16
        BC.top[3]=utop
# SiStER_flow_solve.m:17
        BC.bot[3]=- ubot
# SiStER_flow_solve.m:18
    
    ResL2=1
# SiStER_flow_solve.m:22
    for pit in arange(1,PARAMS.Npicard_max).reshape(-1):
        if pit == 1:
            ResL2init=copy(ResL2)
# SiStER_flow_solve.m:28
        ## ---------------------------------------------------------------------------------
    # Compute visco-elasto-plastic viscosities
    #---------------------------------------------------------------------------------
        SiStER_VEP_rheology
        #---------------------------------------------------------------------------------
    # Assemble L and R matrices
    #---------------------------------------------------------------------------------
        L,R,Kc,Kb=SiStER_assemble_L_R(dx,dy,multiply(Zs,etas),multiply(Zn,etan),rho,BC,PARAMS,srhs_xx,srhs_xy,nargout=4)
# SiStER_flow_solve.m:39
        #---------------------------------------------------------------------------------
    # Residual:  L and R are from current solution S
    #---------------------------------------------------------------------------------
        if (exist('S','var')):
            Res=dot(L,S) - R
# SiStER_flow_solve.m:45
            ResL2=norm(Res,2) / norm(R,2)
# SiStER_flow_solve.m:46
        else:
            S=numpy.linalg.solve(L,R)
# SiStER_flow_solve.m:50
            disp('First solve is linearized')
            Res=dot(L,S) - R
# SiStER_flow_solve.m:51
            ResL2=norm(Res,2) / norm(R,2)
# SiStER_flow_solve.m:52
        #---------------------------------------------------------------------------------
    # Solve for new solution S using Picard or approximate Newton or a
    # combination of the two 
    #---------------------------------------------------------------------------------
        if (pit >= PARAMS.pitswitch):
            if pit == PARAMS.pitswitch:
                disp('switching from Picard to approx. Newton')
            beta=1
# SiStER_flow_solve.m:63
            S=S - multiply(beta,(numpy.linalg.solve(L,Res)))
# SiStER_flow_solve.m:64
            it_type='Newton: '
# SiStER_flow_solve.m:65
        else:
            S=numpy.linalg.solve(L,R)
# SiStER_flow_solve.m:67
            it_type='Picard: '
# SiStER_flow_solve.m:68
        p,vx,vy=SiStER_reshape_solver_output(S,Kc,Nx,Ny,nargout=3)
# SiStER_flow_solve.m:71
        if (ResL2 < PARAMS.conv_crit_ResL2 and pit >= PARAMS.Npicard_min):
            disp(concat(['Final residual = ',num2str(ResL2)]))
            disp(concat([num2str(pit),' iterations converged: L2 norm of residual dropped below ',num2str(PARAMS.conv_crit_ResL2)]))
            break
        else:
            if (pit == PARAMS.Npicard_max):
                disp(concat(['Final residual = ',num2str(ResL2)]))
                disp(concat(['WARNING! ',num2str(pit),' Picard / approx. Newton iterations failed to converge within tolerance of ',num2str(PARAMS.conv_crit_ResL2)]))
    
    
    ## get strain rate on nodes current solution
    EXX,EXY=SiStER_get_strain_rate(vx,vy,dx,dy,BC,nargout=2)
# SiStER_flow_solve.m:86
    EXY_n=SiStER_interp_shear_to_normal_nodes(EXY)
# SiStER_flow_solve.m:88
    EXX_s=SiStER_interp_normal_to_shear_nodes(EXX,dx,dy)
# SiStER_flow_solve.m:89
    epsII_n=sqrt(EXX ** 2 + EXY_n ** 2)
# SiStER_flow_solve.m:90
    epsII_s=sqrt(EXX_s ** 2 + EXY ** 2)
# SiStER_flow_solve.m:91
    # helpful to visualize convergence
# figure(1)
# pcolor(X,Y,log10(etas))
# set(gca,'ydir','reverse')
# axis equal
# caxis([18 25])
# colorbar
# title(num2str(pit))
# pause(.001)
    
    # RESIDUAL FOR INDIVIDUAL VARIABLES
# [pres, vxres, vyres]=SiStER_reshape_solver_output(Res,Kc,Nx,Ny);
# figure(1)
# pcolor(X,Y,vxres)
# set(gca,'ydir','reverse')
# axis equal
# colorbar
# title(num2str(pit))
# pause(.001)
    
    #end
    
    