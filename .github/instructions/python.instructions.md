---
applyTo: "**/*.py"
---

# Python Coding Standards

## General Guidelines
- Follow PEP 8 style guidelines
- Use type hints for all function parameters and return types
- Maximum line length: 100 characters
- Use f-strings for string formatting

## Imports
- Group imports: standard library, third-party, local
- Sort imports alphabetically within groups
- Avoid wildcard imports (`from module import *`)

## Documentation
- Use Google-style docstrings
- Document all public functions, classes, and modules
- Include type information in docstrings

## Example Docstring Format
```python
def function_name(param1: int, param2: str) -> bool:
    """Brief description of function.
    
    Longer description if needed.
    
    Args:
        param1: Description of param1.
        param2: Description of param2.
        
    Returns:
        Description of return value.
        
    Raises:
        ValueError: When param1 is negative.
    """
```

## Mathematical Code Patterns
- Use NumPy for matrix operations
- Prefer vectorized operations over loops
- Document formulas with LaTeX in comments: `# Formula: $$E = mc^2$$`
- Validate numerical stability

## Error Handling
- Use specific exception types
- Provide informative error messages
- Handle edge cases explicitly

## Testing
- Write unit tests for all public functions
- Use pytest as the testing framework
- Aim for >80% code coverage
