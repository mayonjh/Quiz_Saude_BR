class players():


    def __init__(self, nome = None, score = None):
        self.nome = nome
        self.score = score

    def __str__(self):
      return "Player: " + str(self.nome) + "    Score: " + str(self.score)