# Exercício Python 18: Escreva um programa que leia dois números
# inteiros e compare-os. mostrando na tela uma mensagem:
#
# – O primeiro valor é maior
#
# – O segundo valor é maior
#
# – Não existe valor maior, os dois são iguais

primeiro_valor = float(input("primeiro valor: "))
segundo_valor = float(input("segundo valor"))
if primeiro_valor > segundo_valor:
    print("O primeiro valor é maior")
elif primeiro_valor == segundo_valor:
    print("Não existe valor maior, os dois são iguais")
if segundo_valor > primeiro_valor:
    print("O segundo valor é maior")
