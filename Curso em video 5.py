'''     Operadores aritmétricos

+ adição
- subtração
* multiplicação
/ divisão
** potência
// divisão inteira
% resto da divisão

        Ordem de precedência

1 ()
2 **
3 * / // %
4 + -

'''


teste = input("Digite seu nome: ")
print("Prazer em te conhecer {:>20}!".format(teste)) #essa função faz alinhamento a 20 caracteres á direita >
# o sinal ^ alinha ao centro de 20 espaços

n1 = int(input("um valor: "))
n2 = int(input("outro valor: "))
print("a soma é {}: ".format(n1+n2), end="")#esse end impede a quebra de linha, os 2 prints saem na mesma linha
print("teste pra impedir a quebra de linha")
print("teste pra quebrar a linha ")#basta colocar \n no inicio e no final doq vc quer q esteja em outra linha exemplo: Olá \n td bem? \n

'''Exercicios 005'''