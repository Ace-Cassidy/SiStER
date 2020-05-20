# Generated with SMOP  0.41
from libsmop import *
# SiStER_patch_marker_holes.m

    
@function
def SiStER_patch_marker_holes(icn=None,jcn=None,quad=None,Nx=None,Ny=None,Mquad=None,Mquad_crit=None,xm=None,ym=None,x=None,y=None,dx=None,dy=None,im=None,ep=None,idm=None,Tm=None,sxxm=None,sxym=None,epNH=None,epsIIm=None,*args,**kwargs):
    varargin = SiStER_patch_marker_holes.varargin
    nargin = SiStER_patch_marker_holes.nargin

    # function [xm, ym, im, Ifix, mp, ep, idm, Tm, sxxm, sxym, epNH, epsIIm]=SiStER_patch_marker_holes(icn,jcn,quad,Nx,Ny,Mquad,Mquad_crit,xm,ym,x,y,dx,dy,im,ep,idm,Tm,sxxm,sxym,epNH,epsIIm)
    
    # seeds new markers in all quadrants where marker density has fallen below
# the threshold 
# AND THEN assigns those new markers a marker index, a marker phase and a plastic
# strain based on the properties of the markers surrounding them
# (these particular properties are never passed on the grid, e.g. plastic strain...)
    
    # J.-A. Olive, and B.Z. Klein, 2012-2014
    
    M=length(xm)
# SiStER_patch_marker_holes.m:13
    md_crit=copy(Mquad_crit)
# SiStER_patch_marker_holes.m:14
    mark_per_quad=copy(Mquad)
# SiStER_patch_marker_holes.m:15
    mdx=min(dx) / 2
# SiStER_patch_marker_holes.m:16
    mdy=min(dy) / 2
# SiStER_patch_marker_holes.m:17
    ############### LOOK FOR EMPTY (no more markers) QUADRANTS
    
    mp=accumarray(cellarray([icn,jcn,quad]),1,concat([Ny - 1,Nx - 1,4]))
# SiStER_patch_marker_holes.m:21
    empty=find(mp == 0)
# SiStER_patch_marker_holes.m:22
    display_message_if_empty=0
# SiStER_patch_marker_holes.m:24
    if display_message_if_empty == 1:
        if (logical_not(isempty(empty))):
            iEmpty,jEmpty,kEmpty=ind2sub(size(mp),empty,nargout=3)
# SiStER_patch_marker_holes.m:27
            for n in arange(1,min(length(iEmpty),100)).reshape(-1):
                disp(concat(['WARNING ! Empty quadrant number ',num2str(kEmpty(n)),' in cell i = ',num2str(iEmpty(n)),', j = ',num2str(jEmpty(n))]))
    
    
    
    ##### LOCATE QUADRANTS WHERE MARKER DENSITY IS BELOW THRESHOLD
    mpCrInd=find(mp < md_crit)
# SiStER_patch_marker_holes.m:36
    iicr,jjcr,qqcr=ind2sub(size(mp),mpCrInd,nargout=3)
# SiStER_patch_marker_holes.m:37
    iicr=iicr.T
# SiStER_patch_marker_holes.m:38
    jjcr=jjcr.T
# SiStER_patch_marker_holes.m:39
    qqcr=qqcr.T
# SiStER_patch_marker_holes.m:40
    # NEED TO SEED NEW MARKERS IN THOSE QUADRANTS 
# SO THAT WE ARE BACK TO THE INITIAL MARKER DENSITY IN THOSE QUADRANTS
    
    xrsd=[]
# SiStER_patch_marker_holes.m:45
    yrsd=[]
# SiStER_patch_marker_holes.m:46
    im_fix=[]
# SiStER_patch_marker_holes.m:47
    
    ep_fix=[]
# SiStER_patch_marker_holes.m:48
    
    epNH_fix=[]
# SiStER_patch_marker_holes.m:49
    
    te_fix=[]
# SiStER_patch_marker_holes.m:50
    
    sxx_fix=[]
# SiStER_patch_marker_holes.m:51
    
    sxy_fix=[]
# SiStER_patch_marker_holes.m:52
    
    sr_fix=[]
# SiStER_patch_marker_holes.m:53
    
    
    if logical_not(isempty(iicr)):
        for c in arange(1,length(iicr)).reshape(-1):
            # the upper-left node of the corresponding cell is
            icell=iicr(c)
# SiStER_patch_marker_holes.m:60
            jcell=jjcr(c)
# SiStER_patch_marker_holes.m:61
            qcell=qqcr(c)
# SiStER_patch_marker_holes.m:62
            qsize=dot(dot(0.25,dx(jcell)),dy(icell))
# SiStER_patch_marker_holes.m:64
            # mark_per_quad markers, then this critical quadrant needs
            Nfix=dot(ceil(qsize / (dot(mdx,mdy))),mark_per_quad)
# SiStER_patch_marker_holes.m:67
            Nfix=max(Nfix - mp(iicr(c),jjcr(c),qqcr(c)),1)
# SiStER_patch_marker_holes.m:68
            if qcell == 1 or qcell == 4:
                xcorn=x(jcell)
# SiStER_patch_marker_holes.m:72
            else:
                xcorn=x(jcell) + dx(jcell) / 2
# SiStER_patch_marker_holes.m:74
            if qcell == 1 or qcell == 2:
                ycorn=y(icell)
# SiStER_patch_marker_holes.m:77
            else:
                ycorn=y(icell) + dy(icell) / 2
