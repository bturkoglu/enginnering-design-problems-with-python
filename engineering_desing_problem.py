import numpy as np

# This is a sample Python script.
import numpy as np
# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

def CSD(x):  #Compression/tension spring desing
    PCONST = 100  # % PENALTY FUNCTION CONSTANT

    fit = (x[2] + 2) * x[1] * (x[0] ** 2)
    G1 = 1 - (x[1] ** 3 * x[2]) / (71785 * x[0] ** 4)
    G2 = (4 * x[1] ** 2 - x[0] * x[1]) / (12566 * (x[1] * x[0] ** 3 - x[0] ** 4)) + 1 / (5108 * x[0] ** 2)
    G3 = 1 - (140.45 * x[0]) / (x[1] ** 2 * x[2])
    G4 = ((x[0] + x[1]) / 1.5) - 1

    PHI = fit + PCONST * (max(0, G1) ** 2 + max(0, G2) ** 2 + max(0, G3) ** 2 + max(0, G4) ** 2) # % PENALTY FUNCTION
    return PHI

def WBD(x): # Welded Beam Design (WBD)
    P = 6000  # % APPLIED TIP LOAD
    E = 30e6  # % YOUNGS MODULUS OF BEAM
    G = 12e6  # % SHEAR MODULUS OF BEAM
    tem = 14  # % LENGTH OF CANTILEVER PART OF BEAM
    PCONST = 100000  # % PENALTY FUNCTION CONSTANT
    TAUMAX = 13600  # % MAXIMUM ALLOWED SHEAR STRESS
    SIGMAX = 30000  # % MAXIMUM ALLOWED BENDING STRESS
    DELTMAX = 0.25  # % MAXIMUM ALLOWED TIP DEFLECTION
    M = P * (tem + x[1] / 2)  # % BENDING MOMENT AT WELD POINT
    R = np.sqrt((x[1] ** 2) / 4 + ((x[0] + x[2]) / 2) ** 2)  # % SOME CONSTANT
    J = 2 * (np.sqrt(2) * x[0] * x[1] * ((x[1] ** 2) / 4 + ((x[0] + x[2]) / 2) ** 2))  # % POLAR MOMENT OF INERTIA
    print(M, R, J)
    PHI = 1.10471 * x[0] ** 2 * x[1] + 0.04811 * x[2] * x[3] * (14 + x[1])  # % OBJECTIVE FUNCTION
    SIGMA = (6 * P * tem) / (x[3] * x[2] ** 2)  # BENDING STRESS
    DELTA = (4 * P * tem ** 3) / (E * x[2] ** 3 * x[3])  # TIP DEFLECTION
    PC = 4.013 * E * np.sqrt((x[2] ** 2 * x[3] ** 6) / 36) * (1 - x[2] * np.sqrt(E / (4 * G)) / (2 * tem)) / (
                tem ** 2)  # % BUCKLING LOAD
    TAUP = P / (np.sqrt(2) * x[0] * x[1])  # % 1 ST DERIVATIVE OF SHEAR STRESS
    TAUPP = (M * R) / J  # % 2ND DERIVATIVE OF SHEAR STRESS
    TAU = np.sqrt(TAUP ** 2 + 2 * TAUP * TAUPP * x[1] / (2 * R) + TAUPP ** 2)  # % SHEAR STRESS
    G1 = TAU - TAUMAX  # % MAX SHEAR STRESS CONSTRAINT
    G2 = SIGMA - SIGMAX  # ; % MAX BENDING STRESS CONSTRAINT
    # % G3 = L(1) - L(4); % WELD COVERAGE CONSTRAINT
    G3 = DELTA - DELTMAX
    G4 = x[0] - x[3]
    G5 = P - PC
    G6 = 0.125 - x[0]
    # %G4 = 0.10471 * L(1) ^ 2 + 0.04811 * L(3) * L(4) * (14 + L(2)) - 5 # % MAX COST CONSTRAINT
    # % G5 = 0.125 - L(1); % MAX WELD THICKNESS CONSTRAINT
    # % G6 = DELTA - DELTMAX;
    # % MAX TIP DEFLECTION CONSTRAINT
    # % G7 = P - PC; % BUCKLING LOAD CONSTRAINT
    G7 = 1.10471 * x[0] ** 2 + 0.04811 * x[2] * x[3] * (14 + x[1]) - 5  # ;
    PHI = PHI + PCONST * (max(0, G1) ** 2 + max(0, G2) ** 2 + max(0, G3) ** 2 + max(0, G4) ** 2 + max(0, G5) ** 2 + max(0,G6) ** 2 + max(0, G7) ** 2)  # % PENALTY FUNCTION

    return PHI

def PVD(x):  #Pressure Vessel Design
    PCONST = 10000# % PENALTY FUNCTION CONSTANT
    fit = 0.6224 * x[0] * x[2] * x[3] + 1.7781 * x[1] * x[2] ** 2 + 3.1661 * x[0] ** 2 * x[3] + 19.84 * x[0] ** 2 * x[2]
    G1 = -x[0] + 0.0193 * x[2]
    G2 = -x[2] + 0.00954 * x[2]
    G3 = -np.pi * x[2] ** 2 * x[3] - (4 / 3) * np.pi * x[2] ** 3 + 1296000
    G4 = x[3] - 240
    PHI = fit + PCONST * (max(0, G1) ** 2 + max(0, G2) ** 2 + max(0, G3) ** 2 + max(0, G4) ** 2) # % PENALTY FUNCTION

    return PHI

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
    baha=WBD((0.205676,3.478377,9.03681,0.205778))
    print(baha)