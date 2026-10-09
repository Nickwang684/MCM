---
description: Create a mathematical model implementation from description
mode: agent
tools: ['read', 'edit', 'search', 'execute']
---

# Mathematical Model Implementation

Based on the problem description, create a complete mathematical model implementation:

## Steps
1. **Understand the problem**: Analyze the given requirements
2. **Define variables**: List all decision variables and parameters
3. **Formulate constraints**: Express all constraints mathematically
4. **Define objective function**: Specify the optimization goal
5. **Implement in code**: Write clean, documented Python code
6. **Validate**: Add tests and sanity checks

## Output Requirements
- Documented Python code with type hints
- Clear variable naming matching mathematical notation
- Comments explaining each constraint and formula
- Visualization of results
- Summary of model performance

## Template Structure
```python
"""
Model: [Model Name]
Problem: [Brief description]
Author: [Team]
Date: [Date]
"""

import numpy as np
import pandas as pd
from typing import Dict, List, Tuple

def define_parameters() -> Dict:
    """Define model parameters."""
    pass

def build_model(params: Dict) -> Any:
    """Build the optimization model."""
    pass

def solve_model(model: Any) -> Dict:
    """Solve and return results."""
    pass

def visualize_results(results: Dict) -> None:
    """Create visualizations."""
    pass

if __name__ == "__main__":
    params = define_parameters()
    model = build_model(params)
    results = solve_model(model)
    visualize_results(results)
```
