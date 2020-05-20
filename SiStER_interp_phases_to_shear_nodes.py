# Generated with SMOP  0.41
from libsmop import *
# SiStER_interp_phases_to_shear_nodes.m

    
@function
def SiStER_interp_phases_to_shear_nodes(xm=None,ym=None,icn=None,jcn=None,quad=None,x=None,y=None,phases=None,maxPhases=None,*args,**kwargs):
    varargin = SiStER_interp_phases_to_shear_nodes.varargin
    nargin = SiStER_interp_phases_to_shear_nodes.nargin

    # [phasesS] = SiStER_interp_phases_to_shear_nodes(xm,ym,icn,jcn,quad,x,y,phases,maxPhases)
# B.Z. Klein, July 2017, an interp function specific to phase (to shear nodes), to enable 
# exact mixing of several phases
    
    Nx=length(x)
# SiStER_interp_phases_to_shear_nodes.m:7
    Ny=length(y)
# SiStER_interp_phases_to_shear_nodes.m:8
    dx=diff(x)
# SiStER_interp_phases_to_shear_nodes.m:9
    dy=diff(y)
# SiStER_interp_phases_to_shear_nodes.m:10
    JCN=interp1(x,arange(1,length(x)),xm,'nearest','extrap')
# SiStER_interp_phases_to_shear_nodes.m:12
    
    ICN=interp1(y,arange(1,length(y)),ym,'nearest','extrap')
# SiStER_interp_phases_to_shear_nodes.m:13
    
    phasesS=zeros(Ny,Nx,maxPhases)
# SiStER_interp_phases_to_shear_nodes.m:16
    ## Interior Cells
    
    center=jcn > logical_and(1,jcn) < logical_and(Nx,icn) > logical_and(1,icn) < Ny
# SiStER_interp_phases_to_shear_nodes.m:20
    shiftLeft=jcn < logical_and(Nx - 1,icn) > logical_and(1,icn) < Ny
# SiStER_interp_phases_to_shear_nodes.m:21
    shiftUp=jcn > logical_and(1,jcn) < logical_and(Nx,icn) < Ny - 1
# SiStER_interp_phases_to_shear_nodes.m:22
    shiftBoth=jcn < logical_and(Nx - 1,icn) < Ny - 1
# SiStER_interp_phases_to_shear_nodes.m:23
    cell1=logical_and(logical_and(center,((xm - x(JCN)) > 0)),((ym - y(ICN)) > 0))
# SiStER_interp_phases_to_shear_nodes.m:26
    
    cell2=logical_and(logical_and(shiftLeft,((xm - x(JCN)) < 0)),((ym - y(ICN)) > 0))
# SiStER_interp_phases_to_shear_nodes.m:27
    cell3=logical_and(logical_and(shiftBoth,((xm - x(JCN)) < 0)),((ym - y(ICN)) < 0))
# SiStER_interp_phases_to_shear_nodes.m:28
    cell4=logical_and(logical_and(shiftUp,((xm - x(JCN)) > 0)),((ym - y(ICN)) < 0))
# SiStER_interp_phases_to_shear_nodes.m:29
    ### WEIGHTING (equal for now because that is what I'm running)
    
    wc1=0.25
# SiStER_interp_phases_to_shear_nodes.m:33
    wc2=0.25
# SiStER_interp_phases_to_shear_nodes.m:34
    wc3=0.25
# SiStER_interp_phases_to_shear_nodes.m:35
    wc4=0.25
# SiStER_interp_phases_to_shear_nodes.m:36
    # cell 1 (i,j,1)
    
    dxm=xm(cell1) - x(JCN(cell1))
# SiStER_interp_phases_to_shear_nodes.m:41
    dym=ym(cell1) - y(ICN(cell1))
# SiStER_interp_phases_to_shear_nodes.m:42
    ddx=dx(JCN(cell1))
# SiStER_interp_phases_to_shear_nodes.m:43
    ddy=dy(ICN(cell1))
# SiStER_interp_phases_to_shear_nodes.m:44
    wm1=1 - (multiply(dxm,dym) + multiply((ddx - dxm),dym) + multiply((ddy - dym),dxm)) / (multiply(ddx,ddy))
# SiStER_interp_phases_to_shear_nodes.m:46
    w1=accumarray(concat([ICN(cell1).T,JCN(cell1).T]),wm1,concat([Ny,Nx]))
