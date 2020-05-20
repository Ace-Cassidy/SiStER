# Generated with SMOP  0.41
from libsmop import *
# SiStER_VEP_rheology.m

    #==========================================================================
# SiStER_UPDATE_RHEOLOGY
# calculates visco-elasto-plastic rheology terms on shear and normal nodes
# G.Ito 8/20
#==========================================================================
    
    #--------------------------------------------------------------------------
# plastic viscosity (Mohr-Coulomb)
#--------------------------------------------------------------------------
    if (PARAMS.YNPlas == 1):
        dp=p - pold
# SiStER_VEP_rheology.m:12
        ps=ps_old + SiStER_interp_normal_to_shear_nodes(dp,dx,dy)
# SiStER_VEP_rheology.m:13
        ps[ps < 0]=0
# SiStER_VEP_rheology.m:14
        pnn=copy(p)
# SiStER_VEP_rheology.m:15
        pnn[p < 0]=0
# SiStER_VEP_rheology.m:16
        yield_s=multiply((Cohes_s + multiply(Mu_s,ps)),cos(atan(Mu_s)))
# SiStER_VEP_rheology.m:17
        yield_n=multiply((Cohes_n + multiply(Mu_n,pnn)),cos(atan(Mu_n)))
# SiStER_VEP_rheology.m:18
        if (PARAMS.YNElast == 1):
            eta_plas_s=multiply(0.5,yield_s) / max(epsII_s - (yield_s - sqrt(sxxOLD_s ** 2 + sxyOLD ** 2)) / (multiply(dot(2.0,Gs),dt_m)),dot(min(ravel(epsII_s)),1e-06))
# SiStER_VEP_rheology.m:20
            eta_plas_n=multiply(0.5,yield_n) / max(epsII_n - (yield_n - sqrt(sxxOLD ** 2 + sxyOLD_n ** 2)) / (multiply(dot(2.0,Gn),dt_m)),dot(min(ravel(epsII_n)),1e-06))
# SiStER_VEP_rheology.m:21
        else:
            eta_plas_s=multiply(0.5,yield_s) / max(epsII_s,dot(min(ravel(epsII_s)),1e-06))
# SiStER_VEP_rheology.m:23
            eta_plas_n=multiply(0.5,yield_n) / max(epsII_n,dot(min(ravel(epsII_n)),1e-06))
# SiStER_VEP_rheology.m:24
    
    #-------------------------------------------------------------------------
# Ductile viscosity
#-------------------------------------------------------------------------
    
    # previous approach: based on strain rate 
# problem = it should be only the viscous part of strain rate
# Gerya [2010] p. 189 - best to base viscosity on stress
#[etas_new]=SiStER_get_ductile_rheology(MAT,PARAMS,Ts,epsII_s,phase_s);
#[etan_new(2:end,2:end)]=SiStER_get_ductile_rheology(MAT,PARAMS,Tn(2:end,2:end),epsII_n(2:end,2:end),phase_n(2:end,2:end));
    
    # VISCOSITY INDEXED ON STRESS
    
    if PARAMS.YNElast == 1:
        if t == 1 and pit == 1:
            # at this stage we don't have any viscosity
        # but stresses are zero anyway
            sII_n=zeros(size(X))
# SiStER_VEP_rheology.m:47
            sII_s=zeros(size(X))
# SiStER_VEP_rheology.m:48
        else:
            # need sIIOLD_s to initialize bisection (done on shear nodes)
            sIIOLD_s=sqrt(sxxOLD_s ** 2 + sxyOLD ** 2)
# SiStER_VEP_rheology.m:51
            SiStER_viscosity_stress_bisection
            sII_s=copy(sII)
# SiStER_VEP_rheology.m:53
            sII_n=SiStER_interp_shear_to_normal_nodes(sII_s)
