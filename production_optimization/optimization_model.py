import pulp as pl

# Define the optimization problem
model = pl.LpProblem("Production Optimization", pl.LpMaximize)

# Define decision variables
x1 = pl.LpVariable('x1', lowBound=0, cat='Continuous')
x2 = pl.LpVariable('x2', lowBound=0, cat='Continuous')
x3 = pl.LpVariable('x3', lowBound=0, cat='Continuous')
x4 = pl.LpVariable('x4', lowBound=0, cat='Continuous')
x5 = pl.LpVariable('x5', lowBound=0, cat='Continuous')

# Objective function
model += 5*x1 + 4*x2 + 6*x3 + 7*x4 + 8*x5, "Total Profit"

# Constraints
model += 2*x1 + 3*x2 + 1*x3 + 4*x4 + 5*x5 <= 100, "Labor Constraint"
model += 3*x1 + 2*x2 + 4*x3 + 1*x4 + 3*x5 <= 80, "Machine Time Constraint"
model += 4*x1 + 1*x2 + 3*x3 + 2*x4 + 2*x5 <= 70, "Raw Material Constraint"
model += x1 <= 20, "P1 Production Constraint"
model += x2 + x3 >= 10, "P2 and P3 Production Constraint"
model += x4 >= 5, "P4 Production Constraint"
