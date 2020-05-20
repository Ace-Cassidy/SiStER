# Generated with SMOP  0.41
from libsmop import *
# SiStER_interp_markers_to_shear_nodes.m

    
@function
def SiStER_interp_markers_to_shear_nodes(xm=None,ym=None,icn=None,jcn=None,quad=None,x=None,y=None,varargin=None,*args,**kwargs):
    varargin = SiStER_interp_markers_to_shear_nodes.varargin
    nargin = SiStER_interp_markers_to_shear_nodes.nargin

    # [n2interp] = SiStER_interp_markers_to_shear_nodes(xm,ym,icn,jcn,quad,x,y,varargin)
# interpolates marker properties to shear nodes
# First cut - J.A. Olive, March 2011
# Modified by E. Mittelstaedt, April 2011, to allow variable inputs.  
# Modified by B.Z. Klein, Spring 2014, for speedup
# Modified by B.Z. Klein, Summer 2014, for further speedup (vectorized)
    
    Nx=length(x)
# SiStER_interp_markers_to_shear_nodes.m:10
    Ny=length(y)
# SiStER_interp_markers_to_shear_nodes.m:11
    dx=diff(x)
# SiStER_interp_markers_to_shear_nodes.m:12
    dy=diff(y)
# SiStER_interp_markers_to_shear_nodes.m:13
    # MITTELSTAEDT - check for number of properties to interpolate
    numV=size(varargin,2)
# SiStER_interp_markers_to_shear_nodes.m:16
    # MITTELSTAEDT # establish interpolants matrices
    n2interp=repmat(struct('data',zeros(Ny,Nx)),1,numV)
# SiStER_interp_markers_to_shear_nodes.m:20
    JCN=interp1(x,arange(1,length(x)),xm,'nearest','extrap')
# SiStER_interp_markers_to_shear_nodes.m:22
    
    ICN=interp1(y,arange(1,length(y)),ym,'nearest','extrap')
# SiStER_interp_markers_to_shear_nodes.m:23
    
    ## Interior Cells
    
    center=jcn > logical_and(1,jcn) < logical_and(Nx,icn) > logical_and(1,icn) < Ny
# SiStER_interp_markers_to_shear_nodes.m:28
    shiftLeft=jcn < logical_and(Nx - 1,icn) > logical_and(1,icn) < Ny
# SiStER_interp_markers_to_shear_nodes.m:29
    shiftUp=jcn > logical_and(1,jcn) < logical_and(Nx,icn) < Ny - 1
# SiStER_interp_markers_to_shear_nodes.m:30
    shiftBoth=jcn < logical_and(Nx - 1,icn) < Ny - 1
# SiStER_interp_markers_to_shear_nodes.m:31
    cell1=logical_and(logical_and(center,((xm - x(JCN)) > 0)),((ym - y(ICN)) > 0))
# SiStER_interp_markers_to_shear_nodes.m:34
    
    cell2=logical_and(logical_and(shiftLeft,((xm - x(JCN)) < 0)),((ym - y(ICN)) > 0))
# SiStER_interp_markers_to_shear_nodes.m:35
    cell3=logical_and(logical_and(shiftBoth,((xm - x(JCN)) < 0)),((ym - y(ICN)) < 0))
# SiStER_interp_markers_to_shear_nodes.m:36
    cell4=logical_and(logical_and(shiftUp,((xm - x(JCN)) > 0)),((ym - y(ICN)) < 0))
# SiStER_interp_markers_to_shear_nodes.m:37
    ### WEIGHTING (equal for now because that is what I'm running)
    
    wc1=0.25
# SiStER_interp_markers_to_shear_nodes.m:41
    wc2=0.25
# SiStER_interp_markers_to_shear_nodes.m:42
    wc3=0.25
# SiStER_interp_markers_to_shear_nodes.m:43
    wc4=0.25
# SiStER_interp_markers_to_shear_nodes.m:44
    # cell 1 (i,j,1)
    
    dxm=xm(cell1) - x(JCN(cell1))
# SiStER_interp_markers_to_shear_nodes.m:49
    dym=ym(cell1) - y(ICN(cell1))
