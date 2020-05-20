# Generated with SMOP  0.41
from libsmop import *
# SiStER_viscosity_stress_bisection.m

    # BISECTION ALGORITHM FOR LOCAL ITERATIONS
# calculates a deviatoric stress sII that can be fed to the creep laws
# and is consistent with the current viscosity
# this appears to be a necessary step to use a stress-based creep law
# when elasticity is on (i.e., the strain rate is not entirely viscous)
    
    # STARTING VISCOSITY (TO BE ADJUSTED)
    visco=copy(etas_new)
# SiStER_viscosity_stress_bisection.m:8
    # INITIALIZE
    sIILOW=copy(sIIOLD_s)
# SiStER_viscosity_stress_bisection.m:11
    sIIHIGH=copy(sIIOLD_s)
# SiStER_viscosity_stress_bisection.m:12
    visco0=SiStER_get_ductile_rheology_on_nodes_from_stresses(MAT,PARAMS,Ts,sIIOLD_s,phase_s)
# SiStER_viscosity_stress_bisection.m:13
    if PARAMS.YNElast == 1:
        Zs=multiply(Gs,dt_m) / (multiply(Gs,dt_m) + visco0)
# SiStER_viscosity_stress_bisection.m:15
    else:
        Zs=ones(Ny,Nx)
# SiStER_viscosity_stress_bisection.m:17
    
    sIINEW=multiply(multiply(dot(2,visco0),epsII_s),Zs) + multiply((1 - Zs),sIIOLD_s)
# SiStER_viscosity_stress_bisection.m:19
    sIIHIGH[sIINEW > sIIHIGH]=sIINEW(sIINEW > sIIHIGH)
# SiStER_viscosity_stress_bisection.m:20
    sIILOW[sIINEW < sIILOW]=sIINEW(sIINEW < sIILOW)
# SiStER_viscosity_stress_bisection.m:21
    viscoNEW=SiStER_get_ductile_rheology_on_nodes_from_stresses(MAT,PARAMS,Ts,sIINEW,phase_s)
# SiStER_viscosity_stress_bisection.m:23
    if PARAMS.YNElast == 1:
        Zs=multiply(Gs,dt_m) / (multiply(Gs,dt_m) + viscoNEW)
# SiStER_viscosity_stress_bisection.m:25
    else:
        Zs=ones(Ny,Nx)
# SiStER_viscosity_stress_bisection.m:27
    
    sIINEW=multiply(multiply(dot(2,viscoNEW),epsII_s),Zs) + multiply((1 - Zs),sIIOLD_s)
# SiStER_viscosity_stress_bisection.m:29
    sIIHIGH[sIINEW > sIIHIGH]=sIINEW(sIINEW > sIIHIGH)
# SiStER_viscosity_stress_bisection.m:30
    sIILOW[sIINEW < sIILOW]=sIINEW(sIINEW < sIILOW)
# SiStER_viscosity_stress_bisection.m:31
    # 10 iterations of a BISECTION ALGORITHM
    Nbisec=10
# SiStER_viscosity_stress_bisection.m:34
    for i in arange(1,Nbisec).reshape(-1):
        sII=dot(0.5,(sIIHIGH + sIILOW))
# SiStER_viscosity_stress_bisection.m:37
        sIIPAST=copy(sII)
# SiStER_viscosity_stress_bisection.m:38
        visco=SiStER_get_ductile_rheology_on_nodes_from_stresses(MAT,PARAMS,Ts,sII,phase_s)
# SiStER_viscosity_stress_bisection.m:39
        if PARAMS.YNElast == 1:
            Zs=multiply(Gs,dt_m) / (multiply(Gs,dt_m) + visco)
# SiStER_viscosity_stress_bisection.m:41
        else:
            Zs=ones(Ny,Nx)
# SiStER_viscosity_stress_bisection.m:43
        sII=multiply(multiply(dot(2,visco),epsII_s),Zs) + multiply((1 - Zs),sIIOLD_s)
# SiStER_viscosity_stress_bisection.m:45
        sIILOW[sII > sIIPAST]=sIIPAST(sII > sIIPAST)
# SiStER_viscosity_stress_bisection.m:47
        sIIHIGH[sII <= sIIPAST]=sIIPAST(sII <= sIIPAST)
# SiStER_viscosity_stress_bisection.m:48
    