class Calculadora:
    @staticmethod
    def suma(num1, num2):
        return num1 + num2
    
    @staticmethod
    def resta(num1, num2):
        return num1 - num2
    
    @staticmethod
    def multiplicación(num1, num2):
        return num1 * num2

num1 = Calculadora.suma(4, 8)
print(num1)