# SiStER_interp_markers_to_shear_nodes.m:50
    ddx=dx(JCN(cell1))
# SiStER_interp_markers_to_shear_nodes.m:51
    ddy=dy(ICN(cell1))
# SiStER_interp_markers_to_shear_nodes.m:52
    wm1=1 - (multiply(dxm,dym) + multiply((ddx - dxm),dym) + multiply((ddy - dym),dxm)) / (multiply(ddx,ddy))
# SiStER_interp_markers_to_shear_nodes.m:54
    w1=accumarray(concat([ICN(cell1).T,JCN(cell1).T]),wm1)
# SiStER_interp_markers_to_shear_nodes.m:55
    # cell 2 (i, j-1, 2)
    
    dxm=xm(cell2) - x(JCN(cell2))
# SiStER_interp_markers_to_shear_nodes.m:59
    dym=ym(cell2) - y(ICN(cell2))
# SiStER_interp_markers_to_shear_nodes.m:60
    ddx=dx(JCN(cell2) - 1)
# SiStER_interp_markers_to_shear_nodes.m:61
    ddy=dy(ICN(cell2))
# SiStER_interp_markers_to_shear_nodes.m:62
    wm2=1 - (multiply(dxm,dym) + multiply((ddx - dxm),dym) + multiply((ddy - dym),dxm)) / (multiply(ddx,ddy))
# SiStER_interp_markers_to_shear_nodes.m:64
    w2=accumarray(concat([ICN(cell2).T,JCN(cell2).T]),wm2)
# SiStER_interp_markers_to_shear_nodes.m:65
    # cell 3 (i-1, j-1, 3)
    
    dxm=xm(cell3) - x(JCN(cell3))
# SiStER_interp_markers_to_shear_nodes.m:69
    dym=ym(cell3) - y(ICN(cell3))
# SiStER_interp_markers_to_shear_nodes.m:70
    ddx=dx(JCN(cell3) - 1)
# SiStER_interp_markers_to_shear_nodes.m:71
    ddy=dy(ICN(cell3) - 1)
# SiStER_interp_markers_to_shear_nodes.m:72
    wm3=1 - (multiply(dxm,dym) + multiply((ddx - dxm),dym) + multiply((ddy - dym),dxm)) / (multiply(ddx,ddy))
# SiStER_interp_markers_to_shear_nodes.m:74
    w3=accumarray(concat([ICN(cell3).T,JCN(cell3).T]),wm3)
# SiStER_interp_markers_to_shear_nodes.m:75
    # cell 4 (i-1, j, 4)
    
    dxm=xm(cell4) - x(JCN(cell4))
# SiStER_interp_markers_to_shear_nodes.m:79
    dym=ym(cell4) - y(ICN(cell4))
# SiStER_interp_markers_to_shear_nodes.m:80
    ddx=dx(JCN(cell4))
# SiStER_interp_markers_to_shear_nodes.m:81
    ddy=dy(ICN(cell4) - 1)
# SiStER_interp_markers_to_shear_nodes.m:82
    wm4=1 - (multiply(dxm,dym) + multiply((ddx - dxm),dym) + multiply((ddy - dym),dxm)) / (multiply(ddx,ddy))
# SiStER_interp_markers_to_shear_nodes.m:84
    w4=accumarray(concat([ICN(cell4).T,JCN(cell4).T]),wm4)
# SiStER_interp_markers_to_shear_nodes.m:85
    #loop over material properties to interpolate
    
    for vn in arange(1,numV).reshape(-1):
        n2interp(vn).data = copy((dot(wc1,accumarray(concat([ICN(cell1).T,JCN(cell1).T]),multiply(varargin[vn](cell1),wm1))) / w1 + dot(wc2,accumarray(concat([ICN(cell2).T,JCN(cell2).T]),multiply(varargin[vn](cell2),wm2))) / w2 + dot(wc3,accumarray(concat([ICN(cell3).T,JCN(cell3).T]),multiply(varargin[vn](cell3),wm3))) / w3 + dot(wc4,accumarray(concat([ICN(cell4).T,JCN(cell4).T]),multiply(varargin[vn](cell4),wm4))) / w4) / (wc1 + wc2 + wc4 + wc4))
