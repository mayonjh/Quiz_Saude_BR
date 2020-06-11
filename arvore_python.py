from jogadores import players

class NodoArvore:
    def __init__(self, chave=players):
        self.chave = chave
        self.esquerda = None
        self.direita = None
    def getchave(self):
        return self.chave

    def setchave(self, chave):
        self.chave = chave

    def getEsquerda(self):
        return self.esquerda

    def setEsquerda(self, esquerda):
        self.esquerda = esquerda

    def getDireita(self):
        return self.direita

    def setDireita(self, direita):
        self.direita = direita
    def __str__(self):
      return "NOME: " + str(self.chave)


class ArvoreBusca:
    def __init__(self):
        self.root = None

    def insert(self, chave):
        novo_no = NodoArvore(chave)

        if self.empty():            
            self.root = novo_no
        else:                       
            no_raiz = None
            no_aux = self.root

            while (True):
                if no_aux != None:                                                  
                    no_raiz = no_aux                                                 
                    if novo_no.getchave().score < no_aux.getchave().score:   
                        no_aux = no_aux.getEsquerda()
                    else:                                       
                        no_aux = no_aux.getDireita()
                else:                                            

                     if novo_no.getchave().score < no_raiz.getchave().score:    
                        no_raiz.setEsquerda(novo_no)

                     else:                                                              
                        no_raiz.setDireita(novo_no)

                     break 

    def empty(self):
        if self.root == None:
            return True
        return False

    def emOrdem(self, atual):
        if atual != None:
            self.emOrdem(atual.esquerda)
            print(atual.chave, end="\n")
            self.emOrdem(atual.direita)

    def preOrdem(self, atual):
        if atual != None:
            print(atual.chave, end="\n")
            self.preOrdem(atual.esquerda)
            self.preOrdem(atual.direita)

    def posOrdem(self, atual):
        if atual != None:
            self.posOrdem(atual.esquerda)
            self.posOrdem(atual.direita)
            print(atual.chave, end=" \n")

    def maxx(self, atual):
        anterior = None
        while atual is not None:
            anterior = atual
            atual = atual.direita
        return anterior

    def getRoot(self):
        return self.root
