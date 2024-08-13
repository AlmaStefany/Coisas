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

'''                 Exercicio 005                 '''

n = int(input("Digite um numero: "))
a = n - 1
s = n + 1
print("o valor é {}, seu antecessor é {} e o sucessor é {}".format(n, a, s))

# outra forma de fazer
n = int(input("digite um numero: "))
print("o valor é {}, seu antecessor é {} e o sucessor é {}".format(n, (n-1), (n+1)))


'''             Exercicio 006                      '''

n = int(input("Digite um numero: "))
d = n * 2 #dobro
t = n * 3 #triplo
r = n ** (1/2) #raiz quadrada
print("O dobro de {} vale {}".format(n, d))
print("O triplo de {} vale {} \n A raiz quadrada de {} é igual a {:.2}".format(n, t, n, r)) #esse :.2 limita a raiz quadrada mostrar apenas 2 casas decimais flutuantes

# outra forma de fazer
n = int(input("Digite um valor"))
print("O dobro de {} vale {} ".format(n, (n*2)))
print("o triplo de {} vale {} \n a raiz quadada de {} é igual a {} ".format(n, (n*3), n, (n**(1/2))))
