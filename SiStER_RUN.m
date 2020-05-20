function [] = SiStER_RUN(InpFil)

keepvars = {'InpFil'};
clearvars('-except', keepvars{:});
running_from_SiStER_RUN=1;
SiStER_MAIN


end