# SiStER_interp_phases_to_shear_nodes.m:47
    # cell 2 (i, j-1, 2)
    
    dxm=xm(cell2) - x(JCN(cell2))
# SiStER_interp_phases_to_shear_nodes.m:51
    dym=ym(cell2) - y(ICN(cell2))
# SiStER_interp_phases_to_shear_nodes.m:52
    ddx=dx(JCN(cell2) - 1)
# SiStER_interp_phases_to_shear_nodes.m:53
    ddy=dy(ICN(cell2))
# SiStER_interp_phases_to_shear_nodes.m:54
    wm2=1 - (multiply(dxm,dym) + multiply((ddx - dxm),dym) + multiply((ddy - dym),dxm)) / (multiply(ddx,ddy))
# SiStER_interp_phases_to_shear_nodes.m:56
    w2=accumarray(concat([ICN(cell2).T,JCN(cell2).T]),wm2,concat([Ny,Nx]))
# SiStER_interp_phases_to_shear_nodes.m:57
    # cell 3 (i-1, j-1, 3)
    
    dxm=xm(cell3) - x(JCN(cell3))
# SiStER_interp_phases_to_shear_nodes.m:61
    dym=ym(cell3) - y(ICN(cell3))
# SiStER_interp_phases_to_shear_nodes.m:62
    ddx=dx(JCN(cell3) - 1)
# SiStER_interp_phases_to_shear_nodes.m:63
    ddy=dy(ICN(cell3) - 1)
# SiStER_interp_phases_to_shear_nodes.m:64
    wm3=1 - (multiply(dxm,dym) + multiply((ddx - dxm),dym) + multiply((ddy - dym),dxm)) / (multiply(ddx,ddy))
# SiStER_interp_phases_to_shear_nodes.m:66
    w3=accumarray(concat([ICN(cell3).T,JCN(cell3).T]),wm3,concat([Ny,Nx]))
# SiStER_interp_phases_to_shear_nodes.m:67
    # cell 4 (i-1, j, 4)
    
    dxm=xm(cell4) - x(JCN(cell4))
# SiStER_interp_phases_to_shear_nodes.m:71
    dym=ym(cell4) - y(ICN(cell4))
# SiStER_interp_phases_to_shear_nodes.m:72
    ddx=dx(JCN(cell4))
# SiStER_interp_phases_to_shear_nodes.m:73
    ddy=dy(ICN(cell4) - 1)
# SiStER_interp_phases_to_shear_nodes.m:74
    wm4=1 - (multiply(dxm,dym) + multiply((ddx - dxm),dym) + multiply((ddy - dym),dxm)) / (multiply(ddx,ddy))
# SiStER_interp_phases_to_shear_nodes.m:76
    w4=accumarray(concat([ICN(cell4).T,JCN(cell4).T]),wm4,concat([Ny,Nx]))
# SiStER_interp_phases_to_shear_nodes.m:77
    #loop over material properties to interpolate
    
    for n in arange(1,maxPhases).reshape(-1):
        phaseMask=phases == n
# SiStER_interp_phases_to_shear_nodes.m:83
        phasesS[arange(),arange(),n]=(dot(wc1,accumarray(concat([ICN(logical_and(cell1,phaseMask)).T,JCN(logical_and(cell1,phaseMask)).T]),wm1(phaseMask(cell1)),concat([Ny,Nx]))) / w1 + dot(wc2,accumarray(concat([ICN(logical_and(cell2,phaseMask)).T,JCN(logical_and(cell2,phaseMask)).T]),wm2(phaseMask(cell2)),concat([Ny,Nx]))) / w2 + dot(wc3,accumarray(concat([ICN(logical_and(cell3,phaseMask)).T,JCN(logical_and(cell3,phaseMask)).T]),wm3(phaseMask(cell3)),concat([Ny,Nx]))) / w3 + dot(wc4,accumarray(concat([ICN(logical_and(cell4,phaseMask)).T,JCN(logical_and(cell4,phaseMask)).T]),wm4(phaseMask(cell4)),concat([Ny,Nx]))) / w4) / (wc1 + wc2 + wc4 + wc4)
# SiStER_interp_phases_to_shear_nodes.m:85
    
    ## EDGES
    
    ### top edge
    
    topEdge=jcn > logical_and(1,jcn) < logical_and(Nx,icn) == 1
# SiStER_interp_phases_to_shear_nodes.m:98
    shifted=jcn < logical_and(Nx - 1,icn) == 1
