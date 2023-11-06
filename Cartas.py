import random                                                                                               

class Carta:                                                                                                
    def __init__(self):                                                                                     
        self._cartas = []                                                                                       
        self._cartas_atualizadas = []                                                                          
        self._numero_da_carta = None                                                                           
        self._numero_aleatorio = None                                                                          
        self._deck = ["ACE", 2, 3, 4, 5, 6, 7, 8, 9, "JACK", "QUEEN", "KING"]                                 
      
    def numeroAleatorio(self):                                                                             
        self._numero_aleatorio = random.randint(0, len(self._deck) - 1)                                   
        return self._numero_aleatorio                                                                      
    
    def criarCartas(self, quantidade):                                                                    
        for i in range(quantidade):                                                                          
            self._numero_da_carta = self._deck[self.numeroAleatorio()]                                        
            self._cartas.append(self._numero_da_carta)                                                       
          
    def criarCartaASCII(self):                                                                             
        for i in range(0, len(self._cartas)):                                                                   
            print(f" _____\n|{self._cartas[i]} .  |\n| /.\\ |\n|(_._)|\n|  |  |\n|____{self._cartas[i]}|")     

    def insertionSort(self):                                                                               
        self._cartas_atualizadas = self._cartas                                                               
        for i in range(1, len(self._cartas_atualizadas)):                                                      
            chave = self._cartas_atualizadas[i]                                                                    
            j = i - 1                                                                                            
            while j >= 0 and self._deck.index(chave) < self._deck.index(self._cartas_atualizadas[j]):              
                    self._cartas_atualizadas[j + 1] = self._cartas_atualizadas[j]                                       
                    j -= 1                                                                                              
            self._cartas_atualizadas[j + 1] = chave                                                                 
