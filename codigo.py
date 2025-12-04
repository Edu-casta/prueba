import main

num_list = []
for i in range(1,100):
    numeros = range(1,100,i)
    numeros_list = [numero for numero in numeros]
    result = main.Calculadora.suma(numeros_list)
    num_list.append(result)
    
print(num_list)