#Calculadora que opera com dois numeros digitados pelo usuario
print('*** Opções ***')
print('1 - Soma')
print('2 - Subtração')
print('3 - Divisão')
print('4 - Multiplicação')

opcao = str(input('Digite a opção: '))
while opcao > '4' or opcao < '1':
    opcao = str(input('Opção invalida. Digite uma opção de 1 a 4 para continuar: '))

num1 = float(input('Digite o primeiro valor: '))
num2 = float(input('Digite o segundo valor: '))

class Calculadora:
    def __init__(self, num1, num2):
        self.valor1 = num1
        self.valor2 = num2

    def soma(self):
        return self.valor1 + self.valor2

    def subtracao(self):
        return self.valor1 - self.valor2

    def divisao(self):
        return self.valor1 / self.valor2

    def multiplicacao(self):
        return self.valor1 * self.valor2

calculadora = Calculadora(num1, num2)
if opcao == '1':
    print('Opção escolhida: {}'.format(opcao))
    print('{n1} + {n2} = '.format(n1=num1, n2=num2) + str(calculadora.soma()))

elif opcao == '2':
    print('Opção escolhida: {}'.format(opcao))
    print('{n1} - {n2} = '.format(n1=num1, n2=num2) + str(calculadora.subtracao()))

elif opcao == '3':
    print('Opção escolhida: {}'.format(opcao))
    print('{n1} / {n2} = '.format(n1=num1, n2=num2) + str(calculadora.divisao()))

elif opcao == '4':
    print('Opção escolhida: {}'.format(opcao))
    print('{n1} * {n2} = '.format(n1=num1, n2=num2) + str(calculadora.multiplicacao()))