# SiStER_interp_phases_to_shear_nodes.m:99
    # cell 1
    
    cell1=logical_and(shifted,quad) == 2
# SiStER_interp_phases_to_shear_nodes.m:103
    ddx=dx(JCN(cell1) - 1)
# SiStER_interp_phases_to_shear_nodes.m:105
    ddy=dy(1)
# SiStER_interp_phases_to_shear_nodes.m:106
    dxm=xm(cell1) - x(JCN(cell1))
# SiStER_interp_phases_to_shear_nodes.m:107
    dym=ym(cell1) - y(ICN(cell1))
# SiStER_interp_phases_to_shear_nodes.m:108
    wm1=1 - (multiply(dxm,dym) + multiply((ddx - dxm),dym) + multiply((ddy - dym),dxm)) / (multiply(ddx,ddy))
# SiStER_interp_phases_to_shear_nodes.m:109
    w1=accumarray(concat([ICN(cell1).T,JCN(cell1).T]),wm1,concat([1,Nx]))
# SiStER_interp_phases_to_shear_nodes.m:110
    # cell 2
    
    cell2=logical_and(topEdge,quad) == 1
# SiStER_interp_phases_to_shear_nodes.m:114
    ddx=dx(JCN(cell2))
# SiStER_interp_phases_to_shear_nodes.m:116
    ddy=dy(1)
# SiStER_interp_phases_to_shear_nodes.m:117
    dxm=xm(cell2) - x(JCN(cell2))
# SiStER_interp_phases_to_shear_nodes.m:118
    dym=ym(cell2) - y(ICN(cell2))
# SiStER_interp_phases_to_shear_nodes.m:119
    wm2=1 - (multiply(dxm,dym) + multiply((ddx - dxm),dym) + multiply((ddy - dym),dxm)) / (multiply(ddx,ddy))
# SiStER_interp_phases_to_shear_nodes.m:120
    w2=accumarray(concat([ICN(cell2).T,JCN(cell2).T]),wm2,concat([1,Nx]))
# SiStER_interp_phases_to_shear_nodes.m:121
    #loop over material properties to interpolate
    
    for n in arange(1,maxPhases).reshape(-1):
        phaseMask=phases == n
# SiStER_interp_phases_to_shear_nodes.m:127
        temp=(dot(wc1,accumarray(concat([ICN(logical_and(cell1,phaseMask)).T,JCN(logical_and(cell1,phaseMask)).T]),wm1(phaseMask(cell1)),concat([1,Nx]))) / w1 + dot(wc2,accumarray(concat([ICN(logical_and(cell2,phaseMask)).T,JCN(logical_and(cell2,phaseMask)).T]),wm2(phaseMask(cell2)),concat([1,Nx]))) / w2) / (wc1 + wc2)
# SiStER_interp_phases_to_shear_nodes.m:129
        phasesS[1,arange(),n]=temp
# SiStER_interp_phases_to_shear_nodes.m:132
    
    clear('w1','w2')
    ### bottom edge
    
    bottomEdge=jcn > logical_and(1,jcn) < logical_and(Nx,icn) == Ny - 1
# SiStER_interp_phases_to_shear_nodes.m:139
    shifted=jcn < logical_and(Nx - 1,icn) == Ny - 1
# SiStER_interp_phases_to_shear_nodes.m:140
    # cell 1
    
    cell1=logical_and(shifted,quad) == 3
# SiStER_interp_phases_to_shear_nodes.m:144
    ddx=dx(JCN(cell1) - 1)
# SiStER_interp_phases_to_shear_nodes.m:146
    ddy=dy(Ny - 1)
# SiStER_interp_phases_to_shear_nodes.m:147
    dxm=xm(cell1) - x(JCN(cell1))
# SiStER_interp_phases_to_shear_nodes.m:148
    dym=ym(cell1) - y(end() - 1)
# SiStER_interp_phases_to_shear_nodes.m:149
    wm1=1 - (multiply(dxm,dym) + multiply((ddx - dxm),dym) + multiply((ddy - dym),dxm)) / (multiply(ddx,ddy))
# SiStER_interp_phases_to_shear_nodes.m:150
    w1=accumarray(concat([ones(sum(cell1),1),JCN(cell1).T]),wm1,concat([1,Nx]))
# SiStER_interp_phases_to_shear_nodes.m:151
    # cell 2
    
    cell2=logical_and(bottomEdge,quad) == 4
