def myFunction():
  a = 2

# a variavel criada dentro da funcao so pode ser vista dentro da function

def myFunction2():
  a = 2
  def teste():
    print(a)
  teste()

myFunction2()

# variaveis locais sao sao acessiveis dentro do scopo de funcoes dentro de funcoes
a = 200

def printar():
  global a
  a = 300
  print(a)


printar()
print(a)