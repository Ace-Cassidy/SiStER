# Generated with SMOP  0.41
from libsmop import *
# SiStER_rotate_stresses.m

    # update elastic stresses on markers following a solve (but before advection)
    
    ROT=SiStER_get_rotation_rate(vx,vy,dx,dy,BC)
# SiStER_rotate_stresses.m:3
    om=SiStER_interp_shear_nodes_to_markers(ROT,x,y,xm,ym,icn,jcn)
# SiStER_rotate_stresses.m:4
    # rotate markers
    alpha=dot(om,dt_m)
# SiStER_rotate_stresses.m:7
    sxymtemp=multiply(sxxm,sin(dot(2.0,alpha))) + multiply(sxym,cos(dot(2.0,alpha)))
# SiStER_rotate_stresses.m:8
    sxxm=multiply(sxxm,(cos(alpha) ** 2 - sin(alpha) ** 2)) - multiply(sxym,sin(dot(2.0,alpha)))
# SiStER_rotate_stresses.m:9
    sxym=copy(sxymtemp)
# SiStER_rotate_stresses.m:10