# SiStER_interp_phases_to_shear_nodes.m:155
    ddx=dx(JCN(cell2))
# SiStER_interp_phases_to_shear_nodes.m:157
    ddy=dy(Ny - 1)
# SiStER_interp_phases_to_shear_nodes.m:158
    dxm=xm(cell2) - x(JCN(cell2))
# SiStER_interp_phases_to_shear_nodes.m:159
    dym=ym(cell2) - y(end() - 1)
# SiStER_interp_phases_to_shear_nodes.m:160
    wm2=1 - (multiply(dxm,dym) + multiply((ddx - dxm),dym) + multiply((ddy - dym),dxm)) / (multiply(ddx,ddy))
# SiStER_interp_phases_to_shear_nodes.m:161
    w2=accumarray(concat([ones(sum(cell2),1),JCN(cell2).T]),wm2,concat([1,Nx]))
# SiStER_interp_phases_to_shear_nodes.m:162
    #loop over material properties to interpolate
    
    for n in arange(1,maxPhases).reshape(-1):
        phaseMask=phases == n
# SiStER_interp_phases_to_shear_nodes.m:168
        temp=(dot(wc1,accumarray(concat([ones(sum(logical_and(cell1,phaseMask)),1),JCN(logical_and(cell1,phaseMask)).T]),wm1(phaseMask(cell1)),concat([1,Nx]))) / w1 + dot(wc2,accumarray(concat([ones(sum(logical_and(cell2,phaseMask)),1),JCN(logical_and(cell2,phaseMask)).T]),wm2(phaseMask(cell2)),concat([1,Nx]))) / w2) / (wc1 + wc2)
# SiStER_interp_phases_to_shear_nodes.m:170
        phasesS[Ny,arange(),n]=temp
# SiStER_interp_phases_to_shear_nodes.m:173
    
    ### left edge
    
    leftEdge=jcn == logical_and(1,icn) > logical_and(1,icn) < Ny
# SiStER_interp_phases_to_shear_nodes.m:178
    shifted=jcn == logical_and(1,icn) < Ny - 1
# SiStER_interp_phases_to_shear_nodes.m:179
    # cell 1
    
    cell1=logical_and(shifted,quad) == 4
# SiStER_interp_phases_to_shear_nodes.m:183
    ddx=dx(1)
# SiStER_interp_phases_to_shear_nodes.m:185
    ddy=dy(ICN(cell1) - 1)
# SiStER_interp_phases_to_shear_nodes.m:186
    dxm=xm(cell1) - x(1)
# SiStER_interp_phases_to_shear_nodes.m:187
    dym=ym(cell1) - y(ICN(cell1))
# SiStER_interp_phases_to_shear_nodes.m:188
    wm1=1 - (multiply(dxm,dym) + multiply((ddx - dxm),dym) + multiply((ddy - dym),dxm)) / (multiply(ddx,ddy))
# SiStER_interp_phases_to_shear_nodes.m:189
    w1=accumarray(concat([ICN(cell1).T,ones(sum(cell1),1)]),wm1,concat([Ny,1]))
# SiStER_interp_phases_to_shear_nodes.m:190
    # cell 2
    
    cell2=logical_and(leftEdge,quad) == 1
# SiStER_interp_phases_to_shear_nodes.m:194
    ddx=dx(1)
# SiStER_interp_phases_to_shear_nodes.m:196
    ddy=dy(ICN(cell2))
# SiStER_interp_phases_to_shear_nodes.m:197
    dxm=xm(cell2) - x(1)
# SiStER_interp_phases_to_shear_nodes.m:198
    dym=ym(cell2) - y(ICN(cell2))
# SiStER_interp_phases_to_shear_nodes.m:199
    wm2=1 - (multiply(dxm,dym) + multiply((ddx - dxm),dym) + multiply((ddy - dym),dxm)) / (multiply(ddx,ddy))
# SiStER_interp_phases_to_shear_nodes.m:200
    w2=accumarray(concat([ICN(cell2).T,ones(sum(cell2),1)]),wm2,concat([Ny,1]))
# SiStER_interp_phases_to_shear_nodes.m:201
    #loop over material properties to interpolate
    
    for n in arange(1,maxPhases).reshape(-1):
        phaseMask=phases == n
