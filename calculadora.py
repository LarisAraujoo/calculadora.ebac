num1 = float(input('Digite o primeiro número:'))
num2 = float(input('Digite o segundo número:'))

print('1 - Soma')
print('2 - Subtração')
print('3 - Multiplicação')
print('4 - Divisão')

opcao = input("Escolha a operação: ")

if opcao == '1':
  print(num1 + num2)

elif opcao == '2':
  print(num1 - num2)

elif opcao == '3':
  print(num1 * num2)

elif opcao == '4':
  print(num1 / num2)

else:
  print('Opção inválida')