import sympy as sp

# User input values
v_M = float(input("Enter the determined P-M angle (in degrees): "))
gamma = float(input("Enter a value for gamma: "))

# Convert the given P-M angle from degrees to radians
v_M_rad = v_M * sp.pi / 180

# Allow M = Mach number to be a variable
M = sp.symbols('M')


# Define the Prandtl-Meyer equation as f(M) = 0
f = (
    sp.sqrt((gamma + 1) / (gamma - 1))
    * sp.atan(
        sp.sqrt(
            ((gamma - 1) / (gamma + 1)) * (M**2 - 1)
        )
    )
    - sp.atan(sp.sqrt(M**2 - 1))
    - v_M_rad
)


# Take derivative automatically using SymPy
df = sp.diff(f, M)


# Convert symbolic expressions into callable numerical functions
f_func = sp.lambdify(M, f, 'math')
df_func = sp.lambdify(M, df, 'math')


# Educated initial guess
guess = float(input("Enter an initial guess for M: "))


# Newton's Method
for i in range(30):

    old_guess = guess

    new_guess = old_guess - f_func(old_guess) / df_func(old_guess)

    print("Iteration:", i + 1, "Guess:", new_guess)

    # Check for convergence and cut off if the change is small enough
    if abs(new_guess - old_guess) < 1e-8:
        guess = new_guess
        break

    guess = new_guess


print("\nFinal converged Mach number =", guess)