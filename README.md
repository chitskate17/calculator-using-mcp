# Calculator Using MCP

A demo Python calculator application with basic arithmetic operations.

## Features

- Addition
- Subtraction
- Multiplication
- Division
- Power
- Modulo

## Installation

1. Clone the repository:
```bash
git clone https://github.com/chitskate17/calculator-using-mcp.git
cd calculator-using-mcp
```

2. Run the calculator:
```bash
python calculator.py
```

## Usage

### Interactive Mode

Run the calculator in interactive mode:
```bash
python calculator.py
```

Follow the on-screen prompts to perform calculations.

### As a Module

You can also import and use the Calculator class in your own Python code:

```python
from calculator import Calculator

calc = Calculator()
result = calc.add(5, 3)
print(f"5 + 3 = {result}")
```

## Testing

Run the unit tests:
```bash
python -m pytest test_calculator.py
```

## Requirements

- Python 3.6 or higher

## License

MIT License
