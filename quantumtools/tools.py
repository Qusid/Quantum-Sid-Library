from qiskit_aer import Aer
import numpy as np
from sympy import Matrix, Rational, sqrt, simplify, init_printing, latex, Abs
from IPython.display import display, Math

def Eigensol(A):
    # Compute the eigenvalues and eigenvectors
    eigen_data = A.eigenvects()

    # Iterate over each eigenvalue and its corresponding eigenvectors
    for eigenval, multiplicity, eigenspaces in eigen_data:
        # Display the eigenvalue
        display(Math(r"\textbf{Eigenvalue} \quad \lambda = %s" % latex(eigenval)))
        for eigenvec in eigenspaces:
            # Normalize the eigenvector
            norm = sqrt(sum(comp**2 for comp in eigenvec))
            normalized_eigenvec = simplify(eigenvec / norm)
            
            # Extract scalar factor and integer vector
            non_zero_components = [comp for comp in normalized_eigenvec if not comp.is_zero]
            if non_zero_components:
                scalar_factor = simplify(non_zero_components[0])
                # Adjust for negative scalar factors
                if scalar_factor.evalf(chop=True).is_negative:
                    scalar_factor = -scalar_factor
                    integer_vector = -normalized_eigenvec / scalar_factor
                else:
                    integer_vector = normalized_eigenvec / scalar_factor
                integer_vector = simplify(integer_vector)
            else:
                # Handle the case where all components are zero
                scalar_factor = 1
                integer_vector = normalized_eigenvec
            
            # Convert scalar factor and integer vector to LaTeX
            scalar_factor_latex = latex(scalar_factor)
            eigenvec_latex = latex(integer_vector, mat_delim=None, mat_str='pmatrix')
            
            # Display the normalized eigenvector
            display(Math(r"\textbf{Normalized Eigenvector} \quad \mathbf{v} = %s \, %s" % (scalar_factor_latex, eigenvec_latex)))

def MeasureShot(Qc,n):
    Qc.measure(list(range(Qc.num_qubits - 1)),list(range(Qc.num_qubits - 1)))
    backend = Aer.get_backend('qasm_simulator')
    job = backend.run(Qc, shots=n)
    result = job.result()
    return result.get_counts()

#This function will help us the required value from statevector
def ResultFromStateVector(psi,digit, reverse = "False", decimal = "False"):

  if decimal == "true":
    if reverse == "true":
      return  int(psi.draw("latex_source").split('|')[1].split("\\")[0][:(digit)][::-1],2)
    else:
      return  int(psi.draw("latex_source").split('|')[1].split("\\")[0][:(digit)],2)

#when decimal flase and reverse true
  if reverse == "true":
    return  psi.draw("latex_source").split('|')[1].split("\\")[0][:(digit)][::-1]
#when decimal flase and reverse false
  return  psi.draw("latex_source").split('|')[1].split("\\")[0][:(digit)]