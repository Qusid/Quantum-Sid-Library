from qiskit import QuantumCircuit
from qiskit_aer.primitives import Sampler
from qiskit import QuantumRegister
from qiskit.circuit.library import CDKMRippleCarryAdder
from Calculator.Modifier import Modifier

class Adder:
    def __init__(self, a, b):
        self.a = a
        self.b = b
        self.results = None
        self.circuit = None
        self._run_adder()  # Automatically run the computation upon instantiation

    def _run_adder(self):
        Qcr, ls = Modifier(self.a, self.b)
        cin = QuantumRegister(1, name='cin')
        a = QuantumRegister(ls, name='a')
        b = QuantumRegister(ls, name='b')
        out = QuantumRegister(1, name='out')

        Qc1 = QuantumCircuit(cin, a, b, out, name="Modified")

        plist = []
        for i in range((ls * 2) + 2):
            plist.append(i)

        Qc1.append(Qcr, plist[1:])
        Qc1.append(CDKMRippleCarryAdder(ls), plist)
        Qc1.measure_all()

        # Run the quantum computation
        psi = Sampler().run(Qc1, shots=1).result().quasi_dists[0].binary_probabilities()
        self.results = int(next(iter(psi))[:ls + 1], 2)
        self.circuit = Qc1.decompose()  # Store the decomposed circuit

    def __call__(self):
        # Make the instance callable to return the result
        return self.results
