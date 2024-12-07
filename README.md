Here’s a **well-structured and professional README** for your **Quantum-Sid-Library** with details about the new tools and existing functionalities:

---

# Quantum-Sid-Library

**Quantum-Sid-Library** is a Python library designed to provide quantum computing utilities, tools, and arithmetic operations implemented using Qiskit. This library simplifies common quantum computing tasks like addition, subtraction, multiplication, eigenvector computations, and measurement handling.

---

## Features

### 1. **Calculator Module**
   - Perform quantum-based arithmetic operations using Qiskit.
   - **Available Operations**:
     - **Addition**: Perform quantum addition using a ripple-carry adder circuit.
     - **Subtraction**: Perform quantum subtraction with support for two's complement.
     - **Multiplication**: Perform quantum multiplication using controlled addition gates.
   - **Key Functions**:
     - `Bit32.add(a, b)` - Quantum addition of two integers.
     - `Bit32.subtract(a, b)` - Quantum subtraction of two integers.
     - `Bit32.multiply(a, b)` - Quantum multiplication of two integers.
     - Access quantum circuits directly for visualization using:
       - `Bit32.add_circuit(a, b)`
       - `Bit32.subtract_circuit(a, b)`
       - `Bit32.multiply_circuit(a, b)`

---

### 2. **Quantum Tools Module**
   The **Quantum Tools Module** (`quantumtools`) provides utilities to work with quantum circuits, eigenvector computations, and measurement handling.

   - **Eigensol(A)**:
     - Computes and displays eigenvalues and normalized eigenvectors of a given matrix `A`.
     - Provides eigenvectors in a normalized integer form with scalar factors for better interpretability.
     - Uses Sympy for symbolic computation and IPython for LaTeX-based display.

   - **MeasureShot(Qc, n)**:
     - Simulates a quantum circuit `Qc` and measures the qubits `n` times using the Qiskit Aer backend.
     - Returns the measurement counts as a dictionary.

   - **ResultFromStateVector(psi, digit, reverse=False, decimal=False)**:
     - Extracts and interprets the binary value from a quantum state vector.
     - Parameters:
       - `psi`: State vector to analyze.
       - `digit`: Number of bits to extract.
       - `reverse`: If `True`, reverses the bit order (default: `False`).
       - `decimal`: If `True`, converts the result to a decimal value (default: `False`).

---

## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/your-repo/Quantum-Sid-Library.git
   cd Quantum-Sid-Library
   ```

2. Install the library and dependencies:
   ```bash
   pip install -e .
   ```

3. Ensure required dependencies are installed:
   ```bash
   pip install -r requirements.txt
   ```

---

## Usage

### **Example: Quantum Arithmetic**
```python
from Calculator.Arithmetic import Bit32

# Perform quantum addition
result = Bit32.add(5, 6)
print(f"Addition Result: {result}")

# Retrieve quantum circuit for addition
circuit = Bit32.add_circuit(5, 6)
print(f"Addition Circuit:\n{circuit}")
```

### **Example: Eigenvector Computation**
```python
from quantumtools.tools import Eigensol
from sympy import Matrix

# Define a matrix
A = Matrix([[2, 1], [1, 2]])

# Compute eigenvalues and eigenvectors
Eigensol(A)
```

### **Example: Measure Quantum Circuit**
```python
from quantumtools.tools import MeasureShot
from qiskit import QuantumCircuit

# Create a simple quantum circuit
qc = QuantumCircuit(2)
qc.h(0)
qc.cx(0, 1)

# Measure the circuit 1000 times
counts = MeasureShot(qc, 1000)
print(f"Measurement Counts: {counts}")
```

### **Example: Extract Results from State Vector**
```python
from quantumtools.tools import ResultFromStateVector
from qiskit.quantum_info import Statevector

# Create a state vector
psi = Statevector.from_label('00')

# Extract binary result
result = ResultFromStateVector(psi, digit=2, reverse=False, decimal=True)
print(f"Extracted Result: {result}")
```

---

## Dependencies
This library relies on the following Python libraries:
- **Qiskit** (Quantum computing framework)
- **Sympy** (Symbolic mathematics for eigenvalue computations)
- **Numpy** (Numerical computations)
- **IPython** (Interactive visualization of results)

Install dependencies using:
```bash
pip install -r requirements.txt
```

---

## Folder Structure

```
Quantum-Sid-Library/
├── Calculator/
│   ├── Arithmetic.py
│   ├── Modifier.py
│   ├── Upto32BitAdder.py
│   ├── Upto32BitMultiplier.py
│   ├── Upto32Subtractor.py
├── quantumtools/
│   ├── tools.py
├── testing/
│   ├── Calculator_test.py
├── LICENSE
├── README.md
├── requirements.txt
```

---

## Contributing

1. Fork the repository.
2. Create a new branch for your feature/bug fix:
   ```bash
   git checkout -b feature-name
   ```
3. Commit your changes and push to your fork.
4. Create a pull request with a detailed explanation of your changes.

---

## License

This library is licensed under the **MIT License**. See `LICENSE` for more details.

---

## Acknowledgements

Special thanks to the Qiskit community and open-source contributors who make quantum computing accessible to everyone.

---
