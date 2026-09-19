# This code is an attempt to use Newton's method to solve for SP ratio via an initial input guess.
# The goal is to converge within 30 iterations to a usable solution
# In order to perform symbolic math, sympy is imported 

import sympy as sp

# User input values (for HW1, problem 2, A* = 1 m^2, Ae = 3 m^2, Me = 2.3)
A_star = float(input('Enter the area of the throat assuming choked flow (A*, m^2): '))
A_exit = float(input('Enter the exit area (Ae, m^2): '))
M_exit = float(input('Enter the exit Mach number (Me): '))

area_ratio = A_exit / A_star


# Define gamma as a symbolic variable
gamma = sp.symbols('gamma')


# Define the area-Mach equation as f(gamma) = 0
f = (1 / M_exit) * (
    (2 / (gamma + 1))
    * (1 + ((gamma - 1) / 2) * M_exit**2)
)**((gamma + 1) / (2 * (gamma - 1))) - area_ratio


# Take derivative automatically using SymPy
df = sp.diff(f, gamma)


# Convert symbolic expressions into callable functions (for user input)
f_func = sp.lambdify(gamma, f, 'math')
df_func = sp.lambdify(gamma, df, 'math')


# Educated initial guess
guess = float(input("Enter an initial guess for gamma: "))


# Newton's Method (The guess on the left side is the new guess, right side is previous guess)
for i in range(30):

    guess = guess - f_func(guess) / df_func(guess)

    print("Iteration:", i + 1, "Gamma:", guess)

# The guess input below will be the aboslute FINAL guess value computed after 30 iterations
print("\nFinal, converged specific heat ratio =", guess)