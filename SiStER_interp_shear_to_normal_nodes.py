# Generated with SMOP  0.41
from libsmop import *
# SiStER_interp_shear_to_normal_nodes.m

    #==============================================================
    
@function
def SiStER_interp_shear_to_normal_nodes(varS=None,*args,**kwargs):
    varargin = SiStER_interp_shear_to_normal_nodes.varargin
    nargin = SiStER_interp_shear_to_normal_nodes.nargin

    # 
# G.Ito 8/2016
#===============================================================
    
    varN=zeros(size(varS))
# SiStER_interp_shear_to_normal_nodes.m:7
    varN[arange(2,end()),arange(2,end())]=(varS(arange(1,end() - 1),arange(1,end() - 1)) + varS(arange(2,end()),arange(1,end() - 1)) + varS(arange(1,end() - 1),arange(2,end())) + varS(arange(2,end()),arange(2,end()))) / 4
# SiStER_interp_shear_to_normal_nodes.m:8
    return varN