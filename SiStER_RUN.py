# Generated with SMOP  0.41
from libsmop import *
# SiStER_RUN.m

    
@function
def SiStER_RUN(InpFil=None,*args,**kwargs):
    varargin = SiStER_RUN.varargin
    nargin = SiStER_RUN.nargin

    keepvars=cellarray(['InpFil'])
# SiStER_RUN.m:3
    clearvars('-except',keepvars[arange()])
    running_from_SiStER_RUN=1
# SiStER_RUN.m:5
    SiStER_MAIN
    return
    
if __name__ == '__main__':
    pass
    