# SiStER_interp_markers_to_shear_nodes.m:90
    
    ## EDGES
    
    ### top edge
    
    topEdge=jcn > logical_and(1,jcn) < logical_and(Nx,icn) == 1
# SiStER_interp_markers_to_shear_nodes.m:103
    shifted=jcn < logical_and(Nx - 1,icn) == 1
# SiStER_interp_markers_to_shear_nodes.m:104
    # cell 1
    
    cell1=logical_and(shifted,quad) == 2
# SiStER_interp_markers_to_shear_nodes.m:108
    ddx=dx(JCN(cell1) - 1)
# SiStER_interp_markers_to_shear_nodes.m:110
    ddy=dy(1)
# SiStER_interp_markers_to_shear_nodes.m:111
    dxm=xm(cell1) - x(JCN(cell1))
# SiStER_interp_markers_to_shear_nodes.m:112
    dym=ym(cell1) - y(ICN(cell1))
# SiStER_interp_markers_to_shear_nodes.m:113
    wm1=1 - (multiply(dxm,dym) + multiply((ddx - dxm),dym) + multiply((ddy - dym),dxm)) / (multiply(ddx,ddy))
# SiStER_interp_markers_to_shear_nodes.m:114
    w1=accumarray(concat([ICN(cell1).T,JCN(cell1).T]),wm1)
# SiStER_interp_markers_to_shear_nodes.m:115
    # cell 2
    
    cell2=logical_and(topEdge,quad) == 1
# SiStER_interp_markers_to_shear_nodes.m:119
    ddx=dx(JCN(cell2))
# SiStER_interp_markers_to_shear_nodes.m:121
    ddy=dy(1)
# SiStER_interp_markers_to_shear_nodes.m:122
    dxm=xm(cell2) - x(JCN(cell2))
# SiStER_interp_markers_to_shear_nodes.m:123
    dym=ym(cell2) - y(ICN(cell2))
# SiStER_interp_markers_to_shear_nodes.m:124
    wm2=1 - (multiply(dxm,dym) + multiply((ddx - dxm),dym) + multiply((ddy - dym),dxm)) / (multiply(ddx,ddy))
# SiStER_interp_markers_to_shear_nodes.m:125
    w2=accumarray(concat([ICN(cell2).T,JCN(cell2).T]),wm2)
# SiStER_interp_markers_to_shear_nodes.m:126
    #loop over material properties to interpolate
    
    for vn in arange(1,numV).reshape(-1):
        temp=(dot(wc1,accumarray(concat([ICN(cell1).T,JCN(cell1).T]),multiply(varargin[vn](cell1),wm1))) / w1 + dot(wc2,accumarray(concat([ICN(cell2).T,JCN(cell2).T]),multiply(varargin[vn](cell2),wm2))) / w2) / (wc1 + wc2)
# SiStER_interp_markers_to_shear_nodes.m:131
        n2interp(vn).data[1,arange(2,end())]=temp(arange(2,end()))
# SiStER_interp_markers_to_shear_nodes.m:134
    
    clear('w1','w2')
    ### bottom edge
    
    bottomEdge=jcn > logical_and(1,jcn) < logical_and(Nx,icn) == Ny - 1
# SiStER_interp_markers_to_shear_nodes.m:141
    shifted=jcn < logical_and(Nx - 1,icn) == Ny - 1
# SiStER_interp_markers_to_shear_nodes.m:142
    # cell 1
    
    cell1=logical_and(shifted,quad) == 3
# SiStER_interp_markers_to_shear_nodes.m:146
    ddx=dx(JCN(cell1) - 1)
# SiStER_interp_markers_to_shear_nodes.m:148
    ddy=dy(Ny - 1)
# SiStER_interp_markers_to_shear_nodes.m:149
    dxm=xm(cell1) - x(JCN(cell1))
# SiStER_interp_markers_to_shear_nodes.m:150
    dym=ym(cell1) - y(end() - 1)
# SiStER_interp_markers_to_shear_nodes.m:151
    wm1=1 - (multiply(dxm,dym) + multiply((ddx - dxm),dym) + multiply((ddy - dym),dxm)) / (multiply(ddx,ddy))