# SiStER_patch_marker_holes.m:79
            # draw random marker location
            xmrr,ymrr=SiStER_seed_markers_uniformly(xcorn,ycorn,dx(jcell) / 2,dy(icell) / 2,Nfix,nargout=2)
# SiStER_patch_marker_holes.m:83
            xrsd=concat([xrsd,xmrr])
# SiStER_patch_marker_holes.m:85
            yrsd=concat([yrsd,ymrr])
# SiStER_patch_marker_holes.m:86
            #### NOW THAT THE NEW MARKERS ARE SEEDED,
##### ASSIGN PARAMETERS THAT ARE NEVER STORED ON THE EULERIAN GRID
            # the value is assigned based on the average, or max. value of the
# markers that remain in the corresponding CELL (since there's no grid value to interpolate from)
            # CAREFUL THIS CANNOT WORK IF WE END UP WITH AN EMPTY CELL
# if that was to happen, let's just draw "im" randomly
            if isempty((ep(icn == logical_and(icell,jcn) == jcell))) == 1:
                disp('WARNING ! - EMPTY CELL - SOMETHING IS VERY WRONG...')
                im_fix=1 + floor(dot(rand(1,Nfix),max(im)))
# SiStER_patch_marker_holes.m:101
                ep_fix=zeros(1,Nfix)
# SiStER_patch_marker_holes.m:102
                epNH_fix=zeros(1,Nfix)
# SiStER_patch_marker_holes.m:103
                te_fix=zeros(1,Nfix)
# SiStER_patch_marker_holes.m:104
                sxx_fix=zeros(1,Nfix)
# SiStER_patch_marker_holes.m:105
                sxy_fix=zeros(1,Nfix)
# SiStER_patch_marker_holes.m:106
                sr_fix=zeros(1,Nfix)
# SiStER_patch_marker_holes.m:107
            else:
                # assign the average phase of the markers that are left in the cell
                phase_fix=round(mode((im(icn == logical_and(icell,jcn) == jcell))))
# SiStER_patch_marker_holes.m:113
                strain_fix=max((ep(icn == logical_and(icell,jcn) == jcell)))
# SiStER_patch_marker_holes.m:115
                strainNH_fix=max((epNH(icn == logical_and(icell,jcn) == jcell)))
# SiStER_patch_marker_holes.m:116
                # the cell
                temp_fix=mean((Tm(icn == logical_and(icell,jcn) == jcell)))
# SiStER_patch_marker_holes.m:119
                stress_xx_fix=mean((sxxm(icn == logical_and(icell,jcn) == jcell)))
# SiStER_patch_marker_holes.m:121
                stress_xy_fix=mean((sxym(icn == logical_and(icell,jcn) == jcell)))
# SiStER_patch_marker_holes.m:122
                strainrate_fix=mean((epsIIm(icn == logical_and(icell,jcn) == jcell)))
# SiStER_patch_marker_holes.m:123
            im_fix=concat([im_fix,dot(phase_fix,ones(1,Nfix))])
# SiStER_patch_marker_holes.m:127
            ep_fix=concat([ep_fix,dot(strain_fix,ones(1,Nfix))])
# SiStER_patch_marker_holes.m:128
            epNH_fix=concat([epNH_fix,dot(strainNH_fix,ones(1,Nfix))])
# SiStER_patch_marker_holes.m:129
            te_fix=concat([te_fix,dot(temp_fix,ones(1,Nfix))])
# SiStER_patch_marker_holes.m:130
            sxx_fix=concat([sxx_fix,dot(stress_xx_fix,ones(1,Nfix))])
# SiStER_patch_marker_holes.m:131
            sxy_fix=concat([sxy_fix,dot(stress_xy_fix,ones(1,Nfix))])
# SiStER_patch_marker_holes.m:132
            sr_fix=concat([sr_fix,dot(strainrate_fix,ones(1,Nfix))])
# SiStER_patch_marker_holes.m:133
        # NOW ASSIGN PROPERTIES TO THOSE MARKERS
        Npatch=length(xrsd)
# SiStER_patch_marker_holes.m:140
        index_fix=arange(max(idm) + 1,max(idm) + Npatch)
# SiStER_patch_marker_holes.m:141
        Ifix=arange(M + 1,M + Npatch,1)
# SiStER_patch_marker_holes.m:143
        xm[Ifix]=xrsd
# SiStER_patch_marker_holes.m:144
        ym[Ifix]=yrsd
# SiStER_patch_marker_holes.m:145
        im[Ifix]=im_fix
# SiStER_patch_marker_holes.m:146
        ep[Ifix]=ep_fix
# SiStER_patch_marker_holes.m:147
        epNH[Ifix]=epNH_fix
# SiStER_patch_marker_holes.m:148
        idm[Ifix]=index_fix
# SiStER_patch_marker_holes.m:149
        Tm[Ifix]=te_fix
# SiStER_patch_marker_holes.m:150
        sxxm[Ifix]=sxx_fix
# SiStER_patch_marker_holes.m:151
        sxym[Ifix]=sxy_fix
# SiStER_patch_marker_holes.m:152
        epsIIm[Ifix]=sr_fix
# SiStER_patch_marker_holes.m:153
        # uncomment to display number of added markers
#fprintf('\n#d#s#d#s\n', length(Ifix), ' markers added in ', length(iicr), ' cell quadrants.')
    else:
        Ifix=0
# SiStER_patch_marker_holes.m:160
    