class VeiculoAutomotor():

    @property
    def Motorização(self):
        return self.__Motorização

    @Motorização.setter
    def Motorização(self, value):
        self.__Motorização = value

    def Ligar(self):
        return True

    def Brecar(self):
        return True

Fusca = VeiculoAutomotor()
Fusca.Motorização = 1000
Fusca.Ligar()
Fusca.Brecar()
print(Fusca.Motorização)