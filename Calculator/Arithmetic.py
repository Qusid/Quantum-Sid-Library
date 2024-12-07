from Calculator.Upto32BitAdder import Adder
from Calculator.Upto32BitMultiplier import Multiply
from Calculator.Upto32Subtractor import Sub

class Bit32:
    @staticmethod
    def add(num1, num2):
        return Adder(num1, num2)()

    @staticmethod
    def add_circuit(num1, num2):
        return Adder(num1, num2).circuit

    @staticmethod
    def multiply(num1, num2):
        return Multiply.compute(num1, num2)

    @staticmethod
    def multiply_circuit(num1, num2):
        return Multiply.get_circuit(num1, num2)

    @staticmethod
    def subtract(num1, num2):
        return Sub.compute(num1, num2)

    @staticmethod
    def subtract_circuit(num1, num2):
        return Sub.get_circuit(num1, num2)