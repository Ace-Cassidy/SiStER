# Generated with SMOP  0.41
from libsmop import *
# SiStER_initialize_grid.m

    
@function
def SiStER_initialize_grid(xsize=None,ysize=None,GRID=None,*args,**kwargs):
    varargin = SiStER_initialize_grid.varargin
    nargin = SiStER_initialize_grid.nargin

    # [X,Y,x,y,xc,yc,dx,dy,Nx,Ny] = SiStER_initialize_grid(xsize,ysize,GRID)
# sets up the staggered grid coordinates
    
    ## Coded for both regular and variable grid spacing G.Ito 7/15
    
    #GRID.x defines the points in x within which grid spacing can differ
#for x<=GRID.x(1), the APPROXIMATE grid spacing is GRID.dx(1); 
#for GRID.x(1) < x <= GRID.x(2), the approx. spacing is GRID.dx(2);
#for GRID.x(end-1) < x <= xsize, the approx. spacing is GRID.dx(end);
    
    #Thus GRID.dx MUST be longer than GRID.x by 1 entry.
#GRID.x=[0] and GRID.dx=[0.5 1]*1e3 will sent a UNIFORM spacing of 1000m
#The grid is defined in SiStER_initialize_grid_GI.  This is also 
#where Nx will be defined.
    
    #To ensure an EXACT grid spacing, be sure GRID.dx fits as an integer number
#of times in each grid interval GRID.x
    
    ## The same logic is used for y.
    
    x=0
# SiStER_initialize_grid.m:23
    y=0
# SiStER_initialize_grid.m:24
    for i in arange(1,length(GRID.x)).reshape(-1):
        n=round((GRID.x(i) - x(end())) / GRID.dx(i))
# SiStER_initialize_grid.m:26
        dd=(GRID.x(i) - x(end())) / n
# SiStER_initialize_grid.m:27
        x=concat([x,x(end()) + multiply((arange(1,n)),dd)])
# SiStER_initialize_grid.m:28
    
    n=round((xsize - x(end())) / GRID.dx(end()))
# SiStER_initialize_grid.m:30
    dd=(xsize - x(end())) / n
# SiStER_initialize_grid.m:31
    x=concat([x,x(end()) + multiply((arange(1,n)),dd)])
# SiStER_initialize_grid.m:32
    for i in arange(1,length(GRID.y)).reshape(-1):
        n=round((GRID.y(i) - y(end())) / GRID.dy(i))
# SiStER_initialize_grid.m:35
        dd=(GRID.y(i) - y(end())) / n
# SiStER_initialize_grid.m:36
        y=concat([y,y(end()) + multiply((arange(1,n)),dd)])
# SiStER_initialize_grid.m:37
    
    n=round((ysize - y(end())) / GRID.dy(end()))
# SiStER_initialize_grid.m:39
    dd=(ysize - y(end())) / n
# SiStER_initialize_grid.m:40
    y=concat([y,y(end()) + multiply((arange(1,n)),dd)])
# SiStER_initialize_grid.m:41
    Nx=length(x)
# SiStER_initialize_grid.m:43
    Ny=length(y)
# SiStER_initialize_grid.m:44
    
    # 2D Grid
    X,Y=meshgrid(x,y,nargout=2)
# SiStER_initialize_grid.m:47
    # create vectors of grid spacing
    dx=diff(x)
# SiStER_initialize_grid.m:50
    dy=diff(y)
# SiStER_initialize_grid.m:51
    # Create vectors for cell centers positions (staggered nodes)
    xc=dot(0.5,(x(arange(2,Nx)) + x(arange(1,Nx - 1))))
# SiStER_initialize_grid.m:54
    yc=dot(0.5,(y(arange(2,Ny)) + y(arange(1,Ny - 1))))
# SiStER_initialize_grid.m:55
    disp(concat(['** Nx = ',num2str(Nx),' Ny = ',num2str(Ny),' ***']))