# SiStER_interp_markers_to_shear_nodes.m:152
    w1=accumarray(concat([ones(sum(cell1),1),JCN(cell1).T]),wm1)
# SiStER_interp_markers_to_shear_nodes.m:153
    # cell 2
    
    cell2=logical_and(bottomEdge,quad) == 4
# SiStER_interp_markers_to_shear_nodes.m:157
    ddx=dx(JCN(cell2))
# SiStER_interp_markers_to_shear_nodes.m:159
    ddy=dy(Ny - 1)
# SiStER_interp_markers_to_shear_nodes.m:160
    dxm=xm(cell2) - x(JCN(cell2))
# SiStER_interp_markers_to_shear_nodes.m:161
    dym=ym(cell2) - y(end() - 1)
# SiStER_interp_markers_to_shear_nodes.m:162
    wm2=1 - (multiply(dxm,dym) + multiply((ddx - dxm),dym) + multiply((ddy - dym),dxm)) / (multiply(ddx,ddy))
# SiStER_interp_markers_to_shear_nodes.m:163
    w2=accumarray(concat([ones(sum(cell2),1),JCN(cell2).T]),wm2)
# SiStER_interp_markers_to_shear_nodes.m:164
    #loop over material properties to interpolate
    
    for vn in arange(1,numV).reshape(-1):
        temp=(dot(wc1,accumarray(concat([ones(sum(cell1),1),JCN(cell1).T]),multiply(varargin[vn](cell1),wm1))) / w1 + dot(wc2,accumarray(concat([ones(sum(cell2),1),JCN(cell2).T]),multiply(varargin[vn](cell2),wm2))) / w2) / (wc1 + wc2)
# SiStER_interp_markers_to_shear_nodes.m:169
        n2interp(vn).data[Ny,arange(2,end())]=temp(arange(2,end()))
# SiStER_interp_markers_to_shear_nodes.m:172
    
    ### left edge
    
    leftEdge=jcn == logical_and(1,icn) > logical_and(1,icn) < Ny
# SiStER_interp_markers_to_shear_nodes.m:177
    shifted=jcn == logical_and(1,icn) < Ny - 1
# SiStER_interp_markers_to_shear_nodes.m:178
    # cell 1
    
    cell1=logical_and(shifted,quad) == 4
# SiStER_interp_markers_to_shear_nodes.m:182
    ddx=dx(1)
# SiStER_interp_markers_to_shear_nodes.m:184
    ddy=dy(ICN(cell1) - 1)
# SiStER_interp_markers_to_shear_nodes.m:185
    dxm=xm(cell1) - x(1)
# SiStER_interp_markers_to_shear_nodes.m:186
    dym=ym(cell1) - y(ICN(cell1))
# SiStER_interp_markers_to_shear_nodes.m:187
    wm1=1 - (multiply(dxm,dym) + multiply((ddx - dxm),dym) + multiply((ddy - dym),dxm)) / (multiply(ddx,ddy))
# SiStER_interp_markers_to_shear_nodes.m:188
    w1=accumarray(concat([ICN(cell1).T,ones(sum(cell1),1)]),wm1)
# SiStER_interp_markers_to_shear_nodes.m:189
    # cell 2
    
    cell2=logical_and(leftEdge,quad) == 1
# SiStER_interp_markers_to_shear_nodes.m:193
    ddx=dx(1)
# SiStER_interp_markers_to_shear_nodes.m:195
    ddy=dy(ICN(cell2))
# SiStER_interp_markers_to_shear_nodes.m:196
    dxm=xm(cell2) - x(1)
# SiStER_interp_markers_to_shear_nodes.m:197
    dym=ym(cell2) - y(ICN(cell2))
# SiStER_interp_markers_to_shear_nodes.m:198
    wm2=1 - (multiply(dxm,dym) + multiply((ddx - dxm),dym) + multiply((ddy - dym),dxm)) / (multiply(ddx,ddy))
# SiStER_interp_markers_to_shear_nodes.m:199
    w2=accumarray(concat([ICN(cell2).T,ones(sum(cell2),1)]),wm2)
