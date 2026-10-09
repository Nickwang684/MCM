---
name: optimization
description: Mathematical optimization toolkit for solving linear, nonlinear, and integer programming problems. Use when asked to optimize, minimize, maximize, or find optimal solutions.
version: 1.0.0
---

# Optimization Skill

## When to Use This Skill
- Solving linear programming (LP) problems
- Mixed-integer programming (MIP)
- Nonlinear optimization
- Constraint satisfaction problems
- Multi-objective optimization

## Available Tools

### Python Libraries
- **PuLP**: Simple LP/MIP problems
- **CVXPY**: Convex optimization
- **SciPy.optimize**: General nonlinear optimization
- **OR-Tools**: Constraint programming, routing
- **Pyomo**: Advanced optimization modeling

## Problem Formulation Template

### Linear Programming
```python
from pulp import *

# Create problem
prob = LpProblem("Problem_Name", LpMaximize)

# Decision variables
x = LpVariable("x", lowBound=0)
y = LpVariable("y", lowBound=0)

# Objective function
prob += 3*x + 2*y, "Profit"

# Constraints
prob += x + y <= 10, "Resource_1"
prob += 2*x + y <= 15, "Resource_2"

# Solve
prob.solve()

# Results
print(f"Status: {LpStatus[prob.status]}")
print(f"x = {x.varValue}, y = {y.varValue}")
print(f"Optimal value = {value(prob.objective)}")
```

### Convex Optimization
```python
import cvxpy as cp
import numpy as np

# Variables
x = cp.Variable(n)

# Objective
objective = cp.Minimize(cp.sum_squares(A @ x - b))

# Constraints
constraints = [x >= 0, cp.sum(x) == 1]

# Problem
prob = cp.Problem(objective, constraints)
prob.solve()
```

## Best Practices
1. Always verify problem convexity
2. Check constraint feasibility
3. Use warm starts for iterative solving
4. Analyze dual variables for sensitivity
5. Validate results with sanity checks
