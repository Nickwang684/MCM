# GitHub Copilot Instructions for MCM Project

This file provides guidance for GitHub Copilot when working with this mathematical modeling competition (MCM/ICM) project.

## Project Overview

This is a Mathematical Contest in Modeling (MCM) project repository containing:
- Mathematical modeling solutions
- Data analysis and visualization
- Algorithm implementations
- Competition submissions

## Technology Stack

- **Primary Languages**: Python, MATLAB/Octave, R
- **Data Analysis**: NumPy, Pandas, SciPy, scikit-learn
- **Visualization**: Matplotlib, Seaborn, Plotly
- **Documentation**: LaTeX, Markdown
- **Optimization**: CVXPY, PuLP, OR-Tools

## Coding Guidelines

### Python Standards
- Follow PEP 8 style guidelines
- Use type hints for function signatures
- Include docstrings for all functions and classes
- Prefer NumPy operations over Python loops for performance
- Use meaningful variable names that reflect mathematical notation

### Mathematical Code
- Document all mathematical formulas in comments
- Include references to papers or methods used
- Validate numerical results with sanity checks
- Use appropriate precision for floating-point calculations
- Add unit tests for critical algorithms

### Data Processing
- Always validate input data before processing
- Handle missing values explicitly
- Document data sources and preprocessing steps
- Use pandas for structured data manipulation
- Implement reproducible random seeds

### Visualization
- Use clear, descriptive titles and axis labels
- Include legends for multi-series plots
- Use colorblind-friendly color schemes
- Export figures in vector format (PDF/SVG) for reports
- Add grid lines for readability

## File Naming Conventions

- `model_*.py` - Model implementation files
- `data_*.py` - Data processing scripts
- `viz_*.py` - Visualization scripts
- `test_*.py` - Test files
- `utils_*.py` - Utility functions

## Documentation Requirements

- Write clear README files for each problem
- Include mathematical derivations in LaTeX
- Document assumptions and limitations
- Provide usage examples in code comments

## Performance Considerations

- Profile code before optimization
- Use vectorized operations where possible
- Consider memory constraints for large datasets
- Implement caching for expensive computations

## Lessons Learned

<!-- Add lessons learned from interactions here -->
- Keep instructions updated based on project-specific findings
- Document any model-specific requirements or constraints

## Scratchpad

<!-- Use this section for temporary notes and task tracking -->
