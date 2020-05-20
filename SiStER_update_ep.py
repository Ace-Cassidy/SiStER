# Generated with SMOP  0.41
from libsmop import *
# SiStER_update_ep.m

    
    #=========================================================================
# PLASTIC (EXCLUDING ELASTIC) STRAIN ACCUMULATION
# Not sure whether to use the actual non-elastic strain (i.e., with
# current stresses) or the approximate, in which stress is assumed to equal
# yield stress
# G.Ito 8/16; JAO 9/15 for non-healed ep, fixed by JAO 4/2017
#=========================================================================
    
    dep_s=zeros(size(epsII_s))
# SiStER_update_ep.m:10
    dep_s[s_nodes_yield]=multiply(dt_m,max(epsII_s(s_nodes_yield) - (yield_s(s_nodes_yield) - sqrt(sxxOLD_s(s_nodes_yield) ** 2 + sxyOLD(s_nodes_yield) ** 2)) / (multiply(dot(2.0,Gs(s_nodes_yield)),dt_m)),dot(min(ravel(epsII_s)),1e-06)))
# SiStER_update_ep.m:11
    depm=SiStER_interp_shear_nodes_to_markers(reshape(dep_s,Ny,Nx),x,y,xm,ym,icn,jcn)
# SiStER_update_ep.m:14
    ep=(ep + depm) / (dt_m / PARAMS.tau_heal + 1)
# SiStER_update_ep.m:15
    epNH=epNH + depm
# SiStER_update_ep.m:16