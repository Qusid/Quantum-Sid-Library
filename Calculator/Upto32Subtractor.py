from qiskit import QuantumCircuit
from qiskit_aer.primitives import Sampler
from qiskit import QuantumRegister
from qiskit.circuit.library import CDKMRippleCarryAdder
from Calculator.Modifier import Modifier

class Sub:
    def __init__(self, a, b):
        self.a = a
        self.b = b
        self.results = None
        self.circuit = None
        self._run_subtraction()  # Automatically compute result upon instantiation

    def _run_subtraction(self):
        Qcr, ls = Modifier(self.a, self.b)
        cin = QuantumRegister(1, name='cin')
        a_reg = QuantumRegister(ls, name='a')
        b_reg = QuantumRegister(ls, name='b')
        out = QuantumRegister(1, name='out')

        Qc1 = QuantumCircuit(cin, a_reg, b_reg, out, name="Modified")

        plist = []
        for i in range((ls * 2) + 2):
            plist.append(i)

        Qc1.append(Qcr, plist[1:])
        Qc1.append(CDKMRippleCarryAdder(ls).inverse(), plist)

        # Add measurements
        Qc1.measure_all()

        # Run the quantum computation
        psi = Sampler().run(Qc1, shots=1).result().quasi_dists[0].binary_probabilities()
        results = int(next(iter(psi))[: ls + 1], 2)
        
        # Handle two's complement for negative results
        if self.a > self.b:
            self.results = results - (2 ** (ls + 1))
        else:
            self.results = results

        self.circuit = Qc1.decompose()

    def __call__(self):
        # Make the instance callable to return the result
        return self.results

    @staticmethod
    def compute(a, b):
        # Provide static call for computing results
        return Sub(a, b)()

    @staticmethod
    def get_circuit(a, b):
        # Provide static call for accessing the circuit
        return Sub(a, b).circuit
