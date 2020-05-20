# Generated with SMOP  0.41
from libsmop import *
# SiStER_flow_law_function.m

    
@function
def SiStER_flow_law_function(type_=None,pre=None,Ea=None,n=None,R=None,T=None,epsII=None,sII=None,PARAMS=None,*args,**kwargs):
    varargin = SiStER_flow_law_function.varargin
    nargin = SiStER_flow_law_function.nargin

    # [eta] = SiStER_flow_law_function(type,pre,Ea,n,R,T,epsII,sII)
#  gives generic form of ductile creep law 
#  to be used for both diffusion and dislocation creep in
#  get_ductile_rheology functions
#  inputs:
#  type = 'from_stress' or 'from_strain_rate' to set flow law expression
#  with usual parameters: prefactor (pre), activation energy (Ea, J/mol),
#  exponent (n), gas constant (R), temperature (T, in deg C), 
#  second invariant of strain rate (epsII, s^-1) or second invariant
#  of deviatoric stress (sII, Pa)
    
    if strcmp(type_,'from_stress') == 1:
        eta=multiply(multiply(pre ** (- 1),sII ** (1 - n)),exp(Ea / (multiply(R,(T + 273.15)))))
# SiStER_flow_law_function.m:15
    else:
        if strcmp(type_,'from_strain_rate') == 1:
            eta=multiply(multiply(pre ** (- 1.0 / n),epsII ** ((1 - n) / n)),exp((Ea) / (multiply(multiply(n,R),(T + 273.15)))))
# SiStER_flow_law_function.m:20
        else:
            if strcmp(type_,'custom') == 1:
                disp('ERROR ?\xa0CUSTOM VISCOSITY FUNCTION NOT CURRENTLY DEFINED')
                disp('this feature will be available in a future update.')
                eta=PARAMS.customviscofunction(phase,temperature,strain_rate,stress)
# SiStER_flow_law_function.m:27
            else:
                disp('ERROR ? flow law is undefined.')
    