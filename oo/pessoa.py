class Pessoa:
    olhos = 2
    def __init__(self, *filhos, nome=None, idade=48):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f'Olá {id(self)}'

if __name__ == '__main__':
    flavio = Pessoa(nome='Flávio')
    luiz = Pessoa(flavio, nome='Luiz')
    print(Pessoa.cumprimentar(luiz))
    print(id(luiz))
    print(luiz.cumprimentar())
    print(luiz.nome)
    print(luiz.idade)
    for filho in luiz.filhos:
        print(filho.nome)
    luiz.sobrenome = 'Ramalho'
    del luiz.filhos
    luiz.olhos = 1
    del luiz.olhos
    print(luiz.__dict__)
    print(flavio.__dict__)
    Pessoa.olhos = 3
    print(Pessoa.olhos)
    print(luiz.olhos)
    print(flavio.olhos)
    print(id(Pessoa.olhos), id(luiz.olhos), id(flavio.olhos))