# SiStER_interp_phases_to_shear_nodes.m:207
        temp=(dot(wc1,accumarray(concat([ICN(logical_and(cell1,phaseMask)).T,ones(sum(logical_and(cell1,phaseMask)),1)]),wm1(phaseMask(cell1)),concat([Ny,1]))) / w1 + dot(wc2,accumarray(concat([ICN(logical_and(cell2,phaseMask)).T,ones(sum(logical_and(cell2,phaseMask)),1)]),wm2(phaseMask(cell2)),concat([Ny,1]))) / w2) / (wc1 + wc2)
# SiStER_interp_phases_to_shear_nodes.m:209
        phasesS[arange(),1,n]=temp
# SiStER_interp_phases_to_shear_nodes.m:212
    
    ### right edge
    
    rightEdge=jcn == logical_and(Nx - 1,icn) > logical_and(1,icn) < Ny
# SiStER_interp_phases_to_shear_nodes.m:217
    shifted=jcn == logical_and(Nx - 1,icn) < Ny - 1
# SiStER_interp_phases_to_shear_nodes.m:218
    # cell 1
    
    cell1=logical_and(shifted,quad) == 3
# SiStER_interp_phases_to_shear_nodes.m:222
    ddx=dx(Nx - 1)
# SiStER_interp_phases_to_shear_nodes.m:224
    ddy=dy(ICN(cell1) - 1)
# SiStER_interp_phases_to_shear_nodes.m:225
    dxm=xm(cell1) - x(Nx - 1)
# SiStER_interp_phases_to_shear_nodes.m:226
    dym=ym(cell1) - y(ICN(cell1))
# SiStER_interp_phases_to_shear_nodes.m:227
    wm1=1 - (multiply(dxm,dym) + multiply((ddx - dxm),dym) + multiply((ddy - dym),dxm)) / (multiply(ddx,ddy))
# SiStER_interp_phases_to_shear_nodes.m:228
    w1=accumarray(concat([ICN(cell1).T,ones(sum(cell1),1)]),wm1,concat([Ny,1]))
# SiStER_interp_phases_to_shear_nodes.m:229
    # cell 2
    
    cell2=logical_and(rightEdge,quad) == 2
# SiStER_interp_phases_to_shear_nodes.m:233
    ddx=dx(Nx - 1)
# SiStER_interp_phases_to_shear_nodes.m:235
    ddy=dy(ICN(cell2))
# SiStER_interp_phases_to_shear_nodes.m:236
    dxm=xm(cell2) - x(Nx - 1)
# SiStER_interp_phases_to_shear_nodes.m:237
    dym=ym(cell2) - y(ICN(cell2))
# SiStER_interp_phases_to_shear_nodes.m:238
    wm2=1 - (multiply(dxm,dym) + multiply((ddx - dxm),dym) + multiply((ddy - dym),dxm)) / (multiply(ddx,ddy))
# SiStER_interp_phases_to_shear_nodes.m:239
    w2=accumarray(concat([ICN(cell2).T,ones(sum(cell2),1)]),wm2,concat([Ny,1]))
# SiStER_interp_phases_to_shear_nodes.m:240
    #loop over material properties to interpolate
    
    for n in arange(1,maxPhases).reshape(-1):
        phaseMask=phases == n
# SiStER_interp_phases_to_shear_nodes.m:246
        temp=(dot(wc1,accumarray(concat([ICN(logical_and(cell1,phaseMask)).T,ones(sum(logical_and(cell1,phaseMask)),1)]),wm1(phaseMask(cell1)),concat([Ny,1]))) / w1 + dot(wc2,accumarray(concat([ICN(logical_and(cell2,phaseMask)).T,ones(sum(logical_and(cell2,phaseMask)),1)]),wm2(phaseMask(cell2)),concat([Ny,1]))) / w2) / (wc1 + wc2)
# SiStER_interp_phases_to_shear_nodes.m:248
        phasesS[arange(),Nx,n]=temp
# SiStER_interp_phases_to_shear_nodes.m:251
    
    ## CORNERS
    
    # upper left
    
    upperLeft=jcn == logical_and(1,icn) == logical_and(1,quad) == 1
# SiStER_interp_phases_to_shear_nodes.m:258
    ddx=dx(1)
# SiStER_interp_phases_to_shear_nodes.m:260
    ddy=dy(1)
# SiStER_interp_phases_to_shear_nodes.m:261
    dxm=xm(upperLeft) - x(1)
# SiStER_interp_phases_to_shear_nodes.m:262
    dym=ym(upperLeft) - y(1)
