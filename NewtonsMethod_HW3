# This code will be used for analysis of a turbofan with a front fan. Many components are given, but the code
# will assume a consistent thermal efficiency, fuel mass flow rate, and heating value. The kinetic energy balance 
# and uninstalled thrust equation be programmed here with numpy.

import numpy as np
from scipy.optimize import newton # using scipy.optimize rather than programming the Newton's method from scratch

V0 = float(input('Enter V0 (m/s): ')) # user input to get the free stream velocity
V19 = float(input('Enter V19 (m/s): ')) # user input to get the bypass nozzle exit velocity
m_core = 100.0 # kg/s
m9 = 102.0 # kg/s
P = 0.35 * 2 * 50000000   # Watts
def engine(m19):
    m0 = m_core + m19 # total inlet mass flow rate
    V9 = np.sqrt((2*P + m_core*V0**2 - m19*(V19**2 - V0**2)) / m9) # kinetic energy balance equation solved for v9
    F = m9*V9 + m19*V19 - m0*V0 # uninstalled thrust equation
    return m0, V9, F # should return the total mass flow rate, core nozzle exit velocity, and uninstalled thrust

def f(m19):
    m0, V9, F = engine(m19) # kg/s, m/s, N
    return F/m0 - 400 # should be close to zero for iterations to converge

m19 = newton(f, x0=50) # kg/s
m0, V9, F = engine(m19) # kg/s, m/s, N
mf = 2.0 # kg/s
QR = 50000e3   # J/kg
eta_0 = F*V0 / (mf*QR) # unity

print('m19=',m19) # bypass nozzle mass flow rate
print('m0=',m0) # total mass flow rate
print('V9=',V9) # core nozzle exit velocity
print('F=',F) # uninstalled thrust
print('F/m0=',F/m0) # uninstalled thrust per unit mass flow rate (specific thrust)
print('eta_0=',eta_0) # overall engine efficiency
