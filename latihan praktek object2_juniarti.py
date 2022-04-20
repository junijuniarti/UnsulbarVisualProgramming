#juniarti(D0219008)

class kucing:
  def __init__(self, inputName, inputtinggi, inputumur):
    self.name = inputName
    self.tinggi = inputtinggi
    self.umur = inputumur
    
aggora = kucing("aggora",50,10)
somali = kucing("somali",100,2)
persians = kucing("persians",100,30)

print(aggora.__dict__,  somali.__dict__, persians.__dict__)
