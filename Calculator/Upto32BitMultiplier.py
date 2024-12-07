from qiskit import QuantumCircuit
from qiskit_aer.primitives import Sampler
from qiskit import QuantumRegister
from qiskit.circuit.library import CDKMRippleCarryAdder
from Calculator.Modifier import Modifier

class Multiply:
    def __init__(self, a, b):
        self.a = a
        self.b = b
        self.results = None
        self.circuit = None
        self._run_multiplier()  # Automatically compute result upon instantiation

    def _run_multiplier(self):
        Qcr, ls = Modifier(self.a, self.b)
        a = QuantumRegister(ls, name='a')
        b = QuantumRegister(ls, name='b')
        out = QuantumRegister(ls * 2, name='out')
        helper = QuantumRegister(1, name='helper')

        Qc1 = QuantumCircuit(a, b, out, helper, name="Multiplier")

        plist = []
        for i in range(ls * 2 + 1):
            plist.append(i)

        Qc1.append(Qcr, plist)

        gate = CDKMRippleCarryAdder(ls, kind="half").to_gate().control()

        for i in range(ls):
            xlist = [i]
            for k in range(ls, ls * 2):
                xlist.append(k)
            for j in range(ls * 2, ls * 3 + 1):
                xlist.append(j + i)

            xlist.append(ls * 4)
            Qc1.append(gate, xlist)

        # Add measurements
        Qc1.measure_all()

        # Run the quantum computation
        psi = Sampler().run([Qc1], shots=1).result().quasi_dists[0].binary_probabilities()
        self.results = int(next(iter(psi))[: ls * 2 + 1], 2)
        self.circuit = Qc1.decompose(gates_to_decompose={'Multiplier', 'Bin Transform'})

    def __call__(self):
        # Make the instance callable to return the result
        return self.results

    @staticmethod
    def compute(a, b):
        # Provide static call for computing results
        return Multiply(a, b)()

    @staticmethod
    def get_circuit(a, b):
        # Provide static call for accessing the circuit
        return Multiply(a, b).circuit
