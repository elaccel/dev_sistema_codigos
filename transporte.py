class Transporte:
    
    def __init__(self,capacidade, veloMax, ):

        self.__capacidade = capacidade
        self.__veloMax = veloMax
     
    
    def  getCapacidade(self):
            return self.__capacidade
    
    def setCapacidade(self,novaCap):
           if novaCap >0 and <= 50:
                  self.__capacidade
                  
                  

            
    
    def  getVeloMax(self):
            return self.__veloMax
    
    def descrição(self):
         print(f'o {self.tipo} tem{self.capacidade} de pessoas e move a  {self.velomax}km/h')

class Onibus(Transporte):
          def __init__
