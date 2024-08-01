class Fracao:
    def __init__(self, num, den):
        self.numerador = num
        if den is not 0:
            self.denominador = den

        else:
            self.denominador = 1

    def divisao(self):
        return self.numerador/self.denominador


fracao = Fracao(1, 4)


print(fracao.divisao())

print(fracao.numerador)
