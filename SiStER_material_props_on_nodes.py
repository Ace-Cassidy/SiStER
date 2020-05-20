# Generated with SMOP  0.41
from libsmop import *
# SiStER_material_props_on_nodes.m

    #=========================================================================
# Get material properties on nodes from advected properties of markers
# G.Ito 8/16 - replaces previous version, which relied on marker viscosity
# for Picard iterations (J.-A.O.)
#=========================================================================
    
    # PHASE PROPORTIONS AT NORMAL AND SHEAR NODES. G.Ito 8/16
    phase_n=SiStER_interp_phases_to_normal_nodes(xm,ym,icn,jcn,x,y,im,Nphase)
# SiStER_material_props_on_nodes.m:8
    phase_s=SiStER_interp_phases_to_shear_nodes(xm,ym,icn,jcn,qd,x,y,im,Nphase)
# SiStER_material_props_on_nodes.m:9
    # phase_n and _s is a Ny*Nx*Nphase array containing the proportion
# of each phase at each node - this gets used in get_ductile_rheology
# functions
    
    # OLD WAY TO INTERP PHASES: ONLY WORKED WELL WHEN MIXING 2 CONSECUTIVELY 
# NUMBERED PHASES AT ANY NODE
# [n2interp] = SiStER_interp_markers_to_normal_nodes(xm,ym,icn,jcn,x,y,im);
# phase_n=n2interp(1).data;
# phase_n=round(phase_n*1e10)/1e10;  #prevents a case in which phase_n>NPhase
# 
# [n2interp] = SiStER_interp_markers_to_shear_nodes(xm,ym,icn,jcn,qd,x,y,im);
# phase_s=n2interp(1).data;
# phase_s=round(phase_s*1e10)/1e10; #prevents a case in which phase_n>NPhase
    
    # GET MARKER DENSITIES
    rhom=SiStER_get_density(im,Tm,MAT)
# SiStER_material_props_on_nodes.m:25
    # pass density to nodes
    n2interp=SiStER_interp_markers_to_shear_nodes(xm,ym,icn,jcn,qd,x,y,rhom)
# SiStER_material_props_on_nodes.m:27
    rho=n2interp(1).data
# SiStER_material_props_on_nodes.m:28
    # GET MARKER ELASTIC PROPERTIES  G.Ito 8/16
    Gm=SiStER_get_elastic_moduli(im,MAT)
# SiStER_material_props_on_nodes.m:31
    # pass shear modulus to nodes
    n2interp=SiStER_interp_markers_to_normal_nodes(xm,ym,icn,jcn,x,y,1.0 / Gm)
# SiStER_material_props_on_nodes.m:33
    Gn=1.0 / (n2interp(1).data)
# SiStER_material_props_on_nodes.m:34
    n2interp=SiStER_interp_markers_to_shear_nodes(xm,ym,icn,jcn,qd,x,y,1.0 / Gm)
# SiStER_material_props_on_nodes.m:35
    Gs=1.0 / (n2interp(1).data)
# SiStER_material_props_on_nodes.m:36
    # PROPERTIES FOR PLASTICITY  G.Ito 8/16
    cohes=SiStER_get_cohesion(im,ep,MAT)
# SiStER_material_props_on_nodes.m:39
    
    n2interp=SiStER_interp_markers_to_normal_nodes(xm,ym,icn,jcn,x,y,cohes)
# SiStER_material_props_on_nodes.m:40
    Cohes_n=n2interp(1).data
# SiStER_material_props_on_nodes.m:41
    n2interp=SiStER_interp_markers_to_shear_nodes(xm,ym,icn,jcn,qd,x,y,cohes)
# SiStER_material_props_on_nodes.m:42
    Cohes_s=n2interp(1).data
# SiStER_material_props_on_nodes.m:43
    # GET FRICTION BASED ON MARKERS J.A. Olive 4/17
    fric=SiStER_get_friction(im,ep,MAT)
# SiStER_material_props_on_nodes.m:46
    
    n2interp=SiStER_interp_markers_to_normal_nodes(xm,ym,icn,jcn,x,y,fric)
# SiStER_material_props_on_nodes.m:47
    Mu_n=n2interp(1).data
# SiStER_material_props_on_nodes.m:48
    n2interp=SiStER_interp_markers_to_shear_nodes(xm,ym,icn,jcn,qd,x,y,fric)
# SiStER_material_props_on_nodes.m:49
    Mu_s=n2interp(1).data
# SiStER_material_props_on_nodes.m:50
    # ADVECTED strain rate invariant G.Ito 8/16
    n2interp=SiStER_interp_markers_to_normal_nodes(xm,ym,icn,jcn,x,y,epsIIm)
# SiStER_material_props_on_nodes.m:53
    epsII_n=n2interp(1).data
# SiStER_material_props_on_nodes.m:54
    n2interp=SiStER_interp_markers_to_shear_nodes(xm,ym,icn,jcn,qd,x,y,epsIIm)
# SiStER_material_props_on_nodes.m:55
    epsII_s=n2interp(1).data
# SiStER_material_props_on_nodes.m:56
    # OLD STRESSES AND PRESSURES G.Ito 8/16
    n2interp=SiStER_interp_markers_to_normal_nodes(xm,ym,icn,jcn,x,y,sxxm)
# SiStER_material_props_on_nodes.m:60
    sxxOLD[arange(),arange()]=n2interp(1).data
# SiStER_material_props_on_nodes.m:61
    sxxOLD_s=SiStER_interp_normal_to_shear_nodes(sxxOLD,dx,dy)
# SiStER_material_props_on_nodes.m:62
    n2interp=SiStER_interp_markers_to_shear_nodes(xm,ym,icn,jcn,qd,x,y,sxym)
# SiStER_material_props_on_nodes.m:64
    sxyOLD[arange(),arange()]=n2interp(1).data
# SiStER_material_props_on_nodes.m:65
    sxyOLD_n=SiStER_interp_shear_to_normal_nodes(sxyOLD)
# SiStER_material_props_on_nodes.m:66
    #MIGHT WANT TO ADVECT PRESSURES (FOR SPEED?) G.Ito 8/16
    pold=copy(p)
# SiStER_material_props_on_nodes.m:69
    ps_old=SiStER_interp_normal_to_shear_nodes(p,dx,dy)
# SiStER_material_props_on_nodes.m:70
    EXYOLD=copy(EXY)
# SiStER_material_props_on_nodes.m:72
    EXXOLD=copy(EXX)
# SiStER_material_props_on_nodes.m:73
    EXX_sOLD=SiStER_interp_normal_to_shear_nodes(EXX,dx,dy)
# SiStER_material_props_on_nodes.m:74
    EXY_nOLD=SiStER_interp_shear_to_normal_nodes(EXY)
# SiStER_material_props_on_nodes.m:75
    #TEMPERATURE ARRAYS NEEDED FOR DUCTILE RHEOLOGY  G.Ito 8/16
    n2interp=SiStER_interp_markers_to_shear_nodes(xm,ym,icn,jcn,qd,x,y,Tm)
# SiStER_material_props_on_nodes.m:78
    Ts=n2interp(1).data
# SiStER_material_props_on_nodes.m:79
    n2interp=SiStER_interp_markers_to_normal_nodes(xm,ym,icn,jcn,x,y,Tm)
# SiStER_material_props_on_nodes.m:80
    Tn=n2interp(1).data
# SiStER_material_props_on_nodes.m:81