# SiStER_VEP_rheology.m:54
        # and use the stresses to re-update viscosity
        etas_new=SiStER_get_ductile_rheology_on_nodes_from_stresses(MAT,PARAMS,Ts,sII_s,phase_s)
# SiStER_VEP_rheology.m:58
        etan_new(arange(2,end()),arange(2,end()))=SiStER_get_ductile_rheology_on_nodes_from_stresses(MAT,PARAMS,Tn(arange(2,end()),arange(2,end())),sII_n(arange(2,end()),arange(2,end())),phase_n(arange(2,end()),arange(2,end()),arange()))
# SiStER_VEP_rheology.m:59
    else:
        # this seems to yield an easier convergence than the bisection
    # algorithm in this case
        etas_new=SiStER_get_ductile_rheology_on_nodes_from_strain_rate(MAT,PARAMS,Ts,epsII_s,phase_s)
# SiStER_VEP_rheology.m:64
        etan_new(arange(2,end()),arange(2,end()))=SiStER_get_ductile_rheology_on_nodes_from_strain_rate(MAT,PARAMS,Tn(arange(2,end()),arange(2,end())),epsII_n(arange(2,end()),arange(2,end())),phase_n(arange(2,end()),arange(2,end()),arange()))
# SiStER_VEP_rheology.m:65
    
    ##
    
    if PARAMS.YNPlas == 1:
        # identify yielding nodes to update ep
        s_nodes_yield=find(etas_new > eta_plas_s)
# SiStER_VEP_rheology.m:76
        n_nodes_yield=find(etan_new > eta_plas_n)
# SiStER_VEP_rheology.m:77
        etan_new[arange(2,end()),arange(2,end())]=(1.0 / eta_plas_n(arange(2,end()),arange(2,end())) + 1.0 / etan_new(arange(2,end()),arange(2,end())) + 1.0 / PARAMS.etamax) ** - 1
# SiStER_VEP_rheology.m:79
        etas_new=(1.0 / eta_plas_s + 1.0 / etas_new + 1.0 / PARAMS.etamax) ** - 1
# SiStER_VEP_rheology.m:80
        # etan_new(n_nodes_yield)=eta_plas_n(n_nodes_yield);
    # etas_new(s_nodes_yield)=eta_plas_s(s_nodes_yield);
    else:
        etan_new[arange(2,end()),arange(2,end())]=(1.0 / etan_new(arange(2,end()),arange(2,end())) + 1.0 / PARAMS.etamax) ** - 1
# SiStER_VEP_rheology.m:88
        etas_new=(1.0 / etas_new + 1.0 / PARAMS.etamax) ** - 1
# SiStER_VEP_rheology.m:89
    
    etan=copy(etan_new)
# SiStER_VEP_rheology.m:94
    etas=copy(etas_new)
# SiStER_VEP_rheology.m:95
    etan[etan < PARAMS.etamin]=PARAMS.etamin
# SiStER_VEP_rheology.m:96
    etas[etas < PARAMS.etamin]=PARAMS.etamin
# SiStER_VEP_rheology.m:97
    #-------------------------------------------------------------------------
# ELASTICITY TERMS (BASED ON LATEST VISCOSITY)
#-------------------------------------------------------------------------
    if PARAMS.YNElast == 0:
        Zs=ones(size(etas))
# SiStER_VEP_rheology.m:104
        Zn=ones(size(etan))
# SiStER_VEP_rheology.m:105
    else:
        Zs=dot(Gs,dt_m) / (dot(Gs,dt_m) + etas)
# SiStER_VEP_rheology.m:107
        Zn=dot(Gn,dt_m) / (dot(Gn,dt_m) + etan)
# SiStER_VEP_rheology.m:108
    
    # right-hand side (1-Z)*sigmaOLD_ij
    srhs_xx=multiply((1 - Zn),sxxOLD)
# SiStER_VEP_rheology.m:111
    srhs_xy=multiply((1 - Zs),sxyOLD)
# SiStER_VEP_rheology.m:112