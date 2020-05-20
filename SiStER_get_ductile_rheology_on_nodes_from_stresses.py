# Generated with SMOP  0.41
from libsmop import *
# SiStER_get_ductile_rheology_on_nodes_from_stresses.m

    
@function
def SiStER_get_ductile_rheology_on_nodes_from_stresses(MAT=None,PARAMS=None,T=None,sII=None,phase_node=None,*args,**kwargs):
    varargin = SiStER_get_ductile_rheology_on_nodes_from_stresses.varargin
    nargin = SiStER_get_ductile_rheology_on_nodes_from_stresses.nargin

    # [eta]=SiStER_get_ductile_rheology_on_nodes_from_stresses(MAT,PARAMS,T,sII,phase_node)
# computes ductile rheology given phase numbers around a node or cell 
# (phase_node is either phase_n or phase_s)
    
    # G.Ito 8/2016 # JAO 9/2016 fixed parentheses in exp(Ea/(nRT))
# B.Z. Klein 07/17: can now handle nodes surrounded by any number of phases
# that are NOT consecutively numbered (now looping through all phases)
# thanks to new phase interp functions.
# written by J.A. Olive based on BZ Klein's
# get_ductile_rheology_on_nodes_from_strain_rate.m function (Nov. 2017)
#-------------------------------------------------------------------------
    
    pre_diff=permute(repmat(concat([MAT.pre_diff]).T,concat([1,size(T)])),concat([2,3,1]))
# SiStER_get_ductile_rheology_on_nodes_from_stresses.m:14
    ndiff=permute(repmat(concat([MAT.ndiff]).T,concat([1,size(T)])),concat([2,3,1]))
# SiStER_get_ductile_rheology_on_nodes_from_stresses.m:15
    Ediff=permute(repmat(concat([MAT.Ediff]).T,concat([1,size(T)])),concat([2,3,1]))
# SiStER_get_ductile_rheology_on_nodes_from_stresses.m:16
    pre_disc=permute(repmat(concat([MAT.pre_disc]).T,concat([1,size(T)])),concat([2,3,1]))
# SiStER_get_ductile_rheology_on_nodes_from_stresses.m:17
    ndisc=permute(repmat(concat([MAT.ndisc]).T,concat([1,size(T)])),concat([2,3,1]))
# SiStER_get_ductile_rheology_on_nodes_from_stresses.m:18
    Edisc=permute(repmat(concat([MAT.Edisc]).T,concat([1,size(T)])),concat([2,3,1]))
# SiStER_get_ductile_rheology_on_nodes_from_stresses.m:19
    sII[sII == 0]=0.001
# SiStER_get_ductile_rheology_on_nodes_from_stresses.m:21
    
    sII=repmat(sII,concat([1,1,PARAMS.Nphase]))
# SiStER_get_ductile_rheology_on_nodes_from_stresses.m:23
    T=repmat(T,concat([1,1,PARAMS.Nphase]))
# SiStER_get_ductile_rheology_on_nodes_from_stresses.m:24
    # TO BE REPLACED BY SiStER_flow_law_function SOON
#eta_diff=pre_diff.^(-1).*sII.^(1-ndiff).*...
#         exp(Ediff./(PARAMS.R.*(T+273.15)));
#eta_disc=pre_disc.^(-1).*sII.^(1-ndisc).*...
#          exp(Edisc./(PARAMS.R.*(T+273.15)));
    
    eta_diff=SiStER_flow_law_function('from_stress',pre_diff,Ediff,ndiff,PARAMS.R,T,zeros(size(sII)),sII,PARAMS)
# SiStER_get_ductile_rheology_on_nodes_from_stresses.m:32
    eta_disc=SiStER_flow_law_function('from_stress',pre_disc,Edisc,ndisc,PARAMS.R,T,zeros(size(sII)),sII,PARAMS)
# SiStER_get_ductile_rheology_on_nodes_from_stresses.m:33
    # linearly average between viscosity of each phase type
    eta_diffAVG=sum(multiply(eta_diff,phase_node),3)
# SiStER_get_ductile_rheology_on_nodes_from_stresses.m:37
    eta_discAVG=sum(multiply(eta_disc,phase_node),3)
# SiStER_get_ductile_rheology_on_nodes_from_stresses.m:38
    eta=(1.0 / eta_diffAVG + 1.0 / eta_discAVG) ** - 1
# SiStER_get_ductile_rheology_on_nodes_from_stresses.m:40
    eta[eta < PARAMS.etamin]=PARAMS.etamin
# SiStER_get_ductile_rheology_on_nodes_from_stresses.m:41
    return eta