# SiStER_interp_markers_to_shear_nodes.m:200
    #loop over material properties to interpolate
    
    for vn in arange(1,numV).reshape(-1):
        temp=(dot(wc1,accumarray(concat([ICN(cell1).T,ones(sum(cell1),1)]),multiply(varargin[vn](cell1),wm1))) / w1 + dot(wc2,accumarray(concat([ICN(cell2).T,ones(sum(cell2),1)]),multiply(varargin[vn](cell2),wm2))) / w2) / (wc1 + wc2)
# SiStER_interp_markers_to_shear_nodes.m:205
        n2interp(vn).data[arange(2,end() - 1),1]=temp(arange(2,end()))
# SiStER_interp_markers_to_shear_nodes.m:208
    
    ### right edge
    
    rightEdge=jcn == logical_and(Nx - 1,icn) > logical_and(1,icn) < Ny
# SiStER_interp_markers_to_shear_nodes.m:213
    shifted=jcn == logical_and(Nx - 1,icn) < Ny - 1
# SiStER_interp_markers_to_shear_nodes.m:214
    # cell 1
    
    cell1=logical_and(shifted,quad) == 3
# SiStER_interp_markers_to_shear_nodes.m:218
    ddx=dx(Nx - 1)
# SiStER_interp_markers_to_shear_nodes.m:220
    ddy=dy(ICN(cell1) - 1)
# SiStER_interp_markers_to_shear_nodes.m:221
    dxm=xm(cell1) - x(Nx - 1)
# SiStER_interp_markers_to_shear_nodes.m:222
    dym=ym(cell1) - y(ICN(cell1))
# SiStER_interp_markers_to_shear_nodes.m:223
    wm1=1 - (multiply(dxm,dym) + multiply((ddx - dxm),dym) + multiply((ddy - dym),dxm)) / (multiply(ddx,ddy))
# SiStER_interp_markers_to_shear_nodes.m:224
    w1=accumarray(concat([ICN(cell1).T,ones(sum(cell1),1)]),wm1)
# SiStER_interp_markers_to_shear_nodes.m:225
    # cell 2
    
    cell2=logical_and(rightEdge,quad) == 2
# SiStER_interp_markers_to_shear_nodes.m:229
    ddx=dx(Nx - 1)
# SiStER_interp_markers_to_shear_nodes.m:231
    ddy=dy(ICN(cell2))
# SiStER_interp_markers_to_shear_nodes.m:232
    dxm=xm(cell2) - x(Nx - 1)
# SiStER_interp_markers_to_shear_nodes.m:233
    dym=ym(cell2) - y(ICN(cell2))
# SiStER_interp_markers_to_shear_nodes.m:234
    wm2=1 - (multiply(dxm,dym) + multiply((ddx - dxm),dym) + multiply((ddy - dym),dxm)) / (multiply(ddx,ddy))
# SiStER_interp_markers_to_shear_nodes.m:235
    w2=accumarray(concat([ICN(cell2).T,ones(sum(cell2),1)]),wm2)
# SiStER_interp_markers_to_shear_nodes.m:236
    #loop over material properties to interpolate
    
    for vn in arange(1,numV).reshape(-1):
        temp=(dot(wc1,accumarray(concat([ICN(cell1).T,ones(sum(cell1),1)]),multiply(varargin[vn](cell1),wm1))) / w1 + dot(wc2,accumarray(concat([ICN(cell2).T,ones(sum(cell2),1)]),multiply(varargin[vn](cell2),wm2))) / w2) / (wc1 + wc2)
# SiStER_interp_markers_to_shear_nodes.m:241
        n2interp(vn).data[arange(2,end() - 1),Nx]=temp(arange(2,end()))
# SiStER_interp_markers_to_shear_nodes.m:244
    
    ## CORNERS
    
    # upper left
    
    upperLeft=jcn == logical_and(1,icn) == logical_and(1,quad) == 1
# SiStER_interp_markers_to_shear_nodes.m:251
    ddx=dx(1)
# SiStER_interp_markers_to_shear_nodes.m:253
    ddy=dy(1)
# SiStER_interp_markers_to_shear_nodes.m:254
    dxm=xm(upperLeft) - x(1)
# SiStER_interp_markers_to_shear_nodes.m:255
    dym=ym(upperLeft) - y(1)
