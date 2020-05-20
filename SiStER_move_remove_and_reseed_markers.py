# Generated with SMOP  0.41
from libsmop import *
# SiStER_move_remove_and_reseed_markers.m

    # SiStER Update Markers
    
    xm_new,ym_new=SiStER_advect_markers(x,y,xm,ym,dx,dy,dt_m,vx,vy,nargout=2)
# SiStER_move_remove_and_reseed_markers.m:3
    xm=copy(xm_new)
# SiStER_move_remove_and_reseed_markers.m:4
    ym=copy(ym_new)
# SiStER_move_remove_and_reseed_markers.m:5
    # eliminate markers that left domain
    Iin=find(xm <= logical_and(xsize,xm) >= logical_and(0,ym) >= logical_and(0,ym) <= ysize)
# SiStER_move_remove_and_reseed_markers.m:7
    #msg2='  markers removed: ';
#msg=[msg2 num2str(length(xm)-length(Iin))];
#disp(msg)
    xm=xm(Iin)
# SiStER_move_remove_and_reseed_markers.m:12
    ym=ym(Iin)
# SiStER_move_remove_and_reseed_markers.m:13
    im=im(Iin)
# SiStER_move_remove_and_reseed_markers.m:14
    ep=ep(Iin)
# SiStER_move_remove_and_reseed_markers.m:15
    epNH=epNH(Iin)
# SiStER_move_remove_and_reseed_markers.m:16
    Tm=Tm(Iin)
# SiStER_move_remove_and_reseed_markers.m:17
    idm=idm(Iin)
# SiStER_move_remove_and_reseed_markers.m:18
    sxxm=sxxm(Iin)
# SiStER_move_remove_and_reseed_markers.m:19
    sxym=sxym(Iin)
# SiStER_move_remove_and_reseed_markers.m:20
    epsIIm=epsIIm(Iin)
# SiStER_move_remove_and_reseed_markers.m:21
    # locate advected markers with respect to the eulerian grid
    quad,icn,jcn=SiStER_locate_markers_in_grid(xm,ym,x,y,dx,dy,nargout=3)
# SiStER_move_remove_and_reseed_markers.m:24
    # check for holes in the marker distribution, 
# patch with new markers if necessary
# those new markers immediately get assigned a value of phase (im), index 
# (idm) and accumulated plastic strain (ep), i.e., the 2 variables that never get
# passed to nodes.
    xm,ym,im,Ifix,mp,ep,idm,Tm,sxxm,sxym,epNH,epsIIm=SiStER_patch_marker_holes(icn,jcn,quad,Nx,Ny,Mquad,Mquad_crit,xm,ym,x,y,dx,dy,im,ep,idm,Tm,sxxm,sxym,epNH,epsIIm,nargout=12)
# SiStER_move_remove_and_reseed_markers.m:31
    # then they get assigned P, epsII and stresses from grid values
    
    if min(Ifix) > 0:
        xmFIX=xm(Ifix)
# SiStER_move_remove_and_reseed_markers.m:38
        ymFIX=ym(Ifix)
# SiStER_move_remove_and_reseed_markers.m:39
        # markers from their nodal values
    # locate new markers with respect to the eulerian grid
        quadFIX,icnFIX,jcnFIX=SiStER_locate_markers_in_grid(xmFIX,ymFIX,x,y,dx,dy,nargout=3)
# SiStER_move_remove_and_reseed_markers.m:44
        temp=SiStER_interp_normal_nodes_to_markers(p,xc,yc,xmFIX,ymFIX,icnFIX,jcnFIX)
# SiStER_move_remove_and_reseed_markers.m:47
        pm[Ifix]=temp
# SiStER_move_remove_and_reseed_markers.m:48
    
    
    
    # locate all markers with respect to the eulerian grid
    qd,icn,jcn=SiStER_locate_markers_in_grid(xm,ym,x,y,dx,dy,nargout=3)
# SiStER_move_remove_and_reseed_markers.m:55