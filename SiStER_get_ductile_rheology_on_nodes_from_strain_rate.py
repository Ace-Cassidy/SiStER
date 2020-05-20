# Generated with SMOP  0.41
from libsmop import *
# SiStER_get_ductile_rheology_on_nodes_from_strain_rate.m

    
@function
def SiStER_get_ductile_rheology_on_nodes_from_strain_rate(MAT=None,PARAMS=None,T=None,epsII=None,phase_node=None,*args,**kwargs):
    varargin = SiStER_get_ductile_rheology_on_nodes_from_strain_rate.varargin
    nargin = SiStER_get_ductile_rheology_on_nodes_from_strain_rate.nargin

    # [eta]=SiStER_get_ductile_rheology_on_nodes_from_strain_rate(MAT,PARAMS,T,epsII,phase_node)
# computes ductile rheology given phase numbers around a node or cell 
# (phase_node is either phase_n or phase_s)
    
    # G.Ito 8/2016 # JAO 9/2016 fixed parentheses in exp(Ea/(nRT))
# B.Z. Klein 07/17: can now handle nodes surrounded by any number of phases
# that are NOT consecutively numbered (now looping through all phases)
# thanks to new phase interp functions.
    
    pre_diff=permute(repmat(concat([MAT.pre_diff]).T,concat([1,size(T)])),concat([2,3,1]))
# SiStER_get_ductile_rheology_on_nodes_from_strain_rate.m:11
    ndiff=permute(repmat(concat([MAT.ndiff]).T,concat([1,size(T)])),concat([2,3,1]))
# SiStER_get_ductile_rheology_on_nodes_from_strain_rate.m:12
    Ediff=permute(repmat(concat([MAT.Ediff]).T,concat([1,size(T)])),concat([2,3,1]))
# SiStER_get_ductile_rheology_on_nodes_from_strain_rate.m:13
    pre_disc=permute(repmat(concat([MAT.pre_disc]).T,concat([1,size(T)])),concat([2,3,1]))
# SiStER_get_ductile_rheology_on_nodes_from_strain_rate.m:14
    ndisc=permute(repmat(concat([MAT.ndisc]).T,concat([1,size(T)])),concat([2,3,1]))
# SiStER_get_ductile_rheology_on_nodes_from_strain_rate.m:15
    Edisc=permute(repmat(concat([MAT.Edisc]).T,concat([1,size(T)])),concat([2,3,1]))
# SiStER_get_ductile_rheology_on_nodes_from_strain_rate.m:16
    epsII=repmat(epsII,concat([1,1,PARAMS.Nphase]))
# SiStER_get_ductile_rheology_on_nodes_from_strain_rate.m:18
    T=repmat(T,concat([1,1,PARAMS.Nphase]))
# SiStER_get_ductile_rheology_on_nodes_from_strain_rate.m:19
    # TO BE REPLACED BY SiStER_flow_law_function SOON
#eta_diff = pre_diff.^(-1./ndiff).*epsII.^((1-ndiff)./ndiff).* ...
#    exp((Ediff)./(ndiff.*PARAMS.R.*(T+273.15)));
#eta_disc = pre_disc.^(-1./ndisc).*epsII.^((1-ndisc)./ndisc).* ...
#    exp((Edisc)./(ndisc.*PARAMS.R.*(T+273.15)));
    
    eta_diff=SiStER_flow_law_function('from_strain_rate',pre_diff,Ediff,ndiff,PARAMS.R,T,epsII,zeros(size(epsII)),PARAMS)
# SiStER_get_ductile_rheology_on_nodes_from_strain_rate.m:28
    eta_disc=SiStER_flow_law_function('from_strain_rate',pre_disc,Edisc,ndisc,PARAMS.R,T,epsII,zeros(size(epsII)),PARAMS)
# SiStER_get_ductile_rheology_on_nodes_from_strain_rate.m:29
    # linearly average between viscosity of each phase type
    eta_diffAVG=sum(multiply(eta_diff,phase_node),3)
# SiStER_get_ductile_rheology_on_nodes_from_strain_rate.m:33
    eta_discAVG=sum(multiply(eta_disc,phase_node),3)
# SiStER_get_ductile_rheology_on_nodes_from_strain_rate.m:34
    eta=(1.0 / eta_diffAVG + 1.0 / eta_discAVG) ** - 1
# SiStER_get_ductile_rheology_on_nodes_from_strain_rate.m:36
    eta[eta < PARAMS.etamin]=PARAMS.etamin
# SiStER_get_ductile_rheology_on_nodes_from_strain_rate.m:37