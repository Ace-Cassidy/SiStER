# Generated with SMOP  0.41
from libsmop import *
# SiStER_stress_update.m

    # update elastic stresses on markers following a solve (but before advection)
    
    # get marker rotation rates
    ROT=SiStER_get_rotation_rate(vx,vy,dx,dy,BC)
# SiStER_stress_update.m:4
    om=SiStER_interp_shear_nodes_to_markers(ROT,x,y,xm,ym,icn,jcn)
# SiStER_stress_update.m:5
    # compute stress changes on nodes
    dsxx=multiply((multiply(dot(2,etan),EXX) - sxxOLD),Zn)
# SiStER_stress_update.m:8
    dsxy=multiply((multiply(dot(2,etas),EXY) - sxyOLD),Zs)
# SiStER_stress_update.m:9
    # pass stress changes to markers
    dsxxm=SiStER_interp_normal_nodes_to_markers(dsxx,xc,yc,xm,ym,icn,jcn)
# SiStER_stress_update.m:12
    dsxym=SiStER_interp_shear_nodes_to_markers(dsxy,x,y,xm,ym,icn,jcn)
# SiStER_stress_update.m:13
    # UPDATE STRESSED ON MARKERS
    sxxm=sxxm + dsxxm
# SiStER_stress_update.m:16
    sxym=sxym + dsxym
# SiStER_stress_update.m:17
    # ROTATE MARKERS
    alpha=dot(om,dt_m)
# SiStER_stress_update.m:20
    sxymtemp=multiply(sxxm,(sin(alpha) ** 2)) + multiply(sxym,cos(dot(2.0,alpha)))
# SiStER_stress_update.m:21
    sxxm=multiply(sxxm,(cos(alpha) ** 2 - sin(alpha) ** 2)) - multiply(sxym,sin(dot(2.0,alpha)))
# SiStER_stress_update.m:22
    sxym=copy(sxymtemp)
# SiStER_stress_update.m:23
    # get the current second invariant of strain rate to update ep below
# (not needed if PARAMS.epsII_from_stress==0, because we already have it 
# from the last Picard iteration)
    if (PARAMS.YNPlas == 1 and PARAMS.epsII_from_stress == 1):
        exxm=SiStER_interp_normal_nodes_to_markers(EXX,xc,yc,xm,ym,icn,jcn)
# SiStER_stress_update.m:29
        exym=SiStER_interp_shear_nodes_to_markers(EXY,x,y,xm,ym,icn,jcn)
# SiStER_stress_update.m:30
        epsIIm=sqrt(exxm ** 2 + exym ** 2)
# SiStER_stress_update.m:31
    
    # PLASTICITY UPDATE
    if PARAMS.YNPlas == 1:
        # STRESS REDUCTION IN YIELDED REGIONS
        sIItemp=sqrt(sxxm ** 2 + sxym ** 2)
# SiStER_stress_update.m:37
        sxxm[sIItemp >= dot(0.99,syield)]=multiply(sxxm(sIItemp >= dot(0.99,syield)),syield(sIItemp >= dot(0.99,syield))) / sIItemp(sIItemp >= dot(0.99,syield))
# SiStER_stress_update.m:38
        sxym[sIItemp >= dot(0.99,syield)]=multiply(sxym(sIItemp >= dot(0.99,syield)),syield(sIItemp >= dot(0.99,syield))) / sIItemp(sIItemp >= dot(0.99,syield))
# SiStER_stress_update.m:39
        ep[sIItemp >= dot(0.99,syield)]=ep(sIItemp >= dot(0.99,syield)) + dot(dt_m,epsIIm(sIItemp >= dot(0.99,syield)))
# SiStER_stress_update.m:41
        epNH[sIItemp >= dot(0.99,syield)]=ep(sIItemp >= dot(0.99,syield)) + dot(dt_m,epsIIm(sIItemp >= dot(0.99,syield)))
# SiStER_stress_update.m:42
        # STRAIN HEALING
        ep=ep / (dt_m / PARAMS.tau_heal + 1)
# SiStER_stress_update.m:44
    