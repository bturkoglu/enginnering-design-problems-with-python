
                      
%             Chaotic GSA for Mechanical Engineering Design Problems
% 
%                  E-Mail: sajad.win8@gmail.com                   
%                                                                         
%              Homepage: https://github.com/SajadAHMAD1.                            
%                                                                         
%   Main paper: Rather, S. and Bala, P. (2020), "Swarm-based chaotic gravitational search algorithm for solving mechanical engineering design problems",
%                                               World Journal of Engineering, Vol. 17 No. 1, pp. 97-114. https://doi.org/10.1108/WJE-09-2019-0254   

%               Department of Computer Science and Engineering
%               School of Engineering and Technology
%               Pondicherry University- 605014, India
%               
%   Programmer: Sajad Ahmad Rather      
%   Developed in MATLAB R2013a 



% This function gives boundaries and dimension of search space for test functions.

function [down,up,dim]=benchmark_functions_details(Benchmark_Function_ID)

if Benchmark_Function_ID==1     % Welded Beam Design (WBD)
    down=[0.10;0.10;0.10;0.10]; % Lower Bound of Variables
    up=[2;10;10;2];             % Upper Bound of Variables
    dim=4;
end
if Benchmark_Function_ID==2  % Compression Spring Design (CSD)
    down=[0.05;0.25;2.00];   % Lower Bound of Variables
    up=[2.00;1.30;15.0];     % Upper Bound of Variables
    dim=3;

end
if Benchmark_Function_ID==3 % Pressure Vessel Design (PVD)
down=[0;0;10;10];           % Lower Bound of Variables
up= [99;99;200;200];        % Upper Bound of Variables
dim=4;
end

end









