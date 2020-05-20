# Generated with SMOP  0.41
from libsmop import *
# SiStER_update_marker_stresses.m

    #=============================================================================
# Updates stresses on markers for CURRENT solution.  Stress rotation
# occurs after solutions are output
# G.Ito 8/16
#==============================================================================
    
    # Compute STRESS Changes on nodes, interpolate to markers, and apply to marker stresses
    dsxx=multiply((multiply(dot(2,etan),EXX) - sxxOLD),Zn)
# SiStER_update_marker_stresses.m:8
    dsxy=multiply((multiply(dot(2,etas),EXY) - sxyOLD),Zs)
# SiStER_update_marker_stresses.m:9
    dsxxm=SiStER_interp_normal_nodes_to_markers(dsxx,xc,yc,xm,ym,icn,jcn)
# SiStER_update_marker_stresses.m:11
    dsxym=SiStER_interp_shear_nodes_to_markers(dsxy,x,y,xm,ym,icn,jcn)
# SiStER_update_marker_stresses.m:12
    sxxm=sxxm + dsxxm
# SiStER_update_marker_stresses.m:13
    sxym=sxym + dsxym
# SiStER_update_marker_stresses.m:14