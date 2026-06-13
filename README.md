# Calculadora em Python

## Descrição

Este projeto consiste em uma calculadora simples desenvolvida em Python. O programa recebe dois números informados pelo usuário e realiza uma das operações matemáticas disponíveis: soma, subtração, multiplicação ou divisão.

## Como executar o arquivo .sh

1. Conceda permissão de execução:

```bash
chmod 744 calculadora.sh
```

2. Execute o arquivo:

```bash
./calculadora.sh
```

## Como executar o arquivo Python

```bash
python3 calculadora.py
```

## Explicação do código

O programa solicita dois números utilizando a função `input()` e converte os valores para o tipo `float`.

Em seguida, exibe um menu com quatro operações matemáticas. A estrutura condicional `if`, `elif` e `else` é utilizada para verificar a opção escolhida pelo usuário e executar a operação correspondente.

Por fim, o resultado é exibido na tela utilizando a função `print()`.
