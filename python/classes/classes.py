class Pessoa:
    def __init__(self, name, idade, profissao): # definicao de um constructor para a classe Pessoa
        self.name = name
        self.idade = idade
        self.profissao = profissao

    def __str__(self): # o parametro self remete ao proprio objeto
        return ('{\nName: {self.name},\nIdade: {self.idade},\nProfissao:{self.profissao}'
                '}')

    def diasVividos(self):
        return self.idade * 365

p1 = Pessoa("Kaua", 20, "Programador")
p2 = Pessoa("Vinicius", 22, "Estudante")
print(p1.diasVividos())

p1.idade = 30
print(p1.diasVividos())

del p1;