# SiStER_interp_phases_to_shear_nodes.m:263
    wm=1 - (multiply(dxm,dym) + multiply((ddx - dxm),dym) + multiply((ddy - dym),dxm)) / (dot(ddx,ddy))
# SiStER_interp_phases_to_shear_nodes.m:264
    wco=sum(wm)
# SiStER_interp_phases_to_shear_nodes.m:265
    for n in arange(1,maxPhases).reshape(-1):
        phaseMask=phases == n
# SiStER_interp_phases_to_shear_nodes.m:269
        phasesS[1,1,n]=sum(wm(phaseMask(upperLeft))) / wco
# SiStER_interp_phases_to_shear_nodes.m:271
    
    # upper right
    
    upperRight=icn == logical_and(1,jcn) == logical_and(Nx - 1,quad) == 2
# SiStER_interp_phases_to_shear_nodes.m:276
    ddx=dx(Nx - 1)
# SiStER_interp_phases_to_shear_nodes.m:278
    ddy=dy(1)
# SiStER_interp_phases_to_shear_nodes.m:279
    dxm=xm(upperRight) - x(Nx - 1)
# SiStER_interp_phases_to_shear_nodes.m:280
    dym=ym(upperRight) - y(1)
# SiStER_interp_phases_to_shear_nodes.m:281
    wm=1 - (multiply(dxm,dym) + multiply((ddx - dxm),dym) + multiply((ddy - dym),dxm)) / (dot(ddx,ddy))
# SiStER_interp_phases_to_shear_nodes.m:282
    wco=sum(wm)
# SiStER_interp_phases_to_shear_nodes.m:283
    for n in arange(1,maxPhases).reshape(-1):
        phaseMask=phases == n
# SiStER_interp_phases_to_shear_nodes.m:287
        phasesS[1,Nx,n]=sum(wm(phaseMask(upperRight))) / wco
# SiStER_interp_phases_to_shear_nodes.m:289
    
    # lower Right
    
    lowerRight=icn == logical_and(Ny - 1,jcn) == logical_and(Nx - 1,quad) == 3
# SiStER_interp_phases_to_shear_nodes.m:294
    ddx=dx(Nx - 1)
# SiStER_interp_phases_to_shear_nodes.m:296
    ddy=dy(Ny - 1)
# SiStER_interp_phases_to_shear_nodes.m:297
    dxm=xm(lowerRight) - x(Nx - 1)
# SiStER_interp_phases_to_shear_nodes.m:298
    dym=ym(lowerRight) - y(Ny - 1)
# SiStER_interp_phases_to_shear_nodes.m:299
    wm=1 - (multiply(dxm,dym) + multiply((ddx - dxm),dym) + multiply((ddy - dym),dxm)) / (dot(ddx,ddy))
# SiStER_interp_phases_to_shear_nodes.m:300
    wco=sum(wm)
# SiStER_interp_phases_to_shear_nodes.m:301
    for n in arange(1,maxPhases).reshape(-1):
        phaseMask=phases == n
# SiStER_interp_phases_to_shear_nodes.m:305
        phasesS[Ny,Nx,n]=sum(wm(phaseMask(lowerRight))) / wco
# SiStER_interp_phases_to_shear_nodes.m:307
    
    # lower left
    
    lowerLeft=icn == logical_and(Ny - 1,jcn) == logical_and(1,quad) == 4
# SiStER_interp_phases_to_shear_nodes.m:312
    ddx=dx(1)
# SiStER_interp_phases_to_shear_nodes.m:314
    ddy=dy(Ny - 1)
# SiStER_interp_phases_to_shear_nodes.m:315
    dxm=xm(lowerLeft) - x(1)
# SiStER_interp_phases_to_shear_nodes.m:316
    dym=ym(lowerLeft) - y(Ny - 1)
# SiStER_interp_phases_to_shear_nodes.m:317
    wm=1 - (multiply(dxm,dym) + multiply((ddx - dxm),dym) + multiply((ddy - dym),dxm)) / (dot(ddx,ddy))
# SiStER_interp_phases_to_shear_nodes.m:318
    wco=sum(wm)
# SiStER_interp_phases_to_shear_nodes.m:319
    for n in arange(1,maxPhases).reshape(-1):
        phaseMask=phases == n
# SiStER_interp_phases_to_shear_nodes.m:323
        phasesS[Ny,1,n]=sum(wm(phaseMask(lowerLeft))) / wco
# SiStER_interp_phases_to_shear_nodes.m:325
    