# SiStER_interp_markers_to_shear_nodes.m:256
    wm=1 - (multiply(dxm,dym) + multiply((ddx - dxm),dym) + multiply((ddy - dym),dxm)) / (dot(ddx,ddy))
# SiStER_interp_markers_to_shear_nodes.m:257
    wco=sum(wm)
# SiStER_interp_markers_to_shear_nodes.m:258
    for vn in arange(1,numV).reshape(-1):
        n2interp(vn).data[1,1]=sum(multiply(varargin[vn](upperLeft),wm)) / wco
# SiStER_interp_markers_to_shear_nodes.m:261
    
    # upper right
    
    upperRight=icn == logical_and(1,jcn) == logical_and(Nx - 1,quad) == 2
# SiStER_interp_markers_to_shear_nodes.m:266
    ddx=dx(Nx - 1)
# SiStER_interp_markers_to_shear_nodes.m:268
    ddy=dy(1)
# SiStER_interp_markers_to_shear_nodes.m:269
    dxm=xm(upperRight) - x(Nx - 1)
# SiStER_interp_markers_to_shear_nodes.m:270
    dym=ym(upperRight) - y(1)
# SiStER_interp_markers_to_shear_nodes.m:271
    wm=1 - (multiply(dxm,dym) + multiply((ddx - dxm),dym) + multiply((ddy - dym),dxm)) / (dot(ddx,ddy))
# SiStER_interp_markers_to_shear_nodes.m:272
    wco=sum(wm)
# SiStER_interp_markers_to_shear_nodes.m:273
    for vn in arange(1,numV).reshape(-1):
        n2interp(vn).data[1,Nx]=sum(multiply(varargin[vn](upperRight),wm)) / wco
# SiStER_interp_markers_to_shear_nodes.m:276
    
    # lower Right
    
    lowerRight=icn == logical_and(Ny - 1,jcn) == logical_and(Nx - 1,quad) == 3
# SiStER_interp_markers_to_shear_nodes.m:281
    ddx=dx(Nx - 1)
# SiStER_interp_markers_to_shear_nodes.m:283
    ddy=dy(Ny - 1)
# SiStER_interp_markers_to_shear_nodes.m:284
    dxm=xm(lowerRight) - x(Nx - 1)
# SiStER_interp_markers_to_shear_nodes.m:285
    dym=ym(lowerRight) - y(Ny - 1)
# SiStER_interp_markers_to_shear_nodes.m:286
    wm=1 - (multiply(dxm,dym) + multiply((ddx - dxm),dym) + multiply((ddy - dym),dxm)) / (dot(ddx,ddy))
# SiStER_interp_markers_to_shear_nodes.m:287
    wco=sum(wm)
# SiStER_interp_markers_to_shear_nodes.m:288
    for vn in arange(1,numV).reshape(-1):
        n2interp(vn).data[Ny,Nx]=sum(multiply(varargin[vn](lowerRight),wm)) / wco
# SiStER_interp_markers_to_shear_nodes.m:291
    
    # lower left
    
    lowerLeft=icn == logical_and(Ny - 1,jcn) == logical_and(1,quad) == 4
# SiStER_interp_markers_to_shear_nodes.m:296
    ddx=dx(1)
# SiStER_interp_markers_to_shear_nodes.m:298
    ddy=dy(Ny - 1)
# SiStER_interp_markers_to_shear_nodes.m:299
    dxm=xm(lowerLeft) - x(1)
# SiStER_interp_markers_to_shear_nodes.m:300
    dym=ym(lowerLeft) - y(Ny - 1)
# SiStER_interp_markers_to_shear_nodes.m:301
    wm=1 - (multiply(dxm,dym) + multiply((ddx - dxm),dym) + multiply((ddy - dym),dxm)) / (dot(ddx,ddy))
# SiStER_interp_markers_to_shear_nodes.m:302
    wco=sum(wm)
# SiStER_interp_markers_to_shear_nodes.m:303
    for vn in arange(1,numV).reshape(-1):
        n2interp(vn).data[Ny,1]=sum(multiply(varargin[vn](lowerLeft),wm)) / wco
# SiStER_interp_markers_to_shear_nodes.m:306
    